"""
    JANE Processor is used to persist and query the details of exam phase
    processing. We use SQLite when running locally and MySQL when running
    in production.
"""

import logging
from collections import namedtuple
import os
import sqlite3
from phase import Phase
from utility import get_base_filename

LOG = logging.getLogger('repository')


# pylint: disable=too-few-public-methods
class DuplicateError(sqlite3.IntegrityError):
    """Wrapper for SQLite error"""
    pass


class PhaseRepository(object):
    """Persistent storage for phase data"""

    def __init__(self, db_type, db_location):
        db_exists = os.path.exists(db_location)
        if db_type == 'SQLite':
            self.con = sqlite3.connect(db_location)
        elif db_type == 'MySQL':
            raise NotImplementedError()
        else:
            raise NotImplementedError()
        if not db_exists:
            self.initialize()
        self.con.row_factory = self.namedtuple_factory

    def initialize(self):
        """Method used to initialize the database schema."""

        sql = '''CREATE TABLE phase (
                     session_id TEXT,
                     phase_id INT REFERENCES phase_definition(phase_id),
                     file_name TEXT,
                     file_size INT,
                     received INT,
                     processed INT,
                     status TEXT,
                     PRIMARY KEY (file_name))'''
        self.con.execute(sql)

        sql = '''CREATE UNIQUE INDEX phase_session ON phase (phase_id, session_id)'''
        self.con.execute(sql)

        sql = '''CREATE TABLE phase_definition (
                     phase_id INT,
                     phase_name TEXT,
                     PRIMARY KEY (phase_id))'''
        self.con.execute(sql)
        for phase in Phase:
            if not phase.ignored():
                sql = '''INSERT INTO phase_definition (phase_id, phase_name)
                         VALUES (?, ?)'''
                self.con.execute(sql, (phase.value, phase.name))

        sql = '''CREATE VIEW session_phases AS
                    SELECT
                        s.session_id,
                        d.phase_id,
                        d.phase_name
                    FROM phase_definition AS d JOIN 
                        (SELECT DISTINCT session_id FROM phase
                         WHERE session_id IS NOT NULL) AS s
                    ORDER BY session_id, phase_id'''
        self.con.execute(sql)

        self.con.commit()
        LOG.debug('Initialized schema')

    def create(self, data):
        """Method used to insert record in PHASE table."""
        sql = '''INSERT INTO phase
                    (file_name,
                     phase_id,
                     file_size,
                     received,
                     status)
                 VALUES (?, ?, ?, ?, ?)'''
        file_name = get_base_filename(data.file_path)
        params = [file_name,
                  data.phase.value,
                  data.file_size,
                  data.received,
                  data.status.name]
        try:
            self.con.execute(sql, params)
        except sqlite3.Error as ex:
            raise DuplicateError(ex)
        LOG.debug('Inserted record in PHASE table for file %s:', file_name)
        self.con.commit()

    def update(self, data, exclude_session=False):
        """Method used to updated record in PHASE table."""
        processed = data.processed
        status = data.status
        session_id = data.session_id
        file_name = get_base_filename(data.file_path)

        if processed is None and status is None and session_id is None:
            raise ValueError("Nothing to update")
        sql = "UPDATE phase SET"
        params = []
        if processed is not None:
            sql += " processed = ?"
            params.append(processed)
        if status is not None:
            if params:
                sql += ","
            sql += " status = ?"
            params.append(status.name)
        if session_id is not None and not exclude_session:
            if params:
                sql += ","
            sql += " session_id = ?"
            params.append(session_id)
        sql += " where file_name = ?"
        params.append(file_name)

        try:
            self.con.execute(sql, params)
        except sqlite3.Error as ex:
            raise DuplicateError(ex)

        self.con.commit()
        LOG.debug('Updated record in PHASE table for file %s:', file_name)

    def get_sessions(self):
        """Method that returns the details of all phases for every session."""

        cursor = self.con.cursor()
        cursor.execute('''SELECT
                              p.session_id,
                              s.phase_id,
                              p.received,
                              p.processed,
                              p.status
                          FROM session_phases AS s
                              JOIN phase AS p
                                  ON ( p.phase_id = s.phase_id AND
                                       s.session_id = p.session_id )
                          UNION
                          SELECT
                              s.session_id,
                              s.phase_id,
                              p.received,
                              p.processed,
                              p.status
                          FROM session_phases AS s
                              LEFT OUTER JOIN phase AS p
                                  ON ( p.phase_id = s.phase_id AND
                                       s.session_id = p.session_id )
                          ORDER BY p.session_id, s.phase_id''')
        return cursor.fetchall()

    def get_session(self, session_id):
        """Method that returns details of all phases that have been processed
        for a specific session."""

        cursor = self.con.cursor()
        sql = "SELECT COUNT(*) AS phase_count FROM phase WHERE session_id LIKE ?"
        cursor.execute(sql, ('%' + session_id,))
        if cursor.fetchone().phase_count == 0:
            return []
        sql = '''SELECT
                     d.phase_name,
                     datetime(p.received, 'unixepoch') AS received,
                     datetime(p.processed, 'unixepoch') AS processed,
                     p.status,
                     p.file_name
                 FROM phase_definition AS d
                     LEFT OUTER JOIN phase AS p
                         ON ( d.phase_id = p.phase_id AND
                              p.session_id IS NOT NULL)
                 WHERE session_id LIKE ? OR
                       status IS NULL
                 ORDER BY d.phase_id'''
        cursor.execute(sql, ('%' + session_id,))
        return cursor.fetchall()

    def get_phases(self):
        """Method that returns all of the phase files we have attempted to process."""

        cursor = self.con.cursor()
        sql = '''SELECT
                     file_name,
                     datetime(received, 'unixepoch') AS received,
                     status
                 FROM phase
                 ORDER BY file_name'''
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def namedtuple_factory(cursor, row):
        """
        Usage:
        con.row_factory = namedtuple_factory
        """
        fields = []
        for col in cursor.description:
            i = col[0].find('.')
            fields.append(col[0] if i == -1 else col[0][i+1:])
        row_tuple = namedtuple("Row", fields)
        return row_tuple(*row)

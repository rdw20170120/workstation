#!/usr/bin/env python

"""
    JANE Query is used to query the state of exam phase processing.

    It currently supports the following syntax:

    python query.py [session_id]

    When called without a session_id it generates a table of all known
    sessions and details of all phases that have already been processed.

    When called with a session_id it generates a table of all possible phases
    with details provided for those that have been already been processed.
"""



import logging
import sys
import colorama
from phase import Phase
from repository import PhaseRepository
from utility import configure_logging, get_filename_parts

MISSING = "  "
ERROR = colorama.Fore.RED + "\\u2717 ".encode('utf-8')
SUCCESS = "\\u2713 ".encode('utf-8')
LOG = logging.getLogger('query')
DB_LOCATION = '/tmp/jane.db'


def query():
    """Function that prints a table of all known sessions."""

    rows = REPO.get_sessions()
    if rows:
        print("Session ID            ", end='')
        print_phase_heading(func=lambda v: hex(v)[2].upper())
        print("\n----------------------------------------------", end='')
        prev_session_id = ''
        for row in rows:
            session_id = row.session_id
            if session_id != prev_session_id:
                print("\n%s      " % (session_id[-16:],), end='')
            if row.status == 'SUCCESS':
                print(SUCCESS, end='')
            elif row.received is None:
                print(MISSING, end='')
            else:
                print(ERROR, end='')
            prev_session_id = session_id
        print()
        print_phase_legend(mod=2, func=lambda v: hex(v)[2].upper())
    else:
        print("No sessions found")


# pylint: disable=line-too-long
def query_files():
    """Function that prints a table of all phase files and the details of each
    one that we have attempted to process."""
    rows = REPO.get_phases()
    if rows:
        print("Filename                                                       Received         Status")
        print("---------------------------------------------------------------------------------------------------")
        for row in rows:
            file_name = row.file_name[:55]
            received = row.received
            status = row.status
            print("%-55s   %19s   %s" % (file_name, received, status))
    else:
        print("No files found")


def query_session(session_id):
    """Function that prints a table of all phases and the details of each
    one that have been processed for the specified session ID"""

    rows = REPO.get_session(session_id)
    if rows:
        # pylint: disable=line-too-long
        print("Phase              Generated             Received              Processed        Status")
        print("-------------------------------------------------------------------------------------------------")
        for row in rows:
            if row.file_name is None:
                print(row.phase_name)
            else:
                print("%-11s   %19s   %19s   %19s   %s" % (
                    row.phase_name,
                    get_filename_parts(row.file_name).timestamp,
                    row.received if row.received is not None else "",
                    row.processed if row.processed is not None else "",
                    row.status if row.status is not None else ""
                ))
    else:
        print("No phases found for specified session")


def print_phase_legend(func=None, mod=1, include_ignored=False):
    """Simple function to print a listing of phase values and names"""

    print()
    count = 1
    for phase in Phase:
        if include_ignored or not phase.ignored():
            print('%5s = %-11s\t' %
                  (phase.value if func is None else func(phase.value),
                   phase.name), end=' ' if count % mod else '\n')
        count += 1
    print()


def print_phase_heading(func=None, include_ignored=False):
    """Simple function to print a line with all phase values"""

    for phase in Phase:
        if include_ignored or not phase.ignored():
            print(phase.value if func is None else func(phase.value), end=' ')


if __name__ == "__main__":
    configure_logging()
    colorama.init(autoreset=True)
    REPO = PhaseRepository('SQLite', DB_LOCATION)
    if len(sys.argv) == 1:
        query()
    elif sys.argv[1] == '-f':
        query_files()
    else:
        query_session(sys.argv[1])

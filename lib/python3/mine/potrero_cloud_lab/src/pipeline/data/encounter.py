#!/bin/false

import datetime as dt

from pathlib  import Path

from logzero import logger as log

from ..config       import Config
from ..utility.time import as_iso8601_SS
from ..utility.time import datetime_as_int_seconds 
from ..utility.time import datetime_from_int_seconds 
from ..utility.time import is_naive
from ..utility.time import timedelta_as_hours

c = Config()


class CombinedEncounter:
    def __init__(self, identifier, encounter):
        assert isinstance(encounter, dict)
        assert isinstance(identifier, int)
        self._began = datetime_from_int_seconds(encounter['timestamp_began'])
        self._began_iso8601 = encounter['iso8601_began']
        self._ended = datetime_from_int_seconds(encounter['timestamp_ended'])
        self._ended_iso8601 = encounter['iso8601_ended'] 
        self._files = [encounter['extracted_file']]
        self._identifier = identifier
        self._monitor = encounter['monitor']
        self._patient = encounter['patient_partial_id']
        self._weight = encounter['patient_dry_weight']

        assert is_naive(self._began)
        assert is_naive(self._ended)

    def _update_patient(self, encounter):
        patient = encounter['patient_partial_id']
        if self._patient:
            if patient: self._patient = patient 
        else: self._patient = patient

        weight = encounter['patient_dry_weight']
        if self._weight:
            if weight: self._weight = weight 
        else: self._weight = weight

    def continues(self, encounter):
        began = datetime_from_int_seconds(encounter['timestamp_began'])
        assert is_naive(began)
        result = (began - self._ended) < c.allowed_gap
        if result:
            self._ended = datetime_from_int_seconds(
                encounter['timestamp_ended']
                )
            assert is_naive(self._ended)
            self._ended_iso8601 = encounter['iso8601_ended'] 
            self._files.append(encounter['extracted_file'])
            self._update_patient(encounter)
        return result

    def record(self):
        assert is_naive(self._began)
        assert is_naive(self._ended)
        result = {
            'monitor': self._monitor,
            'encounter_id': self._identifier,
            'iso8601_began': self._began_iso8601,
            'iso8601_ended': self._ended_iso8601,
            'patient_partial_id': self._patient,
            'patient_dry_weight': self._weight,
            'timestamp_began': datetime_as_int_seconds(self._began),
            'timestamp_ended': datetime_as_int_seconds(self._ended),
            'extracted_files': self._files,
            }
        hours = timedelta_as_hours(self._ended - self._began)
        log.debug("Writing encounter %s that covered %.6f hours", result, hours)
        return result


class SingleFileEncounter:
    def __init__(self, monitor, extracted_file, accuryn_record):
        assert isinstance(accuryn_record, dict)
        assert isinstance(extracted_file, Path)
        assert isinstance(monitor, str)
        self._began = datetime_from_int_seconds(
            accuryn_record['timestamp_second']
            )
        self._ended = self._began
        self._file = extracted_file
        self._monitor = monitor
        self._patient = accuryn_record['patient_partial_id']
        self._weight = accuryn_record['patient_dry_weight']

        assert is_naive(self._began)
        assert is_naive(self._ended)

    def _as_iso8601(self, timestamp):
        """Return timestamp as an ISO8601 format."""
        assert isinstance(timestamp, dt.datetime)
        return as_iso8601_SS(timestamp)

    def _update_patient(self, accuryn_record):
        patient = accuryn_record['patient_partial_id']
        if self._patient:
            if patient: self._patient = patient 
        else: self._patient = patient

        weight = accuryn_record['patient_dry_weight']
        if self._weight:
            if weight: self._weight = weight 
        else: self._weight = weight

    def continues(self, accuryn_record):
        timestamp = datetime_from_int_seconds(accuryn_record['timestamp_second'])
        assert is_naive(timestamp)
        assert timestamp >= self._ended
        result = (timestamp - self._ended) < c.allowed_gap
        if result: self._ended = timestamp
        self._update_patient(accuryn_record)
        return result

    def record(self):
        result = {
            'iso8601_began': self._as_iso8601(self._began),
            'iso8601_ended': self._as_iso8601(self._ended),
            'monitor': self._monitor,
            'patient_partial_id': self._patient,
            'patient_dry_weight': self._weight,
            'timestamp_began': datetime_as_int_seconds(self._began),
            'timestamp_ended': datetime_as_int_seconds(self._ended),
            'extracted_file': self._file.as_posix(),
            }
        hours = timedelta_as_hours(self._ended - self._began)
        log.debug("Writing encounter %s that covered %.6f hours", result, hours)
        return result


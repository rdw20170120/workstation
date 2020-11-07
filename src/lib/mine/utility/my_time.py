#!/usr/bin/env false
"""My module for time.

Functionality to integrate eventually:

datetime module
date
  .date()              YES      construct from year, month, day
  .fromordinal()       YES      construct from proleptic Gregorian ordinal
  .fromtimestamp()     YES      construct from Unix time as float seconds
  .isoformat()         YES      convert to ISO8601 string
  .replace()           YES      construct using date math
  .today()             YES      construct current local date
  .toordinal()         YES      convert to proleptic Gregorian ordinal
  .replace()           YES      construct using time math
  .isoformat()         YES      convert to ISO8601 string
  .isocalendar()       SOMEDAY  information
  .isoweekday()        SOMEDAY  information
  .timetuple()         SOMEDAY  convert to time.struct_time
  .weekday()           SOMEDAY  information
  .ctime()             NO       prefer date.isoformat()
  .strftime()          NO       prefer date.isoformat()
datetime
  .astimezone()        YES      construct with new timezone
  .combine()           YES      construct from date, time, and tzinfo objects
  .datetime()          YES      construct from year, month, day, hour, minute,
                                  second, microsecond
  .fromordinal()       YES      construct from proleptic Gregorian ordinal
  .fromtimestamp()     YES      construct from Unix time as float seconds
  .isoformat()         YES      convert to ISO8601 string
  .now()               YES      construct current date and time with zone
  .replace()           YES      construct using date and time math
  .timestamp()         YES      convert to Unix time as float seconds
  .toordinal()         YES      convert to proleptic Gregorian ordinal
  .isocalendar()       SOMEDAY  information
  .isoweekday()        SOMEDAY  information
  .strptime()          SOMEDAY  might be useful
  .timetuple()         SOMEDAY  convert to time.struct_time
  .utctimetuple()      SOMEDAY  convert to time.struct_time in UTC
  .weekday()           SOMEDAY  information
  .ctime()             NO       prefer datetime.isoformat()
  .dst()               NO       passthrough to datetime.tzinfo attribute
  .strftime()          NO       prefer datetime.isoformat()
  .today()             NO       prefer date.today()
  .tzname()            NO       passthrough to datetime.tzinfo attribute
  .utcfromtimestamp()  NO       prefer datetime.now()
  .utcnow()            NO       prefer datetime.now()
  .utcoffset()         NO       passthrough to datetime.tzinfo attribute
time                   MAYBE    prefer datetime
  .time()              MAYBE    construct from hour, minute, second,
                                  microsecond
  .dst()               NO       passthrough to time.tzinfo attribute
  .strftime()          NO       prefer time.isoformat()
  .tzname()            NO       passthrough to time.tzinfo attribute
  .utcoffset()         NO       passthrough to time.tzinfo attribute

calendar module        MAYBE    might be useful

time module
time
  .time()              YES      construct current Unix time as float seconds
  .altzone             SOMEDAY  might be useful
  .clock_getres()      SOMEDAY  might be useful
  .clock_gettime()     SOMEDAY  might be useful
  .daylight            SOMEDAY  might be useful
  .get_clock_info()    SOMEDAY  might be useful
  .monotonic()         SOMEDAY  might be useful
  .perf_counter()      SOMEDAY  might be useful
  .process_time()      SOMEDAY  might be useful
  .strptime()          SOMEDAY  might be useful
  .struct_time         SOMEDAY  might be useful
  .timezone            SOMEDAY  might be useful
  .tzname              SOMEDAY  might be useful
  .clock_settime()     MAYBE    unlikely to be useful
  .gmtime()            MAYBE    does better choice exist for conversion?
  .localtime()         MAYBE    does better choice exist for conversion?
  .asctime()           NO       non-ISO8601 conversion
  .clock()             NO       deprecated
  .ctime()             NO       non-ISO8601 conversion
  .sleep()             NO       call directly, do not wrap
  .strftime()          NO       prefer datetime.isoformat()
  .tzset()             NO       not likely to be useful

Eventually represent distinctions of clock time, wall time, local time, and
universal time.

TODO: Refine ISO8601 output formats for compactness
"""
# Internal packages  (absolute references, distributed with Python)
import datetime as dt
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility import my_assert as is_
# Co-located modules (relative references, NOT packaged, in project)


class ProlepticGregorianOrdinal():
    def __init__(self, value):
        if isinstance(value, int):
            if value <= 0: raise ValueError("'{}' is <= 0".format(value))
            self._ordinal = value
        else: raise ValueError(
            "Cannot handle value '{}' of type '{}'".format(value, type(value))
            )

    def as_date(self):
        return dt.date.fromordinal(self._ordinal)

    def as_int(self):
        return self._ordinal


class UnixTime:
    def __init__(self, value):
        if isinstance(value, int): value = float(value)
        if isinstance(value, float):
            self._float_seconds = value
        else: raise ValueError(
            "Cannot handle value '{}' of type '{}'".format(value, type(value))
            )

    def as_datetime(self):
        return dt.datetime.fromtimestamp(self._float_seconds)


def as_iso8601(value, timespec='auto'):
    assert is_.instance(timespec, str)
    assert is_.instance(value, dt.datetime)
    return value.isoformat(timespec=timespec)

def as_iso8601_HH(value):
    return as_iso8601(value, timespec='hours')

def as_iso8601_MM(value):
    return as_iso8601(value, timespec='minutes')

def as_iso8601_mmmmmm(value):
    return as_iso8601(value, timespec='microseconds')

def as_iso8601_SS(value):
    assert is_.instance(value, dt.datetime)
    if value.tzinfo == dt.timezone.utc:
        return value.strftime('%Y%m%dT%H%M%SZ')
    else:
        return as_iso8601(value, timespec='seconds')

def as_iso8601_sss(value):
    return as_iso8601(value, timespec='milliseconds')

def date_from(value):
    return None

def date_from_ordinal(value):
    if isinstance(value, int):
        value = ProlepticGregorianOrdinal(value)
    assert is_.instance(value, ProlepticGregorianOrdinal)
    return value.as_date()

def date_from_datetime(value):
    assert is_.instance(value, dt.datetime)
    return None

def datetime_as_float_seconds(value):
    assert is_.instance(value, dt.datetime)
    return value.timestamp()

def datetime_as_int_seconds(value):
    return int(datetime_as_float_seconds(value))

def datetime_from_ordinal(value):
    if isinstance(value, int):
        value = ProlepticGregorianOrdinal(value)
    assert is_.instance(value, ProlepticGregorianOrdinal)
    return datetime_from_date(value.as_date())

def datetime_from_float_seconds(value):
    if isinstance(value, float):
        value = UnixTime(value)
    assert is_.instance(value, UnixTime)
    return value.as_datetime()

def datetime_from_int_seconds(value):
    if isinstance(value, int):
        value = UnixTime(value)
    assert is_.instance(value, UnixTime)
    return value.as_datetime()

def is_aware(value):
    if isinstance(value, float): return False
    elif isinstance(value, int): return False
    elif isinstance(value, ProlepticGregorianOrdinal): return False
    elif isinstance(value, dt.date): return False
    elif isinstance(value, dt.datetime):
        if value.tzinfo is None: return False
        elif value.tzinfo.utcoffset(value) is None: return False
        else: return True
    elif isinstance(value, dt.time):
        if value.tzinfo is None: return False
        elif value.tzinfo.utcoffset(value) is None: return False
        else: return True
    else: raise ValueError(
        "Irrelevant for value '{}' of type '{}'".format(value, type(value))
        )

def is_naive(value):
    if isinstance(value, float): return True
    elif isinstance(value, int): return True
    elif isinstance(value, ProlepticGregorianOrdinal): return True
    elif isinstance(value, dt.date): return True
    elif isinstance(value, dt.datetime):
        if value.tzinfo is None: return True
        elif value.tzinfo.utcoffset(value) is None: return True
        else: return False
    elif isinstance(value, dt.time):
        if value.tzinfo is None: return True
        elif value.tzinfo.utcoffset(value) is None: return True
        else: return False
    else: raise ValueError(
        "Irrelevant for value '{}' of type '{}'".format(value, type(value))
        )

def now_utc():
    return dt.datetime.now(dt.timezone.utc)

def timedelta_as_hours(value):
    assert is_.instance(value, dt.timedelta)
    return value / dt.timedelta(hours=1)

def timedelta_as_seconds(value):
    assert is_.instance(value, dt.timedelta)
    return value / dt.timedelta(seconds=1)

'''DisabledContent
'''


# TODO: SOMEDAY: Add tests for naive versus aware dates & times
from datetime import datetime as dt_datetime

from .my_assert import has_type
from .my_assert import has_type_message
from .my_assert import unrecognized_message


def datetime_as_compact_string_utc(date_time):
    """Return UTC date_time as a compact string with high precision"""
    return datetime_formatted(date_time, '{0:%Y%m%dT%H%M%S.%f}Z')

def datetime_formatted(date_time, format_string):
    """Return UTC date_time as formatted string"""
    if date_time is None:
        result = ''
    else:
        assert has_type(date_time, dt_datetime), has_type_message(date_time, dt_datetime)
        assert date_time.utcoffset() is None
        result = format_string.format(date_time)
    assert has_type(result, StringType), has_type_message(result, StringType)
    return result

def now():
    """Return UTC datetime for NOW"""
    result = dt_datetime.utcnow()
    assert has_type(result, dt_datetime), has_type_message(result, dt_datetime)
    return result

def timestamp_as_datetime_utc(timestamp):
    """Return UTC datetime for Unix epoch timestamp"""
    if has_type(timestamp, FloatType):
        result = dt_datetime.utcfromtimestamp(timestamp)
    elif has_type(timestamp, IntType):
        result = dt_datetime.utcfromtimestamp(timestamp)
    else:
        raise ValueError(unrecognized_message(timestamp, type(timestamp), 'type'))
    assert has_type(result, dt_datetime), has_type_message(result, dt_datetime)
    return result

''' Disabled content
'''


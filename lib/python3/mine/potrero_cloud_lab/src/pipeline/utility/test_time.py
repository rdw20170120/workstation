#!/bin/false

import datetime as dt

from pytest import mark
from pytest import raises

from .time import as_iso8601_MM
from .time import as_iso8601_SS
from .time import datetime_as_int_seconds
from .time import datetime_from_int_seconds
from .time import is_aware
from .time import is_naive
from .time import now_utc
from .time import timedelta_as_hours
from .time import ProlepticGregorianOrdinal
from .time import UnixTime

# TODO: Consider splitting this module into one per imported module or class
# TODO: Break up tests into individual test methods, so each failure is isolated

epoch_as_datetime = dt.datetime(2020, 5, 10, 20, 5, 3)
epoch_as_int_seconds = 1589155503

def test_as_iso8601_MM():
    v = as_iso8601_MM(epoch_as_datetime)
    assert v == '2020-05-10T20:05'

def test_as_iso8601_SS():
    v = as_iso8601_SS(epoch_as_datetime)
    assert v == '2020-05-10T20:05:03'

def test_date_current():
    dt.date.today()
    # TODO: Test current
    # TODO: dt.date.fromtimestamp(0)
    # TODO: dt.date.fromtimestamp(0.0)

def test_date_maximum():
    dt.date(dt.MAXYEAR, 12, 31)
    # TODO: Test upper limit
    # TODO: dt.date.fromordinal(1)
    # TODO: dt.date.fromtimestamp(0)
    # TODO: dt.date.fromtimestamp(0.0)

def test_date_minimum():
    dt.date(dt.MINYEAR, 1, 1)
    dt.date.fromordinal(1)
    dt.date.fromtimestamp(0)
    dt.date.fromtimestamp(0.0)

def test_date_fromordinal():
    with raises(ValueError):
        dt.date.fromordinal(0)
    # TODO: Test beyond upper limit

def test_timedelta_as_hours():
    v = timedelta_as_hours(dt.timedelta(hours=0))
    assert v == 0
    v = timedelta_as_hours(dt.timedelta(hours=1))
    assert v == 1
    v = timedelta_as_hours(dt.timedelta(hours=100))
    assert v == 100
    v = timedelta_as_hours(dt.timedelta(hours=-1))
    assert v == -1

def test_datetime_as_int_seconds():
    v = datetime_as_int_seconds(epoch_as_datetime)
    assert v == epoch_as_int_seconds

@mark.xfail(raises=NotImplementedError, strict=True)
def test_datetime_combine():
    # TODO: dt.datetime.combine()
    raise NotImplementedError

def test_datetime_current():
    dt.datetime.now()
    dt.datetime.today()
    dt.datetime.utcnow()
    # TODO: Test current
    # TODO: dt.datetime.fromtimestamp(0)
    # TODO: dt.datetime.fromtimestamp(0.0)
    # TODO: dt.datetime.utcfromtimestamp(0)
    # TODO: dt.datetime.utcfromtimestamp(0.0)

def test_datetime_from_int_seconds():
    v = datetime_from_int_seconds(epoch_as_int_seconds)
    assert v == epoch_as_datetime

@mark.xfail(raises=NotImplementedError, strict=True)
def test_date_fromtimestamp():
    # TODO: Test beyond lower limit
    # TODO: Test beyond upper limit
    raise NotImplementedError
    
def test_datetime_maximum():
    dt.datetime(dt.MAXYEAR, 12, 31, 23, 59, 59, 999999)
    dt.datetime.max
    # TODO: Test upper limit
    # TODO: dt.datetime.fromordinal(1)
    # TODO: dt.datetime.fromtimestamp(0)
    # TODO: dt.datetime.fromtimestamp(0.0)
    # TODO: dt.datetime.utcfromtimestamp(0)
    # TODO: dt.datetime.utcfromtimestamp(0.0)

def test_datetime_minimum():
    dt.datetime(dt.MINYEAR, 1, 1, 0, 0, 0, 0)
    dt.datetime.fromordinal(1)
    dt.datetime.min
    # TODO: Test lower limit
    # TODO: dt.datetime.fromtimestamp(0)
    # TODO: dt.datetime.fromtimestamp(0.0)
    # TODO: dt.datetime.utcfromtimestamp(0)
    # TODO: dt.datetime.utcfromtimestamp(0.0)

def test_is_aware():
    assert not is_aware(0)
    assert not is_aware(0.0)
    assert not is_aware(dt.date.today())
    assert not is_aware(dt.date(dt.MAXYEAR, 12, 31))
    assert not is_aware(dt.date(dt.MINYEAR, 1, 1))
    assert not is_aware(dt.date.fromordinal(1))
    assert not is_aware(dt.date.fromtimestamp(0))
    assert not is_aware(dt.date.fromtimestamp(0.0))
    assert not is_aware(dt.datetime.now())
    assert not is_aware(dt.datetime.today())
    assert not is_aware(dt.datetime.utcnow())
    assert not is_aware(dt.datetime(dt.MAXYEAR, 12, 31, 23, 59, 59, 999999))
    assert not is_aware(dt.datetime.max)
    assert not is_aware(dt.datetime(dt.MINYEAR, 1, 1, 0, 0, 0, 0))
    assert not is_aware(dt.datetime.fromordinal(1))
    assert not is_aware(dt.datetime.min)
    assert not is_aware(ProlepticGregorianOrdinal(1))

def test_is_naive():
    assert is_naive(0)
    assert is_naive(0.0)
    assert is_naive(dt.date.today())
    assert is_naive(dt.date(dt.MAXYEAR, 12, 31))
    assert is_naive(dt.date(dt.MINYEAR, 1, 1))
    assert is_naive(dt.date.fromordinal(1))
    assert is_naive(dt.date.fromtimestamp(0))
    assert is_naive(dt.date.fromtimestamp(0.0))
    assert is_naive(dt.datetime.now())
    assert is_naive(dt.datetime.today())
    assert is_naive(dt.datetime.utcnow())
    assert is_naive(dt.datetime(dt.MAXYEAR, 12, 31, 23, 59, 59, 999999))
    assert is_naive(dt.datetime.max)
    assert is_naive(dt.datetime(dt.MINYEAR, 1, 1, 0, 0, 0, 0))
    assert is_naive(dt.datetime.fromordinal(1))
    assert is_naive(dt.datetime.min)
    assert is_naive(ProlepticGregorianOrdinal(1))

def test_now_utc():
    v = now_utc()
    assert v is not None
    assert isinstance(v, dt.datetime)
    assert v.tzinfo is dt.timezone.utc
    assert v.tzinfo.utcoffset(v) is not None

@mark.xfail(raises=AssertionError, strict=True,
    reason='This makes no sense, what am I doing wrong?')
def test_now_utc_is_aware():
    assert is_aware(now_utc())

@mark.xfail(raises=AssertionError, strict=True,
    reason='This makes no sense, what am I doing wrong?')
def test_now_utc_not_is_naive():
    assert not is_naive(now_utc())

def test_proleptic_gregorian_ordinal():
    with raises(ValueError):
        ProlepticGregorianOrdinal(0)
    ProlepticGregorianOrdinal(1)


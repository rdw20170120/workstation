#!/usr/bin/env false
"""TODO: Write

TODO: Consider splitting this module into one per imported module or class
TODO: Break up tests into individual test methods, so each failure is isolated
"""
# Internal packages (absolute references, distributed with Python)
import datetime as dt

# External packages (absolute references, NOT distributed with Python)
from pytest import mark
from pytest import raises
from pytest import skip

# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_
from utility.my_time import as_iso8601_MM
from utility.my_time import as_iso8601_SS
from utility.my_time import datetime_as_int_seconds
from utility.my_time import datetime_from_int_seconds
from utility.my_time import is_aware
from utility.my_time import is_naive
from utility.my_time import now_utc
from utility.my_time import timedelta_as_hours
from utility.my_time import ProlepticGregorianOrdinal
from utility.my_time import UnixTime

# Project modules   (relative references, NOT packaged, in project)


epoch_as_datetime = dt.datetime(2020, 5, 10, 20, 5, 3)


def test_as_iso8601_MM():
    v = as_iso8601_MM(epoch_as_datetime)
    assert is_.equal(v, "2020-05-10T20:05")


def test_as_iso8601_SS():
    v = as_iso8601_SS(epoch_as_datetime)
    assert is_.equal(v, "2020-05-10T20:05:03")


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
    assert is_.equal(v, 0)
    v = timedelta_as_hours(dt.timedelta(hours=1))
    assert is_.equal(v, 1)
    v = timedelta_as_hours(dt.timedelta(hours=100))
    assert is_.equal(v, 100)
    v = timedelta_as_hours(dt.timedelta(hours=-1))
    assert is_.equal(v, -1)


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
    assert is_.false(is_aware(0))
    assert is_.false(is_aware(0.0))
    assert is_.false(is_aware(dt.date.today()))
    assert is_.false(is_aware(dt.date(dt.MAXYEAR, 12, 31)))
    assert is_.false(is_aware(dt.date(dt.MINYEAR, 1, 1)))
    assert is_.false(is_aware(dt.date.fromordinal(1)))
    assert is_.false(is_aware(dt.date.fromtimestamp(0)))
    assert is_.false(is_aware(dt.date.fromtimestamp(0.0)))
    assert is_.false(is_aware(dt.datetime.now()))
    assert is_.false(is_aware(dt.datetime.today()))
    assert is_.false(is_aware(dt.datetime.utcnow()))
    assert is_.false(is_aware(dt.datetime(dt.MAXYEAR, 12, 31, 23, 59, 59, 999999)))
    assert is_.false(is_aware(dt.datetime.max))
    assert is_.false(is_aware(dt.datetime(dt.MINYEAR, 1, 1, 0, 0, 0, 0)))
    assert is_.false(is_aware(dt.datetime.fromordinal(1)))
    assert is_.false(is_aware(dt.datetime.min))
    assert is_.false(is_aware(ProlepticGregorianOrdinal(1)))


def test_is_naive():
    assert is_.true(is_naive(0))
    assert is_.true(is_naive(0.0))
    assert is_.true(is_naive(dt.date.today()))
    assert is_.true(is_naive(dt.date(dt.MAXYEAR, 12, 31)))
    assert is_.true(is_naive(dt.date(dt.MINYEAR, 1, 1)))
    assert is_.true(is_naive(dt.date.fromordinal(1)))
    assert is_.true(is_naive(dt.date.fromtimestamp(0)))
    assert is_.true(is_naive(dt.date.fromtimestamp(0.0)))
    assert is_.true(is_naive(dt.datetime.now()))
    assert is_.true(is_naive(dt.datetime.today()))
    assert is_.true(is_naive(dt.datetime.utcnow()))
    assert is_.true(is_naive(dt.datetime(dt.MAXYEAR, 12, 31, 23, 59, 59, 999999)))
    assert is_.true(is_naive(dt.datetime.max))
    assert is_.true(is_naive(dt.datetime(dt.MINYEAR, 1, 1, 0, 0, 0, 0)))
    assert is_.true(is_naive(dt.datetime.fromordinal(1)))
    assert is_.true(is_naive(dt.datetime.min))
    assert is_.true(is_naive(ProlepticGregorianOrdinal(1)))


def test_now_utc():
    v = now_utc()
    assert is_.not_none(v)
    assert is_.instance(v, dt.datetime)
    assert is_.equal(v.tzinfo, dt.timezone.utc)
    assert is_.equal(v.tzinfo.utcoffset(v), dt.timedelta(0))


@mark.xfail(
    raises=AssertionError,
    strict=True,
    reason="This makes no sense, what am I doing wrong?",
)
def test_now_utc_is_aware():
    assert is_.true(is_aware(now_utc()))


@mark.xfail(
    raises=AssertionError,
    strict=True,
    reason="This makes no sense, what am I doing wrong?",
)
def test_now_utc_not_is_naive():
    assert is_.false(is_naive(now_utc()))


def test_proleptic_gregorian_ordinal():
    with raises(ValueError):
        ProlepticGregorianOrdinal(0)
    ProlepticGregorianOrdinal(1)


"""DisabledContent
# TODO: FIX: These tests are dependent upon the machine's current timezone

epoch_as_int_seconds = 1589141103

def test_datetime_as_int_seconds(config):
    v = datetime_as_int_seconds(epoch_as_datetime)
    assert is_.equal(v, epoch_as_int_seconds)


def test_datetime_from_int_seconds(config):
    if config.running_humanless:
        skip("RESEARCH:  Why does this fail under Jenkins? Timezone?")
    v = datetime_from_int_seconds(epoch_as_int_seconds)
    assert is_.equal(v, epoch_as_datetime)

"""

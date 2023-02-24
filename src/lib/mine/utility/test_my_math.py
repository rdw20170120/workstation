#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from math import isnan

# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_
from utility.my_math import Percentage
from utility.my_math import Rate
from utility.my_math import assert_nan

# Project modules   (relative references, NOT packaged, in project)


def test_assert_nan_00():
    with raises(AssertionError):
        assert_nan(-1.0)


def test_assert_nan_01():
    with raises(AssertionError):
        assert_nan(0)


def test_assert_nan_02():
    with raises(AssertionError):
        assert_nan(1.0)


def test_assert_nan_03():
    with raises(AssertionError):
        assert_nan(False)


def test_assert_nan_04():
    with raises(AssertionError):
        assert_nan(True)


def test_assert_nan_05():
    with raises(TypeError):
        assert_nan("")


def test_assert_nan_06():
    with raises(TypeError):
        assert_nan("text")


def test_assert_nan_07():
    with raises(TypeError):
        assert_nan(None)


def test_percentage_01():
    v = Percentage(0, 1)
    assert is_.equal(v.numerator, 0)
    assert is_.equal(v.denominator, 1)
    assert is_.equal(v.percentage, 0.0)


def test_percentage_02():
    v = Percentage(1, 1)
    assert is_.equal(v.numerator, 1)
    assert is_.equal(v.denominator, 1)
    assert is_.equal(v.percentage, 100.0)


def test_percentage_03():
    v = Percentage(1, 100)
    assert is_.equal(v.numerator, 1)
    assert is_.equal(v.denominator, 100)
    assert is_.equal(v.percentage, 1.0)


def test_percentage_04():
    v = Percentage(100, 1)
    assert is_.equal(v.numerator, 100)
    assert is_.equal(v.denominator, 1)
    assert is_.equal(v.percentage, 10000.0)


def test_percentage_05():
    v = Percentage(-1, 1)
    assert is_.equal(v.numerator, -1)
    assert is_.equal(v.denominator, 1)
    assert is_.equal(v.percentage, -100.0)


def test_percentage_06():
    v = Percentage(1, 0)
    assert is_.equal(v.numerator, 1)
    assert is_.equal(v.denominator, 0)
    assert assert_nan(v.percentage)


def test_rate_01():
    v = Rate(0, "top", 1, "bottom")
    assert is_.equal(v.numerator, 0)
    assert is_.equal(v.numerator_units, "top")
    assert is_.equal(v.denominator, 1)
    assert is_.equal(v.denominator_units, "bottom")
    assert is_.equal(v.rate, 0.0)
    assert is_.equal(v.rate_units, "top/bottom")


def test_rate_02():
    v = Rate(1, "top", 1, "bottom")
    assert is_.equal(v.numerator, 1)
    assert is_.equal(v.numerator_units, "top")
    assert is_.equal(v.denominator, 1)
    assert is_.equal(v.denominator_units, "bottom")
    assert is_.equal(v.rate, 1.0)
    assert is_.equal(v.rate_units, "top/bottom")


def test_rate_03():
    v = Rate(1, "top", 100, "bottom", "tpb")
    assert is_.equal(v.numerator, 1)
    assert is_.equal(v.numerator_units, "top")
    assert is_.equal(v.denominator, 100)
    assert is_.equal(v.denominator_units, "bottom")
    assert is_.equal(v.rate, 0.01)
    assert is_.equal(v.rate_units, "tpb")


def test_rate_04():
    v = Rate(100, "top", 1, "bottom", "tpb")
    assert is_.equal(v.numerator, 100)
    assert is_.equal(v.numerator_units, "top")
    assert is_.equal(v.denominator, 1)
    assert is_.equal(v.denominator_units, "bottom")
    assert is_.equal(v.rate, 100.0)
    assert is_.equal(v.rate_units, "tpb")


def test_rate_05():
    v = Rate(-1, "top", 1, "bottom", "tpb")
    assert is_.equal(v.numerator, -1)
    assert is_.equal(v.numerator_units, "top")
    assert is_.equal(v.denominator, 1)
    assert is_.equal(v.denominator_units, "bottom")
    assert is_.equal(v.rate, -1.0)
    assert is_.equal(v.rate_units, "tpb")


def test_rate_06():
    v = Rate(1, "top", 0, "bottom", "tpb")
    assert is_.equal(v.numerator, 1)
    assert is_.equal(v.numerator_units, "top")
    assert is_.equal(v.denominator, 0)
    assert is_.equal(v.denominator_units, "bottom")
    assert assert_nan(v.rate)
    assert is_.equal(v.rate_units, "tpb")


"""DisabledContent
"""

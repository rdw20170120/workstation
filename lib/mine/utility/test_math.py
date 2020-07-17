#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from math import isnan
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .math import Percentage
from .math import Rate


def test_percentage_01():
    v = Percentage(0, 1)
    assert v.numerator == 0
    assert v.denominator == 1
    assert v.percentage == 0.0

def test_percentage_02():
    v = Percentage(1, 1)
    assert v.numerator == 1
    assert v.denominator == 1
    assert v.percentage == 100.0

def test_percentage_03():
    v = Percentage(1, 100)
    assert v.numerator == 1
    assert v.denominator == 100
    assert v.percentage == 1.0

def test_percentage_04():
    v = Percentage(100, 1)
    assert v.numerator == 100
    assert v.denominator == 1
    assert v.percentage == 10000.0

def test_percentage_05():
    v = Percentage(-1, 1)
    assert v.numerator == -1
    assert v.denominator == 1
    assert v.percentage == -100.0

def test_percentage_06():
    v = Percentage(1, 0)
    assert v.numerator == 1
    assert v.denominator == 0
    assert isnan(v.percentage)

def test_rate_01():
    v = Rate(0, 'top', 1, 'bottom')
    assert v.numerator == 0
    assert v.numerator_units == 'top'
    assert v.denominator == 1
    assert v.denominator_units == 'bottom'
    assert v.rate == 0.0
    assert v.rate_units == 'top/bottom'

def test_rate_02():
    v = Rate(1, 'top', 1, 'bottom')
    assert v.numerator == 1
    assert v.numerator_units == 'top'
    assert v.denominator == 1
    assert v.denominator_units == 'bottom'
    assert v.rate == 1.0
    assert v.rate_units == 'top/bottom'

def test_rate_03():
    v = Rate(1, 'top', 100, 'bottom', 'tpb')
    assert v.numerator == 1
    assert v.numerator_units == 'top'
    assert v.denominator == 100
    assert v.denominator_units == 'bottom'
    assert v.rate == 0.01
    assert v.rate_units == 'tpb'

def test_rate_04():
    v = Rate(100, 'top', 1, 'bottom', 'tpb')
    assert v.numerator == 100
    assert v.numerator_units == 'top'
    assert v.denominator == 1
    assert v.denominator_units == 'bottom'
    assert v.rate == 100.0
    assert v.rate_units == 'tpb'

def test_rate_05():
    v = Rate(-1, 'top', 1, 'bottom', 'tpb')
    assert v.numerator == -1
    assert v.numerator_units == 'top'
    assert v.denominator == 1
    assert v.denominator_units == 'bottom'
    assert v.rate == -1.0
    assert v.rate_units == 'tpb'

def test_rate_06():
    v = Rate(1, 'top', 0, 'bottom', 'tpb')
    assert v.numerator == 1
    assert v.numerator_units == 'top'
    assert v.denominator == 0
    assert v.denominator_units == 'bottom'
    assert isnan(v.rate)
    assert v.rate_units == 'tpb'

'''DisabledContent
'''


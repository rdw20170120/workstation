#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from math import isnan
from math import nan

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)


class Percentage:
    def __init__(self, numerator, denominator):
        self._denominator = denominator
        self._numerator = numerator
        if denominator == 0:
            self._ratio = nan
        else:
            self._ratio = numerator / denominator

    @property
    def denominator(self):
        return self._denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def percentage(self):
        return 100.0 * self._ratio


class Rate(Percentage):
    def __init__(
        self,
        numerator,
        numerator_units,
        denominator,
        denominator_units,
        rate_units=None,
    ):
        super().__init__(numerator, denominator)
        self._denominator_units = denominator_units
        self._numerator_units = numerator_units
        self._rate_units = rate_units
        if self._rate_units is None:
            self._rate_units = "{}/{}".format(
                numerator_units, denominator_units
            )

    @property
    def denominator_units(self):
        return self._denominator_units

    @property
    def numerator_units(self):
        return self._numerator_units

    @property
    def rate(self):
        return self._ratio

    @property
    def rate_units(self):
        return self._rate_units


def assert_nan(actual_value):
    """Assert that actual_value is not-a-number (NaN)."""
    result = isnan(actual_value)
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} is NOT a not-a-number (NaN)".format(actual_value)
        )


"""DisabledContent
"""

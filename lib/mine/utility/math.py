#!/usr/bin/env false
"""
"""
from math import nan


class Percentage:
    def __init__(self, numerator, denominator):
        self._denominator = denominator
        self._numerator = numerator
        if denominator == 0: self._ratio = nan
        else: self._ratio = numerator / denominator

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
    def __init__(self,
        numerator, numerator_units,
        denominator, denominator_units,
        rate_units=None
        ):
        super().__init__(numerator, denominator)
        self._denominator_units = denominator_units
        self._numerator_units = numerator_units
        self._rate_units = rate_units
        if self._rate_units is None:
            self._rate_units = '{}/{}'.format(
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

'''DisabledContent
'''


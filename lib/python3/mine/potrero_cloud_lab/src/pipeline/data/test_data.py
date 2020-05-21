#!/bin/false

from pathlib import Path

from pytest import mark

from .encounter import CombinedEncounter
from .encounter import SingleFileEncounter

@mark.xfail(raises=KeyError,
    reason='Create useful tests for this',
    strict=True)
def test_combined_encounter():
    assert CombinedEncounter(0, {}) is not None

@mark.xfail(raises=KeyError,
    reason='Create useful tests for this',
    strict=True)
def test_single_file_encounter():
    assert SingleFileEncounter('monitor', Path(), {}) is not None


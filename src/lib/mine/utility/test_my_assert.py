#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


this_file = Path(__file__)
this_directory = this_file.parent


def test_absolute_directory():
    assert is_.absolute_directory(this_directory)
    with raises(AssertionError):
        assert is_.absolute_directory(this_file)


def test_absolute_file():
    with raises(AssertionError):
        assert is_.absolute_file(this_directory)
    assert is_.absolute_file(this_file)


def test_absolute_path():
    assert is_.absolute_path(this_directory)
    assert is_.absolute_path(this_file)


def test_equal():
    assert is_.equal(None, None)
    assert is_.equal("", "")
    assert is_.equal("Test", "Test")


def test_existing_absolute_path():
    assert is_.existing_absolute_path(this_directory)
    assert is_.existing_absolute_path(this_file)


def test_instance():
    assert is_.instance(None, type(None))

    with raises(AssertionError) as info:
        assert is_.instance(None, str)
    a = str(info.value)
    assert "Value is None" in a
    assert "<class 'str'>" in a

    assert is_.instance("", str)

    assert is_.instance(None, (type(None), str))
    assert is_.instance("", (type(None), str))
    assert is_.instance("Test", (type(None), str))


def test_not_instance():
    assert is_.not_instance(None, str)
    assert is_.not_instance(None, (bool, float, int, str))


"""DisabledContent
"""

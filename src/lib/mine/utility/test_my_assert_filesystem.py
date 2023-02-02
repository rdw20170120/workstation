#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert_filesystem as fs_is_

# Project modules   (relative references, NOT packaged, in project)


this_file = Path(__file__)
this_directory = this_file.parent


def test_absolute_directory():
    assert fs_is_.absolute_directory(this_directory)
    with raises(AssertionError):
        assert fs_is_.absolute_directory(this_file)


def test_absolute_file():
    with raises(AssertionError):
        assert fs_is_.absolute_file(this_directory)
    assert fs_is_.absolute_file(this_file)


def test_existing_absolute_path():
    assert fs_is_.existing_absolute_path(this_directory)
    assert fs_is_.existing_absolute_path(this_file)


"""DisabledContent
"""

#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert_pathname as pn_is_

# Project modules   (relative references, NOT packaged, in project)


this_file = Path(__file__)
this_directory = this_file.parent


def test_absolute_path():
    assert pn_is_.absolute_path(this_directory)
    assert pn_is_.absolute_path(this_file)


"""DisabledContent
"""

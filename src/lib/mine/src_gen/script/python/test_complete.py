#!/usr/bin/env false
"""Test corresponding source-generation module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# from pytest import fixture
# from pytest import mark
# from pytest import param
# from pytest import raises
# Library modules   (absolute references, NOT packaged, in project)
# from src_gen.common import *
from src_gen.renderer import Renderer
from utility import my_assert as is_

# from utility import my_assert_filesystem as fs_is_
# from utility import my_assert_pathname as pn_is_
# Project modules   (relative references, NOT packaged, in project)
from .complete import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_generator():
    assert is_.nonempty_string(s(generator()))


def test_generator_suite():
    assert is_.nonempty_string(s(generator_suite()))


def test_library():
    assert is_.nonempty_string(s(library()))


def test_main():
    assert is_.nonempty_string(s(main()))


def test_package():
    assert is_.nonempty_string(s(package()))


def test_script():
    assert is_.nonempty_string(s(script()))


def test_suite():
    assert is_.nonempty_string(s(suite()))


"""DisabledContent
"""

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
from .frame import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_maybe_copy_file():
    assert is_.nonempty_string(s(maybe_copy_file(None, None)))


def test_remembering():
    assert is_.nonempty_string(s(remembering(None)))


"""DisabledContent
"""

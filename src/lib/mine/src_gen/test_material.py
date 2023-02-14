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
# from .frame import *
from .material import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_bt():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(bt()), "``")
    assert is_.equal(s(bt(None)), "``")
    assert is_.equal(s(bt("")), "``")
    assert is_.equal(s(bt("Test")), "`Test`")
    assert is_.equal(s(bt("Test", "123")), "`Test123`")


def test_dq():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(dq()), '""')
    assert is_.equal(s(dq(None)), '""')
    assert is_.equal(s(dq("")), '""')
    assert is_.equal(s(dq("Test")), '"Test"')
    assert is_.equal(s(dq("Test", "123")), '"Test123"')


# TODO: def test_nvp():


def test_sq():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(sq()), "''")
    assert is_.equal(s(sq(None)), "''")
    assert is_.equal(s(sq("")), "''")
    assert is_.equal(s(sq("Test")), "'Test'")
    assert is_.equal(s(sq("Test", "123")), "'Test123'")


"""DisabledContent
"""

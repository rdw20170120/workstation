#!/usr/bin/env false
"""Test corresponding source-generation module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# from pytest import raises
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.renderer import Renderer
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .material import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize

# TODO: Expand tests for full pattern

def test_bt_00():
    assert is_.equal(s(bt()), "``")
def test_bt_01():
    assert is_.equal(s(bt(None)), "``")
def test_bt_02():
    assert is_.equal(s(bt("")), "``")
def test_bt_03():
    assert is_.equal(s(bt("Test")), "`Test`")
def test_bt_04():
    assert is_.equal(s(bt("Test", "123")), "`Test123`")


def test_dq_00():
    assert is_.equal(s(dq()), '""')
def test_dq_01():
    assert is_.equal(s(dq(None)), '""')
def test_dq_02():
    assert is_.equal(s(dq("")), '""')
def test_dq_03():
    assert is_.equal(s(dq("Test")), '"Test"')
def test_dq_04():
    assert is_.equal(s(dq("Test", "123")), '"Test123"')


# TODO: def test_nvp():


def test_sq_00():
    assert is_.equal(s(sq()), "''")
def test_sq_01():
    assert is_.equal(s(sq(None)), "''")
def test_sq_02():
    assert is_.equal(s(sq("")), "''")
def test_sq_03():
    assert is_.equal(s(sq("Test")), "'Test'")
def test_sq_04():
    assert is_.equal(s(sq("Test", "123")), "'Test123'")


"""DisabledContent
"""

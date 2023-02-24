#!/usr/bin/env false
"""Test corresponding source-generation module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from src_gen.common import *
from src_gen.renderer import Renderer
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize
will_squash = (None, "", (), [])
wont_squash = (False, True, 0, 0.0, 0j, " ", "Test", {})


def test_eol_00():
    assert is_.equal(s(eol()), "\n")


def test_eol_01():
    with raises(TypeError):
        eol(None)


def test_line_00():
    assert is_.equal(s(line()), "\n")


def test_line_01():
    assert is_.equal(s(line(None)), "\n")


def test_line_02():
    assert is_.equal(s(line("Test")), "Test\n")


def test_squashed_01():
    assert is_.equal(squashed(False), False)


def test_squashed_02():
    assert is_.equal(squashed(True), True)


def test_squashed_03():
    assert is_.equal(squashed(0), 0)


def test_squashed_04():
    assert is_.equal(squashed(0.0), 0.0)


def test_squashed_05():
    assert is_.equal(squashed(0j), 0j)


def test_squashed_06():
    assert is_.equal(squashed(" "), " ")


def test_squashed_07():
    assert is_.equal(squashed("Test"), "Test")


def test_squashed_08():
    assert is_.equal(squashed({}), {})


def test_squashed_09():
    assert is_.equal(squashed(None), None)


def test_squashed_10():
    assert is_.equal(squashed(""), None)


def test_squashed_11():
    assert is_.equal(squashed(()), None)


def test_squashed_12():
    assert is_.equal(squashed((None)), None)


def test_squashed_13():
    assert is_.equal(squashed((None,)), None)


def test_squashed_14():
    assert is_.equal(squashed((None, None)), None)


def test_squashed_15():
    assert is_.equal(squashed([None]), None)


def test_squashed_16():
    assert is_.equal(squashed([None, None]), None)


def test_squashed_17():
    for i in will_squash:
        for j in wont_squash:
            assert is_.equal(squashed((i, j)), j)
            assert is_.equal(squashed([i, j]), j)


def test_squashed_18():
    for i in wont_squash:
        for j in will_squash:
            assert is_.equal(squashed((i, j)), i)
            assert is_.equal(squashed([i, j]), i)


"""DisabledContent
"""

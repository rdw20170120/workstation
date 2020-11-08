#!/usr/bin/env false
"""TODO: Write

TODO: Generate tests
NOTE: There is little value in testing "composed" methods,
e.g., those consisting of 'return [...]'.
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules    (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Co-located modules (relative references, NOT packaged, in project)
from .source import my_visitor_map
from .structure import *
from ...renderer import Renderer


s = Renderer(my_visitor_map)._serialize


def test_header():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        header()
    assert is_.equal(s(header(None)), "# \n")
    assert is_.equal(s(header("")), "# \n")
    assert is_.equal(s(header("Test")), "# Test\n")
    with raises(TypeError):
        header("Test", None)
    with raises(TypeError):
        header("Test", "")
    with raises(TypeError):
        header("Test", "123")
    with raises(TypeError):
        header("Test", level=None)
    with raises(TypeError):
        header("Test", level="")
    with raises(TypeError):
        header("Test", level="123")
    with raises(AssertionError):
        header("Test", level=0)
    assert is_.equal(s(header("Test", level=6)), "###### Test\n")
    with raises(AssertionError):
        header("Test", level=7)


def test_h1():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        h1()
    assert is_.equal(s(h1(None)), "# \n")
    assert is_.equal(s(h1("")), "# \n")
    assert is_.equal(s(h1("Test")), "# Test\n")
    with raises(TypeError):
        h1("Test", None)


def test_h2():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        h2()
    assert is_.equal(s(h2(None)), "## \n")
    assert is_.equal(s(h2("")), "## \n")
    assert is_.equal(s(h2("Test")), "## Test\n")
    with raises(TypeError):
        h2("Test", None)


def test_numbered_list_item():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        numbered_list_item()
    assert is_.equal(s(numbered_list_item(None)), "1. \n")
    assert is_.equal(s(numbered_list_item("")), "1. \n")
    assert is_.equal(s(numbered_list_item("Test")), "1. Test\n")
    with raises(TypeError):
        numbered_list_item("Test", None)
    with raises(TypeError):
        numbered_list_item("Test", "")
    with raises(TypeError):
        numbered_list_item("Test", "123")
    with raises(AssertionError):
        numbered_list_item("Test", level=-1)
    assert is_.equal(
        s(numbered_list_item("Test", level=9)), 9 * 3 * " " + "1. Test\n"
    )
    with raises(AssertionError):
        numbered_list_item("Test", level=10)


def test_nli0():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        nli0()
    assert is_.equal(s(nli0(None)), "1. \n")
    assert is_.equal(s(nli0("")), "1. \n")
    assert is_.equal(s(nli0("Test")), "1. Test\n")
    with raises(TypeError):
        nli0("Test", None)


def test_note():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        note()
    assert is_.equal(s(note(None)), "NOTE: \n")
    assert is_.equal(s(note("")), "NOTE: \n")
    assert is_.equal(s(note("Test")), "NOTE: Test\n")
    with raises(TypeError):
        note("Test", None)


def test_table_header():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(table_header()), "||\n")
    assert is_.equal(s(table_header(None)), "||\n")
    assert is_.equal(s(table_header("")), "||\n")
    assert is_.equal(s(table_header("Test")), "|Test|\n")
    assert is_.equal(s(table_header("Test", None)), "|Test|\n")
    assert is_.equal(s(table_header("Test", "")), "|Test|\n")
    assert is_.equal(s(table_header("Test", "123")), "|Test|123|\n")


def test_table_row():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(table_row()), "||\n")
    assert is_.equal(s(table_row(None)), "||\n")
    assert is_.equal(s(table_row("")), "||\n")
    assert is_.equal(s(table_row("Test")), "|Test|\n")
    assert is_.equal(s(table_row("Test", None)), "|Test|\n")
    assert is_.equal(s(table_row("Test", "")), "|Test|\n")
    assert is_.equal(s(table_row("Test", "123")), "|Test|123|\n")


def test_table_ruler():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(table_ruler()), "||\n")
    assert is_.equal(s(table_ruler(None)), "||\n")
    assert is_.equal(s(table_ruler("")), "||\n")
    assert is_.equal(s(table_ruler("Test")), "|Test|\n")
    assert is_.equal(s(table_ruler("Test", None)), "|Test|\n")
    assert is_.equal(s(table_ruler("Test", "")), "|Test|\n")
    assert is_.equal(s(table_ruler("Test", "123")), "|Test|123|\n")


"""DisabledContent
"""

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
from .material import *
from .material import s as material_s
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_h1_00():
    with raises(TypeError):
        h1()


def test_h1_01():
    assert is_.equal(s(h1(None)), "# \n")


def test_h1_02():
    assert is_.equal(s(h1("")), "# \n")


def test_h1_03():
    assert is_.equal(s(h1("Test")), "# Test\n")


def test_h1_04():
    with raises(TypeError):
        h1("Test", None)


def test_h2_00():
    with raises(TypeError):
        h2()


def test_h2_01():
    assert is_.equal(s(h2(None)), "## \n")


def test_h2_02():
    assert is_.equal(s(h2("")), "## \n")


def test_h2_03():
    assert is_.equal(s(h2("Test")), "## Test\n")


def test_h2_04():
    with raises(TypeError):
        h2("Test", None)


def test_header_00():
    with raises(TypeError):
        header()


def test_header_01():
    assert is_.equal(s(header(None)), "# \n")


def test_header_02():
    assert is_.equal(s(header("")), "# \n")


def test_header_03():
    assert is_.equal(s(header("Test")), "# Test\n")


def test_header_04():
    with raises(TypeError):
        header("Test", None)


def test_header_05():
    with raises(TypeError):
        header("Test", "")


def test_header_06():
    with raises(TypeError):
        header("Test", "123")


def test_header_07():
    with raises(TypeError):
        header("Test", level=None)


def test_header_08():
    with raises(TypeError):
        header("Test", level="")


def test_header_09():
    with raises(TypeError):
        header("Test", level="123")


def test_header_10():
    with raises(AssertionError):
        header("Test", level=0)


def test_header_11():
    assert is_.equal(s(header("Test", level=6)), "###### Test\n")


def test_header_12():
    with raises(AssertionError):
        header("Test", level=7)


def test_numbered_list_item_00():
    with raises(TypeError):
        numbered_list_item()


def test_numbered_list_item_01():
    assert is_.equal(s(numbered_list_item(None)), "1. \n")


def test_numbered_list_item_02():
    assert is_.equal(s(numbered_list_item("")), "1. \n")


def test_numbered_list_item_03():
    assert is_.equal(s(numbered_list_item("Test")), "1. Test\n")


def test_numbered_list_item_04():
    with raises(TypeError):
        numbered_list_item("Test", None)


def test_numbered_list_item_05():
    with raises(TypeError):
        numbered_list_item("Test", "")


def test_numbered_list_item_06():
    with raises(TypeError):
        numbered_list_item("Test", "123")


def test_numbered_list_item_07():
    with raises(AssertionError):
        numbered_list_item("Test", level=-1)


def test_numbered_list_item_08():
    assert is_.equal(s(numbered_list_item("Test", level=9)), 9 * 3 * " " + "1. Test\n")


def test_numbered_list_item_09():
    with raises(AssertionError):
        numbered_list_item("Test", level=10)


def test_nli0_00():
    with raises(TypeError):
        nli0()


def test_nli0_01():
    assert is_.equal(s(nli0(None)), "1. \n")


def test_nli0_02():
    assert is_.equal(s(nli0("")), "1. \n")


def test_nli0_03():
    assert is_.equal(s(nli0("Test")), "1. Test\n")


def test_nli0_04():
    with raises(TypeError):
        nli0("Test", None)


def test_note_00():
    with raises(TypeError):
        note()


def test_note_01():
    assert is_.equal(s(note(None)), "NOTE: \n")


def test_note_02():
    assert is_.equal(s(note("")), "NOTE: \n")


def test_note_03():
    assert is_.equal(s(note("Test")), "NOTE: Test\n")


def test_note_04():
    with raises(TypeError):
        note("Test", None)


def test_s_00():
    assert is_.equal(s(material_s(None)), "\n")


def test_s_01():
    assert is_.equal(s(material_s("")), "\n")


def test_s_02():
    assert is_.equal(s(material_s("text")), "text\n")


def test_s_03():
    assert is_.equal(s(material_s(0)), "0\n")


def test_table_header_00():
    assert is_.equal(s(table_header()), "||\n")


def test_table_header_01():
    assert is_.equal(s(table_header(None)), "||\n")


def test_table_header_02():
    assert is_.equal(s(table_header("")), "||\n")


def test_table_header_03():
    assert is_.equal(s(table_header("Test")), "|Test|\n")


def test_table_header_04():
    assert is_.equal(s(table_header("Test", None)), "|Test|\n")


def test_table_header_05():
    assert is_.equal(s(table_header("Test", "")), "|Test|\n")


def test_table_header_06():
    assert is_.equal(s(table_header("Test", "123")), "|Test|123|\n")


def test_table_row_00():
    assert is_.equal(s(table_row()), "||\n")


def test_table_row_01():
    assert is_.equal(s(table_row(None)), "||\n")


def test_table_row_02():
    assert is_.equal(s(table_row("")), "||\n")


def test_table_row_03():
    assert is_.equal(s(table_row("Test")), "|Test|\n")


def test_table_row_04():
    assert is_.equal(s(table_row("Test", None)), "|Test|\n")


def test_table_row_05():
    assert is_.equal(s(table_row("Test", "")), "|Test|\n")


def test_table_row_06():
    assert is_.equal(s(table_row("Test", "123")), "|Test|123|\n")


def test_table_row_repr():
    assert is_.equal(repr(table_row("Test", "123")), "TableRow(['Test', '123'])")


def test_table_ruler_00():
    assert is_.equal(s(table_ruler()), "||\n")


def test_table_ruler_01():
    assert is_.equal(s(table_ruler(None)), "||\n")


def test_table_ruler_02():
    assert is_.equal(s(table_ruler("")), "||\n")


def test_table_ruler_03():
    assert is_.equal(s(table_ruler("Test")), "|Test|\n")


def test_table_ruler_04():
    assert is_.equal(s(table_ruler("Test", None)), "|Test|\n")


def test_table_ruler_05():
    assert is_.equal(s(table_ruler("Test", "")), "|Test|\n")


def test_table_ruler_06():
    assert is_.equal(s(table_ruler("Test", "123")), "|Test|123|\n")


"""DisabledContent
"""

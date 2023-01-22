#!/usr/bin/env false
"""Test Python fundamentals."""
# Internal packages (absolute references, distributed with Python)
from keyword import kwlist
from sys import version_info

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


def test_python_version():
    assert is_.not_none(version_info)
    assert is_.equal(version_info.major, 3)
    assert is_.at_least(version_info.minor, 6)


def test_kwlist_len():
    assert is_.equal(version_info.major, 3)
    if version_info.minor == 6:
        assert is_.equal(len(kwlist), 33)
    elif version_info.minor == 7:
        assert is_.equal(len(kwlist), 35)
    elif version_info.minor == 8:
        assert is_.equal(len(kwlist), 35)
    elif version_info.minor == 9:
        assert is_.equal(len(kwlist), 36)
    elif version_info.minor == 10:
        assert is_.equal(len(kwlist), 36)
    elif version_info.minor == 11:
        assert is_.equal(len(kwlist), 35)
    else:
        assert False, "No test case for Python version {}".format(version_info)


def test_kwlist_has_false():
    assert is_.in_("False", kwlist)


def test_kwlist_has_none():
    assert is_.in_("None", kwlist)


def test_kwlist_has_true():
    assert is_.in_("True", kwlist)


def test_kwlist_has_and():
    assert is_.in_("and", kwlist)


def test_kwlist_has_as():
    assert is_.in_("as", kwlist)


def test_kwlist_has_assert():
    assert is_.in_("assert", kwlist)


def test_kwlist_has_break():
    assert is_.in_("break", kwlist)


def test_kwlist_has_class():
    assert is_.in_("class", kwlist)


def test_kwlist_has_continue():
    assert is_.in_("continue", kwlist)


def test_kwlist_has_def():
    assert is_.in_("def", kwlist)


def test_kwlist_has_del():
    assert is_.in_("del", kwlist)


def test_kwlist_has_elif():
    assert is_.in_("elif", kwlist)


def test_kwlist_has_else():
    assert is_.in_("else", kwlist)


def test_kwlist_has_except():
    assert is_.in_("except", kwlist)


def test_kwlist_has_finally():
    assert is_.in_("finally", kwlist)


def test_kwlist_has_for():
    assert is_.in_("for", kwlist)


def test_kwlist_has_from():
    assert is_.in_("from", kwlist)


def test_kwlist_has_global():
    assert is_.in_("global", kwlist)


def test_kwlist_has_if():
    assert is_.in_("if", kwlist)


def test_kwlist_has_import():
    assert is_.in_("import", kwlist)


def test_kwlist_has_in():
    assert is_.in_("in", kwlist)


def test_kwlist_has_is():
    assert is_.in_("is", kwlist)


def test_kwlist_has_lambda():
    assert is_.in_("lambda", kwlist)


def test_kwlist_has_nonlocal():
    assert is_.in_("nonlocal", kwlist)


def test_kwlist_has_not():
    assert is_.in_("not", kwlist)


def test_kwlist_has_or():
    assert is_.in_("or", kwlist)


def test_kwlist_has_pass():
    assert is_.in_("pass", kwlist)


def test_kwlist_has_raise():
    assert is_.in_("raise", kwlist)


def test_kwlist_has_return():
    assert is_.in_("return", kwlist)


def test_kwlist_has_try():
    assert is_.in_("try", kwlist)


def test_kwlist_has_while():
    assert is_.in_("while", kwlist)


def test_kwlist_has_with():
    assert is_.in_("with", kwlist)


def test_kwlist_has_yield():
    assert is_.in_("yield", kwlist)


"""DisabledContent
"""

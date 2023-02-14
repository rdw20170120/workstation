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


def test_abort_script():
    assert is_.nonempty_string(s(abort_script()))


def test_debugging_comment():
    assert is_.nonempty_string(s(debugging_comment()))


def test_disable_tracing_unless_maximal():
    assert is_.nonempty_string(s(disable_tracing_unless_maximal()))


def test_disabled_content_footer():
    assert is_.nonempty_string(s(disabled_content_footer()))


def test_enable_tracing_unless_minimal():
    assert is_.nonempty_string(s(enable_tracing_unless_minimal()))


def test_export_if_null():
    assert is_.nonempty_string(s(export_if_null(None, None)))


def test_exported_function():
    assert is_.nonempty_string(s(exported_function("Test", [])))


def test_header_executed():
    assert is_.nonempty_string(s(header_executed()))


def test_header_sourced():
    assert is_.nonempty_string(s(header_sourced()))


def test_maybe_source():
    assert is_.nonempty_string(s(maybe_source(None)))


def test_maybe_source_or_abort():
    assert is_.nonempty_string(s(maybe_source_or_abort(None, None, None)))


def test_source_or_abort():
    assert is_.nonempty_string(s(source_or_abort(None)))


def test_tracing_in_header():
    assert is_.nonempty_string(s(tracing_in_header()))


"""DisabledContent
"""

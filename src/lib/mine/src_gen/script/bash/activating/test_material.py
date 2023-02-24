#!/usr/bin/env false
"""Test corresponding source-generation module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from src_gen.renderer import Renderer
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .material import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_log_debug_00():
    assert is_.equal(s(log_debug()), 'log_debug ""')


def test_log_debug_01():
    assert is_.equal(s(log_debug(None)), 'log_debug ""')


def test_log_debug_02():
    assert is_.equal(s(log_debug("")), 'log_debug ""')


def test_log_debug_03():
    assert is_.equal(s(log_debug("Test")), 'log_debug "Test"')


def test_log_debug_03():
    assert is_.equal(s(log_debug("Test", None)), 'log_debug "Test"')


def test_log_debug_04():
    assert is_.equal(s(log_debug("Test", "")), 'log_debug "Test"')


def test_log_debug_05():
    assert is_.equal(s(log_debug("Test", "123")), 'log_debug "Test123"')


def test_log_error_00():
    assert is_.equal(s(log_error()), 'log_error ""')


def test_log_error_01():
    assert is_.equal(s(log_error(None)), 'log_error ""')


def test_log_error_02():
    assert is_.equal(s(log_error("")), 'log_error ""')


def test_log_error_03():
    assert is_.equal(s(log_error("Test")), 'log_error "Test"')


def test_log_error_04():
    assert is_.equal(s(log_error("Test", None)), 'log_error "Test"')


def test_log_error_05():
    assert is_.equal(s(log_error("Test", "")), 'log_error "Test"')


def test_log_error_06():
    assert is_.equal(s(log_error("Test", "123")), 'log_error "Test123"')


def test_log_good_00():
    assert is_.equal(s(log_good()), 'log_good ""')


def test_log_good_01():
    assert is_.equal(s(log_good(None)), 'log_good ""')


def test_log_good_02():
    assert is_.equal(s(log_good("")), 'log_good ""')


def test_log_good_03():
    assert is_.equal(s(log_good("Test")), 'log_good "Test"')


def test_log_good_04():
    assert is_.equal(s(log_good("Test", None)), 'log_good "Test"')


def test_log_good_05():
    assert is_.equal(s(log_good("Test", "")), 'log_good "Test"')


def test_log_good_06():
    assert is_.equal(s(log_good("Test", "123")), 'log_good "Test123"')


def test_log_info_00():
    assert is_.equal(s(log_info()), 'log_info ""')


def test_log_info_01():
    assert is_.equal(s(log_info(None)), 'log_info ""')


def test_log_info_02():
    assert is_.equal(s(log_info("")), 'log_info ""')


def test_log_info_03():
    assert is_.equal(s(log_info("Test")), 'log_info "Test"')


def test_log_info_04():
    assert is_.equal(s(log_info("Test", None)), 'log_info "Test"')


def test_log_info_05():
    assert is_.equal(s(log_info("Test", "")), 'log_info "Test"')


def test_log_info_06():
    assert is_.equal(s(log_info("Test", "123")), 'log_info "Test123"')


def test_log_warn_00():
    assert is_.equal(s(log_warn()), 'log_warn ""')


def test_log_warn_01():
    assert is_.equal(s(log_warn(None)), 'log_warn ""')


def test_log_warn_02():
    assert is_.equal(s(log_warn("")), 'log_warn ""')


def test_log_warn_03():
    assert is_.equal(s(log_warn("Test")), 'log_warn "Test"')


def test_log_warn_04():
    assert is_.equal(s(log_warn("Test", None)), 'log_warn "Test"')


def test_log_warn_05():
    assert is_.equal(s(log_warn("Test", "")), 'log_warn "Test"')


def test_log_warn_06():
    assert is_.equal(s(log_warn("Test", "123")), 'log_warn "Test123"')


# TODO: def test_header_executed():
# TODO: def test_header_sourced():

"""DisabledContent
"""

#!/usr/bin/env false
"""Test corresponding source-generation module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# from pytest import fixture
# from pytest import mark
# from pytest import param
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
# from src_gen.common import *
# from src_gen.script.bash.material import *
from src_gen.renderer import Renderer
from utility import my_assert as is_

# from utility import my_assert_filesystem as fs_is_
# from utility import my_assert_pathname as pn_is_
# Project modules   (relative references, NOT packaged, in project)
# from .frame import *
from .material import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_log_debug():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(log_debug()), 'log_debug ""')
    assert is_.equal(s(log_debug(None)), 'log_debug ""')
    assert is_.equal(s(log_debug("")), 'log_debug ""')
    assert is_.equal(s(log_debug("Test")), 'log_debug "Test"')
    assert is_.equal(s(log_debug("Test", None)), 'log_debug "Test"')
    assert is_.equal(s(log_debug("Test", "")), 'log_debug "Test"')
    assert is_.equal(s(log_debug("Test", "123")), 'log_debug "Test123"')


def test_log_error():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(log_error()), 'log_error ""')
    assert is_.equal(s(log_error(None)), 'log_error ""')
    assert is_.equal(s(log_error("")), 'log_error ""')
    assert is_.equal(s(log_error("Test")), 'log_error "Test"')
    assert is_.equal(s(log_error("Test", None)), 'log_error "Test"')
    assert is_.equal(s(log_error("Test", "")), 'log_error "Test"')
    assert is_.equal(s(log_error("Test", "123")), 'log_error "Test123"')


def test_log_good():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(log_good()), 'log_good ""')
    assert is_.equal(s(log_good(None)), 'log_good ""')
    assert is_.equal(s(log_good("")), 'log_good ""')
    assert is_.equal(s(log_good("Test")), 'log_good "Test"')
    assert is_.equal(s(log_good("Test", None)), 'log_good "Test"')
    assert is_.equal(s(log_good("Test", "")), 'log_good "Test"')
    assert is_.equal(s(log_good("Test", "123")), 'log_good "Test123"')


def test_log_info():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(log_info()), 'log_info ""')
    assert is_.equal(s(log_info(None)), 'log_info ""')
    assert is_.equal(s(log_info("")), 'log_info ""')
    assert is_.equal(s(log_info("Test")), 'log_info "Test"')
    assert is_.equal(s(log_info("Test", None)), 'log_info "Test"')
    assert is_.equal(s(log_info("Test", "")), 'log_info "Test"')
    assert is_.equal(s(log_info("Test", "123")), 'log_info "Test123"')


def test_log_warn():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(log_warn()), 'log_warn ""')
    assert is_.equal(s(log_warn(None)), 'log_warn ""')
    assert is_.equal(s(log_warn("")), 'log_warn ""')
    assert is_.equal(s(log_warn("Test")), 'log_warn "Test"')
    assert is_.equal(s(log_warn("Test", None)), 'log_warn "Test"')
    assert is_.equal(s(log_warn("Test", "")), 'log_warn "Test"')
    assert is_.equal(s(log_warn("Test", "123")), 'log_warn "Test123"')


# TODO: def test_header_executed():
# TODO: def test_header_sourced():

"""DisabledContent
"""

#!/usr/bin/env false
"""Test corresponding source-generation module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.renderer import Renderer
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .frame import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_abort_if_not_activated(config):
    assert is_.nonempty_string(s(abort_if_not_activated(config)))


def test_maybe_copy_file():
    assert is_.nonempty_string(s(maybe_copy_file(None, None)))


def test_header_executed(config):
    assert is_.nonempty_string(s(header_executed(config)))


def test_header_sourced(config):
    assert is_.nonempty_string(s(header_sourced(config)))


"""DisabledContent
"""

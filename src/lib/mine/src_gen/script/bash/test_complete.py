#!/usr/bin/env false
"""Test corresponding source-generation module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.renderer import Renderer
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .complete import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_executed():
    assert is_.nonempty_string(s(executed()))


def test_sourced():
    assert is_.nonempty_string(s(sourced()))


"""DisabledContent
"""

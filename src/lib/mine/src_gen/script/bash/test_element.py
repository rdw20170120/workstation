#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from src_gen.common import *
from src_gen.renderer import Renderer
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .element import *
from .render import my_visitor_map


# TODO: Generate tests

s = Renderer(my_visitor_map)._serialize


def test_and_():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(and_()), " &&")
    with raises(TypeError):
        and_(None)


def test_bs():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(bs()), "\\\n")
    with raises(TypeError):
        bs(None)


def test_or_():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(or_()), " || ")
    with raises(TypeError):
        or_(None)


def test_pipe():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(pipe()), " | ")
    with raises(TypeError):
        pipe(None)


def test_seq():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(seq()), " ; ")
    with raises(TypeError):
        seq(None)


"""DisabledContent
"""

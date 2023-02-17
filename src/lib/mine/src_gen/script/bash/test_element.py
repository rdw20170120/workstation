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
from .element import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_and_00():
    assert is_.equal(s(and_()), " &&")
def test_and_01():
    with raises(TypeError):
        and_(None)


def test_bs_00():
    assert is_.equal(s(bs()), "\\\n")
def test_bs_01():
    with raises(TypeError):
        bs(None)


def test_or_00():
    assert is_.equal(s(or_()), " || ")
def test_or_01():
    with raises(TypeError):
        or_(None)


def test_pipe_00():
    assert is_.equal(s(pipe()), " | ")
def test_pipe_01():
    with raises(TypeError):
        pipe(None)


def test_seq_00():
    assert is_.equal(s(seq()), " ; ")
def test_seq_01():
    with raises(TypeError):
        seq(None)


"""DisabledContent
"""

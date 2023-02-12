#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from enum import Enum
from numbers import Number
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.common import *
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .render import my_visitor_map


class BacktickQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "BacktickQuoted({})".format(self.elements)


class DoubleQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "DoubleQuoted({})".format(self.elements)


class NameValuePair(object):
    def __init__(self, name, value):
        super().__init__()
        self.name = squashed(name)
        self.value = squashed(value)
        assert is_.not_none(self.name)

    def __repr__(self):
        return "NameValuePair({}, {})".format(self.name, self.value)


class SingleQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "SingleQuoted({})".format(self.elements)


@my_visitor_map.register(BacktickQuoted)
def _visit_backtick_quoted(element, walker):
    walker.emit("`")
    walker.walk(element.elements)
    walker.emit("`")


@my_visitor_map.register(DoubleQuoted)
def _visit_double_quoted(element, walker):
    walker.emit('"')
    walker.walk(element.elements)
    walker.emit('"')


@my_visitor_map.register(Enum)
def _visit_enum(element, walker):
    walker.walk(element.value)


@my_visitor_map.register(NameValuePair)
def _visit_name_value_pair(element, walker):
    walker.walk(element.name)
    walker.emit(" = ")
    walker.walk(element.value)


@my_visitor_map.register(SingleQuoted)
def _visit_single_quoted(element, walker):
    walker.emit("'")
    walker.walk(element.elements)
    walker.emit("'")


"""DisabledContent
"""


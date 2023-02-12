#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from enum import Enum
from numbers import Number
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .render import my_visitor_map


class _BacktickQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "_BacktickQuoted({})".format(self.elements)


class _DoubleQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "_DoubleQuoted({})".format(self.elements)


class _NameValuePair(object):
    def __init__(self, name, value):
        super().__init__()
        self.name = squashed(name)
        self.value = squashed(value)
        assert is_.not_none(self.name)

    def __repr__(self):
        return "_NameValuePair({}, {})".format(self.name, self.value)


class _SingleQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "_SingleQuoted({})".format(self.elements)


@my_visitor_map.register(_BacktickQuoted)
def _visit_backtick_quoted(element, walker):
    walker.emit("`")
    walker.walk(element.elements)
    walker.emit("`")


@my_visitor_map.register(_DoubleQuoted)
def _visit_double_quoted(element, walker):
    walker.emit('"')
    walker.walk(element.elements)
    walker.emit('"')


@my_visitor_map.register(Enum)
def _visit_enum(element, walker):
    walker.walk(element.value)


@my_visitor_map.register(_NameValuePair)
def _visit_name_value_pair(element, walker):
    walker.walk(element.name)
    walker.emit(" = ")
    walker.walk(element.value)


@my_visitor_map.register(_SingleQuoted)
def _visit_single_quoted(element, walker):
    walker.emit("'")
    walker.walk(element.elements)
    walker.emit("'")


"""DisabledContent
"""


#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from enum import Enum
from numbers import Number
from pathlib import Path

# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Co-located modules (relative references, NOT packaged, in project)
from .source import my_visitor_map


###############################################################################


def is_nonstring_iterable(value):
    if isinstance(value, str):
        return False
    if hasattr(value, "__iter__"):
        return True
    return False


def squashed(value):
    """Return `value`, having squashed all empty contents to `None`.

    Pass through all booleans, all numbers including zeros, all nonempty
    strings, all dictionaries, anything not explicitly recognized.  Squash
    empty strings and empty sequences.  Return a nonempty sequence (excluding
    dictionaries) as a squashed list in which all items have been squashed.
    Assume no circular references.
    """
    #   print("squashed began with: '{}'".format(value))
    if value is None:
        #       print("squashed ended with: '{}'".format(None))
        return None
    if value == "":
        #       print("squashed ended with: '{}'".format(None))
        return None
    if value == ():
        #       print("squashed ended with: '{}'".format(None))
        return None
    if value == []:
        #       print("squashed ended with: '{}'".format(None))
        return None
    if isinstance(value, dict):
        #       print("squashed ended with: '{}'".format(value))
        return value
    if not is_nonstring_iterable(value):
        #       print("squashed ended with: '{}'".format(value))
        return value
    else:
        result = []
        for i in value:
            j = squashed(i)
            if j is not None:
                result.append(j)
        if len(result) == 0:
            result = None
        elif len(result) == 1:
            result = result[0]
        #       print("squashed ended with: '{}'".format(result))
        return result


###############################################################################


def eol():
    return "\n"


def line(*text):
    return [text, eol()]


###############################################################################


class _BacktickQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "_BacktickQuoted({})".format(self.elements)


@my_visitor_map.register(_BacktickQuoted)
def _visit_backtick_quoted(element, walker):
    walker.emit("`")
    walker.walk(element.elements)
    walker.emit("`")


def bt(*element):
    return _BacktickQuoted(element)


###############################################################################


class _DoubleQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "_DoubleQuoted({})".format(self.elements)


@my_visitor_map.register(_DoubleQuoted)
def _visit_double_quoted(element, walker):
    walker.emit('"')
    walker.walk(element.elements)
    walker.emit('"')


def dq(*element):
    return _DoubleQuoted(element)


###############################################################################


@my_visitor_map.register(Enum)
def _visit_content(element, walker):
    walker.walk(element.value)


###############################################################################


class _SingleQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "_SingleQuoted({})".format(self.elements)


@my_visitor_map.register(_SingleQuoted)
def _visit_single_quoted(element, walker):
    walker.emit("'")
    walker.walk(element.elements)
    walker.emit("'")


def sq(*element):
    return _SingleQuoted(element)


###############################################################################


class _NameValuePair(object):
    def __init__(self, name, value):
        super().__init__()
        self.name = squashed(name)
        self.value = squashed(value)
        assert is_.not_none(self.name)

    def __repr__(self):
        return "_NameValuePair({}, {})".format(self.name, self.value)


@my_visitor_map.register(_NameValuePair)
def _visit_name_value_pair(element, walker):
    walker.walk(element.name)
    walker.emit(" = ")
    walker.walk(element.value)


def nvp(name, value):
    return _NameValuePair(name, value)


"""DisabledContent
"""

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


def bt(*element):
    return _BacktickQuoted(element)


def dq(*element):
    return _DoubleQuoted(element)


def eol():
    return "\n"


def is_nonstring_iterable(value):
    if isinstance(value, str):
        return False
    if hasattr(value, "__iter__"):
        return True
    return False


def line(*text):
    return [text, eol()]


def nvp(name, value):
    return _NameValuePair(name, value)


def sq(*element):
    return _SingleQuoted(element)


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


"""DisabledContent
"""

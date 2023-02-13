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
from .frame import *


def bt(*element):
    return BacktickQuoted(element)


def dq(*element):
    return DoubleQuoted(element)


def nvp(name, value):
    return NameValuePair(name, value)


def sq(*element):
    return SingleQuoted(element)


"""DisabledContent
"""

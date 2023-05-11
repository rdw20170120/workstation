#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.material import *
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .frame import *


def h1(title):
    return header(title, level=1)


def h2(title):
    return header(title, level=2)


def header(title, level=1):
    assert is_.range(level, 1, 6)
    return line([level * "#", " ", title])


def nli0(text):
    return numbered_list_item(text, level=0)


def note(sentence):
    return line(["NOTE: ", sentence])


def numbered_list_item(text, level=0):
    # TODO: Consider restructing this to compute final content upon rendering
    assert is_.range(level, 0, 9)
    prefix = "1. "
    indent = len(prefix) * " "
    return line([level * indent, prefix, text])


def s(sentence):
    return line(sentence)


def table_header(*column):
    return TableRow(column)


def table_row(*column):
    return TableRow(column)


def table_ruler(*column):
    return TableRow(column)


"""DisabledContent
"""

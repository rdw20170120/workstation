#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.structure import *
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .source import my_visitor_map


###############################################################################


def header(title, level=1):
    assert is_.range(level, 1, 6)
    return line([level * "#", " ", title])


def h1(title):
    return header(title, level=1)


def h2(title):
    return header(title, level=2)


def numbered_list_item(text, level=0):
    # TODO: Consider restructing this to compute final content upon rendering
    assert is_.range(level, 0, 9)
    prefix = "1. "
    indent = len(prefix) * " "
    return line([level * indent, prefix, text])


def nli0(text):
    return numbered_list_item(text, level=0)


def note(sentence):
    return line(["NOTE: ", sentence])


def s(sentence):
    return line(sentence)


###############################################################################


class _TableRow(object):
    def __init__(self, *column):
        super().__init__()
        self.columns = squashed(column)

    def __repr__(self):
        return "_TableRow({})".format(self.columns)


@my_visitor_map.register(_TableRow)
def _visit_table_row(element, walker):
    if is_nonstring_iterable(element.columns):
        for c in element.columns:
            walker.emit("|")
            walker.walk(c)
    else:
        walker.emit("|")
        walker.walk(element.columns)
    walker.emit("|")
    walker.walk(eol())


def table_header(*column):
    return _TableRow(column)


def table_row(*column):
    return _TableRow(column)


def table_ruler(*column):
    return _TableRow(column)


"""DisabledContent
"""

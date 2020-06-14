#!/usr/bin/env false
"""
"""
from pathlib import Path

from ...structure import *
from .source      import visitor_map


###############################################################################

def header(title, level=1):
    assert title
    assert 1 <= level <= 6
    return line([level * '#', ' ', title])

def h1(title): return header(title, level=1)

def h2(title): return header(title, level=2)

def numbered_list_item(text, level=0):
    # TODO: Consider restructing this to compute final content upon rendering
    assert text
    assert 0 <= level <= 9
    prefix = '1. '
    indent = len(prefix) * ' '
    return line([level * indent, prefix, text])

def nli0(text): return numbered_list_item(text, level=0)

def note(sentence):
    assert sentence
    return line(['NOTE: ', sentence])

def s(sentence):
    assert sentence
    return line(sentence)

###############################################################################


class _TableRow(object):
    def __init__(self, *column):
        super().__init__()
        self.columns = squashed(column)
        assert self.columns

    def __repr__(self):
        return "_TableRow({})".format(self.columns)


@visitor_map.register(_TableRow)
def _visit_table_row(element, walker):
    if is_nonstring_iterable(element.columns):
        for c in element.columns:
            walker.emit('|')
            walker.walk(c)
    elif element.columns is None:
        pass
    else:
        walker.emit('|')
        walker.walk(element.columns)
    walker.emit('|')
    walker.walk(eol())

def table_header(*column):
    assert column
    return _TableRow(column)

def table_row(*column):
    assert column
    return _TableRow(column)

def table_ruler(*column):
    assert column
    return _TableRow(column)

'''DisabledContent
'''


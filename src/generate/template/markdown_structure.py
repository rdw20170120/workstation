from pathlib import Path

from .content_structure import *
from .content_structure import _ContentElement
from .markdown          import visitor_map

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


class _TableRow(_ContentElement):
    def __init__(self, column, typename='_TableRow'):
        super().__init__(column, typename)
        assert self.content


@visitor_map.register(_TableRow)
def _visit_table_row(element, walker):
    as_list = element.content_as_list()
    if as_list is not None:
        for c in as_list:
            if c is not None:
                walker.emit('|')
                walker.walk(c)
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


''' Disabled content
'''

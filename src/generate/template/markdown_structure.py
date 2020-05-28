from pathlib import Path

from .content_structure import *
from .markdown          import visitor_map

###############################################################################

def header(title, level=1): return line([level * '#', ' ', title])

def h1(title): return header(title, level=1)

def h2(title): return header(title, level=2)

def numbered_list_item(text, level=0):
    prefix = '1. '
    indent = len(prefix) * ' '
    return line([level * indent, prefix, text])

def nli0(text): return numbered_list_item(text, level=0)

def note(sentence): return line(['NOTE: ', sentence])

def s(sentence): return line(sentence)

###############################################################################

class _TableRow(object):
    def __init__(self, *column):
        super().__init__()
        self.columns = column

@visitor_map.register(_TableRow)
def _visit_table_row(element, walker):
    if element.columns is not None:
        for c in element.columns:
            walker.emit('|')
            walker.walk(c)
        walker.emit('|')
        walker.emit('\n')

def table_header(*column):
    return _TableRow(*column)

def table_row(*column):
    return _TableRow(*column)

def table_ruler(*column):
    return _TableRow(*column)

###############################################################################

''' Disabled content
'''

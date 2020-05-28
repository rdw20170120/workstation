from enum import Enum

from .content import visitor_map

###############################################################################

@visitor_map.register(Enum)
def _visit_content(content, walker):
    walker.walk(content.value)

###############################################################################

def eol(text=None): return [text, '\n']

def line(text=None): return eol(text)

###############################################################################

class _DoubleQuoted(object):
    def __init__(self, *element):
        super().__init__()
        self.content = element

@visitor_map.register(_DoubleQuoted)
def _visit_double_quoted(element, walker):
    walker.emit('"')
    walker.walk(element.content)
    walker.emit('"')

def dq(*element):
    return _DoubleQuoted(*element)

###############################################################################

class _SingleQuoted(object):
    def __init__(self, *element):
        super().__init__()
        self.content = element

@visitor_map.register(_SingleQuoted)
def _visit_single_quoted(element, walker):
    walker.emit("'")
    walker.walk(element.content)
    walker.emit("'")

def sq(*element):
    return _SingleQuoted(*element)

###############################################################################

class _BacktickQuoted(object):
    def __init__(self, *element):
        super().__init__()
        self.content = element

@visitor_map.register(_BacktickQuoted)
def _visit_backtick_quoted(element, walker):
    walker.emit("`")
    walker.walk(element.content)
    walker.emit("`")

def bt(*element):
    return _BacktickQuoted(*element)

###############################################################################

''' Disabled content

# TODO: RESEARCH: Does this need conversion for Python3?
import itertools

def flatten_via_chain(list_):
    return list(itertools.chain.from_iterable(*list_))

def flatten(sequence, types=(list, tuple)):
    """ Flatten sequence made of types, returned as the same outer type as sequence.
    REF: http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
    """
    sequence_type = type(sequence)
    sequence = list(sequence)
    i = 0
    while i < len(sequence):
        while isinstance(sequence[i], types):
            if not sequence[i]:
                sequence.pop(i)
                i -= 1
                break
            else:
                sequence[i:i + 1] = sequence[i]
        i += 1
    return sequence_type(sequence)

'''

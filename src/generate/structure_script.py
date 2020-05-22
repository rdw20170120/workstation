# TODO: RESEARCH: Does this need conversion for Python3?
import itertools

from .script import visitor_map


####################################################################################################

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

####################################################################################################

class _Statement(object):
    def __init__(self, statement):
        object.__init__(self)
        self.statement = statement

@visitor_map.register(_Statement)
def visit_statement(element, walker):
    walker.walk(element.statement)

####################################################################################################

class _Comment(_Statement):
    def __init__(self, *element):
        _Statement.__init__(self, '_Comment')
        self.content = element

@visitor_map.register(_Comment)
def visit_comment(element, walker):
    walker.emit('#')
    if isinstance(element.content, tuple):
        if len(element.content) > 0:
            walker.emit(' ')
            walker.walk(element.content)
    walker.emit('\n')

def comment(*element):
    return _Comment(*element)

####################################################################################################

class _Shebang(_Comment):
    def __init__(self, content):
        _Comment.__init__(self, content)

@visitor_map.register(_Shebang)
def visit_comment(element, walker):
    walker.emit('#!')
    walker.walk(element.content)
    walker.emit('\n')

####################################################################################################

""" Disabled content
"""


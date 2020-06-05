from enum    import Enum
from numbers import Number
from pathlib import Path

from .content import visitor_map


###############################################################################

def is_nonstring_iterable(value):
    if isinstance(value, str): return False
    if hasattr(value, '__iter__'): return True
    return False

def squashed(value):
    """Return `value`, having squashed all empty contents to `None`.

    Pass through all booleans, all numbers including zeros, all nonempty
    strings, all dictionaries, anything not explicitly recognized.  Squash
    empty strings and empty sequences.  Return a nonempty sequence (excluding
    dictionaries) as a squashed list in which all items have been squashed.
    Assume no circular references.
    """
    print("squashed began with: '{}'".format(value))
    if value is None:
        print("squashed ended with: '{}'".format(None))
        return None
    if value == '':
        print("squashed ended with: '{}'".format(None))
        return None
    if value == ():
        print("squashed ended with: '{}'".format(None))
        return None
    if value == []:
        print("squashed ended with: '{}'".format(None))
        return None
    if isinstance(value, dict):
        print("squashed ended with: '{}'".format(value))
        return value
    if isinstance(value, str):
        print("squashed ended with: '{}'".format(value))
        return value
    if not is_nonstring_iterable(value):
        print("squashed ended with: '{}'".format(value))
        return value
    else:
        result = []
        for i in value:
            j = squashed(i)
            if j is not None: result.append(j)
        if len(result) == 0: result = None
        elif len(result) == 1: result = result[0]
        print("squashed ended with: '{}'".format(result))
        return result

###############################################################################

def eol(): return '\n'

def line(*text): return [text, eol()]

###############################################################################


class _BacktickQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "_BacktickQuoted({})".format(self.elements)


@visitor_map.register(_BacktickQuoted)
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


@visitor_map.register(_DoubleQuoted)
def _visit_double_quoted(element, walker):
    walker.emit('"')
    walker.walk(element.elements)
    walker.emit('"')

def dq(*element):
    return _DoubleQuoted(element)

###############################################################################

@visitor_map.register(Enum)
def _visit_content(element, walker):
    walker.walk(element.value)

###############################################################################


class _SingleQuoted(object):
    def __init__(self, elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "_SingleQuoted({})".format(self.elements)


@visitor_map.register(_SingleQuoted)
def _visit_single_quoted(element, walker):
    walker.emit("'")
    walker.walk(element.elements)
    walker.emit("'")

def sq(*element):
    return _SingleQuoted(element)


''' Disabled content

class _ContentElement(object):
    def __init__(self, content, typename='_ContentElement'):
        super().__init__()
        self.typename = typename
        self.content = squashed(content)

    def __repr__(self):
        return self.typename + '(' + repr(self.content) + ')'

#   def __str__(self):
#       return self.__repr__()

    def content_as_list(self):
        result = self.content
        if not isinstance(result, list):
            result = [result]
        return result


@visitor_map.register(_ContentElement)
def _visit_content_element(element, walker):
    walker.walk(element.content)

'''


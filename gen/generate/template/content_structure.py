from enum    import Enum
from numbers import Number
from pathlib import Path

from .content import visitor_map


###############################################################################

def squashed(value):
    """Return `value`, having squashed all empty contents to `None`.

    Pass through all booleans, all numbers including zeros, all nonempty
    strings, all dictionaries, anything not explicitly recognized.  Squash
    empty strings and empty sequences.  Return a nonempty sequence (excluding
    dictionaries) as a squashed list in which all items have been squashed.
    Assume no circular references.
    """
    # print("squashed began with: '{}'".format(value))
    if value is None:
        # print("squashed ended with: '{}'".format(None))
        return None
    if value == '':
        # print("squashed ended with: '{}'".format(None))
        return None
    if value == ():
        # print("squashed ended with: '{}'".format(None))
        return None
    if value == []:
        # print("squashed ended with: '{}'".format(None))
        return None
    if isinstance(value, _ContentElement):
        # print("squashed ended with: '{}'".format(value))
        return value
    if isinstance(value, dict):
        # print("squashed ended with: '{}'".format(value))
        return value
    if isinstance(value, Enum):
        # print("squashed ended with: '{}'".format(value))
        return value
    if isinstance(value, Number):
        # print("squashed ended with: '{}'".format(value))
        return value
    if isinstance(value, Path):
        # print("squashed ended with: '{}'".format(value))
        return value
    if isinstance(value, str):
        # print("squashed ended with: '{}'".format(value))
        return value
    result = []
    for i in value:
        j = squashed(i)
        if j is not None: result.append(j)
    if len(result) == 0: result = None
    elif len(result) == 1: result = result[0]
    # print("squashed ended with: '{}'".format(result))
    return result


class _ContentElement(object):
    def __init__(self, content, typename='_ContentElement'):
        super().__init__()
        self.typename = typename
        self.content = squashed(content)

#   def __repr__(self):
#       return self.typename + '(' + repr(self.content) + ')'

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

def eol(): return _ContentElement('\n')

###############################################################################

@visitor_map.register(Enum)
def _visit_content(element, walker):
    walker.walk(element.value)

###############################################################################

def line(*text): return [text, eol()]

###############################################################################


class _DoubleQuoted(_ContentElement):
    def __init__(self, elements, typename='_DoubleQuoted'):
        super().__init__(elements, typename)


@visitor_map.register(_DoubleQuoted)
def _visit_double_quoted(element, walker):
    walker.emit('"')
    walker.walk(element.content)
    walker.emit('"')

def dq(*element):
    return _DoubleQuoted(element)

###############################################################################


class _SingleQuoted(_ContentElement):
    def __init__(self, elements, typename='_SingleQuoted'):
        super().__init__(elements, typename)


@visitor_map.register(_SingleQuoted)
def _visit_single_quoted(element, walker):
    walker.emit("'")
    walker.walk(element.content)
    walker.emit("'")

def sq(*element):
    return _SingleQuoted(element)

###############################################################################


class _BacktickQuoted(_ContentElement):
    def __init__(self, elements, typename='_BacktickQuoted'):
        super().__init__(elements, typename)


@visitor_map.register(_BacktickQuoted)
def _visit_backtick_quoted(element, walker):
    walker.emit("`")
    walker.walk(element.content)
    walker.emit("`")

def bt(*element):
    return _BacktickQuoted(element)


''' Disabled content
'''


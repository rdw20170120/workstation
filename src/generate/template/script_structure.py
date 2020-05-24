from pathlib import Path

from .script import visitor_map


####################################################################################################

@visitor_map.register(Path)
def _visit_path(element, walker):
    walker.walk(str(element))

####################################################################################################

class _Arguments(object):
    def __init__(self, *argument):
        object.__init__(self)
        self.arguments = argument

@visitor_map.register(_Arguments)
def _visit_arguments(element, walker):
    if element.arguments is not None:
        for a in element.arguments:
            walker.emit(' ')
            walker.walk(a)

####################################################################################################

class _Statement(object):
    def __init__(self, statement):
        object.__init__(self)
        self.statement = statement

@visitor_map.register(_Statement)
def _visit_statement(element, walker):
    walker.walk(element.statement)

####################################################################################################

class _Command(_Statement):
    def __init__(self, command, *argument):
        _Statement.__init__(self, '_Command')
        self.arguments = _Arguments(*argument)
        self.command = command

@visitor_map.register(_Command)
def _visit_command(element, walker):
    walker.walk(element.command)
    walker.walk(element.arguments)

def command(command, *argument):
    return _Command(command, *argument)

####################################################################################################

class _Comment(_Statement):
    def __init__(self, *element):
        _Statement.__init__(self, '_Comment')
        self.content = element

@visitor_map.register(_Comment)
def _visit_comment(element, walker):
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
def _visit_comment(element, walker):
    walker.emit('#!')
    walker.walk(element.content)
    walker.emit('\n')

def shebang_cat():
    return shebang_thru_env('cat')

def shebang_false():
    return shebang_thru_env('false')

def shebang_thru_env(executable):
    return _Shebang(_Command(Path('/usr/bin/env') / executable))

####################################################################################################

''' Disabled content

####################################################################################################

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


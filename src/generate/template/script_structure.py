from pathlib import Path

from .content_structure import *
from .script            import visitor_map

###############################################################################

@visitor_map.register(Path)
def _visit_path(element, walker):
    walker.walk(str(element))

###############################################################################

class _Arguments(object):
    def __init__(self, *argument):
        super().__init__()
        self.arguments = argument

@visitor_map.register(_Arguments)
def _visit_arguments(element, walker):
    if element.arguments is not None:
        for a in element.arguments:
            walker.emit(' ')
            walker.walk(a)

###############################################################################

class _Statement(object):
    def __init__(self, statement):
        super().__init__()
        self.statement = statement

@visitor_map.register(_Statement)
def _visit_statement(element, walker):
    walker.walk(element.statement)

###############################################################################

class _Command(_Statement):
    def __init__(self, command, *argument):
        super().__init__('_Command')
        self.arguments = _Arguments(*argument)
        self.command = command

@visitor_map.register(_Command)
def _visit_command(element, walker):
    walker.walk(element.command)
    walker.walk(element.arguments)

def command(command, *argument):
    return _Command(command, *argument)

###############################################################################

class _Comment(_Statement):
    def __init__(self, *element):
        super().__init__('_Comment')
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

###############################################################################

class _Shebang(_Comment):
    def __init__(self, content):
        super().__init__(content)

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

###############################################################################

''' Disabled content
'''


from pathlib import Path

from .content_structure import *
from .content_structure import _ContentElement
from .script            import visitor_map

###############################################################################

@visitor_map.register(Path)
def _visit_path(element, walker):
    walker.walk(str(element))

###############################################################################


class _Arguments(_ContentElement):
    def __init__(self, content):
        super().__init__(content)


@visitor_map.register(_Arguments)
def _visit_arguments(element, walker):
    as_list = element.content_as_list()
    if as_list is not None:
        for a in as_list:
            if a is not None:
                walker.emit(' ')
                walker.walk(a)

###############################################################################


class _Command(_ContentElement):
    def __init__(self, command, arguments):
        super().__init__(None)
        assert command
        self.command = command
        self.arguments = _Arguments(arguments)


@visitor_map.register(_Command)
def _visit_command(element, walker):
    walker.walk(element.command)
    walker.walk(element.arguments)

def command(command, *argument):
    return _Command(command, argument)

###############################################################################


class _Comment(_ContentElement):
    def __init__(self, elements, tight=False):
        super().__init__(elements)
        if not self.content: tight = True
        self.tight = tight


@visitor_map.register(_Comment)
def _visit_comment(element, walker):
    walker.emit('#')
    if not element.tight:
        walker.emit(' ')
    walker.walk(element.content)
    walker.emit('\n')

def comment(*element):
    return _Comment(element)

###############################################################################


class _Shebang(_Comment):
    def __init__(self, content):
        super().__init__(['!', content], tight=True)
        assert self.content


def shebang_cat():
    return shebang_thru_env('cat')

def shebang_false():
    return shebang_thru_env('false')

def shebang_thru_env(executable):
    assert executable
    return _Shebang(_Command(Path('/usr/bin/env'), executable))


''' Disabled content
'''


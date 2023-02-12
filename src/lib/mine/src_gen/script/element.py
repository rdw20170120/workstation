#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.common import *
from src_gen.element import *
from utility import my_assert as is_
# Project modules   (relative references, NOT packaged, in project)
from .render import my_visitor_map

class Arguments(object):
    def __init__(self, *arguments):
        super().__init__()
        self.arguments = squashed(arguments)

    def __repr__(self):
        return "Arguments({})".format(self.arguments)


class Command(object):
    def __init__(self, executable, *arguments):
        super().__init__()
        self.executable = squashed(executable)
        assert is_.not_none(self.executable)
        if isinstance(arguments, Arguments):
            self.arguments = arguments
        else:
            self.arguments = Arguments(arguments)

    def __repr__(self):
        return "Command({}, {})".format(self.executable, self.arguments)


class Comment(object):
    def __init__(self, *elements, tight=False):
        super().__init__()
        self.elements = squashed(elements)
        if not self.elements:
            tight = True
        self.tight = tight

    def __repr__(self):
        return "Comment({}, {})".format(self.tight, self.elements)


class Expression(object):
    def __init__(self, *elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "Expression({})".format(self.elements)


@my_visitor_map.register(Arguments)
def _visit_arguments(element, walker):
    if is_nonstring_iterable(element.arguments):
        for a in element.arguments:
            if a is not None:
                walker.emit(" ")
                walker.walk(a)
    elif element.arguments is None:
        pass
    else:
        walker.emit(" ")
        walker.walk(element.arguments)


@my_visitor_map.register(Command)
def _visit_command(element, walker):
    walker.walk(element.executable)
    walker.walk(element.arguments)


@my_visitor_map.register(Comment)
def _visit_comment(element, walker):
    walker.emit("#")
    if not element.tight:
        walker.emit(" ")
    walker.walk(element.elements)
    walker.walk(eol())


@my_visitor_map.register(Expression)
def _visit_expression(element, walker):
    if is_nonstring_iterable(element.elements):
        for e in element.elements:
            if e is not None:
                walker.walk(e)
    elif element.elements is None:
        pass
    else:
        walker.walk(element.elements)


@my_visitor_map.register(Path)
def _visit_path(element, walker):
    walker.walk(str(element))

"""DisabledContent
"""

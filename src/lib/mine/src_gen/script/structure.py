#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_
from src_gen.structure import *
from src_gen.source import my_visitor_map

# Project modules   (relative references, NOT packaged, in project)

###############################################################################
def indent(count=1):
    return count * "    "


###############################################################################


@my_visitor_map.register(Path)
def _visit_path(element, walker):
    walker.walk(str(element))


###############################################################################


class _Arguments(object):
    def __init__(self, *arguments):
        super().__init__()
        self.arguments = squashed(arguments)

    def __repr__(self):
        return "_Arguments({})".format(self.arguments)


@my_visitor_map.register(_Arguments)
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


###############################################################################


class _Command(object):
    def __init__(self, executable, *arguments):
        super().__init__()
        self.executable = squashed(executable)
        assert is_.not_none(self.executable)
        if isinstance(arguments, _Arguments):
            self.arguments = arguments
        else:
            self.arguments = _Arguments(arguments)

    def __repr__(self):
        return "_Command({}, {})".format(self.executable, self.arguments)


@my_visitor_map.register(_Command)
def _visit_command(element, walker):
    walker.walk(element.executable)
    walker.walk(element.arguments)


def command(executable, *argument):
    return _Command(executable, argument)


###############################################################################


class _Comment(object):
    def __init__(self, *elements, tight=False):
        super().__init__()
        self.elements = squashed(elements)
        if not self.elements:
            tight = True
        self.tight = tight

    def __repr__(self):
        return "_Comment({}, {})".format(self.tight, self.elements)


@my_visitor_map.register(_Comment)
def _visit_comment(element, walker):
    walker.emit("#")
    if not element.tight:
        walker.emit(" ")
    walker.walk(element.elements)
    walker.walk(eol())


def comment(*element):
    return _Comment(element)


def disabled(*element):
    return comment("DISABLED: ", element)


def fix(*element):
    return todo("FIX: ", element)


def no(*element):
    return comment("NO: ", element)


def note(*element):
    return comment("NOTE: ", element)


def rule():
    # TODO: Make line length configurable
    return line("#" * 79)


def research(*element):
    return todo("RESEARCH: ", element)


def someday(*element):
    return todo("SOMEDAY: ", element)


def todo(*element):
    return comment("TODO: ", element)


###############################################################################


class _Expression(object):
    def __init__(self, *elements):
        super().__init__()
        self.elements = squashed(elements)

    def __repr__(self):
        return "_Expression({})".format(self.elements)


@my_visitor_map.register(_Expression)
def _visit_expression(element, walker):
    if is_nonstring_iterable(element.elements):
        for e in element.elements:
            if e is not None:
                walker.walk(e)
    elif element.elements is None:
        pass
    else:
        walker.walk(element.elements)


def x(*element):
    return _Expression(element)


###############################################################################


def _shebang(command):
    assert is_.instance(command, _Command)
    return _Comment("!", command, tight=True)


def shebang_cat():
    return shebang_thru_env("cat")


def shebang_false():
    return shebang_thru_env("false")


def shebang_thru_env(executable):
    assert is_.not_none(executable)
    return _shebang(_Command(Path("/usr/bin/env"), executable))


"""DisabledContent
"""

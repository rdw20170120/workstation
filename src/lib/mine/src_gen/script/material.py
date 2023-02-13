#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.material import *
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .frame import *


def _shebang(command):
    assert is_.instance(command, Command)
    return Comment("!", command, tight=True)


def command(executable, *argument):
    return Command(executable, argument)


def comment(*element):
    return Comment(element)


def disabled(*element):
    return comment("DISABLED: ", element)


def fix(*element):
    return todo("FIX: ", element)


def indent(count=1):
    return count * "    "


def no(*element):
    return comment("NO: ", element)


def note(*element):
    return comment("NOTE: ", element)


def research(*element):
    return todo("RESEARCH: ", element)


def rule():
    # TODO: Make line length configurable
    return line("#" * 79)


def shebang_cat():
    return shebang_thru_env("cat")


def shebang_false():
    return shebang_thru_env("false")


def shebang_thru_env(executable):
    assert is_.not_none(executable)
    return _shebang(Command(Path("/usr/bin/env"), executable))


def someday(*element):
    return todo("SOMEDAY: ", element)


def todo(*element):
    return comment("TODO: ", element)


def x(*element):
    return Expression(element)


"""DisabledContent
"""

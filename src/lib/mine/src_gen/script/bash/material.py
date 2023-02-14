#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.material import *
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .frame import *


trace_variable = "BO_Trace"
trace_minimal = "TRACE"
trace_maximal = "DEEP"


def assign(variable, *expression):
    return Assign(variable, expression)


def cc(command_embedded_within_comment):
    assert is_.instance(command_embedded_within_comment, Command)
    return bt(command_embedded_within_comment)


def condition(executable, *argument):
    return command(executable, argument)


def directory_exists(directory_name):
    return condition("[[", "-d", directory_name, "]]")


def echo(*argument):
    return command("echo", argument)


def echo_with_level(*argument):
    return [
        "1>&2 ",
        command("echo", dq(argument)),
    ]


def echo_debug(*element):
    return echo_with_level("DEBUG: ", element)


def echo_error(*element):
    return echo_with_level("ERROR: ", element)


def echo_info(*element):
    return echo_with_level("INFO:  ", element)


def echo_warn(*element):
    return echo_with_level("WARN:  ", element)


def elif_(condition, *statement):
    return ElseIf(condition, statement)


def else_(*statement):
    return Else(statement)


def exit(argument=None):
    return command("exit", argument)


def exit_with_status(variable="Status"):
    return exit(vr(variable))


def export(variable, expression=None, options=None):
    if expression is None:
        return command("export", options, variable)
    else:
        return command("export", options, assign(variable, expression))


def fi():
    return Fi()


def file_exists(file_name):
    return condition("[[", "-f", file_name, "]]")


def file_is_readable(file_name):
    return condition("[[", "-r", file_name, "]]")


def function(name, *statement):
    return Function(name, statement)


def if_(condition, *statement):
    return If(condition, statement)


def integer_equal(left, right):
    return condition("[[", left, "-eq", right, "]]")


def integer_not_equal(left, right):
    return condition("[[", left, "-ne", right, "]]")


def local(expression, integer=False, readonly=False):
    if integer:
        if readonly:
            return command("local", "-ir", expression)
        else:
            return command("local", "-i", expression)
    else:
        if readonly:
            return command("local", "-r", expression)
        else:
            return command("local", expression)


def path_is_not_directory(path_name):
    return condition("[[", "!", "-d", path_name, "]]")


def path_is_not_file(path_name):
    return condition("[[", "!", "-f", path_name, "]]")


def path_not_exists(path_name):
    return condition("[[", "!", "-e", path_name, "]]")


def remember_last_status(variable="Status"):
    return assign(vn(variable), "$?")


def return_(argument=None):
    return command("return", argument)


def return_with_status(variable="Status"):
    return return_(vr(variable))


def set_(*argument):
    return command("set", argument)


def shebang_bash():
    return shebang_thru_env("bash")


def shebang_sourced():
    return shebang_false()


def source(file_name):
    return command("source", file_name)


def status_is_failure(variable="Status"):
    return integer_not_equal(vr(variable), 0)


def status_is_success(variable="Status"):
    return integer_equal(vr(variable), 0)


def string_equals(left, right):
    return condition("[[", left, "==", right, "]]")


def string_is_not_null(expression):
    return condition("[[", "-n", expression, "]]")


def string_is_null(expression):
    return condition("[[", "-z", expression, "]]")


def string_not_equal(left, right):
    return condition("[[", left, "!=", right, "]]")


def substitute(executable, *argument):
    return Substitution(command(executable, argument))


def trap(name, signal):
    return command("trap", name, signal)


def vn(name):
    return VariableName(name)


def vr(name):
    return VariableReference(name)


"""DisabledContent
"""

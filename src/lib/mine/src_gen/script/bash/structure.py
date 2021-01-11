#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_
from src_gen.script.source import my_visitor_map
from src_gen.script.structure import *
from src_gen.script.structure import _Command

# Project modules   (relative references, NOT packaged, in project)


###############################################################################


def and_():
    return " &&"


def bs():
    return ["\\", eol()]


def or_():
    return " || "


def pipe():
    return " | "


def seq():
    return " ; "


###############################################################################


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


###############################################################################


def log_debug(*element):
    return command("log_debug", dq(element))


def log_error(*element):
    return command("log_error", dq(element))


def log_good(*element):
    return command("log_good", dq(element))


def log_info(*element):
    return command("log_info", dq(element))


def log_warn(*element):
    return command("log_warn", dq(element))


###############################################################################


def cc(command_embedded_within_comment):
    assert is_.instance(command_embedded_within_comment, _Command)
    return bt(command_embedded_within_comment)


def debugging_comment():
    return [
        note("Uncomment these lines for debugging, placed where needed"),
        comment(
            export("PS4", sq("$ ")),
            seq(),
            set_("-o", "verbose"),
            seq(),
            set_("-o", "xtrace"),
        ),
        comment("Code to debug..."),
        comment(set_("+o", "verbose"), seq(), set_("+o", "xtrace")),
    ]


def disabled_content_footer():
    return [
        line(),
        rule(),
        debugging_comment(),
        command(":", "<<", sq("DisabledContent")),
        eol(),
        line("DisabledContent"),
        line(),
    ]


###############################################################################


def exit(argument=None):
    return command("exit", argument)


def return_(argument=None):
    return command("return", argument)


###############################################################################


def exit_with_status():
    return exit(status())


def remember_last_status():
    return assign(vn("Status"), "$?")


def return_last_status():
    # TODO: Do I need this?
    return return_("$?")


def return_with_status():
    return return_(status())


def status():
    return vr("Status")


def status_is_failure():
    return integer_not_equal(status(), 0)


def status_is_success():
    return integer_equal(status(), 0)


###############################################################################


def set_(*argument):
    assert is_.at_least(len(argument), 1)
    return command("set", argument)


###############################################################################


class _Substitution(object):
    def __init__(self, command):
        super().__init__()
        assert is_.instance(command, _Command)
        self.command = command

    def __repr__(self):
        return "_Substitution({})".format(self.command)


@my_visitor_map.register(_Substitution)
def _visit_substitution(element, walker):
    walker.emit("$(")
    walker.walk(element.command)
    walker.emit(")")


def substitute(executable, *argument):
    return _Substitution(command(executable, argument))


###############################################################################


class _Assign(object):
    def __init__(self, variable, *expression):
        super().__init__()
        self.variable = squashed(variable)
        self.expressions = squashed(expression)

    def __repr__(self):
        return "_Assign({}, {})".format(self.variable, self.expressions)


@my_visitor_map.register(_Assign)
def _visit_assign(element, walker):
    walker.walk(element.variable)
    walker.emit("=")
    walker.walk(element.expressions)


def assign(variable, *expression):
    return _Assign(variable, expression)


def export(variable, expression=None, options=None):
    if expression is None:
        return command("export", options, variable)
    else:
        return command("export", options, assign(variable, expression))


def local(expression, integer=False, readonly=False):
    # TODO: REFACTOR: Reduce redundancy
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


def remembering(name):
    return [
        command("remembering", name),
    ]


###############################################################################


def condition(executable, *argument):
    return command(executable, argument)


def directory_exists(directory_name):
    return condition("[[", "-d", directory_name, "]]")


def file_exists(file_name):
    return condition("[[", "-f", file_name, "]]")


def file_is_readable(file_name):
    return condition("[[", "-r", file_name, "]]")


def integer_equal(left, right):
    return condition("[[", left, "-eq", right, "]]")


def integer_not_equal(left, right):
    return condition("[[", left, "-ne", right, "]]")


def path_is_not_directory(path_name):
    return condition("[[", "!", "-d", path_name, "]]")


def path_not_exists(path_name):
    return condition("[[", "!", "-e", path_name, "]]")


def path_is_not_file(path_name):
    return condition("[[", "!", "-f", path_name, "]]")


def string_equals(left, right):
    return condition("[[", left, "==", right, "]]")


def string_is_not_null(expression):
    return condition("[[", "-n", dq(expression), "]]")


def string_is_null(expression):
    return condition("[[", "-z", dq(expression), "]]")


###############################################################################


class _Else(object):
    def __init__(self, *statement):
        super().__init__()
        self.statements = squashed(statement)
        assert is_.not_none(self.statements)

    def __repr__(self):
        return "_Else({})".format(self.statements)


@my_visitor_map.register(_Else)
def _visit_else(element, walker):
    walker.emit("else")
    walker.walk(eol())
    walker.walk(element.statements)


def else_(*statement):
    return _Else(statement)


###############################################################################


class _ElseIf(object):
    def __init__(self, condition, *statement):
        super().__init__()
        self.condition = squashed(condition)
        assert is_.not_none(self.condition)
        self.statements = squashed(statement)
        assert is_.not_none(self.statements)

    def __repr__(self):
        return "_ElseIf({}, {})".format(self.condition, self.statements)


@my_visitor_map.register(_ElseIf)
def _visit_elif(element, walker):
    walker.emit("elif ")
    walker.walk(element.condition)
    walker.walk(seq())
    walker.emit("then")
    walker.walk(eol())
    walker.walk(element.statements)


def elif_(condition, *statement):
    return _ElseIf(condition, statement)


###############################################################################


class _Fi(object):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "_Fi()"


@my_visitor_map.register(_Fi)
def _visit_fi(element, walker):
    walker.emit("fi")
    walker.walk(eol())


def fi():
    return _Fi()


###############################################################################


class _Function(object):
    def __init__(self, name, *statement):
        super().__init__()
        self.name = squashed(name)
        self.statements = squashed(statement)
        assert is_.not_none(self.statements)

    def __repr__(self):
        return "_Function({})".format(self.statements)


@my_visitor_map.register(_Function)
def _visit_function(element, walker):
    walker.emit(element.name)
    walker.emit("() {")
    walker.walk(eol())
    walker.walk(element.statements)
    walker.emit("}")


def function(name, *statement):
    return _Function(name, statement)


def exported_function(name, *statement):
    return [
        function(name, *statement),
        and_(),
        " ",
        export(name, options="-f"),
        eol(),
    ]


###############################################################################


class _If(object):
    def __init__(self, condition, *statement):
        super().__init__()
        self.condition = squashed(condition)
        assert is_.not_none(self.condition)
        self.statements = squashed(statement)
        assert is_.not_none(self.statements)

    def __repr__(self):
        return "_If({}, {})".format(self.condition, self.statements)


@my_visitor_map.register(_If)
def _visit_if(element, walker):
    walker.emit("if ")
    walker.walk(element.condition)
    walker.walk(seq())
    walker.emit("then")
    walker.walk(eol())
    walker.walk(element.statements)


def if_(condition, *statement):
    return _If(condition, statement)


###############################################################################


def trace_execution():
    return [
        string_is_not_null(vr("BO_Debug")),
        and_(),
        " 1>&2 ",
        echo(dq("Executing ", vr("BASH_SOURCE"))),
        eol(),
    ]


def header_activation():
    return [
        shebang_sourced(),
        trace_execution(),
        no(set_("-e")),
        comment("Intended to be sourced in a Bash shell during activation."),
        no(trap("...", "EXIT")),
        rule(),
    ]


def header_executed():
    return [
        shebang_bash(),
        trace_execution(),
        no(set_("-e")),
        comment("Intended to be executed in a Bash shell."),
        trap("warn_on_error", "EXIT"),
        eol(),
        rule(),
    ]


def header_sourced():
    return [
        shebang_sourced(),
        trace_execution(),
        no(set_("-e")),
        comment("Intended to be sourced in a Bash shell."),
        no(trap("...", "EXIT")),
        rule(),
    ]


def maybe_copy_file(target, source):
    return [
        path_not_exists(target),
        and_(),
        eol(),
        indent(),
        command("cp", source, target),
        eol(),
    ]


def maybe_source(file_name):
    return [
        file_is_readable(file_name),
        and_(),
        eol(),
        indent(),
        source(file_name),
        eol(),
    ]


def shebang_bash():
    return shebang_thru_env("bash")


def shebang_sourced():
    return shebang_false()


def source(file_name):
    return command("source", file_name)


def trap(name, signal):
    return command("trap", name, signal)


###############################################################################


class _VariableName(object):
    def __init__(self, name):
        super().__init__()
        self.name = squashed(name)

    def __repr__(self):
        return "_VariableName({})".format(self.name)


@my_visitor_map.register(_VariableName)
def _visit_variable_name(element, walker):
    walker.walk(element.name)


def vn(name):
    return _VariableName(name)


class _VariableReference(object):
    def __init__(self, name):
        super().__init__()
        self.name = squashed(name)

    def __repr__(self):
        return "_VariableReference({})".format(self.name)


@my_visitor_map.register(_VariableReference)
def _visit_variable_reference(element, walker):
    walker.emit("${")
    walker.walk(element.name)
    walker.emit("}")


def vr(name):
    return _VariableReference(name)


###############################################################################


"""DisabledContent
"""

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


def cc(command_embedded_within_comment):
    assert is_.instance(command_embedded_within_comment, _Command)
    return bt(command_embedded_within_comment)


def debugging_comment():
    return [
        note("Uncomment these lines for debugging, placed where needed"),
        comment(export("PS4", sq("$ ")), seq(), set_("-vx")),
        comment("Code to debug..."),
        comment(set_("+vx")),
    ]


def disabled_content_footer():
    return [
        rule(),
        debugging_comment(),
        line(),
        command(":", "<<", sq("DisabledContent")),
        eol(),
        line("DisabledContent"),
        line(),
    ]


###############################################################################


def abort_script():
    return [
        command("kill", "-INT", "$$"),
        "  ",
        comment("Kill the executing script, but not the shell (terminal)"),
    ]


def exit(argument=None):
    return command("exit", argument)


def return_(argument=None):
    return command("return", argument)


###############################################################################


def exit_with_status(variable="Status"):
    return exit(vr(variable))


def remember_last_status(variable="Status"):
    return assign(vn(variable), "$?")


def return_with_status(variable="Status"):
    return return_(vr(variable))


def status_is_failure(variable="Status"):
    return integer_not_equal(vr(variable), 0)


def status_is_success(variable="Status"):
    return integer_equal(vr(variable), 0)


###############################################################################


def set_(*argument):
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


def export_if_null(variable, expression):
    return [
        string_is_null(dq(vr(variable))),
        and_(),
        " ",
        export(vn(variable), expression),
    ]


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
    return condition("[[", "-n", expression, "]]")


def string_is_null(expression):
    return condition("[[", "-z", expression, "]]")


def string_not_equal(left, right):
    return condition("[[", left, "!=", right, "]]")


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

trace_variable = "BO_Trace"
trace_minimal = "TRACE"
trace_maximal = "DEEP"


def disable_tracing_unless_maximal():
    return []


def enable_tracing_unless_minimal():
    return []


def tracing_in_header():
    return [
        string_is_not_null(dq(vr(trace_variable))),
        and_(),
        " 1>&2 ",
        echo(dq("Executing ", vr("BASH_SOURCE"))),
        and_(),
        " ",
        string_not_equal(dq(vr(trace_variable)), sq(trace_minimal)),
        and_(),
        " ",
        set_("-vx"),
        eol(),
    ]


###############################################################################

def header_executed():
    return [
        shebang_bash(),
        comment("Intended to be executed in a Bash shell."),
        tracing_in_header(),
        no(set_("-e")),
        trap("warn_on_error", "EXIT"),
        eol(),
        rule(),
    ]


def header_sourced():
    return [
        shebang_sourced(),
        comment("Intended to be sourced in a Bash shell."),
        tracing_in_header(),
        no(set_("-e")),
        no(trap("...", "EXIT")),
        rule(),
    ]


###############################################################################

def maybe_source(file_):
    return [
        file_is_readable(file_),
        and_(),
        eol(),
        indent(),
        source(file_),
        eol(),
    ]


def maybe_source_or_abort(file_, script, status):
    return [
        assign(vn(script), file_),
        eol(),
        if_(
            file_is_readable(vr(script)),
            indent(),
            source(vr(script)),
            seq(),
            remember_last_status(status),
            eol(),
            indent(),
            status_is_failure(status),
            and_(),
            eol(),
            indent(),
            indent(),
            abort_script(),
        ),
        fi(),
    ]


def shebang_bash():
    return shebang_thru_env("bash")


def shebang_sourced():
    return shebang_false()


def source(file_name):
    return command("source", file_name)


def source_or_abort(file_, script="Script", status="Status"):
    return [
        assign(vn(script), file_),
        eol(),
        source(dq(vr(script))),
        seq(),
        remember_last_status(status),
        eol(),
        status_is_failure(status),
        and_(),
        eol(),
        indent(),
        abort_script(),
    ]


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

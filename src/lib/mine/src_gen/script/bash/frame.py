#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.frame import *
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .element import *
from .material import *


def abort_script():
    return [
        command("kill", "-INT", "$$"),
        "  ",
        comment("Interrupt the executing script, but do NOT kill the shell (terminal)"),
    ]


def debugging_comment():
    return [
        note("Uncomment these lines for debugging, placed where needed"),
        no(set_("-o errexit", "-o nounset")),
        comment(export("PS4", sq("$ ")), seq(), set_("-o verbose", "-o xtrace")),
        comment("Code to debug..."),
        comment(set_("+o verbose", "+o xtrace")),
    ]


def disable_tracing_unless_maximal():
    return [todo()]


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


def enable_tracing_unless_minimal():
    return [todo()]


def export_if_null(variable, expression):
    return [
        string_is_null(dq(vr(variable))),
        and_(),
        " ",
        export(vn(variable), expression),
    ]


def exported_function(name, *statement):
    return [
        function(name, *statement),
        and_(),
        " ",
        export(name, options="-f"),
        eol(),
    ]


def header_executed(config):
    return [
        shebang_bash(),
        comment("Intended to be executed in a Bash shell."),
        no(set_("-o errexit", "-o nounset")),
        set_("-o pipefail", "+o verbose", "+o xtrace"),
        eol(),
        tracing_in_header(config),
        no(trap("...", "EXIT")),
        rule(),
    ]


def header_initialization(config):
    return [
        shebang_bash(),
        comment(
            "Intended to be executed in a Bash shell during user initialization (login)."
        ),
        no(set_("-o errexit", "-o nounset")),
        set_("-o pipefail", "+o verbose", "+o xtrace"),
        eol(),
        tracing_in_header(config),
        no(trap("...", "EXIT")),
        rule(),
    ]


def header_sourced(config):
    return [
        shebang_sourced(),
        comment("Intended to be executed in a Bash shell via `source`."),
        no(set_("-o errexit", "-o nounset")),
        set_("-o pipefail", "+o verbose", "+o xtrace"),
        eol(),
        tracing_in_header(config),
        no(trap("...", "EXIT")),
        rule(),
    ]


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


def remembering(name):
    return [
        command("remembering", name),
    ]


def source_or_abort(file_, script="Script", status="Status"):
    return [
        assign(vn(script), file_),
        eol(),
        todo("Require script"),
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


def tracing_in_header(config):
    return [
        string_is_not_null(dq(vr(config.var_trace))),
        and_(),
        " ",
        bs(),
        indent(),
        "1>&2 ",
        echo(dq("DEBUG: Executing ", vr("BASH_SOURCE"))),
        and_(),
        " ",
        bs(),
        indent(),
        string_equals(dq(vr(config.var_trace)), config.trace_minimal),
        and_(),
        " ",
        bs(),
        indent(),
        "1>&2 ",
        echo(dq("DEBUG: Tracing ", vr("BASH_SOURCE"))),
        and_(),
        " ",
        bs(),
        indent(),
        set_("-o verbose", "-o xtrace"),
        eol(),
    ]


"""DisabledContent
"""

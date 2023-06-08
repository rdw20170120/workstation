#!/usr/bin/env false
"""Generate script to activate project.

TODO: REFACTOR: Divide into two submodules that respect activating versus briteonyx calls
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.activating.frame import *
from src_gen.script.bash.activating.material import *
from src_gen.script.bash.activating.render import generate

# Project modules   (relative references, NOT packaged, in project)

_script = "_Script"
_status = "_Status"


def _abort_if_activated(config):
    return [
        if_(
            string_is_not_null(dq(vr(config.var_project_directory))),
            indent(),
            "1>&2 ",
            echo(
                dq(
                    "Aborting, this project is already activated as ",
                    sq(vr(config.var_project_directory)),
                )
            ),
            eol(),
            indent(),
            abort_script(),
        ),
        fi(),
    ]


def _abort_if_missing_pwd():
    return [
        if_(
            string_is_null(dq(vr("PWD"))),
            indent(),
            "1>&2 ",
            echo(
                dq(
                    "Aborting, missing environment variable ",
                    sq(vn("PWD")),
                )
            ),
            eol(),
            indent(),
            abort_script(),
        ),
        fi(),
    ]


def _briteonyx_declare_script(config):
    return x(vr(config.var_project_directory), "/BriteOnyx/bin/lib/declare.bash")


def _build(config):
    return [
        _header(config),
        line(),
        _create_capture_directory(config),
        _capture_environment(config, "activation", "before"),
        line(),
        _declare_logging(),
        line(),
        _remember(config),
        line(),
        _declare_briteonyx(config),
        line(),
    ]


def _capture_environment(config, where, when):
    return [
        "(",
        set_("-o", "posix"),
        seq(),
        set_(),
        ")",
        pipe(),
        command(
            "sort",
            ">",
            dq(vr(config.var_capture_directory), "/", when, "/", where, ".env"),
        ),
        eol(),
    ]


def _comments():
    return [
        # TODO: Redesign to automatically wrap comment paragraphs at a set line length
        comment(
            "Activate the BriteOnyx framework to manage this project directory tree"
        ),
        comment(),
        note("We MUST NOT EVER ", cc(exit()), " during BriteOnyx activation!"),
        comment(),
        comment("We cannot use a `trap` here"),
        comment("because it will remain active"),
        comment("within the shell"),
        comment("that will `source` this script."),
        comment(),
        comment("Please see HowTo-use_this_project.md for details."),
        rule(),
    ]


def _create_capture_directory(config):
    return [
        export(vn(config.var_capture_directory), dq(vr("PWD"), "/.BO/capture")),
        eol(),
        command(
            "mkdir",
            "-p",
            dq(vr(config.var_capture_directory), "/after"),
            dq(vr(config.var_capture_directory), "/before"),
            dq(vr(config.var_capture_directory), "/current"),
        ),
        eol(),
    ]


def _declare_briteonyx(config):
    return [
        source_or_abort(_briteonyx_declare_script(config), _script, _status),
    ]


def _declare_logging():
    return [
        source_or_abort(_log4bash_script(), _script, _status),
        line(),
        log_info("Activating ", sq(vr("PWD")), " as the current project"),
        eol(),
    ]


def _declare_remembering():
    return [
        exported_function(
            "remembering",
            indent(),
            comment("Log that we are remembering variable $1"),
            indent(),
            integer_equal("$#", 0),
            and_(),
            eol(),
            indent(2),
            log_error("Variable name is required"),
            and_(),
            eol(),
            indent(2),
            abort_script(),
            indent(),
            command("local", "-r", "Name=$1"),
            eol(),
            indent(),
            log_debug("Remembering ", vr("Name"), " = '${!Name}'"),
            eol(),
        ),
    ]


def _header(config):
    return [
        header_activation(config),
        _comments(),
        _abort_if_activated(config),
        line(),
        _abort_if_missing_pwd(),
    ]


def _log4bash_script():
    return x(vr("PWD"), "/BriteOnyx/bin/lib/declare-log4bash.bash")


def _remember(config):
    return [
        _declare_remembering(),
        line(),
        _remember_project_root(config),
    ]


def _remember_project_root(config):
    return [
        export(vn(config.var_project_directory), vr("PWD")),
        eol(),
        remembering(config.var_project_directory),
        eol(),
    ]


def render(config):
    return generate(_build(config))


"""DisabledContent
"""

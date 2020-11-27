#!/usr/bin/env false
"""Generate script to activate project."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.briteonyx.source import generate as gen
from src_gen.script.bash.briteonyx.structure import *

# Project modules   (relative references, NOT packaged, in project)


def _abort_if_activated():
    return [
        if_(
            string_is_not_null(vr("BO_Project")),
            indent(),
            "1>&2 ",
            echo(
                dq(
                    "Aborting, this project is already activated as ",
                    sq(vr("BO_Project")),
                )
            ),
            eol(),
            indent(),
            _abort_script(),
        ),
        fi(),
    ]


def _abort_script():
    return [
        command("kill", "-INT", "$$"),
        "  ",
        comment("Kill the executing script, but not the shell (terminal)"),
    ]


def _activate_python_virtual_environment():
    return [
        _remember_project_path(),
        line(),
        _remember_system_path(),
        _remember_user_path(),
        line(),
        comment("Reset PATH before activating Python virtual environment"),
        export(vn("PATH"), vr("BO_PathSystem")),
        eol(),
        _capture_environment("PVE-prior"),
        source(x(vr("BO_Project"), "/BriteOnyx/bin/lib/pve-activate.bash")),
        eol(),
        _capture_environment("PVE-after"),
        _remember_pve_path(),
    ]


def _capture_environment(file_name):
    return [
        command("env"),
        pipe(),
        command("sort", ">", x(vr("PWD"), "/BO-", file_name, ".env")),
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


def _create_random_tmpdir():
    local = "_result"
    # TODO: Consider capturing this special variable
    tmpdir = "TMPDIR"
    user = "USER"
    return [
        comment("Create random temporary directory"),
        # TODO: Consider creating method for 'mktemp'
        if_(
            string_equals(dq(vr("BO_OS")), "macOS"),
            indent(),
            assign(
                vn(local),
                substitute("mktemp", "-d", "-t", dq("BO-", vr(user))),
            ),
            eol(),
        ),
        else_(
            indent(),
            assign(
                vn(local),
                substitute(
                    "mktemp", "-d", "-t", dq("BO-", vr(user), "-XXXXXXX")
                ),
            ),
            eol(),
        ),
        fi(),
        if_(
            directory_exists(dq(vr(local))),
            indent(),
            assign(vn(tmpdir), vr(local)),
            eol(),
            indent(),
            log_info("Created temporary directory ", sq(vr(tmpdir))),
            eol(),
        ),
        fi(),
        if_(
            directory_exists(dq(vr(tmpdir))),
            indent(),
            remembering(tmpdir),
            eol(),
            indent(),
            export(vn(tmpdir)),
            eol(),
        ),
        else_(
            indent(),
            log_error(
                "Aborting, failed to establish temporary directory ",
                sq(vr(tmpdir)),
            ),
            eol(),
            indent(),
            _abort_script(),
        ),
        fi(),
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
            _abort_script(),
            indent(),
            command("local", "-r", "Name=$1"),
            eol(),
            indent(),
            log_debug("Remembering ", vr("Name"), " = '${!Name}'"),
            eol(),
        ),
    ]


def _detect_operating_system():
    # TODO: Make appropriate constants
    local = "_result"
    return [
        comment("Detect operating system"),
        todo("Write as function"),
        assign(vn(local), substitute("uname")),
        eol(),
        todo("Add detection of various Linux, when we care"),
        if_(
            string_equals(dq(vr(local)), "Darwin"),
            indent(),
            export(vn("BO_OS"), "macOS"),
            eol(),
        ),
        else_(
            indent(),
            export(vn("BO_OS"), "UNKNOWN"),
            eol(),
        ),
        fi(),
        remembering("BO_OS"),
        eol(),
    ]


def _remember_project_path():
    return [
        note("BriteOnyx scripts"),
        comment("must precede project-specific scripts"),
        comment("so that collisions fail fast."),
        comment("Any collision should be resolved"),
        comment("by renaming the project-specific script"),
        comment("to avoid that collision."),
        export(
            vn("BO_PathProject"),
            x(
                vr("BO_Project"),
                "/BriteOnyx/bin",
                ":",
                vr("BO_Project"),
                "/bin",
            ),
        ),
        eol(),
        remembering("BO_PathProject"),
        eol(),
    ]


def _remember_project_root():
    return [
        export(vn("BO_Project"), vr("PWD")),
        eol(),
        remembering("BO_Project"),
        eol(),
    ]


def _remember_pve_path():
    return [
        string_is_null(vr("BO_PathPve")),
        and_(),
        eol(),
        indent(),
        export(vn("BO_PathPve"), vr("PATH")),
        and_(),
        eol(),
        indent(),
        remembering("BO_PathPve"),
        eol(),
    ]


def _remember_system_path():
    return [
        string_is_null(vr("BO_PathSystem")),
        and_(),
        eol(),
        indent(),
        export(vn("BO_PathSystem"), vr("PATH")),
        and_(),
        eol(),
        indent(),
        remembering("BO_PathSystem"),
        eol(),
    ]


def _remember_user_path():
    return [
        string_is_null(vr("BO_PathUser")),
        and_(),
        eol(),
        indent(),
        export(vn("BO_PathUser"), (vr("HOME"), "/bin")),
        and_(),
        eol(),
        indent(),
        remembering("BO_PathUser"),
        eol(),
    ]


def _source_supporting_scripts():
    return [
        source(x(vr("BO_Project"), "/BriteOnyx/bin/lib/set_path.bash")),
        eol(),
        source(
            x(vr("BO_Project"), "/BriteOnyx/bin/lib/configure-Python.bash")
        ),
        eol(),
        source(x(vr("BO_Project"), "/BriteOnyx/bin/lib/declare.bash")),
        eol(),
        source(x(vr("BO_Project"), "/BriteOnyx/bin/lib/alias-common.bash")),
        eol(),
        source(x(vr("BO_Project"), "/BriteOnyx/bin/lib/alias-git.bash")),
        eol(),
        line(),
        maybe_source(x(vr("BO_Project"), "/bin/lib/declare.bash")),
        maybe_source(x(vr("BO_Project"), "/context.bash")),
        maybe_source(x(vr("BO_Project"), "/alias.bash")),
    ]


def build():
    return [
        header_activation(),
        _comments(),
        _abort_if_activated(),
        line(),
        _capture_environment("incoming"),
        source(x(vr("PWD"), "/BriteOnyx/bin/lib/declare-log4bash.bash")),
        eol(),
        log_info(
            "Activating this directory ",
            sq(vr("PWD")),
            " as the current project",
        ),
        eol(),
        line(),
        _declare_remembering(),
        line(),
        _remember_project_root(),
        remembering("INTERACTIVE_MODE"),
        eol(),
        line(),
        _detect_operating_system(),
        line(),
        _create_random_tmpdir(),
        line(),
        _activate_python_virtual_environment(),
        line(),
        _source_supporting_scripts(),
        line(),
        _capture_environment("outgoing"),
        log_good("BriteOnyx has successfully activated this project"),
        eol(),
        disabled_content_footer(),
    ]


def generate(directory):
    gen(build(), directory, "activate.bash")


"""DisabledContent
"""

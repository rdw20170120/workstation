#!/usr/bin/env false
"""Generate script to activate project."""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from src_gen.script.bash.briteonyx.source import generate as gen
from src_gen.script.bash.briteonyx.structure import *

# Co-located modules (relative references, NOT packaged, in project)


def _abort_if_activated():
    return [
        line(),
        if_(
            string_is_not_null(vr("BO_Project")),
            indent(),
            echo_fatal(
                "This project is already activated as ",
                sq(vr("BO_Project")),
                ", aborting",
            ),
            eol(),
            indent(),
            return_(1),
            "  ",
            comment("Exit from the script, but not from the shell"),
        ),
        fi(),
    ]


def _activate_python_virtual_environment():
    return [
        _remember_project_path(),
        _remember_system_path(),
        _remember_user_path(),
        _reset_path_for_pve(),
        _capture_environment("PVE-prior"),
        eol(),
        line(),
        _source_script(
            (vr("BO_Project"), "/BriteOnyx/bin/lib/pve-activate.bash")
        ),
        _capture_environment("PVE-after"),
        eol(),
        _remember_pve_path(),
        line(),
        _source_script((vr("BO_Project"), "/BriteOnyx/bin/lib/set_path.bash")),
    ]


def _capture_environment(file_name):
    return [
        line(),
        command("env"),
        pipe(),
        command("sort", ">", x(vr("PWD"), "/BO-", file_name, ".env")),
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
        comment(
            "This script, and EVERY script that it calls, must NOT invoke ",
            cc(exit()),
            "!  The",
        ),
        comment(
            "user calling this script must be allowed to preserve their shell and every"
        ),
        comment(
            "effort must be made to inform the user of problems while continuing execution"
        ),
        comment(
            "where possible.  Terminating the shell robs the user of useful feedback and"
        ),
        comment(
            "interrupts their work, which is unacceptable.  Instead, the BASH ",
            cc(return_()),
        ),
        comment(
            "statement should be invoked to end execution with an appropriate status code."
        ),
        comment(),
        comment(
            "Likewise, we must be very careful invoking special BASH options during"
        ),
        comment(
            "BriteOnyx activation, particularly the ",
            cc(set_("-e")),
            " option.  The user is",
        ),
        comment(
            "inheriting the shell that we are configuring, which they will then use for"
        ),
        comment(
            "the rest of their session, each and every time they develop, test, etc.  It"
        ),
        comment(
            "would be very disruptive for the shell to abort on every error raised by"
        ),
        comment(
            "every part of every command that they execute.  If you are unclear about"
        ),
        comment(
            "this, then please experiment by uncommenting the ",
            cc(set_("-x")),
            " command above and",
        ),
        comment(
            "activating a new shell.  Having learned that lesson, let's never use ",
            cc(set_("-x")),
        ),
        comment(
            "in a BASH script intended to be ",
            cc(command("source")),
            "d.  Similarly, the ",
            cc(set_("-e")),
            " BASH",
        ),
        comment(
            "option is problematic because its haphazard behavior does not deliver on its"
        ),
        comment("promised usefulness."),
        rule(),
    ]


def _create_random_tmpdir():
    local = "_result"
    # TODO: Consider capturing this special variable
    tmpdir = "TMPDIR"
    user = "USER"
    return [
        line(),
        comment("Create random temporary directory"),
        # TODO: Consider creating method for 'mktemp'
        if_(
            string_equals(vr("BO_OS"), "macOS"),
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
            directory_exists(vr(local)),
            indent(),
            assign(vn(tmpdir), vr(local)),
            eol(),
            indent(),
            echo_info("Temporary directory ", sq(vr(tmpdir)), " created"),
            eol(),
        ),
        fi(),
        if_(
            directory_exists(vr(tmpdir)),
            indent(),
            echo_info("Remembering ", vn(tmpdir), "=", sq(vr(tmpdir))),
            eol(),
            indent(),
            export(vn(tmpdir)),
            eol(),
        ),
        else_(
            indent(),
            echo_fatal(
                "Failed to establish temporary directory ",
                sq(vr(tmpdir)),
                ", aborting",
            ),
            eol(),
            indent(),
            return_(1),
            "  ",
            comment("Exit from the script, but not from the shell"),
        ),
        fi(),
    ]


def _detect_operating_system():
    # TODO: Make appropriate constants
    local = "_result"
    return [
        line(),
        comment("Detect operating system"),
        assign(vn(local), substitute("uname")),
        eol(),
        if_(
            string_equals(vr(local), "Darwin"),
            indent(),
            export(vn("BO_OS"), "macOS"),
            eol(),
        ),
        else_(
            indent(),
            export(vn("BO_OS"), "Linux"),
            eol(),
        ),
        fi(),
        echo_info("Remembering ", vn("BO_OS"), "=", sq(vr("BO_OS"))),
        eol(),
    ]


def _remember_project_path():
    return [
        line(),
        note(
            "BriteOnyx scripts must precede project-specific scripts so that"
        ),
        comment(
            "collisions fail-fast.  Any collision should result in renaming the project-"
        ),
        comment("specific script to avoid it."),
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
        echo_info(
            "Remembering ", vn("BO_PathProject"), "=", vr("BO_PathProject")
        ),
        eol(),
    ]


def _remember_project_root():
    return [
        line(),
        echo_info(
            "Activating this directory ",
            sq(vr("PWD")),
            " as the current project",
        ),
        eol(),
        export(vn("BO_Project"), vr("PWD")),
        eol(),
    ]


def _remember_pve_path():
    return [
        line(),
        string_is_null(vr("BO_PathPve")),
        and_(),
        bs(),
        indent(),
        export(vn("BO_PathPve"), vr("PATH")),
        and_(),
        bs(),
        indent(),
        echo_info("Remembering ", vn("BO_PathPve"), "=", sq(vr("BO_PathPve"))),
        eol(),
    ]


def _remember_system_path():
    return [
        line(),
        string_is_null(vr("BO_PathSystem")),
        and_(),
        bs(),
        indent(),
        export(vn("BO_PathSystem"), vr("PATH")),
        and_(),
        bs(),
        indent(),
        echo_info(
            "Remembering ", vn("BO_PathSystem"), "=", sq(vr("BO_PathSystem"))
        ),
        eol(),
    ]


def _remember_user_path():
    return [
        line(),
        string_is_null(vr("BO_PathUser")),
        and_(),
        bs(),
        indent(),
        export(vn("BO_PathUser"), (vr("HOME"), "/bin")),
        and_(),
        bs(),
        indent(),
        echo_info(
            "Remembering ", vn("BO_PathUser"), "=", sq(vr("BO_PathUser"))
        ),
        eol(),
    ]


def _reset_path_for_pve():
    return [
        line(),
        comment("Reset PATH before activating Python virtual environment"),
        export(vn("PATH"), vr("BO_PathSystem")),
        eol(),
    ]


# TODO: Make this reusable
def _source_script(script):
    return [
        assign(vn("Script"), script),
        eol(),
        if_(
            file_is_readable(vr("Script")),
            indent(),
            echo_info(sq("source"), "ing script file ", sq(vr("Script"))),
            eol(),
            indent(),
            source(vr("Script")),
            eol(),
        ),
        else_(
            indent(),
            echo_warn(
                "Script file ", sq(vr("Script")), " is not readable, ignoring"
            ),
            eol(),
        ),
        fi(),
    ]


def _source_supporting_scripts():
    return [
        line(),
        _source_script(
            (vr("BO_Project"), "/BriteOnyx/bin/lib/alias-common.bash")
        ),
        line(),
        _source_script(
            (vr("BO_Project"), "/BriteOnyx/bin/lib/alias-git.bash")
        ),
        line(),
        _source_script((vr("BO_Project"), "/alias.bash")),
        line(),
        _source_script((vr("BO_Project"), "/context.bash")),
    ]


def build():
    return [
        header_sourced(),
        _comments(),
        _abort_if_activated(),
        _capture_environment("incoming"),
        eol(),
        _remember_project_root(),
        _detect_operating_system(),
        _create_random_tmpdir(),
        _activate_python_virtual_environment(),
        _source_supporting_scripts(),
        _capture_environment("outgoing"),
        eol(),
        disabled_content_footer(),
    ]


def generate(directory):
    sub = Path(".")
    gen(build(), directory, sub, "activate.bash")


"""DisabledContent
"""

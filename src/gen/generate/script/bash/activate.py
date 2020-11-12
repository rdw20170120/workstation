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
            log_fatal(
                "This project is already activated as ",
                sq(vr("BO_Project")),
                ", aborting",
            ),
            eol(),
            indent(),
            return_(99),
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
        comment("Please see HowTo-use_this_project.md for details."),
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
            log_info("Temporary directory ", sq(vr(tmpdir)), " created"),
            eol(),
        ),
        fi(),
        if_(
            directory_exists(vr(tmpdir)),
            indent(),
            _remembering(tmpdir),
            eol(),
            indent(),
            export(vn(tmpdir)),
            eol(),
        ),
        else_(
            indent(),
            log_fatal(
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
        _remembering("BO_OS"),
        eol(),
    ]


def _remember_project_path():
    return [
        line(),
        note("BriteOnyx scripts"),
        comment("must precede project-specific scripts"),
        comment("so that collisions fail-fast."),
        comment("Any collision should be resolved"),
        comment("by renaming the project- specific script"),
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
        _remembering("BO_PathProject"),
        eol(),
    ]


def _remember_project_root():
    return [
        line(),
        log_info(
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
        _remembering("BO_PathPve"),
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
        _remembering("BO_PathSystem"),
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
        _remembering("BO_PathUser"),
        eol(),
    ]


def _remembering(variable_name):
    return log_info(
        "Remembering ", nvp(vn(variable_name), sq(vr(variable_name)))
    )


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
        header_sourced(),
        _comments(),
        _abort_if_activated(),
        line(),
        _capture_environment("incoming"),
        _remember_project_root(),
        _detect_operating_system(),
        _create_random_tmpdir(),
        _activate_python_virtual_environment(),
        line(),
        _source_supporting_scripts(),
        line(),
        _capture_environment("outgoing"),
        disabled_content_footer(),
    ]


def generate(directory):
    sub = Path(".")
    gen(build(), directory, sub, "activate.bash")


"""DisabledContent
"""

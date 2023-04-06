#!/usr/bin/env false
"""Generate script to activate project.

TODO: REFACTOR: Divide into two submodules that respect activating versus briteonyx calls
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.activating.frame import *
from src_gen.script.bash.activating.material import *

# Project modules   (relative references, NOT packaged, in project)

capture_directory = "BO_DirCapture"
project_alias_script = x(vr("BO_Project"), "/alias.bash")
project_context_script = x(vr("BO_Project"), "/context.bash")
script = "_Script"
status = "_Status"


def _abort_if_activated():
    return [
        if_(
            string_is_not_null(dq(vr("BO_Project"))),
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


def _call_project_scripts():
    briteonyx_alias_script = x(vr("BO_Project"), "/BriteOnyx/bin/lib/alias.bash")
    project_declare_script = x(vr("BO_Project"), "/bin/lib/declare.bash")
    return [
        maybe_source_or_abort(dq(project_declare_script), script, status),
        line(),
        source_or_abort(dq(project_context_script), script, status),
        line(),
        source_or_abort(dq(briteonyx_alias_script), script, status),
        line(),
        source_or_abort(dq(project_alias_script), script, status),
        line(),
    ]


def _capture_environment(where, when):
    return [
        "(",
        set_("-o", "posix"),
        seq(),
        set_(),
        ")",
        pipe(),
        command("sort", ">", dq(vr(capture_directory), "/", when, "/", where, ".env")),
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


def _configure_anaconda():
    configure_anaconda_script = x(
        vr("BO_Project"), "/BriteOnyx/bin/lib/configure_Anaconda.bash"
    )
    return [
        comment("Configure Anaconda environment"),
        _capture_environment("Anaconda", "before"),
        source_or_abort(configure_anaconda_script, script, status),
        _capture_environment("Anaconda", "after"),
        line(),
    ]


def _configure_python():
    configure_python_script = x(
        vr("BO_Project"), "/BriteOnyx/bin/lib/configure_Python.bash"
    )
    return [
        comment("Configure Python"),
        _capture_environment("Python", "before"),
        source_or_abort(configure_python_script, script, status),
        _capture_environment("Python", "after"),
        line(),
    ]


def _create_capture_directory():
    return [
        export(vn(capture_directory), dq(vr("PWD"), "/.BO/capture")),
        eol(),
        command(
            "mkdir",
            "-p",
            dq(vr(capture_directory), "/after"),
            dq(vr(capture_directory), "/before"),
            dq(vr(capture_directory), "/current"),
        ),
        eol(),
    ]

def _create_tmpdir():
    tmpdir = "TMPDIR"
    user = "USER"
    return [
        comment("Establish temporary directory for project"),
            assign(vn(tmpdir), x(vr("BO_Project"), "/tmp")), eol(),
        command("maybe_create_directory_tree", dq(vr(tmpdir))), eol(),
        if_(
            directory_exists(dq(vr(tmpdir))),
            indent(), export(vn(tmpdir)), eol(),
            indent(), remembering(tmpdir), eol(),
        ),
        else_(
            indent(), log_error("Aborting, failed to establish temporary directory ", sq(vr(tmpdir))), eol(),
            indent(), abort_script(),
        ),
        fi(),
    ]



def _declare_briteonyx():
    briteonyx_declare_script = x(vr("BO_Project"), "/BriteOnyx/bin/lib/declare.bash")
    return [
        source_or_abort(briteonyx_declare_script, script, status),
        line(),
        note("We can now use BriteOnyx Bash functionality."),
        line(),
    ]


def _declare_logging():
    log4bash_script = x(vr("PWD"), "/BriteOnyx/bin/lib/declare-log4bash.bash")
    return [
        source_or_abort(log4bash_script, script, status),
        line(),
        log_info("Activating ", sq(vr("PWD")), " as the current project"),
        eol(),
        line(),
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


def _detect_operating_system():
    # TODO: Make appropriate constants
    local = "_result"
    return [
        comment("Detect operating system"),
        todo("Write as function"),
        todo("Add detection of various Linux, when we care"),
        assign(vn(local), substitute("uname")),
        eol(),
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
        line(),
    ]


def _footer():
    return [
        log_good("BriteOnyx has successfully activated this project"),
        eol(),
        log_info("To get started, try executing the 'cycle' alias..."),
        eol(),
        line(),
        disabled_content_footer(),
    ]


def _header():
    return [
        header_activation(),
        _comments(),
        _abort_if_activated(),
        line(),
        _abort_if_missing_pwd(),
        line(),
    ]


def _prepare_file_system():
    alias_sample = x(vr("BO_Project"), "/cfg/sample/alias.bash")
    context_sample = x(vr("BO_Project"), "/cfg/sample/context.bash")
    log_directory = x(vr("BO_Project"), "/log")
    return [
        _create_tmpdir(),
        line(),
        comment("Establish logging directory for project"),
        command("maybe_create_directory_tree", dq(log_directory)), eol(),
        line(),
        maybe_copy_file(dq(alias_sample), dq(project_alias_script)), eol(),
        maybe_copy_file(dq(context_sample), dq(project_context_script)), eol(),
        line(),
    ]


def _prepare_paths():
    set_path_script = x(vr("BO_Project"), "/BriteOnyx/bin/lib/set_path.bash")
    return [
        _remember_paths(),
        line(),
        source_or_abort(set_path_script, script, status),
        line(),
    ]


def _remember():
    return [
        _declare_remembering(),
        line(),
        _remember_project_root(),
        line(),
    ]


def _remember_paths():
    project_path = x(vr("BO_Project"), "/BriteOnyx/bin", ":", vr("BO_Project"), "/bin")
    return [
        export(vn("BO_PathProject"), project_path),
        eol(),
        line(),
        export_if_null("BO_PathSystem", vr("PATH")),
        eol(),
        export_if_null("BO_PathUser", x(vr("HOME"), "/bin")),
        eol(),
        line(),
    ]


def _remember_project_root():
    return [
        export(vn("BO_Project"), vr("PWD")),
        eol(),
        remembering("BO_Project"),
        eol(),
    ]


def build():
    return [
        _header(),
        _create_capture_directory(),
        _capture_environment("activation", "before"),
        _declare_logging(),
        _remember(),
        _declare_briteonyx(),
        _prepare_paths(),
        _detect_operating_system(),
        _prepare_file_system(),
        _configure_anaconda(),
        _configure_python(),
        _call_project_scripts(),
        _capture_environment("activation", "after"),
        _footer(),
    ]


"""DisabledContent
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
            indent(), assign(vn(local), substitute("mktemp", "-d", "-t", dq("BO"))), eol(),
        ),
        else_(
            indent(), assign(vn(local), substitute("mktemp", "-d", "-t", dq("BO-", vr(user), "-XXXXXXX"))), eol(),
        ),
        fi(),
        if_(
            directory_exists(dq(vr(local))),
            indent(), assign(vn(tmpdir), vr(local)), eol(),
            indent(), log_info("Created temporary directory ", sq(vr(tmpdir))), eol(),
        ),
        fi(),
        if_(
            directory_exists(dq(vr(tmpdir))),
            indent(), export(vn(tmpdir)), eol(),
            indent(), remembering(tmpdir), eol(),
        ),
        else_(
            indent(), log_error("Aborting, failed to establish temporary directory ", sq(vr(tmpdir))), eol(),
            indent(), abort_script(),
        ),
        fi(),
    ]


"""

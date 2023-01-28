#!/usr/bin/env false
"""Generate script to activate project."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# from src_gen.script.bash.briteonyx.source import generate as gen
# from src_gen.script.bash.briteonyx.structure import *
from src_gen.script.bash.source import generate as gen
from src_gen.script.bash.structure import *

# Project modules   (relative references, NOT packaged, in project)


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


def _activate_python_virtual_environment(pve_activate_script, script, status):
    return [
        comment("Activate Python virtual environment (PVE)"),
        _capture_environment("PVE-prior"),
        source_or_abort(pve_activate_script, script, status),
        _capture_environment("PVE-after"),
    ]


def _capture_environment(file_name):
    return [
        "(",
        set_("-o", "posix"),
        seq(),
        set_(),
        ")",
        pipe(),
        command("sort", ">", dq(vr("PWD"), "/BO-", file_name, ".env")),
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
            abort_script(),
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
    ]


def _remember_paths():
    project_path = x(
        vr("BO_Project"), "/BriteOnyx/bin", ":", vr("BO_Project"), "/bin"
    )
    return [
        note("We can now use BriteOnyx Bash functionality."),
        line(),
        comment("BriteOnyx scripts"),
        comment("must precede"),
        comment("project-specific scripts"),
        comment("on the PATH"),
        comment("so that collisions fail fast."),
        comment("Any collision should be resolved"),
        comment("by renaming"),
        comment("the project-specific script"),
        comment("to avoid that collision."),
        line(),
        export(vn("BO_PathProject"), project_path), eol(),
        line(),
        export_if_null("BO_PathSystem", vr("PATH")), eol(),
        export("BO_PathTool", ""), eol(),
        export_if_null("BO_PathUser", x(vr("HOME"), "/bin")), eol(),
        line(),
        remembering("BO_PathNative"), eol(),
        remembering("BO_PathProject"), eol(),
        remembering("BO_PathSystem"), eol(),
        remembering("BO_PathTool"), eol(),
        remembering("BO_PathUser"), eol(),
    ]


def _remember_project_root():
    return [
        export(vn("BO_Project"), vr("PWD")), eol(),
        remembering("BO_Project"), eol(),
    ]


def build():
    script = "_Script"
    status = "_Status"
    alias_sample = x(vr("BO_Project"), "/cfg/sample/alias.bash")
    briteonyx_alias_script = x(
        vr("BO_Project"), "/BriteOnyx/bin/lib/alias.bash"
    )
    briteonyx_declare_script = x(
        vr("BO_Project"), "/BriteOnyx/bin/lib/declare.bash"
    )
    configure_python_script = x(
        vr("BO_Project"), "/BriteOnyx/bin/lib/configure-Python.bash"
    )
    context_sample = x(vr("BO_Project"), "/cfg/sample/context.bash")
    log4bash_script = x(vr("PWD"), "/BriteOnyx/bin/lib/declare-log4bash.bash")
    log_directory = x(vr("BO_Project"), "/log")
    project_alias_script = x(vr("BO_Project"), "/alias.bash")
    project_context_script = x(vr("BO_Project"), "/context.bash")
    project_declare_script = x(vr("BO_Project"), "/bin/lib/declare.bash")
    pve_activate_script = x(
        vr("BO_Project"), "/BriteOnyx/bin/lib/pve-activate.bash"
    )
    set_path_script = x(vr("BO_Project"), "/BriteOnyx/bin/lib/set_path.bash")
    return [
        header_activation(),
        _comments(),
        _abort_if_activated(),
        line(),
        _abort_if_missing_pwd(),
        line(),
        _capture_environment("incoming"),
        line(),
        source_or_abort(log4bash_script, script, status),
        line(),
        log_info("Activating ", sq(vr("PWD")), " as the current project"),
        eol(),
        line(),
        _declare_remembering(),
        line(),
        _remember_project_root(),
        remembering("BO_Interactive"),
        eol(),
        line(),
        source_or_abort(briteonyx_declare_script, script, status),
        line(),
        _remember_paths(),
        line(),
        source_or_abort(set_path_script, script, status),
        line(),
        _detect_operating_system(),
        line(),
        _create_random_tmpdir(),
        line(),
        command("maybe_create_directory_tree", log_directory),
        eol(),
        line(),
        _activate_python_virtual_environment(
            pve_activate_script, script, status
        ),
        line(),
        maybe_copy_file(alias_sample, project_alias_script),
        eol(),
        maybe_copy_file(context_sample, project_context_script),
        eol(),
        line(),
        maybe_source_or_abort(project_declare_script, script, status),
        line(),
        source_or_abort(project_context_script, script, status),
        line(),
        source_or_abort(briteonyx_alias_script, script, status),
        line(),
        source_or_abort(project_alias_script, script, status),
        line(),
        _capture_environment("outgoing"),
        log_good("BriteOnyx has successfully activated this project"),
        eol(),
        log_info("To get started, try executing the 'cycle' alias..."),
        eol(),
        line(),
        disabled_content_footer(),
    ]


def generate(directory):
    gen(build(), directory, "activate.bash")


"""DisabledContent
        source(configure_python_script), eol(),
        source(briteonyx_alias_script), eol(),
        line(),
"""

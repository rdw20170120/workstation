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


def _alias_sample(config):
    return x(vr(config.var_project_directory), "/cfg/sample/alias.bash")


def _briteonyx_alias_script(config):
    return x(vr(config.var_project_directory), "/BriteOnyx/bin/lib/alias.bash")


def _briteonyx_declare_script(config):
    return x(vr(config.var_project_directory), "/BriteOnyx/bin/lib/declare.bash")


def _call_project_scripts(config):
    return [
        maybe_source_or_abort(dq(_project_declare_script(config)), _script, _status),
        line(),
        source_or_abort(dq(_project_context_script(config)), _script, _status),
        line(),
        source_or_abort(dq(_briteonyx_alias_script(config)), _script, _status),
        line(),
        source_or_abort(dq(_project_alias_script(config)), _script, _status),
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


def _configure_anaconda(config):
    return [
        comment("Configure Anaconda environment"),
        _capture_environment(config, "Anaconda", "before"),
        source_or_abort(_configure_anaconda_script(config), _script, _status),
        _capture_environment(config, "Anaconda", "after"),
        line(),
    ]


def _configure_anaconda_script(config):
    return x(
        vr(config.var_project_directory), "/BriteOnyx/bin/lib/configure_Anaconda.bash"
    )


def _configure_python(config):
    return [
        comment("Configure Python"),
        _capture_environment(config, "Python", "before"),
        source_or_abort(_configure_python_script(config), _script, _status),
        _capture_environment(config, "Python", "after"),
        line(),
    ]


def _configure_python_script(config):
    return x(
        vr(config.var_project_directory), "/BriteOnyx/bin/lib/configure_Python.bash"
    )


def _context_sample(config):
    return x(vr(config.var_project_directory), "/cfg/sample/context.bash")


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


def _create_logging_directory(config):
    return [
        comment("Establish logging directory for project"),
        export(
            vn(config.var_logging_directory),
            x(vr(config.var_project_directory), "/log"),
        ),
        eol(),
        command("maybe_create_directory_tree", dq(vr(config.var_logging_directory))),
        eol(),
        remembering(config.var_logging_directory),
        eol(),
    ]


def _create_temporary_directory(config):
    return [
        comment("Establish temporary directory for project"),
        export(
            vn(config.var_temporary_directory),
            x(vr(config.var_project_directory), "/tmp"),
        ),
        eol(),
        command("maybe_create_directory_tree", dq(vr(config.var_temporary_directory))),
        eol(),
        remembering(config.var_temporary_directory),
        eol(),
    ]


def _declare_briteonyx(config):
    return [
        source_or_abort(_briteonyx_declare_script(config), _script, _status),
        line(),
        note("We can now use BriteOnyx Bash functionality."),
        line(),
    ]


def _declare_logging():
    return [
        source_or_abort(_log4bash_script(), _script, _status),
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


def _detect_operating_system(config):
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
            export(vn(config.var_operating_system), "macOS"),
            eol(),
        ),
        else_(
            indent(),
            export(vn(config.var_operating_system), "UNKNOWN"),
            eol(),
        ),
        fi(),
        remembering(config.var_operating_system),
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


def _header(config):
    return [
        header_activation(),
        _comments(),
        _abort_if_activated(config),
        line(),
        _abort_if_missing_pwd(),
        line(),
    ]


def _log4bash_script():
    return x(vr("PWD"), "/BriteOnyx/bin/lib/declare-log4bash.bash")


def _prepare_file_system(config):
    return [
        _create_temporary_directory(config),
        line(),
        _create_logging_directory(config),
        line(),
        maybe_copy_file(dq(_alias_sample(config)), dq(_project_alias_script(config))),
        eol(),
        maybe_copy_file(
            dq(_context_sample(config)), dq(_project_context_script(config))
        ),
        eol(),
        line(),
    ]


def _prepare_paths(config):
    return [
        _remember_paths(config),
        line(),
        source_or_abort(_set_path_script(config), _script, _status),
        line(),
    ]


def _project_alias_script(config):
    return x(vr(config.var_project_directory), "/alias.bash")


def _project_context_script(config):
    return x(vr(config.var_project_directory), "/context.bash")


def _project_declare_script(config):
    return x(vr(config.var_project_directory), "/bin/lib/declare.bash")


def _project_path(config):
    return x(
        vr(config.var_project_directory),
        "/BriteOnyx/bin",
        ":",
        vr(config.var_project_directory),
        "/bin",
    )


def _remember(config):
    return [
        _declare_remembering(),
        line(),
        _remember_project_root(config),
        line(),
    ]


def _remember_paths(config):
    return [
        export(vn(config.var_project_path), _project_path(config)),
        eol(),
        line(),
        export_if_null(config.var_system_path, vr("PATH")),
        eol(),
        export_if_null(config.var_user_path, x(vr("HOME"), "/bin")),
        eol(),
        line(),
    ]


def _remember_project_root(config):
    return [
        export(vn(config.var_project_directory), vr("PWD")),
        eol(),
        remembering(config.var_project_directory),
        eol(),
    ]


def _set_path_script(config):
    return x(vr(config.var_project_directory), "/BriteOnyx/bin/lib/set_path.bash")


def build(config):
    return [
        _header(config),
        _create_capture_directory(config),
        _capture_environment(config, "activation", "before"),
        _declare_logging(),
        _remember(config),
        _declare_briteonyx(config),
        _prepare_paths(config),
        _detect_operating_system(config),
        _prepare_file_system(config),
        _configure_anaconda(config),
        _configure_python(config),
        _call_project_scripts(config),
        _capture_environment(config, "activation", "after"),
        _footer(),
    ]


"""DisabledContent
"""

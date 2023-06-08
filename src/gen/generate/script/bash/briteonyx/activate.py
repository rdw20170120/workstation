#!/usr/bin/env false
"""Generate script to activate project.

TODO: REFACTOR: Divide into two submodules that respect activating versus briteonyx calls
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.briteonyx.frame import *
from src_gen.script.bash.briteonyx.material import *
from src_gen.script.bash.briteonyx.render import generate

# Project modules   (relative references, NOT packaged, in project)

_script = "_Script"
_status = "_Status"


def _alias_sample(config):
    return x(vr(config.var_project_directory), "/cfg/sample/alias.bash")


def _briteonyx_alias_script(config):
    return x(vr(config.var_project_directory), "/BriteOnyx/bin/lib/alias.bash")


def _briteonyx_declare_script(config):
    return x(vr(config.var_project_directory), "/BriteOnyx/bin/lib/declare.bash")


def _build(config):
    return [
        note("We can now use BriteOnyx Bash functionality."),
        line(),
        _prepare_paths(config),
        line(),
        _detect_operating_system(config),
        line(),
        _prepare_file_system(config),
        line(),
        _configure_anaconda(config),
        line(),
        _configure_python(config),
        line(),
        _call_project_scripts(config),
        line(),
        _capture_environment(config, "activation", "after"),
        line(),
        _footer(),
    ]


def _call_project_scripts(config):
    return [
        maybe_source_or_abort(dq(_project_declare_script(config)), _script, _status),
        line(),
        source_or_abort(dq(_project_context_script(config)), _script, _status),
        line(),
        source_or_abort(dq(_briteonyx_alias_script(config)), _script, _status),
        line(),
        source_or_abort(dq(_project_alias_script(config)), _script, _status),
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


def _configure_anaconda(config):
    return [
        comment("Configure Anaconda environment"),
        _capture_environment(config, "Anaconda", "before"),
        source_or_abort(_configure_anaconda_script(config), _script, _status),
        _capture_environment(config, "Anaconda", "after"),
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
    ]


def _configure_python_script(config):
    return x(
        vr(config.var_project_directory), "/BriteOnyx/bin/lib/configure_Python.bash"
    )


def _context_sample(config):
    return x(vr(config.var_project_directory), "/cfg/sample/context.bash")


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


def _detect_operating_system(config):
    return [
        comment("Detect operating system"),
        todo("Add detection of various Linux, when we care"),
        export(vn(config.var_operating_system), substitute("uname")),
        eol(),
        remembering(config.var_operating_system),
        eol(),
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
    ]


def _prepare_paths(config):
    return [
        _remember_paths(config),
        line(),
        source_or_abort(_set_path_script(config), _script, _status),
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


def _remember_paths(config):
    return [
        export(vn(config.var_project_path), _project_path(config)),
        eol(),
        line(),
        export_if_null(config.var_system_path, vr("PATH")),
        eol(),
        export_if_null(config.var_user_path, x(vr("HOME"), "/bin")),
        eol(),
    ]


def _set_path_script(config):
    return x(vr(config.var_project_directory), "/BriteOnyx/bin/lib/set_path.bash")


def render(config):
    return generate(_build(config))


"""DisabledContent
"""

#!/usr/bin/env false
"""Generate script to set PATH."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.activating.frame import remembering
from src_gen.script.bash.briteonyx.frame import *
from src_gen.script.bash.briteonyx.material import *

# Project modules   (relative references, NOT packaged, in project)


def _build_path(config):
    return [
        line(),
        assign("PATH", vr(config.var_tool_path)),
        eol(),
        assign("PATH", x(vr("PATH"), ":", vr(config.var_system_path))),
        eol(),
        assign("PATH", x(vr("PATH"), ":", vr(config.var_project_path))),
        eol(),
        assign("PATH", x(vr("PATH"), ":", vr(config.var_user_path))),
        eol(),
        export(vn("PATH")),
        eol(),
    ]


def _comments():
    return [
        comment("Set PATH for project"),
        comment(),
        note("This specific ordering of PATH elements is REQUIRED."),
        comment("The Anaconda environment MUST come first"),
        comment("in order to override everything else."),
        comment("The system PATH element MUST precede any user PATH elements"),
        comment("in order to make collisions fail-fast"),
        comment("and"),
        comment("to defeat simple attempts"),
        comment("at redirecting system commands"),
        comment("as an attack vector."),
        comment("Similarly,"),
        comment("the project PATH element MUST precede the user PATH element"),
        comment("in order to make collisions fail-fast."),
        comment("This arrangement is best"),
        comment("for ensuring consistent behavior"),
        comment("of the environment, the system, and the project."),
        comment("It puts at-risk"),
        comment("only those user-specific commands, tools, and scripts"),
        comment("relevant to the current deployed environment--"),
        comment("where the specific user is best positioned to address them"),
        comment("and failures are most likely limited"),
        comment("to affecting only"),
        comment("the current project and user"),
        comment("(as they should)."),
    ]


def _maybe_initialize_paths(config):
    return [
        string_is_null(dq(vr(config.var_system_path))),
        and_(),
        " ",
        export(config.var_system_path, vr("PATH")),
        eol(),
        string_is_null(dq(vr(config.var_tool_path))),
        and_(),
        " ",
        export(config.var_tool_path, ""),
        eol(),
    ]


def _remember_paths(config):
    return [
        remembering(config.var_project_path),
        eol(),
        remembering(config.var_system_path),
        eol(),
        remembering(config.var_tool_path),
        eol(),
        remembering(config.var_user_path),
        eol(),
        remembering("PATH"),
        eol(),
    ]


def _require_variables(config):
    return [
        require_variable(config.var_project_path),
        eol(),
        require_variable(config.var_system_path),
        eol(),
        todo(require_variable(config.var_tool_path)),
        require_variable(config.var_user_path),
        eol(),
    ]


def build(config):
    return [
        header_sourced(config),
        _comments(),
        line(),
        _maybe_initialize_paths(config),
        line(),
        _require_variables(config),
        line(),
        _build_path(config),
        line(),
        _remember_paths(config),
        line(),
        disabled_content_footer(),
    ]


"""DisabledContent
"""

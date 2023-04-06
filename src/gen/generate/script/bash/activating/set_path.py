#!/usr/bin/env false
"""Generate script to set PATH."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.activating.frame import remembering
from src_gen.script.bash.briteonyx.frame import *
from src_gen.script.bash.briteonyx.material import *
# Project modules   (relative references, NOT packaged, in project)


def _build_path():
    return [
        line(),
        assign("PATH", vr("BO_PathTool")), eol(),
        assign("PATH", x(vr("PATH"), ":", vr("BO_PathSystem"))), eol(),
        assign("PATH", x(vr("PATH"), ":", vr("BO_PathProject"))), eol(),
        assign("PATH", x(vr("PATH"), ":", vr("BO_PathUser"))), eol(),
        export(vn("PATH")), eol(),
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


def _maybe_initialize_paths():
    return [
            string_is_null(dq(vr("BO_PathSystem"))), and_(), " ", export("BO_PathSystem", vr("PATH")), eol(),
            string_is_null(dq(vr("BO_PathTool"))), and_(), " ", export("BO_PathTool", ""), eol(),
    ]

def _remember_paths():
    return [
        remembering("BO_PathProject"), eol(),
        remembering("BO_PathSystem"), eol(),
        remembering("BO_PathTool"), eol(),
        remembering("BO_PathUser"), eol(),
        remembering("PATH"), eol(),
    ]

def _require_variables():
    return [
            require_variable("BO_PathProject"), eol(),
            require_variable("BO_PathSystem"), eol(),
            todo(require_variable("BO_PathTool")),
            require_variable("BO_PathUser"), eol(),
    ]


def build():
    return [
        header_sourced(),
        _comments(),
        line(),
        _maybe_initialize_paths(),
        line(),
        _require_variables(),
        line(),
        _build_path(),
        line(),
        _remember_paths(),
        line(),
        disabled_content_footer(),
    ]


"""DisabledContent
"""

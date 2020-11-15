from . import script_bash
from . import script_briteonyx

from throw_out_your_templates_3_core_visitor_map import VisitorMap

from .structure_bash import *
from .structure_briteonyx import *


class Script(script_briteonyx.Script):
    def __init__(self, content):
        script_briteonyx.Script.__init__(self)
        self._content = content


def build():
    return Script(
        [
            source_header(),
            """# NOTE: We MUST NOT EVER 'exit' during BriteOnyx bootstrap or activation
####################################################################################################
# NOTE: Uncomment the following two lines for debugging
# set -o verbose
# set -o xtrace
# TODO: SOMEDAY: Add inverse commands to isolate debugging

####################################################################################################
# Skip if BriteOnyx is already activated

Msg='$BO_Home is defined, assuming BriteOnyx already activated'
[[ -n "$BO_Home" ]] && logDebug "$Msg" && return 0

####################################################################################################
# Activate BriteOnyx

Script="$(dirname "$0")/../activate.src"
[[ ! -f "$Script" ]] && echo "FATAL: Missing script '$Script'" && return 63
source "$Script"; Status=$?
Msg="FATAL: Status $Status at '$0:$LINENO'"
[[ $Status -ne 0 ]] && echo "$Msg" && return $Status

####################################################################################################
# Verify post-conditions

boVariableRequire   BO_Home || boFailed "$0" "$LINENO" $? || return $?
boDirectoryRequire $BO_Home || boFailed "$0" "$LINENO" $? || return $?

boVariableRequire   BO_Project || boFailed "$0" "$LINENO" $? || return $?
boDirectoryRequire $BO_Project || boFailed "$0" "$LINENO" $? || return $?

####################################################################################################
# Successfully 'return', but do NOT 'exit'
return 0
""",
            disabled_content_footer(),
        ]
    )


VISITOR_MAP = VisitorMap(parent_map=script_bash.VISITOR_MAP)


def render(target_directory, target_file):
    script_bash.render(build(), VISITOR_MAP, target_directory, target_file)


""" Disabled content
"""

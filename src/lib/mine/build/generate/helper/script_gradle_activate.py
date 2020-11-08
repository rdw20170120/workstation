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
            """#!/bin/cat
[[ -n "$BO_Trace" ]] && echo "TRACE: Executing '$BASH_SOURCE'"
####################################################################################################
# NOTE: We MUST NOT EVER 'exit' during BriteOnyx bootstrap or activation
####################################################################################################
# NOTE: Uncomment the following two lines for debugging
# set -o verbose
# set -o xtrace
# TODO: SOMEDAY: Add inverse commands to isolate debugging

####################################################################################################
# Verify pre-conditions

[[   -z "$BO_Home"          ]] && echo 'FATAL: Missing $BO_Home'                && return 63
[[ ! -d "$BO_Home"          ]] && echo "FATAL: Missing directory '$BO_Home'"    && return 63
[[   -z "$BO_Project"       ]] && echo 'FATAL: Missing $BO_Project'             && return 63
[[ ! -d "$BO_Project"       ]] && echo "FATAL: Missing directory '$BO_Project'" && return 63
[[   -z "$BO_GradleVersion" ]] && echo 'FATAL: Missing $BO_GradleVersion'       && return 63
[[   -z "$BO_PathSystem"    ]] && echo 'FATAL: Missing $BO_PathSystem'          && return 63
[[   -z "$JAVA_HOME"        ]] && echo 'FATAL: Missing $JAVA_HOME'              && return 63

Dir=$BO_Home/activation
[[ ! -d "${Dir}" ]] && echo "FATAL: Missing directory '${Dir}'" && return 63

####################################################################################################
# Configure environment for Linux

Script=${Dir}/activate.src
[[ ! -f "${Script}" ]] && echo "FATAL: Missing script '${Script}'" && return 63

source ${Script}

Status=$?
[[ ${Status} -ne 0 ]] && echo "FATAL: Exit code ${Status} at '$0':$LINENO" && return ${Status}

####################################################################################################
# Verify post-conditions

[[ -z "$BO_E_Config"  ]] && echo 'FATAL: Missing $BO_E_Config'  && return 63
[[ -z "$BO_E_Ok"      ]] && echo 'FATAL: Missing $BO_E_Ok'      && return "$BO_E_Config"
[[ -z "$BO_PathLinux" ]] && echo 'FATAL: Missing $BO_PathLinux' && return "$BO_E_Config"

####################################################################################################
# Configure environment for Gradle on Linux

export BO_PathGradle=$JAVA_HOME/bin

PATH=${BO_PathProject}
PATH=$PATH:${BO_PathGradle}
PATH=$PATH:${BO_PathLinux}
PATH=$PATH:${BO_PathSystem}
export PATH

####################################################################################################
: <<'DisabledContent'
DisabledContent
""",
        ]
    )


VISITOR_MAP = VisitorMap(parent_map=script_bash.VISITOR_MAP)


def render(target_directory, target_file):
    script_bash.render(build(), VISITOR_MAP, target_directory, target_file)


""" Disabled content
"""

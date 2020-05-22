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
    return Script([
        '''#!/bin/cat
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

[[   -z "$BO_Home"       ]] && echo 'FATAL: Missing $BO_Home'                && return 63
[[ ! -d "$BO_Home"       ]] && echo "FATAL: Missing directory '$BO_Home'"    && return 63
[[   -z "$BO_Project"    ]] && echo 'FATAL: Missing $BO_Project'             && return 63
[[ ! -d "$BO_Project"    ]] && echo "FATAL: Missing directory '$BO_Project'" && return 63
[[   -z "$BO_PathSystem" ]] && echo 'FATAL: Missing $BO_PathSystem'          && return 63

Dir="$BO_Home/helper/activation"
[[ ! -d "${Dir}" ]] && echo "FATAL: Missing directory '${Dir}'" && return 63

####################################################################################################
# Configure Linux environment

Script="${Dir}/declare.src"
[[ ! -f "${Script}" ]] && echo "FATAL: Missing script '${Script}'" && return 63

source "${Script}"

Status=$?
[[ ${Status} -ne 0 ]] && echo "FATAL: Exit code ${Status} at '$0':$LINENO" && return ${Status}

####################################################################################################
# Verify post-conditions

[[ -z "$BO_E_Config" ]] && echo 'FATAL: Missing $BO_E_Config' && return 63
[[ -z "$BO_E_Ok"     ]] && echo 'FATAL: Missing $BO_E_Ok'     && return "$BO_E_Config"

####################################################################################################
# Configure PATH

export BO_PathLinux="$BO_Home/helper/invocation"
export BO_PathProject="$BO_Project/bin"

PATH="${BO_PathProject}"
PATH="$PATH:${BO_PathLinux}"
PATH="$PATH:${BO_PathSystem}"
export PATH

####################################################################################################
# Configure TMPDIR

if [[ -z "$TMPDIR" ]]; then
  echo 'WARN:  Missing $TMPDIR'
  [[ -z "$TMPDIR" ]] && [[ -n "$HOME"     ]] && export TMPDIR="$HOME/tmp"
  [[ -z "$TMPDIR" ]] && [[ -d /tmp ]] && [[ -n "$USER"     ]] && export TMPDIR="/tmp/$USER"
  [[ -z "$TMPDIR" ]] && [[ -d /tmp ]] && [[ -n "$USERNAME" ]] && export TMPDIR="/tmp/$USERNAME"
  [[ -z "$TMPDIR" ]] && echo 'FATAL: Missing $TMPDIR' && return 63
  # TODO: return "$BO_E_Config"
fi
export TMPDIR=$TMPDIR/$BO_ProjectName
echo "INFO:  Remembering TMPDIR='$TMPDIR'"
[[ ! -d "$TMPDIR" ]] && mkdir -p "$TMPDIR" && echo "INFO:  Created '$TMPDIR'"
[[ ! -d "$TMPDIR" ]] && echo "FATAL: Missing directory '$TMPDIR'" && return 63
# TODO: return "$BO_E_Config"

####################################################################################################
# Define common aliases

alias ignored='hg status --ignored | grep -v work-in-progress | grep -v wip'
alias someday='grep -Einrw TODO . --include=*.bash --include=*.src --include=*.txt | sort | grep -v work-in-progress'
alias todo='grep -Einrw TODO . --include=*.bash --include=*.src --include=*.txt | sort | grep -v work-in-progress | grep -v SOMEDAY'

####################################################################################################
: <<'DisabledContent'
DisabledContent
''',
    ])
    

VISITOR_MAP = VisitorMap(parent_map=script_bash.VISITOR_MAP)


def render(target_directory, target_file):
    script_bash.render(build(), VISITOR_MAP, target_directory, target_file)


""" Disabled content
"""


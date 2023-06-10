#!/usr/bin/env false
# Intended to be executed in a Bash shell via `source`.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
[[ -n "${BO_Trace}" ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
# NO: trap ... EXIT
###############################################################################
# Set PATH for project
#
# NOTE: This specific ordering of PATH elements is REQUIRED.
# The Anaconda environment MUST come first
# in order to override everything else.
# The system PATH element MUST precede any user PATH elements
# in order to make collisions fail-fast
# and
# to defeat simple attempts
# at redirecting system commands
# as an attack vector.
# Similarly,
# the project PATH element MUST precede the user PATH element
# in order to make collisions fail-fast.
# This arrangement is best
# for ensuring consistent behavior
# of the environment, the system, and the project.
# It puts at-risk
# only those user-specific commands, tools, and scripts
# relevant to the current deployed environment--
# where the specific user is best positioned to address them
# and failures are most likely limited
# to affecting only
# the current project and user
# (as they should).

[[ -z "${BO_PathSystem}" ]] && export BO_PathSystem=${PATH}
[[ -z "${BO_PathTool}" ]] && export BO_PathTool=

require_variable BO_PathProject
require_variable BO_PathSystem
# TODO: require_variable BO_PathTool
require_variable BO_PathUser


PATH=${BO_PathTool}
PATH=${PATH}:${BO_PathSystem}
PATH=${PATH}:${BO_PathProject}
PATH=${PATH}:${BO_PathUser}
export PATH

remembering BO_PathProject
remembering BO_PathSystem
remembering BO_PathTool
remembering BO_PathUser
remembering PATH

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
DisabledContent


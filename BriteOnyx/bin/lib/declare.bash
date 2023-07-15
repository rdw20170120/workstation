#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
# me() { echo ${BASH_SOURCE} ; }
me() ( echo ${BASH_SOURCE} ; )
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Declare other Bash function libraries
[[ -z "${BO_Project}" ]] &&
    1>&2 log_fatal "'BO_Project' is undefined, aborting" &&
    return 20

_Script=${BO_Project}/BriteOnyx/bin/lib/declare-base.bash
source "${_Script}" ; abort_on_fail $? "from ${_Script}"

_Script=${BO_Project}/BriteOnyx/bin/lib/declare-require.bash
source "${_Script}" ; abort_on_fail $? "from ${_Script}"

_Script=${BO_Project}/BriteOnyx/bin/lib/declare-common.bash
source "${_Script}" ; abort_on_fail $? "from ${_Script}"

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


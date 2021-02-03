#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# Declare other Bash function libraries
[[ -z "${BO_Project}" ]] &&
    1>&2 echo "'BO_Project' is undefined, aborting" &&
    return 20

_Script=${BO_Project}/BriteOnyx/bin/lib/declare-base.bash
source ${_Script} ; abort_on_fail $? "from ${_Script}"

_Script=${BO_Project}/BriteOnyx/bin/lib/declare-require.bash
source ${_Script} ; abort_on_fail $? "from ${_Script}"

_Script=${BO_Project}/BriteOnyx/bin/lib/declare-common.bash
source ${_Script} ; abort_on_fail $? "from ${_Script}"

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


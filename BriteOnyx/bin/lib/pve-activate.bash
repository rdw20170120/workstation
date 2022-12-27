#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# Activate Python virtual environment (PVE)

# TODO: NOTE: Disabled in favor of using Anaconda

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
export BO_PVE=${BO_Project}/.PVE
export BO_PathPve=${BO_PVE}/bin
export BO_PathTool=${BO_PathPve}
remembering BO_PVE
remembering BO_PathPve
remembering BO_PathTool

_Script=${BO_PathPve}/activate
if [[ -r "${_Script}" ]] ; then
    # Simplify PATH before activating Python virtual environment
    require_variable BO_PathProject
    require_variable BO_PathPve
    require_variable BO_PathSystem
    export PATH=${BO_PathSystem}:${BO_PathPve}:${BO_PathProject}

    log_debug "Sourcing script '${_Script}'"
    source "${_Script}" ; abort_on_fail $? "from ${_Script}"

    _Script=${BO_Project}/BriteOnyx/bin/lib/configure-Python.bash
    log_debug "Sourcing script '${_Script}'"
    source "${_Script}" ; abort_on_fail $? "from ${_Script}"
else
    log_warn "Ignoring, script '${_Script}' is unreadable"
fi
DisabledContent


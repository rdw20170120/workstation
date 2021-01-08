#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell during activation.
# NO: trap ... EXIT
###############################################################################
# Activate Python virtual environment (PVE)

export BO_PVE=${BO_Project}/.PVE
remembering BO_PVE
if [[ ! -d ${BO_PVE} ]] ; then
    log_warn "Missing Python virtual environment directory '${BO_PVE}'"
fi

export BO_PathPve=${BO_PVE}/bin
remembering BO_PathPve

Script=${BO_PathPve}/activate
if [[ -r "${Script}" ]] ; then
    log_debug "Sourcing script '${Script}'"
    source ${Script}
else
    log_warn "Script '${Script}' is not readable, ignoring"
fi

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -o verbose ; set -o xtrace
# Code to debug...
# set +o verbose ; set +o xtrace
: << 'DisabledContent'
DisabledContent


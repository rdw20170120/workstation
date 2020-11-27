#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell during activation.
# NO: trap ... EXIT
###############################################################################
# Activate Python virtual environment (PVE)

export PVE=$BO_Project/.PVE
remembering PVE
if [[ ! -d $PVE ]] ; then
    log_warn "Missing Python virtual environment directory '$PVE'"
fi

Script=$PVE/bin/activate
if [[ -r "$Script" ]] ; then
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


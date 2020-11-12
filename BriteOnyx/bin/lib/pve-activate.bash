#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "DEBUG: Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell.

report_status_and_return() {
    local -ir Status=$?
    [[ "${Status}" -ne 0 ]] && 
        1>&2 echo "FATAL: ${0} returning with status ${Status}"
    return ${Status}
}
trap report_status_and_return EXIT
###############################################################################
# Activate Python virtual environment (PVE)

# Remember Python virtual environment directory
export PVE=$BO_Project/.PVE
if [[ ! -d $PVE ]] ; then
    echo "WARN:  Python virtual environment directory '$PVE' is not found"
fi

# Source Python virtual environment activation script
Script=$PVE/bin/activate
if [[ -r "$Script" ]] ; then
    echo "INFO:  'source'ing script file '$Script'"
    source $Script
else
    echo "WARN:  Script file '$Script' is not readable, ignoring"
fi

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


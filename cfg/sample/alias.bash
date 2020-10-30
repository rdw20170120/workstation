#!/usr/bin/env false
[[ -n "${BO_Trace}" ]] && echo "TRACE: Executing${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell.

report_status_and_return() {
    local -ir Status=$?
    if [[ "${Status}" -eq 0 ]] ; then
        echo "INFO:  ${0} returning with status ${Status}"
    else
        echo "FATAL: ${0} returning with status ${Status}"
    fi
    return ${Status}
}
trap report_status_and_return EXIT
###############################################################################
# BASH alias definitions specific to this project

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


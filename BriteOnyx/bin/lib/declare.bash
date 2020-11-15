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
# Declare other BASH function libraries 

[[ -z "${BO_Project}" ]] &&
    echo "FATAL: 'BO_Project' is undefined, aborting" &&
    return 20

source ${BO_Project}/BriteOnyx/bin/lib/declare-base.bash
source ${BO_Project}/BriteOnyx/bin/lib/declare-require.bash
source ${BO_Project}/BriteOnyx/bin/lib/declare-common.bash

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


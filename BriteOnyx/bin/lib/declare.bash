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

Script=${BO_Project}/BriteOnyx/bin/lib/declare-base.bash
if [[ -r "${Script}" ]] ; then
#   echo "INFO:  Sourcing script ${Script}"
    source ${Script}
    status=$? ; [[ ${status} -ne 0 ]] && return ${status}
else
    echo "FATAL: Script file ${Script} is not readable, aborting"
    return 23
fi

Script=${BO_Project}/BriteOnyx/bin/lib/declare-require.bash
if [[ -r "${Script}" ]] ; then
#   echo "INFO:  Sourcing script ${Script}"
    source ${Script}
    status=$? ; [[ ${status} -ne 0 ]] && return ${status}
else
    echo "FATAL: Script file ${Script} is not readable, aborting"
    return 23
fi

Script=${BO_Project}/BriteOnyx/bin/lib/declare-common.bash
require_script "${Script}"
source "${Script}"
abort_on_fail $? "Failed to source script '${Script}'"

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


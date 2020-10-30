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
# Declare other BASH function libraries 

[[ -z "${BO_Project}" ]] &&
    echo "FATAL: 'BO_Project' is undefined, aborting" &&
    exit 20

Script=${BO_Project}/bin/lib/declare-base.bash
if [[ -r "${Script}" ]] ; then
    echo "INFO:  Sourcing script ${Script}"
    source ${Script}
    status=$? ; [[ ${status} -ne 0 ]] && exit ${status}
else
    echo "FATAL: Script file ${Script} is not readable, aborting"
    exit 23
fi

Script=${BO_Project}/bin/lib/declare-require.bash
if [[ -r "${Script}" ]] ; then
    echo "INFO:  Sourcing script ${Script}"
    source ${Script}
    status=$? ; [[ ${status} -ne 0 ]] && exit ${status}
else
    echo "FATAL: Script file ${Script} is not readable, aborting"
    exit 23
fi

Script=${BO_Project}/bin/lib/declare-common.bash
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


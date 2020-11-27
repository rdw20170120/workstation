#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell during activation.
# NO: trap ... EXIT
###############################################################################
# Library of helpful base BASH functions

abort_on_fail() {
    # Abort execution on fail of previous command
    [[ "$#" -lt 1 ]] &&
        log_error "Requires 1-2 argument(s) instead of $#" &&
        exit 127
    [[ "$#" -gt 2 ]] &&
        log_error "Requires 1-2 argument(s) instead of $#" &&
        exit 127
    # $1 = exit status of previous command (from $?)
    # $2 = OPTIONAL message to print on fail
    local -ir status=$1
    if [[ ${status} -ne 0 ]] ; then
        if [[ -z "$2" ]] ; then
            log_error "Aborting with status ${status}: Last command failed"
        else
            log_error "Aborting with status ${status}: $2"
        fi
        # NOTE: This is the one exception to NOT calling 'exit' from a function
        exit ${status}
    fi
    return 0
} && export -f abort_on_fail

abort_on_fail_with_output() {
    # Abort execution on fail of previous command, with output
    require_arguments $# 3
    # $1 = exit status of previous command (from $?)
    # #2 = file of captured output from command
    # $3 = message to print on fail
    local -ir status=$1
    [[ ${status} -ne 0 ]] &&
        [[ -n "$2" ]] &&
        [[ -r "$2" ]] &&
        log_error "OUTPUT:" &&
        cat $2
    abort_on_fail ${status} "$3"
} && export -f abort_on_fail_with_output

report_on_fail() {
    # Report status on fail of previous command
    require_arguments $# 2
    # $1 = exit status of previous command (from $?)
    # $2 = message to print on fail
    local -ir status=$1
    [[ ${status} -ne 0 ]] &&
        log_error "Status ${status}: Last command failed: $2"
    return 0
} && export -f report_on_fail

report_status_and_exit() {
    local -ir Status=$?
    [[ "${Status}" -ne 0 ]] && 
        log_warn "${0} exiting with status ${Status}"
    exit ${Status}
} && export -f report_status_and_exit

report_status_and_return() {
    local -ir Status=$?
    [[ "${Status}" -ne 0 ]] && 
        log_warn "${0} returning with status ${Status}"
    return ${Status}
} && export -f report_status_and_return

require_arguments() {
    # Require that caller received expected number of arguments
    [[ "$#" -ne 2 ]] &&
        log_error "Requires 2 argument(s) instead of $#" &&
        exit 127
    # $1 = actual number of arguments (from $#) received by caller
    # $2 = expected number of arguments
    [[ "$1" -eq $2 ]]
    abort_on_fail $? "Requires $2 arguments instead of $1"
} && export -f require_arguments

require_arguments_at_least() {
    # Require that caller received at least expected number of arguments
    [[ "$#" -ne 2 ]] &&
        log_error "Requires 2 argument(s) instead of $#" &&
        exit 127
    # $1 = actual number of arguments (from $#) received by caller
    # $2 = expected minimum number of arguments
    [[ "$1" -ge "$2" ]]
    abort_on_fail $? "Requires at least $2 arguments instead of $1"
} && export -f require_arguments_at_least

warn_on_error() {
    local -ir Status=$?
    [[ "${Status}" -ne 0 ]] && 
        log_warn "Status ${Status} from script ${0}"
    exit ${Status}
} && export -f warn_on_error

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -o verbose ; set -o xtrace
# Code to debug...
# set +o verbose ; set +o xtrace
: << 'DisabledContent'
DisabledContent


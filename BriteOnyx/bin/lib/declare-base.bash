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
# Library of helpful base BASH functions

abort_on_fail() {
    # Abort execution on fail of previous command
    [[ "$#" -lt 1 ]] &&
        echo "FATAL: Requires 1-2 argument(s) instead of $#" &&
        exit 127
    [[ "$#" -gt 2 ]] &&
        echo "FATAL: Requires 1-2 argument(s) instead of $#" &&
        exit 127
    # $1 = exit status of previous command (from $?)
    # $2 = OPTIONAL message to print on fail
    local -ir status=$1
    if [[ ${status} -ne 0 ]] ; then
        if [[ -z "$2" ]] ; then
            log_fatal "Status ${status}: Last command failed"
        else
            log_fatal "Status ${status}: $2"
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
        echo "FATAL: OUTPUT:" &&
        cat $2
    abort_on_fail ${status} "$3"
} && export -f abort_on_fail_with_output

log_debug() {
    # Log a message with DEBUG severity
    require_arguments $# 1
    # $1 = message
    echo "DEBUG: $1"
} && export -f log_debug

log_error() {
    # Log a message with ERROR severity
    require_arguments $# 1
    # $1 = message
    echo "ERROR: $1"
} && export -f log_error

log_fatal() {
    # Log a message with FATAL severity
    require_arguments $# 1
    # $1 = message
    echo "FATAL: $1"
} && export -f log_fatal

log_info() {
    # Log a message with INFO severity
    require_arguments $# 1
    # $1 = message
    echo "INFO:  $1"
} && export -f log_info

log_warn() {
    # Log a message with WARN severity
    require_arguments $# 1
    # $1 = message
    echo "WARN:  $1"
} && export -f log_warn

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

require_arguments() {
    # Require that caller received expected number of arguments
    [[ "$#" -ne 2 ]] &&
        echo "FATAL: Requires 2 argument(s) instead of $#" &&
        exit 127
    # $1 = actual number of arguments (from $#) received by caller
    # $2 = expected number of arguments
    [[ "$1" -eq $2 ]]
    abort_on_fail $? "Requires $2 arguments instead of $1"
} && export -f require_arguments

status_invert() {
    # Return inverse of status $1
    require_arguments $# 1
    # $1 = exit status from previous command (from $?)
    [[ "$1" -eq 0 ]] && return 1
    return 0
}

status_invert   0 ; [[ $? -eq 1 ]] ; abort_on_fail $? "Test 1 failed"
status_invert   1 ; [[ $? -eq 0 ]] ; abort_on_fail $? "Test 2 failed"
status_invert   2 ; [[ $? -eq 0 ]] ; abort_on_fail $? "Test 3 failed"
status_invert 127 ; [[ $? -eq 0 ]] ; abort_on_fail $? "Test 4 failed"
status_invert 128 ; [[ $? -eq 0 ]] ; abort_on_fail $? "Test 5 failed"
status_invert 129 ; [[ $? -eq 0 ]] ; abort_on_fail $? "Test 6 failed"
status_invert 254 ; [[ $? -eq 0 ]] ; abort_on_fail $? "Test 7 failed"
status_invert 255 ; [[ $? -eq 0 ]] ; abort_on_fail $? "Test 8 failed"
status_invert 256 ; [[ $? -eq 0 ]] ; abort_on_fail $? "Test 9 failed"

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


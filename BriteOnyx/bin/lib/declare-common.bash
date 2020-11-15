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
# Library of helpful common BASH functions

delete_file() {
    # Delete file $1
    require_arguments $# 1
    # $1 = file
    rm "$1"
    abort_on_fail $? "Could not delete file '$1'"
    forbid_path "$1"
} && export -f delete_file

execute_script() {
    # Execute script $1
    require_arguments_at_least $# 1
    # $1 = script file to execute
    # Additional optional arguments are passed to script
    require_script "$1" ; local -r Script=$1
    shift 1
    ${Script} $@
    abort_on_fail $? "Failed to execute script ${Script}"
} && export -f execute_script

expect_failure() {
    # Expect failure as actual status $1
    require_arguments $# 1
    # $1 = actual status code (from last command)
    require_value "$1" ; local -ir Actual=$1
    [[ "${Actual}" -eq 0 ]] &&
        log_error "Expected failure, but instead got status ${Actual}" &&
        exit 86
} && export -f expect_failure

expect_success() {
    # Expect success as actual status $1
    require_arguments $# 1
    # $1 = actual status code (from last command)
    require_value "$1" ; local -ir Actual=$1
    [[ "${Actual}" -ne 0 ]] &&
        log_error "Expected success, but instead got status ${Actual}" &&
        exit 86
} && export -f expect_success

maybe_delete_file() {
    # Delete file $1, if it exists
    require_arguments $# 1
    # $1 = file
    [[ -e "$1" ]] && delete_file "$1"
    forbid_path "$1"
} && export -f maybe_delete_file

status_invert() {
    # Return inverse of status $1
    require_arguments $# 1
    # $1 = exit status from previous command (from $?)
    [[ "$1" -eq 0 ]] && return 1
    return 0
} && export -f status_invert

write_file() {
    # Write content $2 to file $1
    require_arguments $# 2
    # $1 = target file
    # $2 = source content
    >$1 echo -n "$2"
    abort_on_fail $? "Failed to write file '$1'"
    require_file "$1"
} && export -f write_file

status_invert   0 ; [[ $? -eq 1 ]] ; abort_on_fail $? "status_invert test 1 failed"
status_invert   1 ; [[ $? -eq 0 ]] ; abort_on_fail $? "status_invert test 2 failed"
status_invert   2 ; [[ $? -eq 0 ]] ; abort_on_fail $? "status_invert test 3 failed"
status_invert 127 ; [[ $? -eq 0 ]] ; abort_on_fail $? "status_invert test 4 failed"
status_invert 128 ; [[ $? -eq 0 ]] ; abort_on_fail $? "status_invert test 5 failed"
status_invert 129 ; [[ $? -eq 0 ]] ; abort_on_fail $? "status_invert test 6 failed"
status_invert 254 ; [[ $? -eq 0 ]] ; abort_on_fail $? "status_invert test 7 failed"
status_invert 255 ; [[ $? -eq 0 ]] ; abort_on_fail $? "status_invert test 8 failed"
status_invert 256 ; [[ $? -eq 0 ]] ; abort_on_fail $? "status_invert test 9 failed"

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


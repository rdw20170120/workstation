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
# Library of helpful common BASH functions

delete_file() {
    # Delete file $1
    require_arguments $# 1
    # $1 = file
    rm "$1"
    abort_on_fail $? "Could not delete file '$1'"
    forbid_path "$1"
} && export -f delete_file

maybe_delete_file() {
    # Delete file $1, if it exists
    require_arguments $# 1
    # $1 = file
    if [[ -e "$1" ]] ; then
        delete_file "$1"
    fi
    forbid_path "$1"
} && export -f maybe_delete_file

write_file() {
    # Write content $2 to file $1
    require_arguments $# 2
    # $1 = target file
    # $2 = source content
    >$1 echo -n "$2"
    abort_on_fail $? "Could not write file '$1'"
    require_file "$1"
} && export -f write_file

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


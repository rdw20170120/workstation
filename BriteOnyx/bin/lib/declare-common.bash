#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
# me() { echo ${BASH_SOURCE} ; }
me() ( echo ${BASH_SOURCE} ; )
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Library of helpful common Bash functions

copy_file() {
    # Copy file $1 to $2
    require_arguments $# 2
    # $1 = source file
    # $2 = target file
    require_file "$1"
    cp "$1" "$2"
    abort_on_fail $? "Could not copy file '$1' to '$2'"
    require_file "$2"
} && export -f copy_file

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
    # TODO: Use `which` to allow searching PATH for script
    local Script
    Script=$1
    Script=$(which ${Script})
    require_script "${Script}"
    shift 1
    log_trace "Executing script ${Script}"
    "${Script}" $@
    abort_on_fail $? "Failed to execute script ${Script}"
} && export -f execute_script

expect_failure() {
    # Expect failure as actual status $1 regarding context $2
    require_arguments $# 2
    # $1 = actual status code (from last command)
    # $2 = context
    require_value "$1" ; local -ir Actual=$1
    require_value "$2" ; local -r  Context=$2
    if [[ "${Actual}" -eq 0 ]] ; then
        log_error "Expected failure, but instead got success status ${Actual} for ${Context}"
        exit 86
    else
        log_good "Expected failure, got status ${Actual} for ${Context}"
    fi
    return 0
} && export -f expect_failure

expect_success() {
    # Expect success as actual status $1 regarding context $2
    require_arguments $# 2
    # $1 = actual status code (from last command)
    # $2 = context
    require_value "$1" ; local -ir Actual=$1
    require_value "$2" ; local -r  Context=$2
    if [[ "${Actual}" -eq 0 ]] ; then
        log_good "Expected success, got status ${Actual} for ${Context}"
    else
        log_error "Expected success, but instead got failure status ${Actual} for ${Context}"
        exit 86
    fi
    return 0
} && export -f expect_success

maybe_copy_file() {
    # Copy file $1 to $2, if $2 does not already exist
    require_arguments $# 2
    require_file "$1"
    [[ ! -e "$2" ]] && cp "$1" "$2"
    require_file "$2"
} && export -f maybe_copy_file

maybe_create_directory_tree() {
    # Create directory $1, if it does not already exist, including parents
    require_arguments $# 1
    [[ ! -e "$1" ]] && \
        log_debug "Creating directory '$1'" && \
        mkdir -p "$1"
    require_directory "$1"
} && export -f maybe_create_directory_tree

maybe_delete_directory_tree() {
    # Delete directory $1, if it exists, including children
    require_arguments $# 1
    [[ -d "$1" ]] && \
        log_debug "Deleting directory '$1'" && \
        rm -fr "$1"
    forbid_path "$1"
} && export -f maybe_delete_directory_tree

maybe_delete_file() {
    # Delete file $1, if it exists
    require_arguments $# 1
    # $1 = file
    [[ -e "$1" ]] && delete_file "$1"
    forbid_path "$1"
} && export -f maybe_delete_file

maybe_recreate_directory_tree() {
    # Recreate directory $1, including parents
    require_arguments $# 1
    maybe_delete_directory_tree "$1"
    maybe_create_directory_tree "$1"
} && export -f maybe_recreate_directory_tree

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
    > "$1" echo -n "$2"
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
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


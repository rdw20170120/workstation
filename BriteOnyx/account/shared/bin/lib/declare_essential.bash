#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
# NOTE: Each new definition of this function via `source` REPLACES the previous
me() { echo ${BASH_SOURCE} ; }
# NOTE: Must still use raw Bash syntax until we have declared essential functions
# NOTE: Special header since this script is called while initializing Bash
1>&2 echo "TRACE: Executing '$(me)'"
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Declare essential Bash functions

################################################################################
# Declare logging functions
# NOTE: Reference environment variables for terminal control codes,
# which will initially be no-ops
# until defined in setup_terminal.bash

log_() {
    # Log message $1 at priority level $2 with a UTC timestamp
    # $1 = message to log
    # $2 = priority level (just one letter of D/E/F/G/I/T/W)
    # $3 = terminal control codes to match priority level
    local -r Text="$1"
    local -r Level="$2"
    local -r Control="$3"
    local -r Timestamp=$(date -u +"%Y%m%d %H%M%SZ")

    1>&2 echo "${Control}[${Timestamp} ${Level}] ${Text}${BO_ColorReset}"
} && export -f log_

log_debug() {
    # Log message $1 at DEBUG priority level
    # $1 = message to log
    log_ "$1" "D" "${BO_ColorDebug}"
} && export -f log_debug

log_error() {
    # Log message $1 at ERROR priority level
    # $1 = message to log
    log_ "$1" "E" "${BO_ColorError}"
} && export -f log_error

log_fatal() {
    # Log message $1 at FATAL priority level
    # $1 = message to log
    log_ "$1" "F" "${BO_ColorFatal}"
} && export -f log_fatal

log_good() {
    # Log message $1 at GOOD priority level
    # $1 = message to log
    log_ "$1" "G" "${BO_ColorGood}"
} && export -f log_good

log_info() {
    # Log message $1 at INFO priority level
    # $1 = message to log
    log_ "$1" "I" "${BO_ColorInfo}"
} && export -f log_info

log_trace() {
    # Log message $1 at TRACE priority level
    # $1 = message to log
    log_ "$1" "T" "${BO_ColorTrace}"
} && export -f log_trace

log_warn() {
    # Log message $1 at WARN priority level
    # $1 = message to log
    log_ "$1" "W" "${BO_ColorWarn}"
} && export -f log_warn

################################################################################

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
    local -ir Status=$1
    if [[ ${Status} -ne 0 ]] ; then
        if [[ -z "$2" ]] ; then
            log_error "Aborting with status ${Status}: Last command failed"
        else
            log_error "Aborting with status ${Status}: $2"
        fi
        # NOTE: This is the ONE exception to NOT calling 'exit' from a function
        exit ${Status}
    fi
    return 0
} && export -f abort_on_fail

################################################################################

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

require_script() {
    # Require script $1
    require_arguments $# 1
    # $1 = script that is required
    require_value "$1"
    [[ -r "$1" ]]
    abort_on_fail $? "Missing script '$1'"
} && export -f require_script

require_value() {
    # Require value $1
    require_arguments $# 1
    # $1 = value that is required
    [[ -n "$1" ]]
    abort_on_fail $? "Missing value '$1'"
} && export -f require_value

require_variable() {
    # Require variable $1
    require_arguments $# 1
    # $1 = name of variable that is required
    require_value "$1"
    local -r Name=$1
    [[ -n "${!Name}" ]]
    abort_on_fail $? "Undefined variable '$1'"
} && export -f require_variable

################################################################################

parent_of() {
    # Return the parent directory for filesystem entry $1
    # $1 = filesystem entry (file or directory)
    echo -n $(dirname $1)
} && export -f parent_of

prepare_to_source_optional() {
    # Prepare to `source` optional script $1,
    # returning 0 if the script is found and
    # returning 1 if the script is not found
    # Should be invoked like this:
    # _Script=DIR/SCRIPT.bash
    # prepare_to_source_optional "${_Script}" && source "${_Script}"
    if [[ -r "${_Script}" ]] ; then
        log_debug "Sourcing optional script '${_Script}'"
        return 0
    else
        log_info "Missing optional script '${_Script}'"
    fi
    return 1
} && export -f prepare_to_source_optional

prepare_to_source_required() {
    # Prepare to `source` required script $1,
    # returning 0 if the script is found and
    # abort if the script is not found
    # Should be invoked like this:
    # _Script=DIR/SCRIPT.bash
    # prepare_to_source_required "${_Script}" && source "${_Script}"
    if [[ -r "${_Script}" ]] ; then
        log_debug "Sourcing required script '${_Script}'"
        return 0
    fi
    abort_on_fail 99 "from prepare_to_source_required '${_Script}'"
} && export -f prepare_to_source_required

###############################################################################

get_temporary_file() {
    # Return a temporary file absolute pathname
    # Uses `$BO_DirTemp`
    # TODO: require_directory_in BO_DirTemp
    mktemp ${BO_DirTemp}/XXXXXXXX
    abort_on_fail $? "from mktemp"
} && export -f get_temporary_file

###############################################################################

export BO_DirTemp=${HOME}/tmp
[[ ! -e "${BO_DirTemp}" ]] &&
    echo "Creating directory '${BO_DirTemp}'" &&
    mkdir "${BO_DirTemp}"

prepare_to_source() {
    # TODO: DELETE
    prepare_to_source_required "${_Script}"
} && export -f prepare_to_source

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
# TODO: Show Bash's currently-active short options: `printf %s\\n "$-"`
# TODO: Show Bash's currently-active options: `set -o | grep -Fw on`
DisabledContent


#!/usr/bin/env false
# Intended to be executed in a Bash shell via `source`.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
[[ "${BO_Trace:-UNDEFINED}" != UNDEFINED ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace:-UNDEFINED}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
###############################################################################
# Declare essential Bash functions

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
        # NOTE: This is the one exception to NOT calling 'exit' from a function
        exit ${Status}
    fi
    return 0
} && export -f abort_on_fail

log_() {
    local -r Text="$1"
    local Level="$2"
    local -r Timestamp=$(date -u +"%Y%m%d %H%M%SZ")

    # Default Level to "info"
    [[ -z ${Level} ]] && Level=I

    1>&2 echo "[${Timestamp} ${Level}] ${Text}"
} && export -f log_

log_debug() {
    log_ "$1" D
} && export -f log_debug

log_error() {
    log_ "$1" E
} && export -f log_error

log_good() {
    log_ "$1" G
} && export -f log_good

log_info() {
    log_ "$@" I
} && export -f log_info

log_warn() {
    log_ "$1" W
} && export -f log_warn

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

###############################################################################
# TODO: Show Bash's currently-active short options: `printf %s\\n "$-"`
# TODO: Show Bash's currently-active options: `set -o | grep -Fw on`
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
DisabledContent


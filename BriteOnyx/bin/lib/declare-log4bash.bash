#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# Copied from https://github.com/fredpalmer/log4bash/blob/master/log4bash.sh
# on 24-Nov-2020
# by Rob Williams <rob.williams@optum.com>
#--------------------------------------------------------------------------------------------------
# log4bash - Makes logging in Bash scripting suck less
# Copyright (c) Fred Palmer
# Licensed under the MIT license
# http://github.com/fredpalmer/log4bash
#--------------------------------------------------------------------------------------------------
# This should probably be the right way - didn't have time to experiment though
# TODO: Implement this properly, if there is a real need to ever have color disabled.
# INTERACTIVE_MODE="$([ tty --silent ] && echo on || echo off)"
# INTERACTIVE_MODE=$([[ "$(uname)" == "Darwin" ]] && echo "on" || echo "off")

declare -x INTERACTIVE_MODE=OFF
[[ -n "${TERM}" ]] &&
    [[ "${TERM}" != "dumb" ]] &&
    INTERACTIVE_MODE=${TERM}
[[ -n "${COLORTERM}" ]] &&
    INTERACTIVE_MODE=${COLORTERM}

#--------------------------------------------------------------------------------------------------
# Begin Logging Section

if [[ "${INTERACTIVE_MODE}" == "OFF" ]] ; then
    # Then we don't care about log colors
    declare -rx LOG_DEFAULT_COLOR=""
    declare -rx LOG_DEBUG_COLOR=""
    declare -rx LOG_ERROR_COLOR=""
    declare -rx LOG_INFO_COLOR=""
    declare -rx LOG_WARN_COLOR=""
    declare -rx LOG_GOOD_COLOR=""
else
    declare -rx LOG_DEFAULT_COLOR="\033[0m"
    declare -rx LOG_DEBUG_COLOR="\033[1;34m"
    declare -rx LOG_ERROR_COLOR="\033[1;31m"
    declare -rx LOG_INFO_COLOR="\033[1m"
    declare -rx LOG_WARN_COLOR="\033[1;33m"
    declare -rx LOG_GOOD_COLOR="\033[1;32m"
fi

log_() {
    local text="$1"
    local level="$2"
    local color="$3"

    # Default level to "info"
    [[ -z ${level} ]] && level=I
    [[ -z ${color} ]] && color="${LOG_INFO_COLOR}"

    1>&2 echo -e "${color}[$(date -u +"%Y%m%d %H%M%SZ") ${level}] ${text}${LOG_DEFAULT_COLOR}"

    return 0
} && export -f log_

log_debug() {
    log_ "$1" D "${LOG_DEBUG_COLOR}"
} && export -f log_debug

log_error() {
    log_ "$1" E "${LOG_ERROR_COLOR}"
} && export -f log_error

log_good() {
    log_ "$1" G "${LOG_GOOD_COLOR}"
} && export -f log_good

log_info() {
    log_ "$@"
} && export -f log_info

log_warn() {
    log_ "$1" W "${LOG_WARN_COLOR}"
} && export -f log_warn

# This function scrubs the output of any control characters used in colorized output
# It's designed to be piped through with text that needs scrubbing.  The scrubbed
# text will come out the other side!
scrubbed() {
    # Essentially this strips all the control characters for log colors
    sed "s/[[:cntrl:]]\[[0-9;]*m//g"
} && export -f scrubbed

log_debug 'This is a debug message.'
log_info  'This is an informational message.'
log_warn  'This is a warning message.'
log_error 'This is an error message.'
log_good  'This is a good message.'

# End Logging Section
#--------------------------------------------------------------------------------------------------
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
# Useful global variables that users may wish to reference
SCRIPT_ARGS="$@"
SCRIPT_NAME="$0"
SCRIPT_NAME="${SCRIPT_NAME#\./}"
SCRIPT_NAME="${SCRIPT_NAME##/*/}"
SCRIPT_BASE_DIR="$(cd "$( dirname "$0")" && pwd )"

#--------------------------------------------------------------------------------------------------
# Begin Help Section

HELP_TEXT=""

# This function is called in the event of an error.
# Scripts which source this script may override by defining their own "usage" function
usage() {
    echo -e "${HELP_TEXT}"
    exit 99
}

# End Help Section
#--------------------------------------------------------------------------------------------------

log_campfire() {
    # This function performs a campfire notification with the arguments passed to it
    if [[ -z ${CAMPFIRE_API_AUTH_TOKEN} || -z ${CAMPFIRE_NOTIFICATION_URL} ]] ; then
        log_warning "CAMPFIRE_API_AUTH_TOKEN and CAMPFIRE_NOTIFICATION_URL are required."
        return 1
    fi
    local campfire_message="
    {
        \"message\": {
            \"type\":\"TextMessage\",
            \"body\":\"$@\"
        }
    }"
    curl                                                            \
        --write-out "\r\n"                                          \
        --user ${CAMPFIRE_API_AUTH_TOKEN}:X                         \
        --header 'Content-Type: application/json'                   \
        --data "${campfire_message}"                                \
        ${CAMPFIRE_NOTIFICATION_URL}
    return $?
}

log_captains()  {
    if type -P figlet >/dev/null ; then
        figlet -f computer -w 120 "$1"
    else
        log "$1"
    fi
    log_speak "$1"
    return 0
}

log_speak() {
    if type -P say >/dev/null ; then
        local easier_to_say="$1"
        case "${easier_to_say}" in
            studionowdev*)
                easier_to_say="studio now dev ${easier_to_say#studionowdev}"
                ;;
            studionow*)
                easier_to_say="studio now ${easier_to_say#studionow}"
                ;;
        esac
        say "${easier_to_say}"
    fi
    return 0
} && export -f log_speak
DisabledContent


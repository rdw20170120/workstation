#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# Copied from https://github.com/fredpalmer/log4bash/blob/master/log4bash.sh
# on 24-Nov-2020
# by Rob Williams <rob@refactory.biz>
#--------------------------------------------------------------------------------------------------
# log4bash - Makes logging in Bash scripting suck less
# Copyright (c) Fred Palmer
# Licensed under the MIT license
# http://github.com/fredpalmer/log4bash
#--------------------------------------------------------------------------------------------------
# This should probably be the right way - didn't have time to experiment though
# TODO: Implement this properly, if there is a real need to ever have color disabled.
# BO_Interactive="$([ tty --silent ] && echo on || echo off)"
# BO_Interactive=$([[ "$(uname)" == "Darwin" ]] && echo "on" || echo "off")

declare -x BO_Interactive=OFF
[[ -n "${TERM}" ]] &&
    [[ "${TERM}" != "dumb" ]] &&
    BO_Interactive=${TERM}
[[ -n "${COLORTERM}" ]] &&
    BO_Interactive=${COLORTERM}

#--------------------------------------------------------------------------------------------------
# Begin Logging Section

if [[ "${BO_Interactive}" == "OFF" ]] ; then
    declare -rx BO_LogColorDebug=
    declare -rx BO_LogColorDefault=
    declare -rx BO_LogColorError=
    declare -rx BO_LogColorGood=
    declare -rx BO_LogColorInfo=
    declare -rx BO_LogColorWarn=
else
    # NOTE: These have been configured
    # using the built-in `Solarized Dark` color preset
    # for iTerm2 3.3.20210223
    # running on Apple macOS 11.0.1 (Big Sur)
    declare -rx BO_LogColorDebug="\033[0;34m"
    declare -rx BO_LogColorDefault="\033[0m"
    declare -rx BO_LogColorError="\033[1;31m"
    declare -rx BO_LogColorGood="\033[1;37m"
    declare -rx BO_LogColorInfo="\033[0;32m"
    declare -rx BO_LogColorWarn="\033[0;33m"
fi

echo_with_color() {
    local -r Color="$1"
    local -r Text="$2"

    echo -e "${Color}${Text}${BO_LogColorDefault}"
} && export -f echo_with_color

log_() {
    local -r Text="$1"
    local Level="$2"
    local Color="$3"
    local -r Timestamp=$(date -u +"%Y%m%d %H%M%SZ")

    # Default Level to "info"
    [[ -z ${Level} ]] && Level=I
    [[ -z ${Color} ]] && Color="${BO_LogColorInfo}"

    1>&2 echo_with_color "${Color}" "[${Timestamp} ${Level}] ${Text}"
} && export -f log_

log_debug() {
    log_ "$1" D "${BO_LogColorDebug}"
} && export -f log_debug

log_error() {
    log_ "$1" E "${BO_LogColorError}"
} && export -f log_error

log_good() {
    log_ "$1" G "${BO_LogColorGood}"
} && export -f log_good

log_info() {
    log_ "$@"
} && export -f log_info

log_warn() {
    log_ "$1" W "${BO_LogColorWarn}"
} && export -f log_warn

# This function scrubs the output of any control characters used in colorized output
# It's designed to be piped through with text that needs scrubbing.  The scrubbed
# text will come out the other side!
scrubbed() {
    # Essentially this strips all the control characters for log colors
    sed "s/[[:cntrl:]]\[[0-9;]*m//g"
} && export -f scrubbed

log_sample_messages() {
    log_debug 'This is a debug message.'
    log_info  'This is an informational message.'
    log_warn  'This is a warning message.'
    log_error 'This is an error message.'
    log_good  'This is a good message.'
} && export -f log_sample_messages

show_color_swatches() {
    # ANSI color sequences
    echo_with_color "\033[0;30m" "0;30 Black"
    echo_with_color "\033[0;31m" "0;31 Red"
    echo_with_color "\033[0;32m" "0;32 Green"
    echo_with_color "\033[0;33m" "0;33 Brown/Orange"
    echo_with_color "\033[0;34m" "0;34 Blue"
    echo_with_color "\033[0;35m" "0;35 Purple"
    echo_with_color "\033[0;36m" "0;36 Cyan"
    echo_with_color "\033[0;37m" "0;37 Light Gray"
    echo_with_color "\033[1;30m" "1;30 Dark Gray"
    echo_with_color "\033[1;31m" "1;31 Light Red"
    echo_with_color "\033[1;32m" "1;32 Light Green"
    echo_with_color "\033[1;33m" "1;33 Yellow"
    echo_with_color "\033[1;34m" "1;34 Light Blue"
    echo_with_color "\033[1;35m" "1;35 Light Purple"
    echo_with_color "\033[1;36m" "1;36 Light Cyan"
    echo_with_color "\033[1;37m" "1;37 White"
} && export -f show_color_swatches

# show_color_swatches
log_sample_messages

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


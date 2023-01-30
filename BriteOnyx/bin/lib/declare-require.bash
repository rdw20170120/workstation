#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# Library of helpful Bash functions to express requirements

forbid_path() {
    # Forbid path $1
    require_arguments $# 1
    # $1 = path that is forbidden
    require_value "$1"
    [[ ! -e "$1" ]]
    abort_on_fail $? "Existing forbidden path '$1'"
} && export -f forbid_path

require_command() {
    # Require command $1
    require_arguments $# 1
    # $1 = command that is required
    require_value "$1"
    &>/dev/null which $1
    abort_on_fail $? "Missing command '$1'"
} && export -f require_command

require_command_in() {
    # Require command referenced in variable $1
    require_arguments $# 1
    # $1 = variable holding reference to command that is required
    require_variable "$1"
    local -r Name=$1
    require_command "${!Name}"
} && export -f require_command_in

require_directory() {
    # Require directory $1
    require_arguments $# 1
    # $1 = directory that is required
    require_value "$1"
    [[ -d "$1" ]]
    abort_on_fail $? "Missing directory '$1'"
} && export -f require_directory

require_directory_in() {
    # Require directory referenced in variable $1
    require_arguments $# 1
    # $1 = variable holding reference to directory that is required
    require_variable "$1"
    local -r Name=$1
    require_directory "${!Name}"
} && export -f require_directory_in

require_file() {
    # Require file $1
    require_arguments $# 1
    # $1 = file that is required
    require_value "$1"
    [[ -r "$1" ]]
    abort_on_fail $? "Missing file '$1'"
} && export -f require_file

require_file_in() {
    # Require file referenced in variable $1
    require_arguments $# 1
    # $1 = variable holding reference to file that is required
    require_variable "$1"
    local -r Name=$1
    require_file "${!Name}"
} && export -f require_file_in

require_function() {
    # Require function $1
    require_arguments $# 1
    # $1 = function that is required
    require_value "$1"
    &>/dev/null \
        declare -f $1
    abort_on_fail $? "Missing function '$1'"
} && export -f require_function

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
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


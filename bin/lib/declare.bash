#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell.
# NO: trap ... EXIT
###############################################################################
# Declare other BASH function libraries 

# TODO: CONTENT

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -o verbose ; set -o xtrace
# Code to debug...
# set +o verbose ; set +o xtrace
: << 'DisabledContent'

source ${BO_Project}/bin/lib/declare-NAME.bash  ; abort_on_fail $? "Failed to source script"

DisabledContent


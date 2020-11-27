#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell during activation.
# NO: trap ... EXIT
###############################################################################
# Declare other BASH function libraries 

[[ -z "${BO_Project}" ]] &&
    log_error "'BO_Project' is undefined, aborting" &&
    return 20

source ${BO_Project}/BriteOnyx/bin/lib/declare-base.bash
source ${BO_Project}/BriteOnyx/bin/lib/declare-require.bash
source ${BO_Project}/BriteOnyx/bin/lib/declare-common.bash

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -o verbose ; set -o xtrace
# Code to debug...
# set +o verbose ; set +o xtrace
: << 'DisabledContent'
DisabledContent


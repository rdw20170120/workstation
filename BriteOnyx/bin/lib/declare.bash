#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a Bash shell during activation.
# NO: trap ... EXIT
###############################################################################
# Declare other Bash function libraries 

[[ -z "${BO_Project}" ]] &&
    1>&2 echo "'BO_Project' is undefined, aborting" &&
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


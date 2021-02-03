#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# Jenkins-specific Bash alias definitions

# Jenkins
# will not be using
# any Bash alias definitions,
# since those are focused
# on supporting interactive use
# by a human.

# This file
# should be copied into place
# by `Jenkins/run_for_Jenkins`
# so that BriteOnyx activation
# is satisfied.

# NOTE: `${BO_Project}/alias.bash`
# is excluded by `.gitignore`;
# do NOT commit
# `${BO_Project}/alias.bash`
# to source control.

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


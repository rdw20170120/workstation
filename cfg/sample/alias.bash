#!/usr/bin/env false
# Intended to be sourced in a Bash shell.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# User/machine-specific Bash alias definitions

# Bash alias definitions
# specific to this copy
# of this project
# for this user
# on this machine.
# This file is sourced
# by `activate.bash`.
# You can manually source it
# into your current shell
# as a means to update
# with your latest edits.

# This is a sample.
# It is intended
# to be copied to
# `${BO_Project}/alias.bash`.
# `activate.bash`
# does this if it is missing
# (e.g., initial clone).

# NOTE: `${BO_Project}/alias.bash`
# is excluded by `.gitignore`;
# do NOT commit
# `${BO_Project}/alias.bash`
# to source control.

# alias NAME='COMMAND ARGS...'

alias vdiff='&> /dev/null meld'

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a Bash shell during activation.
# NO: trap ... EXIT
###############################################################################
# User/machine-specific Bash alias definitions

# Bash alias definitions
# specific to this copy
# of this project
# for this user
# on this machine.
# This file is sourced
# by the 'activate.bash' script.
# You can manually source it
# into your current shell
# as a means to update
# with your latest edits.

# This is a sample
# set of Bash aliases.
# It is intended
# to be copied to
# ${BO_Project}/alias.bash
# and edited as needed.
# The ${BO_Project}/activate.bash script
# does this if it is absent
# (initial clone).
# NOTE: ${BO_Project}/alias.bash
# is excluded by .gitignore;
# do NOT commit
# ${BO_Project}/alias.bash
# to source control.

# alias NAME='COMMAND ARGS...'

alias vdiff='&> /dev/null meld'

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -o verbose ; set -o xtrace
# Code to debug...
# set +o verbose ; set +o xtrace
: << 'DisabledContent'
DisabledContent


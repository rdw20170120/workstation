#!/usr/bin/env false
# Intended to be executed in a Bash shell via `source`.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
[[ -n "${BO_Trace}" ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
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

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
DisabledContent


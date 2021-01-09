#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a Bash shell during activation.
# NO: trap ... EXIT
###############################################################################
# Git alias definitions

# TODO: Implement

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -o verbose ; set -o xtrace
# Code to debug...
# set +o verbose ; set +o xtrace
: << 'DisabledContent'
# TODO: Create a script like BriteOnyx/bin/git-undelete
git reset
git ls-files -d -z | xargs -0 git checkout --
DisabledContent


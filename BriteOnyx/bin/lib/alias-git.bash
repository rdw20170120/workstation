#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell during activation.
# NO: trap ... EXIT
###############################################################################
# BASH alias definitions for source control

alias src_add='git add .'
alias src_branches='git branch --list -a'
alias src_commit='git commit'
alias src_ignored='git status --ignored'
alias src_log='git shortlog | tail -n -25'
alias src_pull='git pull'
alias src_push='git push'
alias src_status='git status'

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


#!/usr/bin/env false
[[ -n "${BO_Trace}" ]] && echo "TRACE: Executing${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell.

report_status_and_return() {
    local -ir Status=$?
    if [[ "${Status}" -eq 0 ]] ; then
        echo "INFO:  ${0} returning with status ${Status}"
    else
        echo "FATAL: ${0} returning with status ${Status}"
    fi
    return ${Status}
}
trap report_status_and_return EXIT
###############################################################################
# BASH alias definitions for source control

alias add='git add .'
alias branches='git branch --list -a'
alias commit='git commit'
alias ignored='git status --ignored'
alias ignored='git status --ignored'
alias log='git shortlog | tail -n -25'
alias pull='git pull'
alias push='git push'
alias status='git status'

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
# TODO: Create a script like BriteOnyx/bin/git-undelete
git reset
git ls-files -d -z | xargs -0 git checkout --
DisabledContent


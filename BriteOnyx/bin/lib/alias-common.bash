#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a Bash shell during activation.
# NO: trap ... EXIT
###############################################################################
# Common Bash alias definitions

# TODO: Consider augmenting the other forms of 'grep' too
grep_options='--color=auto'
grep_options+=' --exclude-dir=.git'
grep_options+=' --exclude-dir=.pytest_cache'
grep_options+=' --exclude-dir=.PVE'
grep_options+=' --exclude-dir=coverage'
# TODO: It appears that '--exclude-from' is not supported on macOS Mojave 10.14.6
# TODO: Perhaps I should consider installing a compatible 'grep' using Homebrew
# grep_options+=' --exclude-from=${BO_Project}/.grep-exclude-from'
# NOTE: For now, let's handle this by brute force
grep_options+=' --exclude="*.pyc"'
grep_options+=' --exclude="*.swp"'
alias grep="grep ${grep_options}"

alias cycle='clear ; test-run && gen-run -vvv && app-run -vvv'
alias list_sort_by_size='sort -nr --key=5'
alias logs_reset='rm -fr ${BO_Project}/log ; mkdir ${BO_Project}/log'
alias sync_generate='meld src/gen/generate/custom src/gen/generate/shared'
alias todo='grep -ER TODO ${BO_Project} | grep -v /log/'

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -o verbose ; set -o xtrace
# Code to debug...
# set +o verbose ; set +o xtrace
: << 'DisabledContent'
DisabledContent


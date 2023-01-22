#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# Common Bash alias definitions

# TODO: Consider augmenting the other forms of 'grep' too
grep_options='--color=auto'
grep_options+=' --exclude-dir=.git'
grep_options+=' --exclude-dir=.pytest_cache'
grep_options+=' --exclude-dir=coverage'
# TODO: It appears that '--exclude-from' is not supported on macOS Mojave 10.14.6
# TODO: Perhaps I should consider installing a compatible `grep`
# grep_options+=' --exclude-from="${BO_Project}/.grep-exclude-from"'
# NOTE: For now, let's handle this by brute force
grep_options+=' --exclude="*.pyc"'
grep_options+=' --exclude="*.swp"'
alias grep="grep ${grep_options}"

alias cycle='clear ; test-run && gen-run -vvv && app-run -vvv'
alias list_sort_by_size='sort -nr --key=5'
alias logs_reset='rm -fr "${BO_Project}/log" ; mkdir "${BO_Project}/log"'
alias redeclare='source "${BO_Project}/BriteOnyx/bin/lib/declare.bash"'
alias sync_generate='meld src/gen/generate/custom src/gen/generate/shared'
alias todo='grep -FR TODO "${BO_Project}" | grep -Fv .log | grep -Fv .out'

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
grep_options+=' --exclude-dir=.PVE'
DisabledContent


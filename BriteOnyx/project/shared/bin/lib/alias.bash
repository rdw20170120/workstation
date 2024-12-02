#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
# me() { echo ${BASH_SOURCE} ; }
me() ( echo ${BASH_SOURCE} ; )
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Common Bash alias definitions

grep_options='--color=auto'
grep_options+=' --exclude-dir=.anaconda'
grep_options+=' --exclude-dir=.coverage'
grep_options+=' --exclude-dir=.git'
grep_options+=' --exclude-dir=.hg'
grep_options+=' --exclude-dir=.pytest_cache'
grep_options+=' --exclude-dir=__pycache__'
grep_options+=' --exclude-dir=coverage'
# TODO: Consider augmenting the other forms of 'grep' too
# TODO: It appears that '--exclude-from' is not supported on macOS Mojave 10.14.6
# TODO: Perhaps I should consider installing a compatible `grep`
# grep_options+=' --exclude-from="${BO_Project}/.grep-exclude-from"'
# NOTE: For now, let's handle this by brute force
grep_options+=' --exclude="*.pyc"'
grep_options+=' --exclude="*.swp"'
alias grep="grep ${grep_options}"
unset grep_options

alias cycle='clear ; test-run && gen-run -vvv && py-format && app-run -vvv'
# TODO: alias generate='clear ; gen-run && py-format && gen-merge'
alias generate='clear ; gen-run && py-format'
alias gen-unsnapshot='rm -fr "${BO_DirSnapshot}/generated"'
alias list_sort_by_size='sort -nr --key=5'
alias logs_reset='rm -fr "${BO_DirLog}" ; mkdir "${BO_DirLog}"'
alias redeclare='source "${BO_Project}/BriteOnyx/bin/lib/declare.bash"'
alias someday='grep -FiR SOMEDAY "${BO_Project}" | grep -Fv .log | grep -Fv .out'
alias todo='grep -FiR TODO "${BO_Project}" | grep -Fv .log | grep -Fv .out'

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


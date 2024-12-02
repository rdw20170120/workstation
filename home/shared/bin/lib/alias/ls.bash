#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
me() { echo ${BASH_SOURCE} ; }
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Alias for ls

alias lB='ls -Aln'
alias lF='ls -AFln'
alias lL='ls -Lln'
alias lR='ls -AlnR'
alias la='ls -Al'
alias ll='ls -l'

: << 'DisabledContent'
DisabledContent


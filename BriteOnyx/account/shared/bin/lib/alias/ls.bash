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

alias la='ls -AFGhl -D "%Y-%m-%d %H:%M:%S"'
alias lc='ls -FG'
alias ll='ls -FGhl -D "%Y-%m-%d %H:%M:%S"'
alias lr='ls -FGhlRX -D "%Y-%m-%d %H:%M:%S"'

# Show tracking files touched during startup script execution
alias show-ran='ls -AFGhlrt -D "%Y-%m-%d %H:%M:%S" ~/.ran_* ~/.config/bash/.ran_* ~/.config/nushell/.ran_*'

: << 'DisabledContent'
DisabledContent


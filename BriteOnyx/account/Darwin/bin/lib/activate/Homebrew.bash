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
# Activate Homebrew

export BO_PathHomebrewBefore=${PATH}

if >/dev/null which brew ; then
    eval "$(${HOMEBREW_PREFIX}/bin/brew shellenv)"
else
    log_warn "Missing 'brew', skipping activation of Homebrew"
fi

export BO_PathHomebrewAfter=${PATH}

: << 'DisabledContent'
DisabledContent


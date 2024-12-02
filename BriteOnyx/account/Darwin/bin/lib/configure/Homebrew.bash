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
# Configure Homebrew

case "${BO_ARCH}" in
    arm64) 
        # NOTE: On Apple macOS running on Apple Silicon
        export HOMEBREW_PREFIX=/opt/homebrew
        ;;
    x86_64)
        # NOTE: On Apple macOS running on Intel CPU
        export HOMEBREW_PREFIX=/usr/local
        ;;
    *)
        log_warn "HOMEBREW_PREFIX is UNKNOWN for architecture '${BO_ARCH}'"
        export HOMEBREW_PREFIX=${HOME}/HomeBrew
        ;;
esac

export BO_PathHomebrew=${HOMEBREW_PREFIX}/bin:${HOMEBREW_PREFIX}/sbin

: << 'DisabledContent'
DisabledContent


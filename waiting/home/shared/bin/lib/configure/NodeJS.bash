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
# Configure NodeJS (and related tools)

# Node Version Manager (NVM)
# based on Homebrew install
export NVM_DIR="${HOME}/.nvm"
[[ ! -e "${NVM_DIR}" ]] && mkdir "${NVM_DIR}"

: << 'DisabledContent'
DisabledContent


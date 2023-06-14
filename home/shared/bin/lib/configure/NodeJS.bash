#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Configure NodeJS (and related tools)

# Node Version Manager (NVM)
# based on Homebrew install
export NVM_DIR="${HOME}/.nvm"
[[ ! -e "${NVM_DIR}" ]] && mkdir "${NVM_DIR}"

: << 'DisabledContent'
DisabledContent


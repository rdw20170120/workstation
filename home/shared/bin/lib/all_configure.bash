#!/bin/false
# NOTE:  This file is intended to be executed while initializing a Bash shell.
################################################################################

_Script=${HOME}/bin/lib/configure/bash.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure/dircolors.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure/grep.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure/less.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure/vim.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure/Anaconda.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure/Homebrew.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure/Kubernetes.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure/NodeJS.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure/Pyenv.bash
prepare_to_source "${_Script}" && source "${_Script}"

unset _Script

: << 'DisabledContent'
DisabledContent


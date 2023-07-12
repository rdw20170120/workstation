#!/usr/bin/env false
# NOTE:  This file is intended to be executed while initializing a Bash shell.
################################################################################

_Script=${HOME}/bin/lib/activate/Anaconda.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/activate/Homebrew.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/activate/NodeJS.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/activate/Pyenv.bash
prepare_to_source "${_Script}" && source "${_Script}"

unset _Script

: << 'DisabledContent'
DisabledContent


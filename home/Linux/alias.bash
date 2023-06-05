#!/usr/bin/env false
# Intended to be sourced in a Bash shell.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# TODO: DESCRIPTION

_Script=${HOME}/bin/lib/alias_for_cd.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/alias_for_git.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/alias_for_inputrc.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/alias_for_ls.bash
prepare_to_source "${_Script}" && source "${_Script}"

unset _Script

: << 'DisabledContent'
DisabledContent


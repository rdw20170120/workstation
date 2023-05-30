#!/usr/bin/env false
# Intended to be sourced in a Bash shell.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# TODO: DESCRIPTION

_Script=${HOME}/bin/lib/alias_for_cd.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

_Script=${HOME}/bin/lib/alias_for_git.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

_Script=${HOME}/bin/lib/alias_for_inputrc.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

_Script=${HOME}/bin/lib/alias_for_ls.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

unset _Script

: << 'DisabledContent'
DisabledContent


#!/usr/bin/env bash
# Intended to be executed in a Bash shell during user initialization (login).
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
[[ -n "${BO_Trace}" ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
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

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
DisabledContent


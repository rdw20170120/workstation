#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT export this function, it only works if defined locally
# NOTE: Each new definition of this function REPLACES the previous via `source`
me() { echo ${BASH_SOURCE} ; }
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# TODO: DELETE: Hard-coded for now, until I implement code-generation below

# TODO: DISABLED
# _Script=${HOME}/bin/lib/activate/Anaconda.bash
# prepare_to_source_required "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/activate/Homebrew.bash
prepare_to_source_required "${_Script}" && source "${_Script}"

# TODO: DISABLED
# _Script=${HOME}/bin/lib/activate/Pyenv.bash
# prepare_to_source_required "${_Script}" && source "${_Script}"

################################################################################
# Generate and `source` a temporary script to `source` other scripts
_MyDir=$(parent_of $(me))
_Script=$(get_temporary_file)
log_debug "Generating script '${_Script}'"
cat >"${_Script}" <<EndOfScript
log_trace "Executing '${_Script}'"

# Nothing to do yet

unset _Script

EndOfScript
require_script "${_Script}" && source "${_Script}"

unset _Script

################################################################################
: << 'DisabledContent'
DisabledContent


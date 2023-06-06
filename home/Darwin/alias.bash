#!/usr/bin/env false
# Intended to be executed in a Bash shell during user initialization (login).
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
[[ "${BO_Trace:-UNDEFINED}" != UNDEFINED ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace:-UNDEFINED}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
# NO: trap ... EXIT
################################################################################

_Script=${HOME}/bin/lib/alias_for_bash.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/alias_for_cd.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/alias_for_git.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/alias_for_inputrc.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/alias_for_ls.bash
prepare_to_source "${_Script}" && source "${_Script}"

unset _Script

# For using Spacemacs (Emacs) on Apple macOS (Darwin) based on manual installation
# alias emacs='/Applications/Emacs.app/Contents/MacOS/emacs-nw'

# ssh
# alias connect_to_dev='ssh DevAtAws'

: << 'DisabledContent'
DisabledContent


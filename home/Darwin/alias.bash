#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################

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

_Script=${HOME}/bin/lib/alias_for_ls.bash
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

unset _Script

: << 'DisabledContent'
# For using Spacemacs (Emacs) on Apple macOS (Darwin) based on manual installation
alias emacs='/Applications/Emacs.app/Contents/MacOS/emacs-nw'

# ssh
alias connect_to_dev='ssh DevAtAws'
DisabledContent


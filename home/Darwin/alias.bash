#!/usr/bin/env false
# This script is sourced into a Bash shell during user initialization.
################################################################################

_Script=${HOME}/bin/lib/alias_for_Bash.bash
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


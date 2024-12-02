#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
me() { echo ${BASH_SOURCE} ; }
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Aliases for working with ~/.inputrc

alias configure_readline_from='bind -f'
alias show_readline_keymap_current='bind -p'
alias show_readline_keymap_emacs-ctlx='bind -pm emacs-ctlx'
alias show_readline_keymap_emacs-meta='bind -pm emacs-meta'
alias show_readline_keymap_emacs-standard='bind -pm emacs-standard'
alias show_readline_keymap_vi-command='bind -pm vi-command'
alias show_readline_keymap_vi-insert='bind -pm vi-insert'
alias show_readline_keymap_vi-move='bind -pm vi-move'
alias show_readline_macros='bind -s'
alias show_readline_variables='bind -v'

: << 'DisabledContent'
DisabledContent


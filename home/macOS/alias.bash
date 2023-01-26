#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.

# Add an "alert" alias for long running commands.  Use like so:
# sleep 10; alert
# alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

alias dir='dir --color=auto'
alias vdir='vdir --color=auto'

alias la='ls -Al'
alias lB='ls -Aln'
alias ll='ls -l'
alias lL='ls -Lln'

alias vim='nvim'

alias jump_experiment='cd ~/repo/GitLab/wip/experiment'
alias jump_workstation='cd ~/repo/GitHub/wip/workstation'

# For working with two local copies of the same repository
alias jump_reference='cd "${BO_DirReference}"'
alias jump_Work_In_Progress='cd "${BO_DirWorkInProgress}"'

# Git
alias git_diff_check='git diff --check'
alias git_rebase_continue='git rebase --continue'
alias ignored='git status --ignored'
alias status='git status'
alias unstage='git restore --staged'

# For working with ~/.inputrc
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


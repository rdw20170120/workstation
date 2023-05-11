#!/bin/false
# NOTE:  This file is intended to be sourced into a Bash shell.

# Add an "alert" alias for long running commands.  Use like so:
# sleep 10; alert
# alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# cd
alias jump_build='cd ~/repo/GitHub/wip/build'
alias jump_experiment='cd ~/repo/GitLab/wip/experiment'
alias jump_interview='cd ~/repo/GitHub/wip/spring-test-project/complete'
alias jump_javascript='cd ~/repo/GitHub/wip/javascript'
alias jump_mono='cd ~/repo/GitLab/wip/private-mono'
alias jump_pythonspeed='cd ~/repo/GitLab/wip/pythonspeed'
alias jump_workstation='cd ~/repo/GitHub/wip/workstation'
# For working with two local copies of the same repository
alias jump_reference='cd "${BO_DirReference}"'
alias jump_Work_In_Progress='cd "${BO_DirWorkInProgress}"'

# git
alias gi='git status --ignored'
alias git_branch_delete='git branch --delete'
alias git_branch_list='git branch --list'
alias git_diff_check='git diff --check'
alias git_log_nice='git log --all --decorate --graph --oneline'
alias git_nostash='git stash clear'
alias git_rebase_continue='git rebase --continue'
alias git_rebase_finish='git push origin HEAD --force'
alias git_rebase_prepare='git fetch origin'
alias git_rebase_start='git rebase origin'
alias git_stage='git stage'
alias git_stash='git stash push'
alias git_unstage='git restore --staged'
alias git_unstash='git stash apply'
alias gs='git status'

# ls (and related)
alias dir='dir --color=auto'
alias lB='ls -Aln'
alias lL='ls -Lln'
alias la='ls -Alo'
alias ll='ls -lo'
alias vdir='vdir --color=auto'

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


#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Aliases for git

alias gi='git status --ignored'
alias git_branch_delete='git branch --delete'
alias git_branch_list='git branch --list'
alias git_branch_list_remote='git branch --remotes'
alias git_diff_check='git diff --check'
alias git_log_nice='git log --all --decorate --graph --oneline'
alias git_nostash='git stash clear'
alias git_rebase_abort='git rebase --abort'
alias git_rebase_continue='git rebase --continue'
alias git_rebase_finish='git push origin HEAD --force'
alias git_rebase_prepare='git fetch origin'
alias git_rebase_start='git rebase origin'
alias git_stage='git stage'
alias git_stash='git stash push'
alias git_unstage='git restore --staged'
alias git_unstash='git stash apply'
alias gs='git status'

: << 'DisabledContent'
DisabledContent


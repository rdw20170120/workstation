#!/usr/bin/env false
# NO: set -e
# DISABLED: set -x
# Intended to be `source`d in a BASH shell by the user.
###############################################################################
# BASH alias definitions for source control

alias add='git add .'
alias branches='git branch --list -a'
alias commit='git commit'
alias ignored='git status --ignored'
alias ignored='git status --ignored'
alias log='git shortlog | tail -n -25'
alias pull='git pull'
alias push='git push'
alias status='git status'

###############################################################################
: << 'DisabledContent'
# TODO: Create a script like BriteOnyx/bin/git-undelete
git reset
git ls-files -d -z | xargs -0 git checkout --
DisabledContent


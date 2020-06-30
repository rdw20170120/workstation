#!/usr/bin/env false
# NO: set -e
# DISABLED: set -x
# Intended to be `source`d in a BASH shell by the user.
###############################################################################
# BASH alias definitions for source control

alias add='git add .'
alias commit='git commit'
alias ignored='git status --ignored'
alias ignored='git status --ignored'
alias log='git shortlog | tail -n -10'
alias pull='git pull'
alias push='git push'
alias status='git status'

# TODO: Consider augmenting the other forms of 'grep' too
grep_options='--color=auto'
grep_options+=' --exclude-dir=.git'
grep_options+=' --exclude-dir=.pytest_cache'
grep_options+=' --exclude-dir=.PVE'
# TODO: It appears that '--exclude-from' is not supported on macOS Mojave 10.14.6
# TODO: Perhaps I should consider installing a compatible 'grep' using Homebrew
# grep_options+=' --exclude-from=$BO_Project/.grep-exclude-from'
# NOTE: For now, let's handle this by brute force
grep_options+=' --exclude="*.pyc"'
grep_options+=' --exclude="*.swp"'

alias grep="grep $grep_options"

alias todo='grep -ER TODO $BO_Project'

###############################################################################
: << 'DisabledContent'
# TODO: Create a script like BriteOnyx/bin/git-undelete
git reset
git ls-files -d -z | xargs -0 git checkout --
DisabledContent


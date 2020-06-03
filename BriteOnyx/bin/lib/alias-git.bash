#!/bin/false
# NOTE: Intended to be sourced into a BASH shell

# BASH alias definitions for source control

alias add='git add .'
alias commit='git commit'
alias ignored='git status --ignored'
alias ignored='git status --ignored'
alias log='git shortlog'
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

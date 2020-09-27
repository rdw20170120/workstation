#!/usr/bin/env false
# NO: set -e
# DISABLED: set -x
# Intended to be sourced in a BASH shell by the user.
###############################################################################
# BASH alias definitions specific to this project

alias cycle='clear ; test-run && gen-run -vvv && app-run -vvv'

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

alias list-sort-by_size='sort -nr --key=5'

alias logs-reset='rm -fr ${BO_Project}/log ; mkdir ${BO_Project}/log'

alias todo='grep -ER TODO $BO_Project | grep -v /log/'

###############################################################################
: << 'DisabledContent'
DisabledContent


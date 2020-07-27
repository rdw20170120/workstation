#!/usr/bin/env false
# NO: set -e
# DISABLED: set -x
# Intended to be `source`d in a BASH shell by the user.
###############################################################################
# BASH alias definitions specific to this project

alias cycle='clear ; test-run && generate && app-run -vv'
alias list-sort='sort -nr --key=5'

###############################################################################
: << 'DisabledContent'
DisabledContent


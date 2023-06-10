#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Configure less

export PAGER=less

################################################################################
# Make less more friendly
# for non-text input files,
# see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

: << 'DisabledContent'
DisabledContent


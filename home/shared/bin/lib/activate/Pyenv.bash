#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Activate Pyenv

if >/dev/null which pyenv ; then
    eval "$(pyenv init -)"
    # eval "$(pyenv init --path)"
else
    echo "DEBUG: Missing 'pyenv', skipping activation of Pyenv"
fi

: << 'DisabledContent'
DisabledContent


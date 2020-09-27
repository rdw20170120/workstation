#!/usr/bin/env false
# NO: set -e
# DISABLED: set -x
# Intended to be sourced in a BASH shell by the user.
###############################################################################
# Activate Python virtual environment (PVE)

# Remember Python virtual environment directory
export PVE=$BO_Project/.PVE
if [[ ! -d $PVE ]] ; then
    echo "WARN:  Python virtual environment directory '$PVE' is not found"
fi

# Source Python virtual environment activation script
Script=$PVE/bin/activate
if [[ -r "$Script" ]] ; then
    echo "INFO:  'source'ing script file '$Script'"
    source $Script
else
    echo "WARN:  Script file '$Script' is not readable, ignoring"
fi

###############################################################################
: << 'DisabledContent'
DisabledContent


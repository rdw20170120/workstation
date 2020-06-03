#!/bin/false
# NOTE: Intended to be sourced into a BASH shell by another script.

# Remember Python virtual environment directory
export PVE=$BO_Project/.PVE
if [[ ! -d $PVE ]] ; then
    echo "WARN:  Python virtual environment directory '$PVE' is not found"
fi

# Source the Python virtual environment activation script
Script=$PVE/bin/activate
if [[ -r "$Script" ]] ; then
    echo "INFO:  'source'ing script file '$Script'"
    source $Script
else
    echo "WARN:  Script file '$Script' is not readable, ignoring"
fi

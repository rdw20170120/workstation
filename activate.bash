#!/usr/bin/env/false
# NOTE: Intended to be sourced into a BASH shell by the user.
###############################################################################
# NOTE: We MUST NOT EVER 'exit' during BriteOnyx bootstrap or activation
# NOTE: NO: set -e
# DISABLED: set -x
###############################################################################
# Activate the BriteOnyx framework to manage this project directory tree
#
# NOTE: This script, and EVERY script that it calls, must NOT invoke 'exit'!
# The user calling this script must be allowed to preserve their shell and
# every effort must be made to inform the user of problems while continuing
# execution where possible.  Terminating the shell robs the user of useful
# feedback and interrupts their work, which is unacceptable.  Instead, the BASH
# 'return' statement should be invoked to end execution with an appropriate
# status code.
###############################################################################

if [[ -n "$BO_Project" ]] ; then
    echo "FATAL: This project is already activated as '$BO_Project', aborting"
    return 1  # Exit from the script, but not from the shell
fi

env | sort > $PWD/BO-incoming.env

echo "INFO:  Activating this directory '$PWD' as the current project"
export BO_Project=$PWD

# Detect operating system
dir=$(uname)
if [[ "$dir" == "Darwin" ]] ; then
    export BO_OS=macOS
else
    export BO_OS=Linux
fi
echo "INFO:  Remembering BO_OS='$BO_OS'"

# Create random temporary directory
if [[ "$BO_OS" == "macOS" ]] ; then
    dir=$(mktemp -d -t "BO-$USER")
else
    # TODO: FIX: for Ubuntu
    dir=$(mktemp -d -t "BO-$USER")
fi
if [[ -d "$dir" ]] ; then
    TMPDIR=$dir
    echo "INFO:  Temporary directory '$TMPDIR' created"
fi
if [[ -d "$TMPDIR" ]] ; then
    echo "INFO:  Remembering TMPDIR='$TMPDIR'"
    export TMPDIR
else
    echo "FATAL: Failed to establish temporary directory '$TMPDIR', aborting"
    return 1  # Exit from the script, but not from the shell
fi

export BO_PathProject=$BO_Project/bin
echo "INFO:  Remembering BO_PathProject=$BO_PathProject"

[[ -z "$BO_PathSystem" ]] && \
    export BO_PathSystem=$PATH && \
    echo "INFO:  Remembering BO_PathSystem='$BO_PathSystem'"

[[ -z "$BO_PathUser" ]] && \
    export BO_PathUser=$HOME/bin && \
    echo "INFO:  Remembering BO_PathUser='$BO_PathUser'"

# Reset PATH before activating Python virtual environment
export PATH=$BO_PathSystem

env | sort > $PWD/BO-PVE-prior.env

Script=$BO_Project/bin/lib/pve-activate.bash
if [[ -r "$Script" ]] ; then
    echo "INFO:  'source'ing script file '$Script'"
    source $Script
else
    echo "WARN:  Script file '$Script' is not readable, ignoring"
fi

env | sort > $PWD/BO-PVE-after.env

[[ -z "$BO_PathPve" ]] && \
    export BO_PathPve=$PATH && \
    echo "INFO:  Remembering BO_PathPve='$BO_PathPve'"

export PATH=$BO_PathSystem:$BO_PathPve:$BO_PathProject:$BO_PathUser
echo "INFO:  Remembering 'PATH' as '$PATH'"

Script=$BO_Project/alias-git.bash
if [[ -r "$Script" ]] ; then
    echo "INFO:  'source'ing script file '$Script'"
    source $Script
else
    echo "WARN:  Script file '$Script' is not readable, ignoring"
fi

Script=$BO_Project/alias-project.bash
if [[ -r "$Script" ]] ; then
    echo "INFO:  'source'ing script file '$Script'"
    source $Script
else
    echo "WARN:  Script file '$Script' is not readable, ignoring"
fi

Script=$BO_Project/context.bash
if [[ -r "$Script" ]] ; then
    echo "INFO:  'source'ing script file '$Script'"
    source $Script
else
    echo "WARN:  Script file '$Script' is not readable, ignoring"
fi

env | sort > $PWD/BO-outgoing.env

###############################################################################
: << 'DisabledContent'
DisabledContent


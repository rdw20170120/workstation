#!/usr/bin/env bash -e
# This script is intended to be executed by a user in a BASH shell.

# Compile all Python source

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

echo "INFO: Found these files..."
python3 -m compileall -f $DirProject/src


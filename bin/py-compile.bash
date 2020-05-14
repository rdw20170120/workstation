#!/bin/bash
set -ex

# Compile all Python source

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

echo "INFO: Found these files..."
python3 -m compileall -f $DirProject/src


#!/usr/bin/env bash -ex
# This script is intended to be executed by a user in a BASH shell.

# Report Python dependencies

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

pip3 freeze --all


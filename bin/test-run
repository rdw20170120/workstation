#!/usr/bin/env bash
set -e
# This script is intended to be executed by a user in a BASH shell.

# Run tests

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

clear
cd $DirProject/src
py.test --log-file=pytest.log --show-capture=no


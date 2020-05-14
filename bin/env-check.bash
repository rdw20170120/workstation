#!/usr/bin/env bash -e
# This script is intended to be executed by a user in a BASH shell.

# Check BASH environment

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

File=$DirProject/cfg/env.out

if [[ ! -r "$File" ]] ; then
    echo "FATAL: BASH environment file '$File' is unreadable, aborting"
    exit 1
fi

echo "INFO: Checking BASH environment against '$File'"
env-report.bash | diff - $File


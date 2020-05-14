#!/usr/bin/env bash -e
# This script is intended to be executed by a user in a BASH shell.

# Check all

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

py-check.bash
dep-check.bash
env-check.bash
tool-check.bash


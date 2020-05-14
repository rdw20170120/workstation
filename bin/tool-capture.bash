#!/usr/bin/env bash -ex
# This script is intended to be executed by a user in a BASH shell.

# Capture tool dependencies

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

File=$DirProject/cfg/tool.out

echo "INFO: Capturing tool dependencies to '$File'"
tool-report.bash > $File


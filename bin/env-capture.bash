#!/bin/bash
set -ex

# Capture BASH environment

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

File=$DirProject/cfg/env.out

echo "INFO: Capturing BASH environment to '$File'"
env-report.bash > $File


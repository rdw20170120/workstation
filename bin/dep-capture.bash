#!/bin/bash
# Capture Python dependencies

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

File=$DirProject/cfg/requirements.txt

echo "INFO: Capturing Python dependencies to '$File'"
dep-report.bash > $File


#!/bin/bash
# Check Python dependencies

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

File=$DirProject/cfg/requirements.txt

if [[ ! -r "$File" ]] ; then
    echo "FATAL: Python dependencies file '$File' is unreadable, aborting"
    exit 1
fi

echo "INFO: Checking Python dependencies against '$File'"
dep-report.bash | diff - $File


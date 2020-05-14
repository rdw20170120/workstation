#!/bin/bash
# Capture tool dependencies

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

File=$DirProject/cfg/tool.out

echo "INFO: Capturing tool dependencies to '$File'"
tool-report.bash > $File


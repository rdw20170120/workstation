#!/bin/bash
# Check tool dependencies

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

File=$DirProject/cfg/tool.out

if [[ ! -r "$File" ]] ; then
    echo "FATAL: Tool dependencies file '$File' is unreadable, aborting"
    exit 1
fi

echo "INFO: Checking tool dependencies against '$File'"
tool-report.bash | diff - $File


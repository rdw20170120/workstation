#!/bin/bash
# Create Python virtual environment directory

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

if [[ -z "$PVE" ]] ; then
    echo "FATAL: Environment variable 'PVE' is undefined, aborting"
    exit 1
fi

echo "INFO: Creating Python virtual environment directory '$PVE'"
python3 -m venv $PVE


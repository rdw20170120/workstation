#!/bin/bash
# Remove Python virtual environment directory

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

if [[ -z "$PVE" ]] ; then
    echo "FATAL: Environment variable 'PVE' is undefined, aborting"
    exit 1
fi

echo "INFO: Removing Python virtual environment directory '$PVE'"
rm -fr $PVE


#!/usr/bin/env bash -e
# This script is intended to be executed by a user in a BASH shell.

# Wipe project directory, which is a deeper clean

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

if [[ -z "$PVE" ]] ; then
    echo "FATAL: Environment variable 'PVE' is undefined, aborting"
    exit 1
fi

clean.bash

echo "INFO: Wiping (cleaning deeper)..."
rm -fr $DirProject/.pytest_cache 
rm -fr $DirProject/log 
pve-rm.bash

# TODO: Wipe other caches such as for 'pip'


#!/bin/bash
# Reinstall Python virtual environment directory

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

if [[ -z "$PVE" ]] ; then
    echo "FATAL: Environment variable 'PVE' is undefined, aborting"
    exit 1
fi

echo "INFO: Reinstalling Python virtual environment directory '$PVE'"
pve-rm.bash
pve-create.bash
dep-install.bash


#!/bin/bash
# Recreate Python virtual environment directory

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

if [[ -z "$PVE" ]] ; then
    echo "FATAL: Environment variable 'PVE' is undefined, aborting"
    exit 1
fi

echo "INFO: Recreating Python virtual environment directory '$PVE'"
wipe.bash
pve-create.bash

pip3 install pip wheel --upgrade --upgrade-strategy=eager
pip3 install logzero pytest


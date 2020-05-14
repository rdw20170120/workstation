#!/bin/bash
# Run application
set -ex

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

cd $DirProject/src
python3 -m TODO


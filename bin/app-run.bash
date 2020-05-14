#!/bin/bash
# Run application

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

cd $DirProject/src
python3 -m TODO


#!/bin/bash
# Run tests

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

clear
cd $DirProject/src
py.test --log-file=pytest.log --show-capture=no


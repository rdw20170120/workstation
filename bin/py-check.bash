#!/bin/bash
set -ex

# Check Python code

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

clear
python3 -m tabnanny -v $DirProject/src >$DirProject/cfg/tabnanny.out
cat $DirProject/cfg/tabnanny.out | grep -v 'listing directory' | grep -v 'Clean bill of health.'
echo 'INFO: No output means all Python code passes all checks'


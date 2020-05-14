#!/bin/bash
set -ex

# Install Python dependencies

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

File=$DirProject/cfg/requirements.txt

if [[ ! -r "$File" ]] ; then
    echo "FATAL: Python requirements file '$File' is unreadable, aborting"
    exit 1
fi

echo "INFO: Installing Python dependencies from '$File'"
pip3 install -r $File


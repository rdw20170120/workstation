#!/bin/bash
# Check all dependencies
set -ex

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

py-check.bash
dep-check.bash
env-check.bash
tool-check.bash


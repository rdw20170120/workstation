#!/bin/bash
# Capture all dependencies
set -ex

if [[ -z "$DirProject" ]] ; then
    echo "FATAL: Environment variable 'DirProject' is undefined, aborting"
    exit 1
fi

dep-capture.bash
env-capture.bash
tool-capture.bash


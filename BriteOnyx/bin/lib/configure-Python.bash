#!/bin/false
# NOTE: Intended to be sourced into a BASH shell by another script.

# Configure Python path
DirMine=$BO_Project/lib/mine
DirThird=$BO_Project/lib/third_party
export PYTHONPATH=$PYTHONPATH:$DirThird:$DirMine
echo "DEBUG: PYTHONPATH=$PYTHONPATH"

export PYTHONCOERCELOCALE=warn

# Set Python to use ASCII encoding, not UTF-8
# TODO: RESEARCH: Why does this set encoding for standard I/O channels,
# but not the default encoding?
export PYTHONIOENCODING=ASCII:warn
# export PYTHONUTF8=0

# Set Python to use UTF-8 encoding
export PYTHONIOENCODING=utf8:warn
export PYTHONUTF8=1


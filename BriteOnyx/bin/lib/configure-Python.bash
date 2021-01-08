#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell during activation.
# NO: trap ... EXIT
###############################################################################
# Configure Python

# Configure Python path
DirMine=${BO_Project}/src/lib/mine
DirThird=${BO_Project}/src/lib/third_party
export PYTHONPATH=${PYTHONPATH}:${DirThird}:${DirMine}
remembering PYTHONPATH

export PYTHONCOERCELOCALE=warn

# Set Python to use ASCII encoding, not UTF-8
# TODO: RESEARCH: Why does this set encoding
# for standard I/O channels,
# but not the default encoding?
export PYTHONIOENCODING=ASCII:warn
# export PYTHONUTF8=0

# Set Python to use UTF-8 encoding
export PYTHONIOENCODING=utf8:warn
export PYTHONUTF8=1

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -o verbose ; set -o xtrace
# Code to debug...
# set +o verbose ; set +o xtrace
: << 'DisabledContent'
DisabledContent


#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# Configure Python

# Configure Python path
DirMine=${BO_Project}/src/lib/mine
DirThird=${BO_Project}/src/lib/third_party
export PYTHONPATH=${PYTHONPATH}:"${DirThird}":"${DirMine}"
remembering PYTHONPATH

export PYTHONCOERCELOCALE=warn
remembering PYTHONCOERCELOCALE

# Set Python to use UTF-8 encoding
export PYTHONIOENCODING=utf8:warn
export PYTHONUTF8=1
remembering PYTHONIOENCODING
remembering PYTHONUTF8

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'

# Set Python to use ASCII encoding, not UTF-8
# TODO: RESEARCH: Why does this set encoding
# for standard I/O channels,
# but not the default encoding?
export PYTHONIOENCODING=ASCII:warn
export PYTHONUTF8=0
remembering PYTHONIOENCODING
remembering PYTHONUTF8
DisabledContent


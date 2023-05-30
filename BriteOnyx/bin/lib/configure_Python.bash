#!/usr/bin/env false
# Intended to be sourced in a Bash shell.
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

# Remember Python commands
export BO_cmd_python3=$(which python3)
remembering BO_cmd_python3
export BO_cmd_black="${BO_cmd_python3} -m black"
remembering BO_cmd_black
export BO_cmd_compileall="${BO_cmd_python3} -m compileall"
remembering BO_cmd_compileall
export BO_cmd_coverage="${BO_cmd_python3} -m coverage"
remembering BO_cmd_coverage
export BO_cmd_pip="${BO_cmd_python3} -m pip"
remembering BO_cmd_pip
export BO_cmd_pytest="${BO_cmd_python3} -m pytest"
remembering BO_cmd_pytest
export BO_cmd_tabnanny="${BO_cmd_python3} -m tabnanny"
remembering BO_cmd_tabnanny

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


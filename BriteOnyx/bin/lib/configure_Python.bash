#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
# me() { echo ${BASH_SOURCE} ; }
me() ( echo ${BASH_SOURCE} ; )
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Configure Python

# Configure Python path
DirMine=${BO_Project}/src/lib/mine
DirThird=${BO_Project}/src/lib/third_party
export PYTHONPATH=${PYTHONPATH}:"${DirThird}":"${DirMine}"
remembering PYTHONPATH

# Configure Python locale
export PYTHONCOERCELOCALE=warn
remembering PYTHONCOERCELOCALE
# export PYTHONUNBUFFERED=1
# remembering PYTHONUNBUFFERED

# Configure Python to use UTF-8 encoding
export PYTHONIOENCODING=utf8:warn
remembering PYTHONIOENCODING
export PYTHONUTF8=1
remembering PYTHONUTF8

# Remember secondary Python commands
export BO_cmd_black="${BO_cmd_python3} -m black"
remembering BO_cmd_black
export BO_cmd_compileall="${BO_cmd_python3} -m compileall"
remembering BO_cmd_compileall
export BO_cmd_coverage="${BO_cmd_python3} -m coverage"
remembering BO_cmd_coverage
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


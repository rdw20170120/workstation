#!/usr/bin/env false
[[ -n "${BO_Trace}" ]] && echo "TRACE: Executing${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell.

report_status_and_return() {
    local -ir Status=$?
    if [[ "${Status}" -eq 0 ]] ; then
        echo "INFO:  ${0} returning with status ${Status}"
    else
        echo "FATAL: ${0} returning with status ${Status}"
    fi
    return ${Status}
}
trap report_status_and_return EXIT
###############################################################################
# Configure Python

# Configure Python path
DirMine=$BO_Project/src/lib/mine
DirThird=$BO_Project/src/lib/third_party
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

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


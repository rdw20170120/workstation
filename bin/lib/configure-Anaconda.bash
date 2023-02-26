#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
[[ -z "${BO_Project}" ]] &&
    1>&2 echo "ERROR: Aborting, this project is NOT ACTIVATED" &&
    exit 99
require_directory_in BO_Project

# Configure BriteOnyx for Anaconda environment
export BO_DirAnaconda=${BO_Project}/.anaconda
remembering BO_DirAnaconda
export BO_FileAnacondaJson=${BO_Project}/cfg/anaconda.json
remembering BO_FileAnacondaJson
export BO_FileAnacondaYaml=${BO_Project}/cfg/anaconda.yml
remembering BO_FileAnacondaYaml

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
_Script="${BO_Project}/BriteOnyx/bin/lib/initialize-Anaconda.bash"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

_Script="${BO_Project}/BriteOnyx/bin/anaconda-create-maybe"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

DisabledContent


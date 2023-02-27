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

_Script="${BO_Project}/BriteOnyx/bin/lib/initialize_Anaconda.bash"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

export BO_PathAnaconda=${CONDA_PREFIX}/bin:${CONDA_PREFIX}/condabin
remembering BO_PathAnaconda
export BO_PathTool=${BO_PathAnaconda}
remembering BO_PathTool
export CONDA_PYTHON_EXE=${CONDA_PREFIX}/bin/python
remembering CONDA_PYTHON_EXE

Script="${BO_Project}/BriteOnyx/bin/lib/set_path.bash"
source "${Script}" ; Status=$?
[[ ${Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

# Configure BriteOnyx for Anaconda environment
export BO_cmd_conda=$(which conda)
remembering BO_cmd_conda
export BO_DirAnaconda=${BO_Project}/.anaconda
remembering BO_DirAnaconda
export BO_FileAnacondaJson=${BO_Project}/cfg/anaconda.json
remembering BO_FileAnacondaJson
export BO_FileAnacondaYaml=${BO_Project}/cfg/anaconda.yml
remembering BO_FileAnacondaYaml

_Script="${BO_Project}/BriteOnyx/bin/lib/maybe_create_Anaconda_environment.bash"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


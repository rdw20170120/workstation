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
[[ -z "${BO_Project}" ]] &&
    1>&2 log_error "Aborting, this project is NOT ACTIVATED" &&
    exit 99
require_directory_in BO_Project

export BO_DirAnaconda=${BO_Project}/.anaconda
remembering BO_DirAnaconda

if [[ -z "${CONDA_PREFIX}" ]] ; then
    log_warn "CONDA_PREFIX is missing, Anaconda does not appear to be installed, skipping configuration for Anaconda."
    return 0
fi

# Save PS1 since Anaconda is about to modify it
export BO_PS1=${PS1}

_Script="${BO_Project}/BriteOnyx/bin/lib/initialize_Anaconda.bash"
require_script "${_Script}"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

# Remember Anaconda commands
export BO_cmd_conda="$(which conda)"
remembering BO_cmd_conda
export BO_cmd_mamba="$(which mamba)"
remembering BO_cmd_mamba

require_directory_in BO_DirCapture
maybe_create_directory_tree ${BO_DirCapture}/current
export BO_FileAnacondaJson=${BO_DirCapture}/current/anaconda.json
remembering BO_FileAnacondaJson
export BO_FileAnacondaYaml=${BO_DirCapture}/current/anaconda.yml
remembering BO_FileAnacondaYaml

_Script="${BO_Project}/BriteOnyx/bin/lib/maybe_create_Anaconda_environment.bash"
require_script "${_Script}"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

# NOTE: Restore PS1 since I don't like Anaconda put the environment prefix there
export PS1=${BO_PS1}

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
export CONDA_PYTHON_EXE=${CONDA_PREFIX}/bin/python
remembering CONDA_PYTHON_EXE
DisabledContent


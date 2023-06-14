#!/usr/bin/env false
# Intended to be sourced in a Bash shell.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
[[ -z "${BO_Project}" ]] &&
    1>&2 echo "ERROR: Aborting, this project is NOT ACTIVATED" &&
    exit 99

require_directory_in BO_DirCapture
require_directory_in BO_Project
require_variable BO_DirAnaconda
require_variable BO_PathAnacondaBase

# Maybe create Anaconda environment
_ShouldCreate=true

[[ -d "${BO_DirAnaconda}" ]] && _ShouldCreate=false

if [[ "${_ShouldCreate}" == "true" ]] ; then
    execute_script anaconda-destroy
    execute_script anaconda-create
else
    log_info "Keeping Anaconda environment in directory '${BO_DirAnaconda}'"
fi

# Activate Anaconda virtual environment for this project
(set -o posix ; set) | sort >"${BO_DirCapture}/before/conda_activate.env"
log_info "Activating Anaconda environment in directory '${BO_DirAnaconda}'"
require_directory_in BO_DirAnaconda
export _CONDA_ROOT=${CONDA_PREFIX}
remembering _CONDA_ROOT
_Script=${_CONDA_ROOT}/bin/activate
log_debug "Sourcing script '${_Script}'"
require_script "${_Script}"
source "${_Script}" "${BO_DirAnaconda}"
Status=$?
[[ ${Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)
(set -o posix ; set) | sort >"${BO_DirCapture}/after/conda_activate.env"

# Configure PATH to include Anaconda virtual environment FIRST
export BO_PathAnacondaProject=${BO_DirAnaconda}/bin
remembering BO_PathAnacondaProject
export BO_PathAnaconda=${BO_PathAnacondaProject}:${BO_PathAnacondaBase}
remembering BO_PathAnaconda

_Script="${BO_Project}/BriteOnyx/bin/lib/set_path.bash"
require_script "${_Script}"
source "${_Script}" ; Status=$?
[[ ${Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

# Populate the newly-created Anaconda virtual environment
[[ "${_ShouldCreate}" == "true" ]] && execute_script anaconda-populate

# Remember primary Python commands
export BO_cmd_python3=$(which python3)
remembering BO_cmd_python3
export BO_cmd_pip="${BO_cmd_python3} -m pip"
remembering BO_cmd_pip

# Populate the newly-created Anaconda virtual environment
[[ "${_ShouldCreate}" == "true" ]] && execute_script python-populate

unset _ShouldCreate

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
require_variable BO_cmd_conda
${BO_cmd_conda} info
require_variable BO_cmd_mamba
${BO_cmd_mamba} info
DisabledContent


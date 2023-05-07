#!/usr/bin/env false
# Intended to be sourced in a Bash shell.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
[[ -z "${BO_Project}" ]] &&
    1>&2 echo "ERROR: Aborting, this project is NOT ACTIVATED" &&
    exit 99
require_directory_in BO_Project
require_variable BO_cmd_conda
require_variable BO_DirAnaconda
require_directory_in BO_DirCapture

# Create Anaconda environment
ShouldCreate=true

[[ -d "${BO_DirAnaconda}" ]] && ShouldCreate=false

if [[ "${ShouldCreate}" == "true" ]] ; then
    execute_script anaconda-destroy
    execute_script anaconda-create
else
    log_info "Keeping Anaconda environment in directory '${BO_DirAnaconda}'"
fi

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

export BO_PathAnaconda=${BO_DirAnaconda}/bin
remembering BO_PathAnaconda
export BO_PathTool=${BO_PathAnaconda}
remembering BO_PathTool

_Script="${BO_Project}/BriteOnyx/bin/lib/set_path.bash"
require_script "${_Script}"
source "${_Script}" ; Status=$?
[[ ${Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

[[ "${ShouldCreate}" == "true" ]] && execute_script anaconda-populate

unset ShouldCreate

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
${BO_cmd_conda} info
mamba info
DisabledContent


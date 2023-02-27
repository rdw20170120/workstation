#!/usr/bin/env bash
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
trap warn_on_error EXIT
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

require_directory_in BO_DirAnaconda
log_info "Activating Anaconda environment in directory '${BO_DirAnaconda}'"
(set -o posix ; set) | sort >"${BO_DirCapture}/before/conda_activate.env"
${BO_cmd_conda} activate "${BO_DirAnaconda}"
(set -o posix ; set) | sort >"${BO_DirCapture}/after/conda_activate.env"

export BO_PathAnaconda=${BO_DirAnaconda}/bin:${BO_PathAnaconda}
remembering BO_PathAnaconda
export BO_PathTool=${BO_PathAnaconda}
remembering BO_PathTool

Script="${BO_Project}/BriteOnyx/bin/lib/set_path.bash"
source "${Script}" ; Status=$?
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
    # NOTE: Is it necessary to initialize Anaconda (and Mamba) again after activation?
    Script="${BO_Project}/BriteOnyx/bin/lib/initialize-Anaconda.bash"
    source "${Script}" ; Status=$?
    [[ ${Status} -ne 0 ]] &&
        kill -INT $$  # Kill the executing script, but not the shell (terminal)

DisabledContent


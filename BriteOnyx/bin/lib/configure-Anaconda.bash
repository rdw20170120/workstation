#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
[[ -z "${BO_Project}" ]] &&
    1>&2 echo "ERROR: Aborting, this project is NOT ACTIVATED" &&
    exit 99

# Initilize Anaconda
require_directory_in CONDA_PREFIX
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('${CONDA_PREFIX}/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "${CONDA_PREFIX}/etc/profile.d/conda.sh" ]; then
        . "${CONDA_PREFIX}/etc/profile.d/conda.sh"
    else
        export PATH="${CONDA_PREFIX}/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "${CONDA_PREFIX}/etc/profile.d/mamba.sh" ]; then
    . "${CONDA_PREFIX}/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<

# Configure BriteOnyx for Anaconda environment
require_directory_in BO_Project
export BO_DirAnaconda=${BO_Project}/.anaconda
remembering BO_DirAnaconda
export BO_FileAnaconda=${BO_Project}/anaconda.yml
remembering BO_FileAnaconda

maybe_delete_directory_tree "${BO_DirAnaconda}"
log_info "Creating Anaconda environment in directory '${BO_DirAnaconda}'"
mamba create --prefix "${BO_DirAnaconda}"
require_directory "${BO_DirAnaconda}"
log_info "Activating Anaconda environment in directory '${BO_DirAnaconda}'"
mamba activate "${BO_DirAnaconda}"

_Script=${BO_Project}/BriteOnyx/bin/lib/set_path.bash
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

# Install desired packages into Anaconda environment
_Packages="python=3.11.*"
_Packages="${_Packages} black"
_Packages="${_Packages} coverage"
_Packages="${_Packages} pip"
_Packages="${_Packages} pytest"
# _Packages="${_Packages} tabnanny"
mamba install --yes ${_Packages}
mamba list --explicit >"${BO_FileAnaconda}"
require_file "${BO_FileAnaconda}"

log_info "Showing Anaconda environment variables"
env | grep -i CONDA

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
mamba install --file "${BO_FileAnaconda}"
DisabledContent


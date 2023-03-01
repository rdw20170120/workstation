#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
[[ -z "${BO_Project}" ]] &&
    1>&2 echo "ERROR: Aborting, this project is NOT ACTIVATED" &&
    exit 99
require_directory_in BO_DirCapture
require_directory_in CONDA_PREFIX

# Save PS1 since Anaconda is about to modify it
export BO_PS1=${PS1}

# Initialize Anaconda
(set -o posix ; set) | sort >"${BO_DirCapture}/before/conda_sh.env"
_Script=${CONDA_PREFIX}/etc/profile.d/conda.sh
log_debug "Sourcing script '${_Script}'"
require_script "${_Script}"
source "${_Script}" ; Status=$?
[[ ${Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)
(set -o posix ; set) | sort >"${BO_DirCapture}/after/conda_sh.env"

# Initialize Mamba too
(set -o posix ; set) | sort >"${BO_DirCapture}/before/mamba_sh.env"
_Script=${CONDA_PREFIX}/etc/profile.d/mamba.sh
log_debug "Sourcing script '${_Script}'"
require_script "${_Script}"
source "${_Script}" ; Status=$?
[[ ${Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)
(set -o posix ; set) | sort >"${BO_DirCapture}/after/mamba_sh.env"

# NOTE: Restore PS1 since I don't like having Anaconda put the environment prefix there
export PS1=${BO_PS1}

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


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
require_directory_in BO_DirCapture
require_directory_in CONDA_PREFIX

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

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


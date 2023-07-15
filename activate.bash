#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
me() { echo ${BASH_SOURCE} ; }
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Activate the BriteOnyx framework to manage this project directory tree
#
# NOTE: We MUST NOT EVER `exit` during BriteOnyx activation!
#
# We cannot use a `trap` here
# because it will remain active
# within the shell
# that will `source` this script.
#
# Please see HowTo-use_this_project.md for details.
###############################################################################
if [[ -n "${BO_Project}" ]] ; then
    1>&2 log_fatal "Aborting, this project is already activated as '${BO_Project}'"
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
fi

if [[ -z "${PWD}" ]] ; then
    1>&2 log_fatal "Aborting, missing environment variable 'PWD'"
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
fi

# Establish temporary directory for project
export BO_DirTemp=${PWD}/.BO/tmp
mkdir -p "${BO_DirTemp}"

# Establish capture directories for project
export BO_DirCapture="${BO_DirTemp}/capture"
mkdir -p "${BO_DirCapture}/after" "${BO_DirCapture}/before" "${BO_DirCapture}/current"
(set -o posix ; set) | sort > "${BO_DirCapture}/before/activation.env"

_Script=${PWD}/BriteOnyx/bin/lib/declare-log4bash.bash
# TODO: Require script
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

log_info "Activating '${PWD}' as the current project"

remembering() {
    # Log that we are remembering variable $1
    [[ $# -eq 0 ]] &&
        log_error "Variable name is required" &&
        kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
    local -r Name=$1
    log_debug "Remembering ${Name} = '${!Name}'"
} && export -f remembering

export BO_DirSnapshot=${PWD}/.BO/snapshot

remembering BO_DirCapture
remembering BO_DirSnapshot
remembering BO_DirTemp

export BO_Project=${PWD}
remembering BO_Project

_Script=${BO_Project}/BriteOnyx/bin/lib/declare.bash
# TODO: Require script
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

# NOTE: We can now use BriteOnyx Bash functionality.

# TODO: Remove
# export BO_PathProject=${BO_Project}/BriteOnyx/bin:${BO_Project}/bin

[[ -z "${BO_PathSystem}" ]] && export BO_PathSystem=${PATH}
[[ -z "${BO_PathUser}" ]] && export BO_PathUser=${HOME}/bin

_Script=${BO_Project}/BriteOnyx/bin/lib/set_path.bash
require_script "${_Script}"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

# Detect operating system
# TODO: Add detection of various Linux, when we care
export BO_OS=$(uname)
remembering BO_OS

# Establish logging directory for project
export BO_DirLog=${BO_Project}/.BO/log
maybe_create_directory_tree "${BO_DirLog}"
remembering BO_DirLog

maybe_copy_file "${BO_Project}/cfg/sample/alias.bash" "${BO_Project}/alias.bash"
maybe_copy_file "${BO_Project}/cfg/sample/context.bash" "${BO_Project}/context.bash"

# Configure Anaconda environment
(set -o posix ; set) | sort > "${BO_DirCapture}/before/Anaconda.env"
_Script=${BO_Project}/BriteOnyx/bin/lib/configure_Anaconda.bash
require_script "${_Script}"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
(set -o posix ; set) | sort > "${BO_DirCapture}/after/Anaconda.env"

# Configure Python
(set -o posix ; set) | sort > "${BO_DirCapture}/before/Python.env"
_Script=${BO_Project}/BriteOnyx/bin/lib/configure_Python.bash
require_script "${_Script}"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
(set -o posix ; set) | sort > "${BO_DirCapture}/after/Python.env"

_Script="${BO_Project}/bin/lib/declare.bash"
if [[ -r ${_Script} ]] ; then
    source ${_Script} ; _Status=$?
    [[ ${_Status} -ne 0 ]] &&
        kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
fi

_Script="${BO_Project}/context.bash"
require_script "${_Script}"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

_Script="${BO_Project}/BriteOnyx/bin/lib/alias.bash"
require_script "${_Script}"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

_Script="${BO_Project}/alias.bash"
require_script "${_Script}"
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

(set -o posix ; set) | sort > "${BO_DirCapture}/after/activation.env"

log_good "BriteOnyx has successfully activated this project"
log_info "To get started, try executing the 'cycle' alias..."

unset _Script
unset _Status

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
DisabledContent


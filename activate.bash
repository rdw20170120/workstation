#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
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
    1>&2 echo "Aborting, this project is already activated as '${BO_Project}'"
    kill -INT $$  # Kill the executing script, but not the shell (terminal)
fi

if [[ -z "${PWD}" ]] ; then
    1>&2 echo "Aborting, missing environment variable 'PWD'"
    kill -INT $$  # Kill the executing script, but not the shell (terminal)
fi

(set -o posix ; set) | sort > ${PWD}/BO-incoming.env

_Script=${PWD}/BriteOnyx/bin/lib/declare-log4bash.bash
source ${_Script} ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

log_info "Activating '${PWD}' as the current project"

remembering() {
    # Log that we are remembering variable $1
    [[ $# -eq 0 ]] &&
        log_error "Variable name is required" &&
        kill -INT $$  # Kill the executing script, but not the shell (terminal)
    local -r Name=$1
    log_debug "Remembering ${Name} = '${!Name}'"
} && export -f remembering

export BO_Project=${PWD}
remembering BO_Project
remembering INTERACTIVE_MODE

_Script=${BO_Project}/BriteOnyx/bin/lib/declare.bash
source ${_Script} ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

# NOTE: We can now use BriteOnyx Bash functionality.

# BriteOnyx scripts
# must precede
# project-specific scripts
# on the PATH
# so that collisions fail fast.
# Any collision should be resolved
# by renaming
# the project-specific script
# to avoid that collision.

export BO_PathProject=${BO_Project}/BriteOnyx/bin:${BO_Project}/bin

[[ -z "${BO_PathSystem}" ]] && export BO_PathSystem=${PATH}
[[ -z "${BO_PathUser}" ]] && export BO_PathUser=${HOME}/bin

remembering BO_PathProject
remembering BO_PathSystem
remembering BO_PathUser

_Script=${BO_Project}/BriteOnyx/bin/lib/set_path.bash
source ${_Script} ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

# Detect operating system
# TODO: Write as function
# TODO: Add detection of various Linux, when we care
_result=$(uname)
if [[ "${_result}" == Darwin ]] ; then
    export BO_OS=macOS
else
    export BO_OS=UNKNOWN
fi
remembering BO_OS

# Create random temporary directory
if [[ "${BO_OS}" == macOS ]] ; then
    _result=$(mktemp -d -t "BO-${USER}")
else
    _result=$(mktemp -d -t "BO-${USER}-XXXXXXX")
fi
if [[ -d "${_result}" ]] ; then
    TMPDIR=${_result}
    log_info "Created temporary directory '${TMPDIR}'"
fi
if [[ -d "${TMPDIR}" ]] ; then
    remembering TMPDIR
    export TMPDIR
else
    log_error "Aborting, failed to establish temporary directory '${TMPDIR}'"
    kill -INT $$  # Kill the executing script, but not the shell (terminal)
fi

maybe_create_directory_tree ${BO_Project}/log

# Activate Python virtual environment (PVE)
(set -o posix ; set) | sort > ${PWD}/BO-PVE-prior.env
_Script=${BO_Project}/BriteOnyx/bin/lib/pve-activate.bash
source ${_Script} ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)
(set -o posix ; set) | sort > ${PWD}/BO-PVE-after.env

maybe_copy_file ${BO_Project}/cfg/sample/alias.bash ${BO_Project}/alias.bash
maybe_copy_file ${BO_Project}/cfg/sample/context.bash ${BO_Project}/context.bash

_Script=${BO_Project}/bin/lib/declare.bash
if [[ -r ${_Script} ]] ; then
    source ${_Script} ; _Status=$?
    [[ ${_Status} -ne 0 ]] &&
        kill -INT $$  # Kill the executing script, but not the shell (terminal)
fi

_Script=${BO_Project}/context.bash
source ${_Script} ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

_Script=${BO_Project}/BriteOnyx/bin/lib/alias.bash
source ${_Script} ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

_Script=${BO_Project}/alias.bash
source ${_Script} ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

(set -o posix ; set) | sort > ${PWD}/BO-outgoing.env
log_good "BriteOnyx has successfully activated this project"
log_info "To get started, try executing the 'cycle' alias..."

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


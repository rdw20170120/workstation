#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a Bash shell during activation.
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

env | sort > ${PWD}/BO-incoming.env
source ${PWD}/BriteOnyx/bin/lib/declare-log4bash.bash
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

# Detect operating system
# TODO: Write as function
_result=$(uname)
# TODO: Add detection of various Linux, when we care
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

# NOTE: BriteOnyx scripts
# must precede project-specific scripts
# so that collisions fail fast.
# Any collision should be resolved
# by renaming the project-specific script
# to avoid that collision.
export BO_PathProject=${BO_Project}/BriteOnyx/bin:${BO_Project}/bin
remembering BO_PathProject

[[ -z "${BO_PathSystem}" ]] &&
    export BO_PathSystem=${PATH} &&
    remembering BO_PathSystem
[[ -z "${BO_PathUser}" ]] &&
    export BO_PathUser=${HOME}/bin &&
    remembering BO_PathUser

# Reset PATH before activating Python virtual environment
export PATH=${BO_PathSystem}
env | sort > ${PWD}/BO-PVE-prior.env
source ${BO_Project}/BriteOnyx/bin/lib/pve-activate.bash
env | sort > ${PWD}/BO-PVE-after.env
export BO_PathTool=${BO_PathPve}
remembering BO_PathTool

source ${BO_Project}/BriteOnyx/bin/lib/set_path.bash
source ${BO_Project}/BriteOnyx/bin/lib/configure-Python.bash
source ${BO_Project}/BriteOnyx/bin/lib/declare.bash
source ${BO_Project}/BriteOnyx/bin/lib/alias-common.bash
source ${BO_Project}/BriteOnyx/bin/lib/alias-git.bash

[[ ! -e ${BO_Project}/alias.bash ]] &&
    cp ${BO_Project}/cfg/sample/alias.bash ${BO_Project}/alias.bash
[[ ! -e ${BO_Project}/context.bash ]] &&
    cp ${BO_Project}/cfg/sample/context.bash ${BO_Project}/context.bash

[[ -r ${BO_Project}/bin/lib/declare.bash ]] &&
    source ${BO_Project}/bin/lib/declare.bash
[[ -r ${BO_Project}/alias.bash ]] &&
    source ${BO_Project}/alias.bash
[[ -r ${BO_Project}/context.bash ]] &&
    source ${BO_Project}/context.bash

env | sort > ${PWD}/BO-outgoing.env
log_good "BriteOnyx has successfully activated this project"
log_info "To get started, try executing the 'cycle' alias..."

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -o verbose ; set -o xtrace
# Code to debug...
# set +o verbose ; set +o xtrace
: << 'DisabledContent'
DisabledContent


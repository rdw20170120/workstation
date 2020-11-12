#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "DEBUG: Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell.

report_status_and_return() {
    local -ir Status=$?
    [[ "${Status}" -ne 0 ]] && 
        1>&2 echo "FATAL: ${0} returning with status ${Status}"
    return ${Status}
}
trap report_status_and_return EXIT
###############################################################################
# Activate the BriteOnyx framework to manage this project directory tree
#
# NOTE: We MUST NOT EVER `exit` during BriteOnyx activation!
#
# Please see HowTo-use_this_project.md for details.
###############################################################################

if [[ -n "${BO_Project}" ]] ; then
    1>&2 echo "FATAL: This project is already activated as '${BO_Project}', aborting"
    return 99  # Exit from the script, but not from the shell
fi

env | sort > ${PWD}/BO-incoming.env

1>&2 echo "INFO:  Activating this directory '${PWD}' as the current project"
export BO_Project=${PWD}

# Detect operating system
_result=$(uname)
if [[ "${_result}" == "Darwin" ]] ; then
    export BO_OS=macOS
else
    export BO_OS=Linux
fi
1>&2 echo "INFO:  Remembering BO_OS = '${BO_OS}'"

# Create random temporary directory
if [[ "${BO_OS}" == "macOS" ]] ; then
    _result=$(mktemp -d -t "BO-${USER}")
else
    _result=$(mktemp -d -t "BO-${USER}-XXXXXXX")
fi
if [[ -d "${_result}" ]] ; then
    TMPDIR=${_result}
    1>&2 echo "INFO:  Temporary directory '${TMPDIR}' created"
fi
if [[ -d "${TMPDIR}" ]] ; then
    1>&2 echo "INFO:  Remembering TMPDIR = '${TMPDIR}'"
    export TMPDIR
else
    1>&2 echo "FATAL: Failed to establish temporary directory '${TMPDIR}', aborting"
    return 1  # Exit from the script, but not from the shell
fi

# NOTE: BriteOnyx scripts
# must precede project-specific scripts
# so that collisions fail-fast.
# Any collision should be resolved
# by renaming the project- specific script
# to avoid that collision.
export BO_PathProject=${BO_Project}/BriteOnyx/bin:${BO_Project}/bin
1>&2 echo "INFO:  Remembering BO_PathProject = '${BO_PathProject}'"

[[ -z "${BO_PathSystem}" ]] && \
    export BO_PathSystem=${PATH} && \
    1>&2 echo "INFO:  Remembering BO_PathSystem = '${BO_PathSystem}'"

[[ -z "${BO_PathUser}" ]] && \
    export BO_PathUser=${HOME}/bin && \
    1>&2 echo "INFO:  Remembering BO_PathUser = '${BO_PathUser}'"
# Reset PATH before activating Python virtual environment
export PATH=${BO_PathSystem}
env | sort > ${PWD}/BO-PVE-prior.env
source ${BO_Project}/BriteOnyx/bin/lib/pve-activate.bash
env | sort > ${PWD}/BO-PVE-after.env

[[ -z "${BO_PathPve}" ]] && \
    export BO_PathPve=${PATH} && \
    1>&2 echo "INFO:  Remembering BO_PathPve = '${BO_PathPve}'"

source ${BO_Project}/BriteOnyx/bin/lib/set_path.bash
source ${BO_Project}/BriteOnyx/bin/lib/configure-Python.bash
source ${BO_Project}/BriteOnyx/bin/lib/declare.bash
source ${BO_Project}/BriteOnyx/bin/lib/alias-common.bash
source ${BO_Project}/BriteOnyx/bin/lib/alias-git.bash

[[ -r "${BO_Project}/bin/lib/declare.bash" ]] && 
    source ${BO_Project}/bin/lib/declare.bash
[[ -r "${BO_Project}/context.bash" ]] && 
    source ${BO_Project}/context.bash
[[ -r "${BO_Project}/alias.bash" ]] && 
    source ${BO_Project}/alias.bash

env | sort > ${PWD}/BO-outgoing.env

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


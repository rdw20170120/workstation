#!/usr/bin/env false
[[ -n "${BO_Trace}" ]] && echo "TRACE: Executing${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a BASH shell.

report_status_and_return() {
    local -ir Status=$?
    if [[ "${Status}" -eq 0 ]] ; then
        echo "INFO:  ${0} returning with status ${Status}"
    else
        echo "FATAL: ${0} returning with status ${Status}"
    fi
    return ${Status}
}
trap report_status_and_return EXIT
###############################################################################
# Activate the BriteOnyx framework to manage this project directory tree
#
# NOTE: We MUST NOT EVER `exit` during BriteOnyx activation!
#
# This script, and EVERY script that it calls, must NOT invoke `exit`!  The
# user calling this script must be allowed to preserve their shell and every
# effort must be made to inform the user of problems while continuing execution
# where possible.  Terminating the shell robs the user of useful feedback and
# interrupts their work, which is unacceptable.  Instead, the BASH `return`
# statement should be invoked to end execution with an appropriate status code.
#
# Likewise, we must be very careful invoking special BASH options during
# BriteOnyx activation, particularly the `set -e` option.  The user is
# inheriting the shell that we are configuring, which they will then use for
# the rest of their session, each and every time they develop, test, etc.  It
# would be very disruptive for the shell to abort on every error raised by
# every part of every command that they execute.  If you are unclear about
# this, then please experiment by uncommenting the `set -x` command above and
# activating a new shell.  Having learned that lesson, let's never use `set -x`
# in a BASH script intended to be `source`d.  Similarly, the `set -e` BASH
# option is problematic because its haphazard behavior does not deliver on its
# promised usefulness.
###############################################################################

if [[ -n "${BO_Project}" ]] ; then
    echo "FATAL: This project is already activated as '${BO_Project}', aborting"
    return 1  # Exit from the script, but not from the shell
fi

env | sort > ${PWD}/BO-incoming.env

echo "INFO:  Activating this directory '${PWD}' as the current project"
export BO_Project=${PWD}

# Detect operating system
_result=$(uname)
if [[ "${_result}" == "Darwin" ]] ; then
    export BO_OS=macOS
else
    export BO_OS=Linux
fi
echo "INFO:  Remembering BO_OS='${BO_OS}'"

# Create random temporary directory
if [[ "${BO_OS}" == "macOS" ]] ; then
    _result=$(mktemp -d -t "BO-${USER}")
else
    _result=$(mktemp -d -t "BO-${USER}-XXXXXXX")
fi
if [[ -d "${_result}" ]] ; then
    TMPDIR=${_result}
    echo "INFO:  Temporary directory '${TMPDIR}' created"
fi
if [[ -d "${TMPDIR}" ]] ; then
    echo "INFO:  Remembering TMPDIR='${TMPDIR}'"
    export TMPDIR
else
    echo "FATAL: Failed to establish temporary directory '${TMPDIR}', aborting"
    return 1  # Exit from the script, but not from the shell
fi

# NOTE: BriteOnyx scripts must precede project-specific scripts so that
# collisions fail-fast.  Any collision should result in renaming the project-
# specific script to avoid it.
export BO_PathProject=${BO_Project}/BriteOnyx/bin:${BO_Project}/bin
echo "INFO:  Remembering BO_PathProject=${BO_PathProject}"

[[ -z "${BO_PathSystem}" ]] && \
    export BO_PathSystem=${PATH} && \
    echo "INFO:  Remembering BO_PathSystem='${BO_PathSystem}'"

[[ -z "${BO_PathUser}" ]] && \
    export BO_PathUser=${HOME}/bin && \
    echo "INFO:  Remembering BO_PathUser='${BO_PathUser}'"

# Reset PATH before activating Python virtual environment
export PATH=${BO_PathSystem}

env | sort > ${PWD}/BO-PVE-prior.env

Script=${BO_Project}/BriteOnyx/bin/lib/pve-activate.bash
if [[ -r "${Script}" ]] ; then
    echo "INFO:  'source'ing script file '${Script}'"
    source ${Script}
else
    echo "WARN:  Script file '${Script}' is not readable, ignoring"
fi

env | sort > ${PWD}/BO-PVE-after.env

[[ -z "${BO_PathPve}" ]] && \
    export BO_PathPve=${PATH} && \
    echo "INFO:  Remembering BO_PathPve='${BO_PathPve}'"

Script=${BO_Project}/BriteOnyx/bin/lib/set_path.bash
if [[ -r "${Script}" ]] ; then
    echo "INFO:  'source'ing script file '${Script}'"
    source ${Script}
else
    echo "WARN:  Script file '${Script}' is not readable, ignoring"
fi

Script=${BO_Project}/BriteOnyx/bin/lib/alias-common.bash
if [[ -r "${Script}" ]] ; then
    echo "INFO:  'source'ing script file '${Script}'"
    source ${Script}
else
    echo "WARN:  Script file '${Script}' is not readable, ignoring"
fi

Script=${BO_Project}/BriteOnyx/bin/lib/alias-git.bash
if [[ -r "${Script}" ]] ; then
    echo "INFO:  'source'ing script file '${Script}'"
    source ${Script}
else
    echo "WARN:  Script file '${Script}' is not readable, ignoring"
fi

Script=${BO_Project}/alias.bash
if [[ -r "${Script}" ]] ; then
    echo "INFO:  'source'ing script file '${Script}'"
    source ${Script}
else
    echo "WARN:  Script file '${Script}' is not readable, ignoring"
fi

Script=${BO_Project}/context.bash
if [[ -r "${Script}" ]] ; then
    echo "INFO:  'source'ing script file '${Script}'"
    source ${Script}
else
    echo "WARN:  Script file '${Script}' is not readable, ignoring"
fi

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


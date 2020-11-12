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
# Set PATH for project
#
# NOTE: This specific ordering of PATH elements is REQUIRED.
# The Python virtual environment MUST come first
# in order to override the system Python.
# For now,
# that PATH element also includes the system PATH element,
# which is repeated here for when that is eventually fixed.
# The system PATH element MUST precede any user PATH elements
# in order to make collisions fail-fast
# and
# to defeat simple attempts at redirecting system commands
# as an attack vector.
# Similarly,
# the project PATH element MUST precede the user PATH element
# in order to make collisions fail-fast.
# This arrangement is best for ensuring consistent behavior
# of the Python virtual environment, the system, and the project.
# It puts at-risk only those user-specific commands, tools, and scripts
# relevant to the current deployed environment
# --where the specific user is best positioned to address them
# and failures are most likely limited to affecting only them (as they should).

export PATH=${BO_PathPve}:${BO_PathSystem}:${BO_PathProject}:${BO_PathUser}
1>&2 echo "INFO:  Remembering 'PATH' as '${PATH}'"

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


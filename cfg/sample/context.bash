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
# User/machine-specific context

# BASH configuration
# specific to this copy
# of this project
# for this user
# on this machine.
# This file is sourced
# by the 'activate.bash' script.
# You can manually source it
# into your current shell
# as a means to reset your execution context.
# See ${BO_Project}/src/app/${BO_NameApp}/config.py
# for a description of each environment variable used.

# NOTE:  This is a sample application context.
# It is intended
# to be copied to ${BO_Project}/context.bash
# and edited as needed.
# NOTE: Do NOT commit ${BO_Project}/context.bash to source control.

export BO_NameApp=MODULE

# TODO: Implement

# NOTE: Use the following settings
# to activate special task execution modes
# as documented in the
# src/lib/mine/task/config.py Python module.

# This block of settings
# are defaults for the safest task execution mode.

export FakeIt=defined
export Quick=1000000
export ReservedDiskSpaceInBytes=$((10 * 1024 * 1024 * 1024))
export Run=Dry

# This block of settings
# can be selectively uncommented
# to relax the previous safeties.
# NOTE: It is best to leave these commented-out here,
# then manually execute these commands individually
# to alter only the current shell
# while you are testing.

# export Run=Force
# unset FakeIt
# unset Quick
# unset Run

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# set -o verbose
# set -o xtrace
# Code to debug...
# set +o verbose
# set +o xtrace
: << 'DisabledContent'
DisabledContent


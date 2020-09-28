#!/usr/bin/env false
# NO: set -e
# DISABLED: set -x
# Intended to be sourced in a BASH shell by the user.
###############################################################################
# User/machine-specific context
# BASH configuration specific to this copy of this project on this workstation
# for this user.
# This file is sourced by the 'activate.bash' script.  You can manually source
# it into your current shell as a means to reset your execution context.
# See $BO_Project/src/app/MODULE/config.py for a description of each.

# NOTE:  This is a sample application context.
# It is intended to be copied to $BO_Project/context.bash and edited as needed.
# NOTE: Do NOT commit $BO_Project/context.bash to source control.

# TODO: Implement

# NOTE: Use these settings to activate special execution modes.
# This block of settings are defaults for the safest execution mode.
# 'Quick' can be edited to a different value, which is the maximum file size in
# bytes that will be processed.

export FakeIt=defined
export Quick=1000000
export ReservedDiskSpaceInBytes=$((10 * 1024 * 1024 * 1024))
export Run=Dry

# This block of settings can be selectively uncommented to relax the previous
# safeties.  NOTE: It is best to leave these commented-out here, then manually
# execute these commands individually to alter only the current shell while
# you are testing.

# export Run=Force
# unset FakeIt
# unset Quick
# unset Run

###############################################################################
: << 'DisabledContent'
DisabledContent

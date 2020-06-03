#!/bin/false
# NOTE: Intended to be sourced into a BASH shell

# This file is sourced by the 'activate.bash' script.  You can manually source
# it into your current shell as a means to reset your execution context.

# User/machine-specific context

# TODO: Implement

# NOTE: Use these settings to activate special execution modes.
# This block of settings are defaults for the safest execution mode.
# 'Quick' can be edited to a different value, which is the maximum file size in
# bytes that will be processed.
export FakeIt=defined
export Quick=1000000
export Run=Dry

# This block of settings can be selectively uncommented to relax the previous
# safeties.  NOTE: It is best to leave these commented-out here, then manually
# execute these commands individually to alter only the current shell while
# you are testing.

# export Run=Force
# unset FakeIt
# unset Quick
# unset Run

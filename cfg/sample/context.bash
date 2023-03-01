#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# User/machine-specific Bash environment context

unset BO_RunningHumanless

# Bash environment
# specific to this copy
# of this project
# for this user
# on this machine.
# This file is sourced
# by `activate.bash`.
# You can manually source it
# into your current shell
# as a means to update
# with your latest edits.

# This is a sample.
# It is intended
# to be copied to
# `${BO_Project}/context.bash`.
# The `activate.bash` script
# does this if it is missing
# (e.g.,
# when first executed after
# `git clone`
# )
# so that BriteOnyx activation
# is satisfied.

# NOTE: `${BO_Project}/context.bash`
# is excluded by `.gitignore`;
# do NOT commit
# `${BO_Project}/context.bash`
# to source control.

# See the various `config.py`
# within the Python source
# for a description
# of each environment variable
# used.

export BO_NameApp=MODULE
remembering BO_NameApp

require_directory_in HOME

# Remember how to execute various tools
export BO_cmd_python3=$(which python3)
remembering BO_cmd_python3
export BO_cmd_black="${BO_cmd_python3} -m black"
remembering BO_cmd_black
export BO_cmd_compileall="${BO_cmd_python3} -m compileall"
remembering BO_cmd_compileall
export BO_cmd_coverage="${BO_cmd_python3} -m coverage"
remembering BO_cmd_coverage
export BO_cmd_meld=$(which meld)
remembering BO_cmd_meld
export BO_cmd_pip="${BO_cmd_python3} -m pip"
remembering BO_cmd_pip
export BO_cmd_pytest="${BO_cmd_python3} -m pytest"
remembering BO_cmd_pytest
export BO_cmd_tabnanny="${BO_cmd_python3} -m tabnanny"
remembering BO_cmd_tabnanny

###############################################################################
# NOTE: Use the following settings
# activate special task execution modes
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
# NOTE:  It can be extremely useful
# to test BriteOnyx activation
# by invoking it in a subshell like so:
# `cd PROJECT_ROOT_DIRECTORY`
# `bash -c 'source activate.bash'`
#
# During such testing,
# it can be useful
# to also uncomment the follow lines
# to execute a 'cycle' (see the alias).

# test-run
# abort_on_fail $? "from test-run"
# gen-run -vvv
# abort_on_fail $? "from gen-run -vvv"
# app-run -vvv
# abort_on_fail $? "from app-run -vvv"

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


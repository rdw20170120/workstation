#!/usr/bin/env false
# Intended to be executed in a Bash shell via `source`.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
[[ -n "${BO_Trace}" ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
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

export BO_NameApp=my_app
remembering BO_NameApp

require_directory_in HOME

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
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
DisabledContent


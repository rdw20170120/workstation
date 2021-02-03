#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# Jenkins-specific Bash environment context

export BO_RunningHumanless=defined

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

# This file
# should be copied into place
# by `Jenkins/run_for_Jenkins`
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

export BO_NameApp=NAME

require_directory_in_variable HOME

# Establish Python and dependencies

export BO_DirHomePython=${PYTHON_HOME}
export BO_PathPython=${BO_DirHomePython}/bin:${HOME}/.local/bin
export BO_PathTool=${BO_PathPython}:${BO_PathTool}

_Script=${BO_Project}/BriteOnyx/bin/lib/set_path.bash
source ${_Script} ; abort_on_fail $? "from ${_Script}"

execute_script dep-install

_Script=${BO_Project}/BriteOnyx/bin/lib/configure-Python.bash
source ${_Script} ; abort_on_fail $? "from ${_Script}"

# Establish Java

export BO_DirHomeJava=${JAVA_HOME}
export BO_PathJava=${BO_DirHomeJava}/bin
export BO_PathTool=${BO_PathJava}:${BO_PathTool}

export BO_PathTool=${BO_PathPython}:${BO_PathJava}

_Script=${BO_Project}/BriteOnyx/bin/lib/set_path.bash
source ${_Script} ; abort_on_fail $? "from ${_Script}"

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


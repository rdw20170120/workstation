#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# User/machine-specific Bash environment context

unset BO_RunningHumanless

_Script=${BO_Project}/BriteOnyx/bin/lib/configure-Anaconda.bash
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

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
export python3=$(which python3)
remembering python3
export black="${python3} -m black"
remembering black
# export compileall=$(which compileall)
export compileall="${python3} -m compileall"
remembering compileall
# export coverage=$(which coverage)
export coverage="${python3} -m coverage"
remembering coverage
# export pip=$(which pip)
export pip="${python3} -m pip"
remembering pip
# export pytest=$(which pytest)
export pytest="${python3} -m pytest"
remembering pytest
# export tabnanny=$(which tabnanny)
export tabnanny="${python3} -m tabnanny"
remembering tabnanny
# TODO: Stop using venv in favor of Anaconda environments
# export venv=$(which venv)
# remembering venv

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'

export BO_DirHomeConfluent=/opt/Confluent/confluent-5.5.1
require_directory_in BO_DirHomeConfluent
export BO_PathConfluent=${BO_DirHomeConfluent}/bin

export BO_DirHomeJava=/opt/OpenJDK/jdk-15.jdk/Contents/Home
require_directory_in BO_DirHomeJava
export BO_PathJava=${BO_DirHomeJava}/bin
export JAVA_HOME=${BO_DirHomeJava}

export BO_DirHomeTestSSL=${HOME}/tool/testssl.sh-3.0
require_directory_in BO_DirHomeTestSSL
export BO_PathTestSSL=${BO_DirHomeTestSSL}

# Java should preceed Confluent
# in the PATH
# (since the latter depends upon the former).
# At this point in the activation
# BO_PathTool already contains BO_PathPve.
# TODO: Remove ${BO_PathSystem} from ${BO_PathPve}
# Then move ${BO_PathPve} before ${BO_PathConfluent}
# Then move ${BO_PathPve} before ${BO_PathJava}
export BO_PathTool=${BO_PathJava}:${BO_PathConfluent}:${BO_PathTestSSL}:${BO_PathTool}

source "${BO_Project}/BriteOnyx/bin/lib/set_path.bash"

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

DisabledContent


#!/usr/bin/env false
[[ -n "${BO_Debug}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}"
# NO: set -e
# Intended to be sourced in a Bash shell during activation.
# NO: trap ... EXIT
###############################################################################
# User/machine-specific context

# Bash configuration
# specific to this copy
# of this project
# for this user
# on this machine.
# This file is sourced
# by the 'activate.bash' script.
# You can manually source it
# into your current shell
# as a means to update
# with your latest edits.

# This is a sample
# Bash environment context.
# It is intended
# to be copied to
#  ${BO_Project}/context.bash
# and edited as needed.
# The ${BO_Project}/activate.bash script
# does this if it is absent
# (initial clone).
# NOTE: ${BO_Project}/context.bash
# is excluded by .gitignore;
# do NOT commit
# ${BO_Project}/context.bash
# to source control.

# See ${BO_Project}/src/app/${BO_NameApp}/config.py
# for a description of each environment variable used.

export BO_NameApp=MODULE

# TODO: Implement

require_directory_in_variable HOME

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
# export PS4='$ ' ; set -o verbose ; set -o xtrace
# Code to debug...
# set +o verbose ; set +o xtrace
: << 'DisabledContent'

export BO_DirHomeConfluent=/opt/Confluent/confluent-5.5.1
require_directory_in_variable BO_DirHomeConfluent
export BO_PathConfluent=${BO_DirHomeConfluent}/bin

export BO_DirHomeJava=/opt/OpenJDK/jdk-15.jdk/Contents/Home
require_directory_in_variable BO_DirHomeJava
export BO_PathJava=${BO_DirHomeJava}/bin
export JAVA_HOME=${BO_DirHomeJava}

export BO_DirHomeTestSSL=${HOME}/tool/testssl.sh-3.0
require_directory_in_variable BO_DirHomeTestSSL
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

source ${BO_Project}/BriteOnyx/bin/lib/set_path.bash

DisabledContent


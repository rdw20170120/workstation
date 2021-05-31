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

# This is a sample.
# It is intended
# to be copied to
# `${BO_Project}/context.bash`.
# The `Jenkins/run` script
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

require_variable BO_PathNative
export BO_PathSystem=${BO_PathNative}
source "${BO_Project}/BriteOnyx/bin/lib/set_path.bash"

# Remember how to execute various tools
export black=$(which black)
export compileall=$(which compileall)
export coverage=$(which coverage)
export pip=$(which pip)
export pytest=$(which pytest)
export tabnanny=$(which tabnanny)
export venv=$(which venv)

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
# Since this script is
# executing under `Jenkins/run`,
# it will be affected by
# `nix-shell`
# to have `BO_PathSystem`
# set for our packages
# installed by `shell.nix`.
# Therefore, we must
# capture that path
# into this new environment.
export BO_PathNix=${BO_PathSystem}
export BO_PathTool=${BO_PathNix}
DisabledContent


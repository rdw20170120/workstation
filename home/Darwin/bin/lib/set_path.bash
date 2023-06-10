#!/usr/bin/env false
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Configure paths, especially PATH

################################################################################
# Remember variants of the system PATH
[[ -z "${BO_PathNative}" ]] && export BO_PathNative=${PATH}
[[ -z "${BO_PathOriginal}" ]] && export BO_PathOriginal=${PATH}

################################################################################
# NOTE: Order matters!
# Anaconda should override all
# (win all collisions)
# as the preferred package manager
# for projects being developed and/or deployed.
# Then the system package manager comes second,
# which is
# APT for Ubuntu (handled under the native system path)
# and Homebrew (currently) for Apple macOS.
# Other non-native tools follow
# such as VMware Fusion (if installed).
# The original system path is next.
# The user path is last
# (so the user MUST resolve collisions).
# This allows easier manipulation
# by (un)commenting entries.
BO_PathSystem=${BO_PathAnacondaBase}
BO_PathSystem+=:${BO_PathHomebrew}
BO_PathSystem+=:${BO_PathOriginal}
export BO_PathSystem

export BO_PathTool=${BO_PathKrew}
export BO_PathUser=${HOME}/bin

PATH=${BO_PathSystem}
PATH+=:${BO_PathTool}
PATH+=:${BO_PathUser}
export PATH

: << 'DisabledContent'
DisabledContent


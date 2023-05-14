#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Configure paths

################################################################################
# Remember the native and original system PATHs
[[ -z "${BO_PathOriginal}" ]] && export BO_PathOriginal=${PATH}
export BO_PathNative=${BO_PathOriginal}

################################################################################
# NOTE: Order matters!
# Anaconda should override all
# (win all collisions)
# as the preferred package manager
# for projects being developed and/or deployed.
# However, Anaconda is managed
# using project-specific environments
# that are incorporated into the PATH
# as part of the BriteOnyx activation
# for each project.
# Therefore, Anaconda is absent here.
# Then the system package manager comes second,
# which is
# APT for Ubuntu (handled under the native system path)
# and Homebrew (currently) for Apple macOS.
# Other non-native tools follow
# such as VMware Fusion (if installed).
# The native system path is next.
# The user path is last
# (so user MUST resolve collisions).
# Build up the system path from the end,
# starting with the native path,
# then moving forward.
# This allows easier manipulation by (un)commenting entries.
BO_PathSystem=${BO_PathNative}
export BO_PathSystem
export BO_PathUser=${HOME}/bin
export PATH=${BO_PathSystem}:${BO_PathUser}

: << 'DisabledContent'
DisabledContent


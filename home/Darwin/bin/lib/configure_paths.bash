#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Configure paths

################################################################################
# Remember the native and original system PATHs
[[ -z "${BO_PathOriginal}" ]] && export BO_PathOriginal=${PATH}
export BO_PathNative=${BO_PathOriginal}

################################################################################
# Homebrew
# NOTE: On Apple macOS running on Apple Silicon (ARM64)
# export HOMEBREW_PREFIX=/opt/homebrew
# NOTE: On Apple macOS running on Intel CPU
# export HOMEBREW_PREFIX=/usr/local
# eval "$(${HOMEBREW_PREFIX}/bin/brew shellenv)"
# export BO_PathAfterHomebrew=${PATH}
# export BO_PathHomebrew=${HOMEBREW_PREFIX}/bin:${HOMEBREW_PREFIX}/sbin

################################################################################
# Kubernetes CLI
# export BO_PathKrew=${HOME}/.krew/bin

################################################################################
# Node Version Manager (NVM)
# export NVM_DIR="${HOME}/.nvm"
# TODO: Incorporate these scripts into the relevant project(s) when needed
# [ -s "${HOMEBREW_PREFIX}/opt/nvm/nvm.sh" ] && \
#     source "${HOMEBREW_PREFIX}/opt/nvm/nvm.sh"
# [ -s "${HOMEBREW_PREFIX}/opt/nvm/etc/bash_completion.d/nvm" ] && \
#     source "${HOMEBREW_PREFIX}/opt/nvm/etc/bash_completion.d/nvm"

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
# BO_PathSystem=${BO_PathHomebrew}:${BO_PathSystem}
# BO_PathSystem=${BO_PathKrew}:${BO_PathSystem}
export BO_PathSystem
export BO_PathUser=${HOME}/bin
export PATH=${BO_PathSystem}:${BO_PathUser}

################################################################################
# Anaconda (Mambaforge)
# export CONDA_PREFIX=${HOMEBREW_PREFIX}/Caskroom/mambaforge/base
# export BO_PathAnacondaBase=${CONDA_PREFIX}/bin:${CONDA_PREFIX}/condabin

: << 'DisabledContent'
DisabledContent


#!/usr/bin/env false
################################################################################
# Configure Anaconda (Mambaforge)

export CONDA_PREFIX=${HOME}/mambaforge
export BO_PathAnacondaBase=${CONDA_PREFIX}/bin:${CONDA_PREFIX}/condabin

: << 'DisabledContent'
# export CONDA_PREFIX=${HOMEBREW_PREFIX}/Caskroom/mambaforge/base
DisabledContent


#!/usr/bin/env false
################################################################################
# Configure Anaconda (Mambaforge)

# NOTE: This presumes installing Anaconda directly,
# NOT thru Homebrew
export CONDA_PREFIX=${HOME}/mambaforge
export BO_PathAnacondaBase=${CONDA_PREFIX}/bin:${CONDA_PREFIX}/condabin
export BO_PathAnaconda=${BO_PathAnacondaBase}

: << 'DisabledContent'
DisabledContent


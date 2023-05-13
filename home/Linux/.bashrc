#!/bin/false
# NOTE:  This file is intended to be executed as part of starting a Bash shell.
################################################################################
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

umask u=rwx,g=,o=

################################################################################
# If not running interactively, don't do anything
case $- in
  *i*) ;;
  *) return;;
esac

################################################################################
# Configure terminal first, since other scripts depend upon it
_Script=${HOME}/bin/lib/configure_terminal.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

################################################################################
# Configure other things, alphabetically

_Script=${HOME}/bin/lib/configure_bash.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

_Script=${HOME}/bin/lib/configure_chroot.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

_Script=${HOME}/bin/lib/configure_dircolors.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

_Script=${HOME}/bin/lib/configure_less.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

_Script=${HOME}/bin/lib/configure_vim.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

################################################################################
# Anaconda (Mambaforge)
export CONDA_PREFIX=${HOME}/mambaforge
export BO_PathAnacondaBase=${CONDA_PREFIX}/bin:${CONDA_PREFIX}/condabin

################################################################################
# Configure paths last, since it depends upon most other scripts
_Script=${HOME}/bin/lib/configure_paths.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

################################################################################
# Finally, define aliases to help the user
_Script=${HOME}/alias.bash
if [[ -r "${_Script}" ]] ; then
    echo "INFO: Sourcing script '${_Script}'"
    source "${_Script}"
else
    echo "WARN: Skipping missing script '${_Script}'"
fi

unset _Script

: << 'DisabledContent'
DisabledContent


#!/bin/false
# NOTE:  This file is intended to be executed as part of starting a Bash shell.
# TODO: REFACTOR: Based on operating system support, relevant command, etc.
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
################################################################################
# Homebrew
export HOMEBREW_PREFIX=/opt/homebrew
eval "$(${HOMEBREW_PREFIX}/bin/brew shellenv)"
export BO_PathAfterHomebrew=${PATH}
export BO_PathHomebrew=${HOMEBREW_PREFIX}/bin:${HOMEBREW_PREFIX}/sbin

################################################################################
# Anaconda (Mambaforge)
export CONDA_PREFIX=${HOMEBREW_PREFIX}/Caskroom/mambaforge/base
export BO_PathAnacondaBase=${CONDA_PREFIX}/bin:${CONDA_PREFIX}/condabin

DisabledContent


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

prepare_to_source() {
    # Prepare to `source` script $1,
    # returning 0 if the script is found and
    # returning 1 if the script is not found
    # Should be invoked like this:
    # prepare_to_source "${_Script}" && source "${_Script}"
    if [[ -r "${_Script}" ]] ; then
        echo "INFO: Sourcing script '${_Script}'"
        return 0
    else
        echo "WARN: Skipping missing script '${_Script}'"
    fi
    return 1
} && export -f prepare_to_source

################################################################################
# Configure terminal first, since other scripts depend upon it
_Script=${HOME}/bin/lib/configure_terminal.bash
prepare_to_source "${_Script}" && source "${_Script}"

################################################################################
# Configure other things, alphabetically

_Script=${HOME}/bin/lib/configure_bash.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure_chroot.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure_dircolors.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure_less.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/configure_vim.bash
prepare_to_source "${_Script}" && source "${_Script}"

################################################################################
# Configure paths last, since it depends upon most other scripts
_Script=${HOME}/bin/lib/configure_paths.bash
prepare_to_source "${_Script}" && source "${_Script}"

################################################################################
# Define aliases to help the user
_Script=${HOME}/alias.bash
prepare_to_source "${_Script}" && source "${_Script}"

unset _Script

: << 'DisabledContent'
DisabledContent


#!/bin/false
# NOTE:  This script is executed via `source` while initializing a Bash shell.
################################################################################
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

umask u=rwx,g=,o=

################################################################################
# If not running interactively, don't do anything
case $- in
  *i*) ;;
  *) 
      echo "WARN: Noninteractive shell, skipping Bash initialization"
      return;;
esac

export BO_ARCH=$(uname -m)
export BO_OS=$(uname)

export BO_PathNative=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/sbin

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

_Script=${HOME}/bin/lib/setup_terminal.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/all_configure.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/set_path.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/all_activate.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/set_path.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/SamsClub.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/all_alias.bash
prepare_to_source "${_Script}" && source "${_Script}"

unset _Script

: << 'DisabledContent'
# Create ~/bin/lib subdirectories
# that can then be iterated using a simple loop
# Configure scripts will set whatever variables, etc.
# that can be before updating PATH
# while
# Activate scripts will rely upon PATH being complete
# Most commands will not need either kind of script
# built-in commands will not need an activate script
# while externally-added tools will likely need both kinds of script
DisabledContent


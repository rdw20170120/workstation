#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
me() { echo ${BASH_SOURCE} ; }
# NOTE: Must still use raw Bash syntax until we have declared essential functions
# NOTE: Special header since this script is called while initializing Bash
1>&2 echo "TRACE: Executing '$(me)'"
# NO: Do NOT `trap` since it will stay active in the shell
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
        1>&2 echo "WARN: Noninteractive shell, skipping Bash initialization"
        return;;
esac

export BO_ARCH=$(uname -m)
export BO_OS=$(uname)

# TODO: export BO_PathNative=

prepare_to_source() {
    # Prepare to `source` script $1,
    # returning 0 if the script is found and
    # returning 1 if the script is not found
    # Should be invoked like this:
    # prepare_to_source "${_Script}" && source "${_Script}"
    if [[ -r "${_Script}" ]] ; then
        log_info "Sourcing script '${_Script}'"
        return 0
    else
        log_warn "Skipping missing script '${_Script}'"
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


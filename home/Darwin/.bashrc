#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT export this function, it only works if defined locally
# NOTE: Each new definition of this function REPLACES the previous via `source`
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

################################################################################
export BO_ARCH=$(uname -m)
export BO_OS=$(uname)

_Script=${HOME}/bin/lib/declare/essential.bash
# NOTE: Must still use raw Bash syntax until we have declared essential functions
if [[ -r "${_Script}" ]]; then
    1>&2 echo "INFO:  Sourcing '${_Script}'"
    source "${_Script}"
else
    1>&2 echo "WARN:  Missing '${_Script}'"
fi
# Now we can use our essential Bash functions to help

_Script=${HOME}/bin/lib/setup_terminal.bash
prepare_to_source "${_Script}" && source "${_Script}"

unset _Script

################################################################################
export BO_PathNative=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

log_good "To activate BriteOnyx, execute 'source ~/source_me.bash'"

################################################################################
: << 'DisabledContent'
DisabledContent


#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
me() { echo ${BASH_SOURCE} ; }
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Configure bash

# export FIGNORE=
# export GLOBIGNORE=
# export HISTTIMEFORMAT=
# export TIMEFORMAT=
# shopt -s globstar (unsupported in BASH 3.2.57)
export HISTCONTROL=ignoreboth
export HISTFILESIZE=500
export HISTSIZE=500
shopt -s checkwinsize cmdhist histappend huponexit lithist
shopt -u sourcepath

################################################################################
# Needed? (These are handled by Apple macOS)
# export LANG
# export LC_ALL
# export TZ

################################################################################
# Enable programmable completion features
# You don't need to enable this
# if it's already enabled in /etc/bash.bashrc
# and /etc/profile sources /etc/bash.bashrc.
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    source /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    source /etc/bash_completion
  fi
fi

: << 'DisabledContent'
DisabledContent


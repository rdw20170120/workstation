#!/bin/false
# NOTE:  This file is intended to be executed as part of starting a Bash shell.
################################################################################
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

umask u=rwx,g=,o=

################################################################################
# If not running interactively,
# don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

################################################################################
# Customize terminal
export COLORTERM=truecolor
export TERM=xterm-256color

################################################################################
# Set a fancy prompt
# (non-color, unless we know we "want" color)
# case "$TERM" in
#     xterm-color|*-256color) color_prompt=yes;;
# esac

# Uncomment for a colored prompt,
# if the terminal has the capability;
# turned off by default
# to not distract the user:
# the focus in a terminal window
# should be on the output of commands,
# not on the prompt
# force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	    # We have color support;
	    # assume it's compliant with Ecma-48 (ISO/IEC-6429).
	    # Lack of such support is extremely rare,
	    # and such a case
	    # would tend to support setf rather than setaf.
	    color_prompt=yes
    else
	    color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm
# set the title to user@host:dir
case "$TERM" in
    xterm*|rxvt*)
        # PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
        PS1="\[\e]0;\w\a\]$PS1"
        ;;
    *)
        ;;
esac

if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
fi

# Colored GCC warnings and errors
# export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

################################################################################
# Make less more friendly
# for non-text input files,
# see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

################################################################################
# Set variable identifying the chroot you work in
# (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

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

################################################################################
# Environment
export CLICOLOR=true
export GREP_OPTIONS='--color=auto'
export PAGER=less
# Needed?
# LANG
# LC_ALL
# TZ

################################################################################
# Configure for Neovim
export EDITOR="nvim"
export VISUAL="nvim"
 
################################################################################
# Bash
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
# Alias definitions
# You may want to put all your additions
# into a separate file like ~/.bash_aliases,
# instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.
[[ -r ~/alias.bash ]] && source ~/alias.bash

################################################################################
# Remember the native and original system PATHs
[[ -z "${BO_PathOriginal}" ]] && export BO_PathOriginal=${PATH}
export BO_PathNative=${BO_PathOriginal}

################################################################################
# Anaconda (Mambaforge)
export CONDA_PREFIX=${HOME}/mambaforge
export BO_PathAnacondaBase=${CONDA_PREFIX}/bin:${CONDA_PREFIX}/condabin

##############################################################################
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
BO_PathSystem=${BO_PathAnacondaBase}:${BO_PathSystem}
export BO_PathSystem
export BO_PathUser=${HOME}/bin
export PATH=${BO_PathSystem}:${BO_PathUser}

: << 'DisabledContent'
export BO_PathAnacondaBefore=${PATH}
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/ubuntu/mambaforge/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/ubuntu/mambaforge/etc/profile.d/conda.sh" ]; then
        . "/home/ubuntu/mambaforge/etc/profile.d/conda.sh"
    else
        export PATH="/home/ubuntu/mambaforge/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "/home/ubuntu/mambaforge/etc/profile.d/mamba.sh" ]; then
    . "/home/ubuntu/mambaforge/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<
export BO_PathAnacondaAfter=${PATH}
DisabledContent

#!/bin/false
# NOTE:  This file is intended to be executed as part of starting a Bash shell.

# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

[[ -z "${BO_PathOriginal}" ]] && export BO_PathOriginal=${PATH}

################################################################################
# Anaconda
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/x299424/mambaforge/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/x299424/mambaforge/etc/profile.d/conda.sh" ]; then
        . "/Users/x299424/mambaforge/etc/profile.d/conda.sh"
    else
        export PATH="/Users/x299424/mambaforge/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "/Users/x299424/mambaforge/etc/profile.d/mamba.sh" ]; then
    . "/Users/x299424/mambaforge/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<
export BO_PathAnaconda=${CONDA_PREFIX}/bin

################################################################################
# Homebrew
# eval "$(/opt/homebrew/bin/brew shellenv)"
export HOMEBREW_PREFIX=/opt/homebrew
export HOMEBREW_CELLAR=${HOMEBREW_PREFIX}/Cellar
export HOMEBREW_REPOSITORY=${HOMEBREW_PREFIX}
# export MANPATH=${HOMEBREW_PREFIX}/share/man${MANPATH+:$MANPATH}:
# export INFOPATH=${HOMEBREW_PREFIX}/share/info:${INFOPATH:-}
export BO_PathHomebrew=${HOMEBREW_PREFIX}/bin:${HOMEBREW_PREFIX}/sbin

export BO_PathMacPorts=/opt/local/bin:/opt/local/sbin
# export BO_PathVmware=/Applications/VMware\ Fusion.app/Contents/Public

################################################################################
# Added by Nix installer
if [ -e ~/.nix-profile/etc/profile.d/nix.sh ]; then
    source ~/.nix-profile/etc/profile.d/nix.sh
fi
# Disable use of Nix channels,
# in favor of release pinning
# when ready.
# export NIX_PATH=
export BO_PathNix=${HOME}/.nix-profile/bin

################################################################################
# NOTE: Order matters!
# Anaconda should override all (win all collisions).
# Then Homebrew comes second.
# Other non-native tools follow.
# Native system path is next.
# User path is last (so user MUST resolve collisions).
export BO_PathNative=/usr/bin:/bin:/usr/sbin:/sbin
BO_PathSystem=${BO_PathAnaconda}
BO_PathSystem=${BO_PathSystem}:${BO_PathNix}
BO_PathSystem=${BO_PathSystem}:${BO_PathHomebrew}
BO_PathSystem=${BO_PathSystem}:${BO_PathMacPorts}
# BO_PathSystem=${BO_PathSystem}:${BO_PathVmware}
BO_PathSystem=${BO_PathSystem}:${BO_PathNative}
export BO_PathSystem
export BO_PathUser=${HOME}/bin
export PATH=${BO_PathSystem}:${BO_PathUser}

################################################################################
# If not running interactively,
# don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

################################################################################
# Environment
export CLICOLOR=true
# TODO: Change to Spacemacs?
export EDITOR=nvim
export GREP_OPTIONS='--color=auto'
export PAGER=less

# These are handled by Apple macOS
# LANG
# LC_ALL
# TZ

################################################################################
# Bash
shopt -s checkwinsize cmdhist histappend huponexit lithist
shopt -u sourcepath
# shopt -s globstar (unsupported in BASH 3.2.57)
# export FIGNORE=
# export GLOBIGNORE=
export HISTCONTROL=ignoreboth
export HISTFILESIZE=500
export HISTSIZE=500
# export HISTTIMEFORMAT=
# export TIMEFORMAT=

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
export COLORTERM=truecolor
export TERM=xterm-256color

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
# Alias definitions
# You may want to put all your additions
# into a separate file like ~/.bash_aliases,
# instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.
[[ -r ~/alias.bash ]] && source ~/alias.bash
[[ -r ~/alias-SWA.bash ]] && source ~/alias-SWA.bash

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


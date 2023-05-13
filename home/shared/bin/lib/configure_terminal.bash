#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Configure terminal
export CLICOLOR=true
# TODO: Where is this supported (macOS, Ubuntu, etc.)?
export COLORTERM=truecolor
# TODO: Is this handled by iTerm2?
export TERM=xterm-256color

################################################################################
# Set a fancy prompt
# (non-color, unless we know we "want" color)
case "$TERM" in
  xterm-color|*-256color) color_prompt=yes;;
esac

################################################################################
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

################################################################################
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

unset color_prompt force_color_prompt

: << 'DisabledContent'
DisabledContent


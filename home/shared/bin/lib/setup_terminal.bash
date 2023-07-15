#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
me() { echo ${BASH_SOURCE} ; }
[[ -n "${BO_Trace}" ]] && log_trace "Executing '$(me)'" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Setup terminal

# Let iTerm2 set TERM, so do not override here
# NO: export TERM=xterm-256color
# TODO: Where is this supported (macOS, Ubuntu, etc.), needed?
# TODO: export CLICOLOR=true
# TODO: export COLORTERM=truecolor

################################################################################
# TODO: Test first whether we have `tput`
tput init

################################################################################
# Remember desired colors for logging

export BO_ColorReset=$(tput sgr0)
export BO_ColorDebug=$(tput setaf 6)
export BO_ColorError=$(tput setaf 1)
export BO_ColorFatal=$(tput setaf 5)
export BO_ColorGood=$(tput setaf 7)
export BO_ColorInfo=$(tput setaf 2)
export BO_ColorTrace=$(tput setaf 4)
export BO_ColorWarn=$(tput setaf 3)

: << 'DisabledContent'
NORMAL=$(tput sgr0)

BLACK=$(tput setaf 0)
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
BLUE=$(tput setaf 4)
MAGENTA=$(tput setaf 5)
CYAN=$(tput setaf 6)
WHITE=$(tput setaf 7)
LIME_YELLOW=$(tput setaf 190)
POWDER_BLUE=$(tput setaf 153)

BLINK=$(tput blink)
BRIGHT=$(tput bold)
REVERSE=$(tput smso)
UNDERLINE=$(tput smul)

echo "${BLACK}This is black${NORMAL}"
echo "${RED}This is red${NORMAL}"
echo "${GREEN}This is green${NORMAL}"
echo "${YELLOW}This is yellow${NORMAL}"
echo "${BLUE}This is blue${NORMAL}"
echo "${MAGENTA}This is magenta${NORMAL}"
echo "${CYAN}This is cyan${NORMAL}"
echo "${WHITE}This is white${NORMAL}"
echo "${LIME_YELLOW}This is lime yellow${NORMAL}"
echo "${POWDER_BLUE}This is powder blue${NORMAL}"

echo "${REVERSE}${BLACK}This is reverse black${NORMAL}"
echo "${UNDERLINE}${RED}This is underline red${NORMAL}"
echo "${BLINK}${GREEN}This is blink green${NORMAL}"
echo "${BRIGHT}${YELLOW}This is bright yellow${NORMAL}"
echo "${REVERSE}${BLUE}This is reverse blue${NORMAL}"
echo "${UNDERLINE}${MAGENTA}This is underline magenta${NORMAL}"
echo "${BLINK}${CYAN}This is blink cyan${NORMAL}"
echo "${BRIGHT}${WHITE}This is bright white${NORMAL}"
echo "${REVERSE}${LIME_YELLOW}This is reverse lime yellow${NORMAL}"
echo "${UNDERLINE}${POWDER_BLUE}This is underline powder blue${NORMAL}"

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

DisabledContent


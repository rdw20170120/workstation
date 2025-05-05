#!/usr/bin/env false
###################################################################################################
# NOTE:  This file is intended to be sourced into a Bash shell.
###################################################################################################
touch $(dirname ${BASH_SOURCE})/.ran_script_dot_bashrc

source "${HOME}/.config/bash/XDG.bash"
source "${XDG_CONFIG_HOME}/bash/noninteractive.bash"

###################################################################################################
: << 'DisabledContent'
DisabledContent

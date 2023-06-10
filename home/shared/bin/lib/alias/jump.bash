#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Aliases for cd

# Configure for jumping to interesting source-control repository local working directories
alias jump_build='cd ~/repo/GitHub/wip/build'
alias jump_experiment='cd ~/repo/GitLab/wip/experiment'
alias jump_interview='cd ~/repo/GitHub/wip/spring-test-project/complete'
alias jump_javascript='cd ~/repo/GitHub/wip/javascript'
alias jump_mono='cd ~/repo/GitLab/wip/private-mono'
alias jump_pythonspeed='cd ~/repo/GitLab/wip/pythonspeed'
alias jump_workstation='cd ~/repo/GitHub/wip/workstation'

# For working with two local copies of the same repository
alias jump_reference='cd "${BO_DirReference}"'
alias jump_Work_In_Progress='cd "${BO_DirWorkInProgress}"'
[[ -z "${BO_DirReference}" ]] && export BO_DirReference=~/repo/GitHub/ref/workstation
[[ -z "${BO_DirWorkInProgress}" ]] && export BO_DirWorkInProgress=~/repo/GitHub/wip/workstation

: << 'DisabledContent'
DisabledContent


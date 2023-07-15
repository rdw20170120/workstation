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
alias jump_WorkInProgress='cd "${BO_DirWorkInProgress}"'
alias sync_WIP='dir-merge "${BO_DirReference}" "${BO_DirWorkInProgress}"'
[[ -z "${BO_DirReference}" ]] && export BO_DirReference=~/repo/GitHub/ref/workstation
[[ -z "${BO_DirWorkInProgress}" ]] && export BO_DirWorkInProgress=~/repo/GitHub/wip/workstation

: << 'DisabledContent'
DisabledContent


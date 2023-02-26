#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
[[ -z "${BO_Project}" ]] &&
    1>&2 echo "ERROR: Aborting, this project is NOT ACTIVATED" &&
    exit 99

# Initilize Anaconda
require_directory_in CONDA_PREFIX
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('${CONDA_PREFIX}/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    _Script="${CONDA_PREFIX}/etc/profile.d/conda.sh"
    if [ -f "${_Script}" ]; then
        log_debug "Sourcing script '${_Script}'"
        source "${_Script}"
    else
        export PATH="${CONDA_PREFIX}/bin:$PATH"
    fi
fi
unset __conda_setup

# Initialize Mamba too
_Script="${CONDA_PREFIX}/etc/profile.d/mamba.sh"
if [ -f "${_Script}" ]; then
    log_debug "Sourcing script '${_Script}'"
    source "${_Script}"
fi
# <<< conda initialize <<<

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
# Save PS1 since Anaconda is about to modify it
export BO_PS1=${PS1}

# NOTE: Restore PS1 since I don't like having Anaconda put the environment prefix there
export PS1=${BO_PS1}

DisabledContent


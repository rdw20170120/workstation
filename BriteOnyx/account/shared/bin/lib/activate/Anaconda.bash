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
# Activate Anaconda

export BO_PathAnacondaBefore=${PATH}

if [[ -z "${CONDA_PREFIX}" ]]; then
    log_debug "Missing 'CONDA_PREFIX', skipping activation of Anaconda"
    return 0
fi

_Script="${CONDA_PREFIX}/bin/activate"
require_script "${_Script}" && source "${_Script}"

# >>> conda initialize >>>
__conda_setup="$('${CONDA_PREFIX}/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "${CONDA_PREFIX}/etc/profile.d/conda.sh" ]; then
        . "${CONDA_PREFIX}/etc/profile.d/conda.sh"
    else
        export PATH="${CONDA_PREFIX}/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "${CONDA_PREFIX}/etc/profile.d/mamba.sh" ]; then
    . "${CONDA_PREFIX}/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<

conda config --set auto_activate_base True

export BO_PathAnacondaAfter=${PATH}

unset _Script

: << 'DisabledContent'
DisabledContent


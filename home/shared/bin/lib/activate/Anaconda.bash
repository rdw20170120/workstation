#!/usr/bin/env false
################################################################################
# Activate Anaconda

export BO_PathAnacondaBefore=${PATH}

if [[ -z "${CONDA_PREFIX}" ]]; then
    echo "DEBUG: Missing 'CONDA_PREFIX', skipping activation of Anaconda"
    return 0
fi

_Script="${CONDA_PREFIX}/bin/activate"
prepare_to_source "${_Script}" && source "${_Script}"

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


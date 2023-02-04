#!/usr/bin/env false
# Intended to be sourced in a Bash shell during activation.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
[[ -z "${BO_Project}" ]] &&
    1>&2 echo "ERROR: Aborting, this project is NOT ACTIVATED" &&
    exit 99

# Save PS1 since Anaconda is about to modify it
BO_PS1=${PS1}

# Initilize Anaconda
require_directory_in CONDA_PREFIX
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
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

# Configure BriteOnyx for Anaconda environment
require_directory_in BO_Project
export BO_DirAnaconda=${BO_Project}/.anaconda
remembering BO_DirAnaconda
export BO_FileAnacondaJson=${BO_Project}/cfg/anaconda.json
remembering BO_FileAnacondaJson
export BO_FileAnacondaYaml=${BO_Project}/cfg/anaconda.yml
remembering BO_FileAnacondaYaml

_BO_CreateAnacondaEnvironment=true
if [[ -d "${BO_DirAnaconda}" ]] ; then
    _BO_CreateAnacondaEnvironment=false
fi

if [[ "${_BO_CreateAnacondaEnvironment}" == "true" ]] ; then
    log_warn "Creating Anaconda environment in directory '${BO_DirAnaconda}'"
    maybe_delete_directory_tree "${BO_DirAnaconda}"
    mamba create --prefix "${BO_DirAnaconda}"
else
    log_info "Keeping Anaconda environment in directory '${BO_DirAnaconda}'"
fi

require_directory "${BO_DirAnaconda}"
log_info "Activating Anaconda environment in directory '${BO_DirAnaconda}'"
mamba activate "${BO_DirAnaconda}"

export BO_PathAfterAnaconda=${PATH}
remembering BO_PathAfterAnaconda
export BO_PathTool=${BO_DirAnaconda}/bin:${CONDA_PREFIX}/condabin

_Script=${BO_Project}/BriteOnyx/bin/lib/set_path.bash
source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    kill -INT $$  # Kill the executing script, but not the shell (terminal)

# TODO: Extract management of Anaconda environment into separate scripts
# TODO: Extract package list into a function

# Need Python itself
_Packages="python=3.11.*"

# Need Python support tools
_Packages="${_Packages} ansi2html"
_Packages="${_Packages} black"
_Packages="${_Packages} coverage"
# TODO: FIX: Why does icdiff=2.0.* seem to all be corrupted?
_Packages="${_Packages} icdiff=1.9.*"
_Packages="${_Packages} pip"
_Packages="${_Packages} pytest"
_Packages="${_Packages} pytest-cov"
_Packages="${_Packages} pytest-html"
_Packages="${_Packages} pytest-icdiff"
_Packages="${_Packages} pytest-sugar"
# _Packages="${_Packages} tabnanny"

# Need Python packages required by project source code
_Packages="${_Packages} awscli"
_Packages="${_Packages} boto3"
_Packages="${_Packages} logzero"

if [[ "${_BO_CreateAnacondaEnvironment}" == "true" ]] ; then
    log_debug "Installing desired packages into Anaconda environment '${BO_DirAnaconda}'"
    mamba install --yes ${_Packages}
fi

log_info "Capturing installed packages to file '${BO_FileAnacondaJson}'"
mamba list --no-pip >"${BO_FileAnacondaJson}"
require_file "${BO_FileAnacondaJson}"
log_info "Capturing installed packages to file '${BO_FileAnacondaYaml}'"
mamba list --explicit --export --md5 --no-pip >"${BO_FileAnacondaYaml}"
require_file "${BO_FileAnacondaYaml}"

unset _BO_CreateAnacondaEnvironment

# NOTE: Restore PS1 since I don't like having Anaconda put the environment prefix there
export PS1=${BO_PS1}

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


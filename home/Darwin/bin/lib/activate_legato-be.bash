#!/usr/bin/env false
# Intended to be directly executed by the user in a Bash shell via `source`.
set -o pipefail +o verbose +o xtrace
[[ "${BO_Trace:-UNDEFINED}" != UNDEFINED ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace:-UNDEFINED}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
###############################################################################
# Activate a virtual environment from outside the project's source-control repository.

if [[ -z "${HOME}" ]]; then
    echo "FATAL: Variable 'HOME' is undefined"
    exit 1
fi

_Script=${HOME}/bin/lib/declare-essential.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/declare-git.bash
require_script "${_Script}" ; source "${_Script}"

unset _Script

_Project=legato-be
_DirProject=$(git_working_directory "${HOME}/repo/SamsClub/wip" ${_Project})

echo "Setting the execution PATH"
[[ -z "${BO_PathSystem}" ]] && export BO_PathSystem=${PATH}
# BO_PathTool=${BO_PathAnacondaBase}
# export BO_PathTool
PATH=
# PATH+=:${BO_PathTool}
PATH+=:${BO_PathSystem}
# PATH+=:${BO_PathProject}
PATH+=:${BO_PathUser}
export PATH

echo "Jumping into project directory '${_DirProject}'"
cd "${_DirProject}"

# Remember primary Python commands
export BO_cmd_python3=$(which python3)
export BO_cmd_pip="${BO_cmd_python3} -m pip"
export BO_cmd_pipenv="${BO_cmd_python3} -m pipenv"

# ${BO_cmd_pipenv} install
# NO: ${BO_cmd_pipenv} install -r ./requirements_arm64.txt
# ${BO_cmd_pipenv} shell
# ${BO_cmd_pipenv} install pre-commit --dev
# pre-commit install -t pre-push

# Start server with dev database
# TODO: pipenv run ./manage.py runserver --settings=pim.env.dev

# Start server with local database (must have Postgresql installed)
# TODO: pipenv run ./manage.py runserver

# TODO: Ensure `docker-compose.yml` points at `Dockerfile.m1`
docker compose build
docker compose up

###############################################################################
# Test this script:
# clear ; bash -c "source ~/bin/lib/activate_legato-be.bash" ; echo "Status: $?"
# TODO: Show Bash's currently-active short options: `printf %s\\n "$-"`
# TODO: Show Bash's currently-active options: `set -o | grep -Fw on`
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
DisabledContent


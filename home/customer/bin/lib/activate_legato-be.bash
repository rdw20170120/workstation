#!/usr/bin/env false
# Intended to be executed in a Bash shell via `source` directly by the user.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
[[ "${BO_Trace:-UNDEFINED}" != UNDEFINED ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace:-UNDEFINED}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
###############################################################################
# Activate from outside the project's source-control repository.

if [[ -z "${HOME}" ]]; then
    echo "FATAL: Variable 'HOME' is undefined"
    exit 1
fi

_Script=${HOME}/bin/lib/declare/essential.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/declare/git.bash
require_script "${_Script}" ; source "${_Script}"

_Script=${HOME}/bin/lib/declare/PostgreSQL.bash
require_script "${_Script}" ; source "${_Script}"

_Script=${HOME}/credential.bash
require_script "${_Script}" ; source "${_Script}"

unset _Script

_Project=legato-be
_DirProject=$(git_working_directory "${HOME}/repo/SamsClub/wip" ${_Project})

echo "Jumping into project directory '${_DirProject}'"
cd "${_DirProject}"

alias ${_Project}_sync="dir-merge ~/Documents/SamsClub/${_Project} ~/repo/SamsClub/wip/${_Project}"

export DB_HOST=${DB_HostFqdnDev}
export DB_NAME=${DB_NameDev}
export DB_PASSWORD=${DB_PassDevAdmin}
export DB_USER=${DB_UserDevAdmin}

# TODO: NOTE: For now, don't try to run locally
# since it is so problematic.
# Just run within Docker container

# Remember primary Python commands
# export BO_cmd_python3=$(which python3)
# export BO_cmd_pip="${BO_cmd_python3} -m pip"
# export BO_cmd_pipenv="${BO_cmd_python3} -m pipenv"

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
# Now that this is tested, do this manually from now on
# docker compose build
# docker compose up

###############################################################################
# Test this script:
# clear ; bash -c "source ~/bin/lib/activate_legato-be.bash" ; echo "Status: $?"
# TODO: Show Bash's currently-active short options: `printf %s\\n "$-"`
# TODO: Show Bash's currently-active options: `set -o | grep -Fw on`
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
DisabledContent


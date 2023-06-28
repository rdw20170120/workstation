#!/usr/bin/env false
# Intended to be executed in a Bash shell via `source` directly by the user.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace ; shopt -s expand_aliases
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
_Generation=V2
export BO_DirReference=$(git_working_directory "${HOME}/repo/SamsClub/ref/${_Generation}" ${_Project})
export BO_DirWorkInProgress=$(git_working_directory "${HOME}/repo/SamsClub/wip" ${_Project})
_DirProject=${BO_DirWorkInProgress}

echo "Jumping into project directory '${_DirProject}'"
cd "${_DirProject}"

export DB_HOST=legato-pim-postgres-stage${PostgresHostSuffix}
export DB_NAME=postgres
export DB_PASSWORD=${PostgresPassRemoteRegular}
export DB_USER=${PostgresUserRemoteRegular}@legato-pim-postgres-stage

echo "INFO: Show available project aliases by executing 'show_project_alias'"
alias show_project_alias="alias | grep ${_Project}"
alias ${_Project}_build="./build_for_Rob"
alias ${_Project}_run='docker compose up'
alias ${_Project}_sync="dir-merge ~/Documents/SamsClub/${_Project} ~/repo/SamsClub/wip/${_Project}"
show_project_alias

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
# Remember primary Python commands
export BO_cmd_python3=$(which python3)
export BO_cmd_pip="${BO_cmd_python3} -m pip"
export BO_cmd_pipenv="${BO_cmd_python3} -m pipenv"

DisabledContent


#!/usr/bin/env false
# Intended to be executed in a Bash shell via `source`.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
[[ "${BO_Trace:-UNDEFINED}" != UNDEFINED ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace:-UNDEFINED}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
###############################################################################
# Declare Bash functions for `git`
# TODO: Implement: Consider installing Git pre-commit hook
# First, by installing the tool: `brew install pre-commit`
# Then by using the tool: `cd REPO ; pre-commit install`

git_repo_url() {
  # Return URL of remote Git repository with prefix $1 and name $2
  # $1 = git repository URL prefix
  # $2 = git repository name
  echo $1/$2.git
}

git_status_is_clean() {
  # Return whether status of git working directory $1 is clean
  # $1 = git working directory
  # Exit code 0 = clean
  # Exit code 1 = dirty
  pushd "$1" >/dev/null
  local -r _Output=$(git status --porcelain)
  popd >/dev/null
  [[ -z "${_Output}" ]]
}

git_working_directory() {
  # Return path of local working directory with parent directory $1 and repository name $2
  # $1 = parent directory of git working directory
  # $2 = git repository name
  echo $1/$2
}

maybe_bare() {
  # Maybe bare clone git repository $3,
  # which exists at URL $2/$3.git and
  # which will be cloned to directory $1/$3
  # (if it does not already exist).
  # $1 = parent directory of git working directory
  # $2 = git repository URL prefix
  # $3 = git repository name
  if [[ ! -d "$1" ]] ; then
    mkdir -p "$1"
  fi
  cd "$1"

  local -r _Dir=$(git_working_directory "$1" $3)
  if [[ ! -d "${_Dir}" ]] ; then
    local -r _Repo=$(git_repo_url $2 $3)
    echo "INFO: Cloning --bare git repo ${_Repo}"
    git clone --bare ${_Repo} "${_Dir}"
# else
#   TODO: Why does this fail?
#   There is something special about a bare clone
#   that I apparently do not yet understand.
#   maybe_pull "$1" $2 $3
  fi
}

maybe_clone() {
  # Maybe clone git repository $3,
  # which exists at URL $2/$3.git and
  # which will be cloned to directory $1/$3
  # (if it does not already exist).
  # $1 = parent directory of git working directory
  # $2 = git repository URL prefix
  # $3 = git repository name
  if [[ ! -d "$1" ]] ; then
    mkdir -p "$1"
  fi
  cd "$1"

  local -r _Dir=$(git_working_directory "$1" $3)
  if [[ ! -d "${_Dir}" ]] ; then
    local -r _Repo=$(git_repo_url $2 $3)
    echo "INFO: Cloning git repo ${_Repo}"
    git clone ${_Repo} "${_Dir}"
  else
    maybe_pull "$1" $2 $3
  fi
}

maybe_pull() {
  # Maybe pull git repository $3,
  # which exists at URL $2/$3.git and
  # which has been cloned to directory $1/$3.
  # $1 = parent directory of git working directory
  # $2 = git repository URL prefix
  # $3 = git repository name
  local -r _Dir=$(git_working_directory "$1" $3)
  if git_status_is_clean "${_Dir}" ; then
    echo "INFO:  Working directory is clean: ${_Dir}"
    pushd "${_Dir}" >/dev/null
    git fetch --all --prune
    git pull --all
    popd >/dev/null
  else
    echo "WARN:  Working directory is DIRTY: ${_Dir}"
  fi
}

###############################################################################
# TODO: Show Bash's currently-active short options: `printf %s\\n "$-"`
# TODO: Show Bash's currently-active options: `set -o | grep -Fw on`
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
DisabledContent

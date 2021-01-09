#!/bin/false
# This script is intended to be sourced into another script within Bash.

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

  if [[ ! -d "$3" ]] ; then
    git clone $2/$3.git
  else
    maybe_pull $1 $2 $3
  fi
}

maybe_pull() {
  # Maybe pull git repository $3,
  # which exists at URL $2/$3.git and
  # which has been cloned to directory $1/$3.
  # $1 = parent directory of git working directory
  # $2 = git repository URL prefix
  # $3 = git repository name
  if git_status_is_clean $1/$3 ; then
    echo "INFO:  Working directory is clean: $1/$3"
    pushd $1/$3 >/dev/null
    git pull
    popd >/dev/null
  else
    echo "WARN:  Working directory is DIRTY: $1/$3"
  fi
}

git_status_is_clean() {
  # Return whether status of git working directory $1 is clean
  # $1 = git working directory
  # Exit code 0 = clean
  # Exit code 1 = dirty
  pushd $1 >/dev/null
  local -r output=$(git status --porcelain)
  popd >/dev/null
  [[ -z "$output" ]]
}


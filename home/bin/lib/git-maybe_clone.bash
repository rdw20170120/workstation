#!/bin/false
# This script is intended to be sourced into another script within BASH.
set -ex

maybe_clone() {
  # Maybe clone git repository $3, which exists at URL $2/$3.git and which will
  # be cloned to directory $1/$3 (if it does not already exist).
  # $1 = parent directory of new git checkout directory
  # $2 = git repository URL prefix
  # $3 = git repository name
  if [[ ! -d "$1" ]] ; then
    mkdir -p "$1"
  fi
  cd "$1"

  if [[ ! -d "$3" ]] ; then
    git clone $2/$3.git
  fi
}


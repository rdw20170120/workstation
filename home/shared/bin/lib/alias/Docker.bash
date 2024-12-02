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
# Aliases for Docker

alias docker-compose-build-debug='docker compose build --no-cache --progress=plain --pull'
alias docker-compose-pull='docker compose pull'
alias docker-compose-up-as_is='docker compose up'
alias docker-compose-up-recreate='docker compose up --build --force-recreate'
alias docker-container-clean='docker rm $(docker ps --filter=status=created --filter=status=exited --quiet)'
alias docker-image-clean='docker rmi $(docker images --all --filter=dangling=true --quiet)'
alias docker-image-list='docker image ls | tail --lines=+2 | sort | grep -Fv "<none>"'
alias docker-prune-builder='docker builder prune --all --force'
alias docker-prune-buildx='docker buildx prune --all --force'
alias docker-prune-image='docker image prune --all --force'
alias docker-prune-system='docker system prune --all --force'

: << 'DisabledContent'
DisabledContent


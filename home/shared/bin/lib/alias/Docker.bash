#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Aliases for Docker

alias docker-clean-images='docker rmi $(docker images --all --filter=dangling=true --quiet)'
alias docker-clean-ps='docker rm $(docker ps --filter=status=created --filter=status=exited --quiet)'
alias docker-compose-build-debug='docker compose build --no-cache --progress=plain --pull'
alias docker-compose-pull='docker compose pull'
alias docker-compose-up-recreate='docker compose up --build --force-recreate'
alias docker-compose-up-as_is='docker compose up'
alias docker-prune-builder='docker builder prune --all --force'
alias docker-prune-image='docker image prune --all --force'
alias docker-prune-system='docker system prune --all --force'

: << 'DisabledContent'
DisabledContent


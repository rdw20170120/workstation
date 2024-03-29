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
# Library of Bash functions
# to support bootstrapping a new development workstation
# shared across operating systems

distribute_archive() {
    # Distribute contents of archive extracted in directory $1
    local -r DirTemp=$1

    log_debug "Distributing files from bootstrap archive extracted into '${DirTemp}'"
    maybe_copy_file "${DirTemp}" "${HOME}" .bash_logout
    maybe_copy_file "${DirTemp}" "${HOME}" .bash_profile
    maybe_copy_file "${DirTemp}" "${HOME}" .bashrc
    maybe_copy_file "${DirTemp}" "${HOME}" .inputrc
    maybe_copy_file "${DirTemp}" "${HOME}" .profile
    maybe_copy_file "${DirTemp}" "${HOME}" .vimrc
    maybe_copy_file "${DirTemp}" "${HOME}" alias.bash
    maybe_copy_file "${DirTemp}" "${HOME}" config .ssh
    maybe_copy_file "${DirTemp}" "${HOME}" init.vim .config/nvim
    maybe_copy_file "${DirTemp}" "${HOME}" plug.vim .config/nvim/autoload
    maybe_copy_file "${DirTemp}" "${HOME}" plug.vim .local/share/nvim/site/autoload
    maybe_copy_file "${DirTemp}" "${HOME}" plug.vim .vim/autoload
    # TODO: This causes problems on macOS, so I need to copy the files individually
#   maybe_copy_files "${DirTemp}" "${HOME}" bin

    return 0
} && export -f distribute_archive

maybe_backup_file() {
    # Backup file $1, if not already done
    local -r FileSource=$1
    local -r FileTarget=$1.original

    log_debug "Backing up file '${FileSource}' to '${FileTarget}'"
#   [[ ! -e "${FileTarget}" ]] && cp --preserve "${FileSource}" "${FileTarget}"
    [[ ! -e "${FileTarget}" ]] && cp -p "${FileSource}" "${FileTarget}"

    return 0
} && export -f maybe_backup_file

maybe_copy_file() {
    # Copy file $3 from directory $1 to directory $2,
    # including optional subdirectory $4
    # if not already done
    local    DirSource=$1
    local    DirTarget=$2
    local -r File=$3
    local -r Sub=$4

    if [[ -n "${Sub}" ]]; then
        DirSource=${DirSource}/${Sub}
        DirTarget=${DirTarget}/${Sub}
    fi
    if [[ ! -e "${DirTarget}" ]]; then
        if [[ -r "${DirSource}/${File}" ]]; then
            log_debug "Creating directory '${DirTarget}'"
            mkdir -p "${DirTarget}"
        fi
    fi
    if [[ ! -e "${DirTarget}/${File}" ]]; then
        if [[ -r "${DirSource}/${File}" ]]; then
            log_debug "Copying file '${DirSource}/${File}' to '${DirTarget}/${File}'"
#           cp --preserve --update \
#               "${DirSource}/${File}" \
#               "${DirTarget}/${File}"
            cp -p \
                "${DirSource}/${File}" \
                "${DirTarget}/${File}"
        fi
    fi

    return 0
} && export -f maybe_copy_file

prepare_git_access() {
    # Prepare SSH access to public Git hosts
    local -r FileKnown=${HOME}/.ssh/known_hosts
    local -r FileKey=${HOME}/.ssh/id_rsa

    if [[ ! -e "${FileKnown}" ]]; then
        log_debug "Remember relevant SSH host keys"
        ssh-keyscan -H github.com >>"${FileKnown}"
        ssh-keyscan -H gitlab.com >>"${FileKnown}"
    fi

    return 0
} && export -f prepare_git_access

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
# This function
# causes problems on macOS
# because I cannot use
# the `--update` flag,
# so my local edits
# get overwritten each time
# I run the bootstrap
maybe_copy_files() {
    # Copy files from directory $1 to directory $2,
    # including optional subdirectory $3
    # if not already done
    local    DirSource=$1
    local    DirTarget=$2
    local -r Sub=$3

    if [[ -n "${Sub}" ]]; then
        DirSource=${DirSource}/${Sub}
        DirTarget=${DirTarget}/${Sub}
        if [[ ! -e "${DirTarget}" ]]; then
            log_debug "Creating directory '${DirTarget}'"
            mkdir -p "${DirTarget}"
        fi
    fi
    log_debug "Copying files in directory '${DirSource}' to directory '${DirTarget}'"
#   cp --preserve --recursive --update \
#       ${DirSource}/* \
#       ${DirTarget}/
    cp -pR \
        ${DirSource}/* \
        ${DirTarget}/

    return 0
} && export -f maybe_copy_files

DisabledContent


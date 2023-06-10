#!/usr/bin/env false
# Intended to be executed in a Bash shell via `source` during activation.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
[[ -n "${BO_Trace}" ]] && \
    1>&2 echo "DEBUG: Executing ${BASH_SOURCE}" && \
    [[ "${BO_Trace}" == TRACE ]] && \
    1>&2 echo "DEBUG: Tracing ${BASH_SOURCE}" && \
    set -o verbose -o xtrace
# NO: trap ... EXIT
###############################################################################
# TODO: DESCRIPTION

# TODO: CONTENT
###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace

: << 'DisabledContent'
DisabledContent


#!/usr/bin/env cat
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################

prepare_to_source() {
    # Prepare to `source` script $1,
    # returning 0 if the script is found and
    # returning 1 if the script is not found
    # Should be invoked like this:
    # prepare_to_source "${_Script}" && source "${_Script}"
    if [[ -r "${_Script}" ]] ; then
        echo "INFO: Sourcing script '${_Script}'"
        return 0
    else
        echo "WARN: Skipping missing script '${_Script}'"
    fi
    return 1
}

_Script=${HOME}/bin/lib/alias_for_cd.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/alias_for_git.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/alias_for_inputrc.bash
prepare_to_source "${_Script}" && source "${_Script}"

_Script=${HOME}/bin/lib/alias_for_ls.bash
prepare_to_source "${_Script}" && source "${_Script}"

unset _Script

: << 'DisabledContent'
# Add an "alert" alias for long running commands.  Use like so:
# sleep 10; alert
# alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
DisabledContent


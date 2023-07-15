#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
# me() { echo ${BASH_SOURCE} ; }
me() ( echo ${BASH_SOURCE} ; )
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################

_MyDir=$(parent_of $(me))

require_variable BO_RepoBriteOnyx

# Generate and `source` a temporary script to `source` other scripts
_Script=$(get_temporary_file)
log_debug "Generating script '${_Script}'"
cat >"${_Script}" <<EndOfScript
log_trace "Executing '${_Script}'"

_Script=${BO_RepoBriteOnyx}/BriteOnyx/all/account/bin/lib/all_initialize.bash
require_script "\${_Script}" && source "\${_Script}"

_Script=${_MyDir}/all_declare.bash
require_script "\${_Script}" && source "\${_Script}"

_Script=${_MyDir}/all_configure.bash
require_script "\${_Script}" && source "\${_Script}"

_Script=${BO_RepoBriteOnyx}/BriteOnyx/all/account/bin/lib/set_path.bash
require_script "\${_Script}" && source "\${_Script}"

_Script=${_MyDir}/all_activate.bash
require_script "\${_Script}" && source "\${_Script}"

_Script=${BO_RepoBriteOnyx}/BriteOnyx/all/account/bin/lib/set_path.bash
require_script "\${_Script}" && source "\${_Script}"

_Script=${_MyDir}/all_alias.bash
require_script "\${_Script}" && source "\${_Script}"

unset _Script

EndOfScript
require_script "${_Script}" && source "${_Script}"

unset _Script

: << 'DisabledContent'
# Create ~/bin/lib subdirectories
# that can then be iterated using a simple loop
# Configure scripts will set whatever variables, etc.
# that can be before updating PATH
# while
# Activate scripts will rely upon PATH being complete
# Most commands will not need either kind of script
# built-in commands will not need an activate script
# while externally-added tools will likely need both kinds of script
DisabledContent


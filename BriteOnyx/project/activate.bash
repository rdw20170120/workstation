#!/usr/bin/env false
# This script is executed via `source` while initializing a Bash shell.
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
me() { echo ${BASH_SOURCE} ; }
# NOTE: Must still use raw Bash syntax until we have declared essential functions
# NOTE: Special header since this script is called while initializing Bash
1>&2 echo "TRACE: Executing '$(me)'"
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
_MyDir=$(parent_of $(me))
require_variable BO_OS

# Establish temporary directory for project
export BO_DirTemp=${PWD}/.BO/tmp
mkdir -p "${BO_DirTemp}"

# Establish capture directories for project
export BO_DirCapture="${BO_DirTemp}/capture"
mkdir -p "${BO_DirCapture}/after" "${BO_DirCapture}/before" "${BO_DirCapture}/current"
(set -o posix ; set) | sort > "${BO_DirCapture}/before/activation.env"

# TODO: DELETE: Quit using log4bash
# _Script=${PWD}/BriteOnyx/bin/lib/declare-log4bash.bash
# TODO: Require script
# source "${_Script}" ; _Status=$?
# [[ ${_Status} -ne 0 ]] &&
#     kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

log_info "Activating '${PWD}' as the current project"

remembering() {
    # Log that we are remembering variable $1
    [[ $# -eq 0 ]] &&
        log_error "Variable name is required" &&
        kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
    local -r Name=$1
    log_debug "Remembering ${Name} = '${!Name}'"
} && export -f remembering

export BO_DirSnapshot=${PWD}/.BO/snapshot

remembering BO_DirCapture
remembering BO_DirSnapshot
remembering BO_DirTemp

export BO_Project=${PWD}
remembering BO_Project

# Generate and `source` a temporary script to `source` other scripts
_Script=$(get_temporary_file)
log_debug "Generating script '${_Script}'"
cat >"${_Script}" <<EndOfScript
log_trace "Executing '${_Script}'"

_Script=${_MyDir}/shared/bin/lib/activate.bash
require_script "\${_Script}" && source "\${_Script}" ; abort_on_fail \$? "from \${_Script}"

# TODO: _Script=${_MyDir}/${BO_OS}/bin/lib/activate.bash
# TODO: require_script "\${_Script}" && source "\${_Script}" ; abort_on_fail \$? "from \${_Script}"
EndOfScript
require_script "${_Script}" && source "${_Script}" ; abort_on_fail $? "from ${_Script}"

################################################################################
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


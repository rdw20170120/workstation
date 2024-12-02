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

# Generate and `source` a temporary script to `source` other scripts
_Script=$(get_temporary_file)
log_debug "Generating script '${_Script}'"
cat >"${_Script}" <<EndOfScript
log_trace "Executing '${_Script}'"

# NOTE: Must still use raw syntax until we have declared essential functions
_Script=${_MyDir}/shared/bin/lib/activate.bash
if [[ -r "\${_Script}" ]]; then
    1>&2 echo "INFO:  Sourcing '\${_Script}'"
    source "\${_Script}" ; _Status=\$?
    [[ \${_Status} -ne 0 ]] &&
        1>&2 echo "FATAL:  Sourcing '\${_Script}'" &&
        kill -INT \$$  # Interrupt the executing script, but do NOT kill the shell (terminal)
else
    1>&2 echo "WARN:  Missing '\${_Script}'"
    return 99
fi
# Now we can use our essential functions

_Script=${_MyDir}/${BO_OS}/bin/lib/activate.bash
require_script "\${_Script}" && source "\${_Script}" ; abort_on_fail \$? "from \${_Script}"
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


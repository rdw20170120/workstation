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

################################################################################
_Script=${_MyDir}/declare_essential.bash
# NOTE: Must still use raw Bash syntax until we have declared essential functions
if [[ -r "${_Script}" ]]; then
    1>&2 echo "INFO:  Sourcing '${_Script}'"
    source "${_Script}"
else
    1>&2 echo "WARN:  Missing '${_Script}'"
    return 99
fi
# Now we can use our essential Bash functions to help

################################################################################

_Script=${_MyDir}/setup_terminal.bash
require_script "${_Script}" && source "${_Script}" ; abort_on_fail $? "from ${_Script}"

_Script=${_MyDir}/all_declare.bash
require_script "${_Script}" && source "${_Script}" ; abort_on_fail $? "from ${_Script}"

_Script=${_MyDir}/all_configure.bash
require_script "${_Script}" && source "${_Script}" ; abort_on_fail $? "from ${_Script}"

_Script=${_MyDir}/set_PATH.bash
require_script "${_Script}" && source "${_Script}" ; abort_on_fail $? "from ${_Script}"

_Script=${_MyDir}/all_activate.bash
require_script "${_Script}" && source "${_Script}" ; abort_on_fail $? "from ${_Script}"

_Script=${_MyDir}/set_PATH.bash
require_script "${_Script}" && source "${_Script}" ; abort_on_fail $? "from ${_Script}"

_Script=${_MyDir}/all_alias.bash
require_script "${_Script}" && source "${_Script}" ; abort_on_fail $? "from ${_Script}"

################################################################################
: << 'DisabledContent'
DisabledContent


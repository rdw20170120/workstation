#!/usr/bin/env false
# NO: set -o errexit -o nounset
set -o pipefail +o verbose +o xtrace
# NO: Do NOT `export` this function, it only works if defined locally
me() { echo ${BASH_SOURCE} ; }
[[ -n "${BO_Trace}" ]] && log_trace "Executing $(me)" && \
    [[ "${BO_Trace}" == TRACE ]] && set -o verbose -o xtrace
# NO: Do NOT `trap` since it will stay active in the shell
################################################################################
# Activate the BriteOnyx framework to manage this directory tree as a project
#
# NOTE: We MUST NOT EVER `exit` during BriteOnyx activation!
#
# We cannot use a `trap` here
# because it will remain active
# within the shell
# that will `source` this script.
#
# Please see HowTo-use_this_project.md for details.
###############################################################################
if [[ -n "${BO_Project}" ]] ; then
    1>&2 log_fatal "Aborting, this project is already activated as '${BO_Project}'"
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
fi

if [[ -z "${PWD}" ]] ; then
    1>&2 log_fatal "Aborting, missing environment variable 'PWD'"
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
fi

[[ -z "${BO_ARCH}" ]] && export BO_ARCH=$(uname -m)
[[ -z "${BO_OS}" ]] && export BO_OS=$(uname)

# Activate BriteOnyx at the user-account level
# NOTE: This will reactivate BriteOnyx at the user-account level
# if it has already been done in the Bash shell session.
# Watch for any issues to arise.
_Script=${PWD}/BriteOnyx/account/activate.bash
# NOTE: Must use raw syntax until we have declared essential functions
if [[ -r "${_Script}" ]]; then
    1>&2 echo "INFO:  Sourcing '${_Script}'"
    source "${_Script}" ; _Status=$?
    [[ ${_Status} -ne 0 ]] &&
        1>&2 echo "FATAL:  Sourcing '${_Script}'" &&
        kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
else
    1>&2 echo "WARN:  Missing '${_Script}'"
    return 99
fi
# Now we can use our essential functions

# Activate BriteOnyx at the project level
_Script=${PWD}/BriteOnyx/project/activate.bash
require_script "${_Script}" && source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    1>&2 echo "FATAL:  Sourcing '${_Script}'" &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

exit 0

[[ -z "${BO_PathSystem}" ]] && export BO_PathSystem=${PATH}
[[ -z "${BO_PathUser}" ]] && export BO_PathUser=${HOME}/bin

_Script=${BO_Project}/BriteOnyx/bin/lib/set_path.bash
require_script "${_Script}" && source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    1>&2 echo "FATAL:  Sourcing '${_Script}'" &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

# Detect operating system
# TODO: Add detection of various Linux, when we care
export BO_OS=$(uname)
remembering BO_OS

# Establish logging directory for project
export BO_DirLog=${BO_Project}/.BO/log
maybe_create_directory_tree "${BO_DirLog}"
remembering BO_DirLog

maybe_copy_file "${BO_Project}/cfg/sample/alias.bash" "${BO_Project}/alias.bash"
maybe_copy_file "${BO_Project}/cfg/sample/context.bash" "${BO_Project}/context.bash"

# Configure Anaconda environment
(set -o posix ; set) | sort > "${BO_DirCapture}/before/Anaconda.env"
_Script=${BO_Project}/BriteOnyx/bin/lib/configure_Anaconda.bash
require_script "${_Script}" && source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    1>&2 echo "FATAL:  Sourcing '${_Script}'" &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
(set -o posix ; set) | sort > "${BO_DirCapture}/after/Anaconda.env"

# Configure Python
(set -o posix ; set) | sort > "${BO_DirCapture}/before/Python.env"
_Script=${BO_Project}/BriteOnyx/bin/lib/configure_Python.bash
require_script "${_Script}" && source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    1>&2 echo "FATAL:  Sourcing '${_Script}'" &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
(set -o posix ; set) | sort > "${BO_DirCapture}/after/Python.env"

_Script="${BO_Project}/bin/lib/declare.bash"
if [[ -r ${_Script} ]] ; then
    source ${_Script} ; _Status=$?
    [[ ${_Status} -ne 0 ]] &&
        1>&2 echo "FATAL:  Sourcing '${_Script}'" &&
        kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)
fi

_Script="${BO_Project}/context.bash"
require_script "${_Script}" && source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    1>&2 echo "FATAL:  Sourcing '${_Script}'" &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

_Script="${BO_Project}/BriteOnyx/bin/lib/alias.bash"
require_script "${_Script}" && source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    1>&2 echo "FATAL:  Sourcing '${_Script}'" &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

_Script="${BO_Project}/alias.bash"
require_script "${_Script}" && source "${_Script}" ; _Status=$?
[[ ${_Status} -ne 0 ]] &&
    1>&2 echo "FATAL:  Sourcing '${_Script}'" &&
    kill -INT $$  # Interrupt the executing script, but do NOT kill the shell (terminal)

(set -o posix ; set) | sort > "${BO_DirCapture}/after/activation.env"

log_good "BriteOnyx has successfully activated this project in this Bash shell session."
log_info "To get started, try executing the 'cycle' alias..."

unset _Script
unset _Status

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# NO: set -o errexit -o nounset
# export PS4='$ ' ; set -o verbose -o xtrace
# Code to debug...
# set +o verbose +o xtrace
: << 'DisabledContent'
DisabledContent


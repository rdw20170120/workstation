from . import script_bash
from . import script_briteonyx

from throw_out_your_templates_3_core_visitor_map import VisitorMap

from .structure_bash import *
from .structure_briteonyx import *


class Script(script_briteonyx.Script):
    def __init__(self, content):
        script_briteonyx.Script.__init__(self)
        self._content = content


def build():
    return Script([
        source_header(),
        '''# NOTE: Assumes this project has been activated using the BriteOnyx framework.
# NOTE: We MUST NOT EVER 'exit' during BriteOnyx bootstrap or activation
####################################################################################################
# NOTE: Uncomment the following two lines for debugging
# set -o verbose
# set -o xtrace
# TODO: SOMEDAY: Add inverse commands to isolate debugging

####################################################################################################
# Declare needed functionality to support the BriteOnyx framework
# NOTE: We use the 'bo' prefix by convention for all our BriteOnyx support functions.

####################################################################################################
# Functions in this section should NOT call functions from following sections

boLog () {
  # Log the message $1 to STDERR
  # NOTE:  Should only be called from this script
  # $1 = message
  echo -e "$1" >&2
} && export -f boLog

boNodeCanonical () {
  # Return the canonical pathname for file system node $1
  # NOTE: Must be called via command substitution, e.g.:
  #   "$(boNodeCanonical '$1')"
  [[ $# -eq 1 ]] || return 100
  # $1 = pathname of file system node
  declare Result
  # NOTE: This call to "readlink" is not supported on Apple Mac OS X, so deal with it...
  Result="$(readlink -m $1)"
  [[ $? -eq 0   ]] && echo "$Result" && return 0
  [[ "$1" = "." ]] && echo "$PWD"       && return 0
  echo "$1"
} && export -f boNodeCanonical

boTrace () {
  # Trace message $1
  # $1 = message
  [[ -n "$BO_Trace" ]] && boLog "TRACE: $1"
} && export -f boTrace

boTraceEntry () {
  # Trace the entry of execution into caller with source location name $1 and line $2 called with
  #   argument count $3 and arguments $4
  [[ $# -eq 4 ]] || return 100
  # $1 = caller source location name ($FUNCNAME or $0)
  # $2 = caller source location line ($LINENO)
  # $3 = caller argument count ($#)
  # $4 = caller arguments ($*)
  boTrace "'$1:$2' called with $3 args: '$4'"
} && export -f boTraceEntry

boTraceValue () {
  # Trace value $2 described as $1
  [[ $# -eq 2 ]] || return 100
  # $1 = description of value
  # $2 = value
  boTrace "$1 = '$2'"
} && export -f boTraceValue

boTraceVariable () {
  # Trace environment variable $1
  [[ $# -eq 1 ]] || return 100
  # $1 = name of environment variable
  declare -r Name="$1"
  declare -r Value="${!Name}"
  boTraceValue "Variable '$Name'" "$Value"
} && export -f boTraceVariable

####################################################################################################
# Functions in this section should NOT call functions from following sections

boDirectoryExists () {
  boNodeIsDirectory "$1"
} && export -f boDirectoryExists

boFileExists () {
  boNodeIsFile "$1"
} && export -f boFileExists

boNodeExists () {
  # Return whether node $1 exists
  [[ $# -eq 1 ]] || return 100
  # $1 = node pathname
  [[ -e "$1" ]]
} && export -f boNodeExists

boNodeIsDirectory () {
  # Return whether node $1 is a directory
  [[ $# -eq 1 ]] || return 100
  # $1 = node pathname
  [[ -d "$1" ]]
} && export -f boNodeIsDirectory

boNodeIsFile () {
  # Return whether node $1 is a file
  [[ $# -eq 1 ]] || return 100
  # $1 = node pathname
  [[ -f "$1" ]]
} && export -f boNodeIsFile

boVariableIsMissing () {
  # Return whether environment variable $1 is missing (undefined or empty)
  [[ $# -eq 1 ]] || return 100
  # $1 = name of environment variable
  declare -r Name="$1"
  declare -r Value="${!Name}"
  [[ -z "$Value" ]]
} && export -f boVariableIsMissing

####################################################################################################
# Functions in this section should NOT call functions from following sections

boLogDebug () {
  boLog "DEBUG: $1"
} && export -f boLogDebug

boLogError () {
  boLog "ERROR: $1"
} && export -f boLogError

boLogFatal () {
  boLog "FATAL: $1"
} && export -f boLogFatal

boLogInfo () {
  boLog "INFO:  $1"
} && export -f boLogInfo

boLogWarn () {
  boLog "WARN:  $1"
} && export -f boLogWarn

####################################################################################################
# Functions in this section should NOT call functions from following sections

boAbort () {
  boTraceEntry "$FUNCNAME" "$LINENO" $# "$*"
  # Abort execution due to previous command's status $3 while reporting fatal log message $5
  #   (including source location name $1 and line $2) and propagating outgoing status code $4
  # TODO: Rename to boFail?
  [[ $# -eq 5 ]] || return 100
  # $1 = caller source location name ($FUNCNAME or $0)
  # $2 = caller source location line ($LINENO)
  # $3 = incoming status code from previous command ($?, non-zero)
  # $4 = outgoing status code (repeat $? unless overriding)
  # $5 = message
  [[ "$3" -eq 0 ]] && return 100
  boLogFatal "ABORT: Status $3 at '$1:$2' -> status $4: $5"
  return "$4"
} && export -f boAbort

boFailed () {
  boTraceEntry "$FUNCNAME" "$LINENO" $# "$*"
  # Log failed execution due to previous command's status $3 as reported at source location name
  #   $1 and line $2, then propagate the failed status
  [[ $# -eq 3 ]] || return 100
  # $1 = caller source location name ($FUNCNAME or $0)
  # $2 = caller source location line ($LINENO)
  # $3 = incoming status code from previous command ($?, non-zero)
  [[ "$3" -eq 0 ]] && return 100
  boLogFatal "FAILED: Status $3 at '$1:$2'"
  return "$3"
} && export -f boFailed

####################################################################################################
# Functions in this section should NOT call functions from following sections

boArgsRequire () {
  boTraceEntry "$FUNCNAME" "$LINENO" $# "$*"
  # Require that the actual argument count $3 equal the expected argument count $4 in the caller
  #   with source location name $1 and line $2
  [[ $# -eq 4 ]] || return 100
  # $1 = caller source location name ($FUNCNAME or $0)
  # $2 = caller source location line ($LINENO)
  # $3 = actual argument count ($#)
  # $4 = expected argument count
  declare -r Msg="Expected $4 arguments but got $3!"
  [[ $3 -eq $4 ]] || boAbort "$1" "$2" $? 100 "$Msg" || return $?
} && export -f boArgsRequire

####################################################################################################
# Functions in this section should NOT call functions from following sections

boDirectoryCreate () {
  boTraceEntry "$FUNCNAME" "$LINENO" $# "$*"
  # Create directory $1, if it does not already exist
  boArgsRequire "$FUNCNAME" "$LINENO" $# 1 || return $?
  # $1 = directory pathname
  declare Msg="Directory '$1' already exists, skipping creation."
  boNodeIsDirectory "$1" && boLogDebug "$Msg"                            && return $?
  Msg="Unable to create directory '$1', failed!"
  mkdir -p "$1"           || boAbort "$FUNCNAME" "$LINENO" $? 100 "$Msg" || return $?
  boDirectoryRequire "$1" || boAbort "$FUNCNAME" "$LINENO" $? 100 "$Msg" || return $?
} && export -f boDirectoryCreate

boDirectoryRequire () {
  boTraceEntry "$FUNCNAME" "$LINENO" $# "$*"
  # Require directory $1, abort if it is missing
  boArgsRequire "$FUNCNAME" "$LINENO" $# 1 || return $?
  # $1 = pathname of required directory
  boNodeIsDirectory "$1" && return $?
  Msg="Directory '$1' is required but is missing!"
  boNodeExists "$1" || boAbort "$FUNCNAME" "$LINENO" $? 100 "$Msg" || return $?
  Msg="Directory '$1' is required but is blocked by a non-directory!"
  boAbort "$FUNCNAME" "$LINENO" 100 100 "$Msg" || return $?
} && export -f boDirectoryRequire

boFileRequire () {
  boTraceEntry "$FUNCNAME" "$LINENO" $# "$*"
  # Require that file $1 exists, abort if it is missing
  # TODO: Should we check other characteristics like readability or executability?
  boArgsRequire "$FUNCNAME" "$LINENO" $# 1 || return $?
  # $1 = required script file pathname
  declare -r Msg="File '$1' is required but missing!"
  boNodeIsFile "$1" || boAbort "$FUNCNAME" "$LINENO" $? 100 "$Msg" || return $?
} && export -f boFileRequire

boScriptRequire () {
  # Require that script file $1 exists, abort if it is missing
  # TODO: Should we check other characteristics like readability or executability?
  boFileRequire "$1" || boFailed "$FUNCNAME" "$LINENO" $? || return $?
} && export -f boScriptRequire

boVariableRequire () {
  boTraceEntry "$FUNCNAME" "$LINENO" $# "$*"
  # Require environment variable $1, abort if it is missing
  boArgsRequire "$FUNCNAME" "$LINENO" $# 1 || return $?
  # $1 = name of required environment variable
  declare -r Msg="Variable '$1' is required but is undefined or empty!"
  ! boVariableIsMissing "$1" || boAbort "$FUNCNAME" "$LINENO" $? 100 "$Msg" || return $?
} && export -f boVariableRequire

####################################################################################################
# Functions in this section should NOT call functions from following sections

boExecute () {
  boTraceEntry "$FUNCNAME" "$LINENO" $# "$*"
  # Execute command $1; if it fails, abort with message $2
  boArgsRequire "$FUNCNAME" "$LINENO" $# 2 || return $?
  # $1 = command to execute
  # $2 = message for abort upon failure
  boLogDebug "Executing command: $1"
  $1 || boAbort "$FUNCNAME" "$LINENO" $? $? "$2" || return $?
} && export -f boExecute

####################################################################################################
# Successfully 'return', but do NOT 'exit'
return 0
''',
        disabled_content_footer(),
    ])
    

VISITOR_MAP = VisitorMap(parent_map=script_bash.VISITOR_MAP)


def render(target_directory, target_file):
    script_bash.render(build(), VISITOR_MAP, target_directory, target_file)


""" Disabled content
"""


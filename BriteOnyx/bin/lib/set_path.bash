#!/usr/bin/env false
# Intended to be sourced in a Bash shell.
[[ -n "${BO_Trace}" ]] && 1>&2 echo "Executing ${BASH_SOURCE}" && [[ "${BO_Trace}" != 'TRACE' ]] && set -vx
# NO: set -e
# NO: trap ... EXIT
###############################################################################
# Set PATH for project

# NOTE: This specific ordering of PATH elements is REQUIRED and ESSENTIAL.
#
# The Anaconda environment MUST come first
# in order to override everything else.
# Anaconda should override all (win all collisions)
# as the preferred package manager
# for projects being developed and/or deployed.
#
# The system package manager comes second, which is
# Homebrew (currently) for Apple macOS.
# APT for Debian and Ubuntu 
# are available on the system path,
# so it does not require special treatment.
#
# All such separately-installed
# package managers, development platforms, and individual tools
# should override any system-installed programs,
# therefore they are included in `BO_PathTool`
# at the front of `PATH`.
#
# The original system path `BO_PathOriginal` is next.
# This usually consists of `PATH` as it exists
# before executing any user-specific shell login scripts.
# The system PATH element `BO_PathSystem`
# MUST precede
# any user PATH element `BO_PathUser`
# in order to make collisions fail-fast and
# to defeat simple attempts at redirecting system commands as an attack vector.
#
# Similarly,
# the project PATH element `BO_PathProject`
# MUST precede
# the user PATH element `BO_PathUser`
# in order to make collisions fail-fast
# in favor of the project over the user.
# The user path is last as `BO_PathUser`.
#
# This arrangement is best for ensuring consistent behavior
# of the environment, the system, and the project.
# It puts at-risk only
# those user-specific commands, tools, and scripts
# relevant to the currently-deployed environment--
# where the specific user is best positioned to address them
# and failures are most likely limited to affecting only
# the current project and user (as they should).

require_variable BO_Project

# Projects should modify PATH mostly by setting `BO_PathProject`
[[ -z "${BO_PathProject}" ]] && export BO_PathProject=${BO_Project}/bin:${BO_Project}/BriteOnyx/bin

# Remember variants of the system `PATH`
[[ -z "${BO_PathNative}" ]] && export BO_PathNative=${PATH}
[[ -z "${BO_PathOriginal}" ]] && export BO_PathOriginal=${PATH}
export BO_PathSystem=${BO_PathOriginal}

require_variable BO_PathProject
require_variable BO_PathSystem
require_variable BO_PathTool
require_variable BO_PathUser

# Most system-level modifications to `PATH`
# should happen to `BO_PathToolOther`
BO_PathTool=${BO_PathAnaconda}
BO_PathTool+=:${BO_PathHomebrew}
BO_PathTool+=:${BO_PathToolOther}
export BO_PathTool

# Only the user should modify `BO_PathUser`
[[ -z "${BO_PathUser}" ]] && export BO_PathUser=${HOME}/bin

# This assemblage of `PATH`
# should remain fixed and invariant,
# except by modifying the elements properly
# as described above.
# TODO: However, a project-specific virtual environment
# should come FIRST on `PATH`
# before ANY other elements.
PATH=${BO_PathTool}
PATH+=:${BO_PathSystem}
PATH+=:${BO_PathProject}
PATH+=:${BO_PathUser}
export PATH

remembering BO_PathProject
remembering BO_PathSystem
remembering BO_PathTool
remembering BO_PathUser
remembering PATH

###############################################################################
# NOTE: Uncomment these lines for debugging, placed where needed
# export PS4='$ ' ; set -vx
# Code to debug...
# set +vx

: << 'DisabledContent'
DisabledContent


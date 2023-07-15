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
# Set PATH for project

# TODO: REWRITE: detailed explanation

# Summary:
# - This specific ordering of PATH elements is REQUIRED and ESSENTIAL.
# - Project PATH element `BO_PathProject`
#   - Project manipulates its PATH primarily here
#   - Project-specific `bin` directory
#   - Project-specific Anaconda environment PATH
# - Tool PATH element `BO_PathTool`
#   - used as-is, NOT modified by the project AT ALL
#   - defaulted if not already set
# - System PATH element `BO_PathSystem`
#   - used as-is, NOT modified by the project AT ALL
#   - defaulted if not already set
# - BriteOnyx PATH element `BO_PathBriteOnyx`
#   - Project may override the incoming setting to pick a specific release
#   - defaulted?
# - User PATH element `BO_PathUser`
#   - used as-is, NOT modified by the project AT ALL
#   - defaulted if not already set
# - 
# The project PATH element `BO_PathProject` MUST come FIRST
# to override ALL other PATH elements.
# This allows the project to control its environment
# over and above what the user and the system may have installed.
#
# The tool PATH element `BO_PathTool` MUST come next
# so that the user can control what tools they wish to use
# instead of any provided by the system.
#
# The `base` Anaconda environment MUST come first
# on the tool PATH element `BO_PathTool`
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
# The system PATH element `BO_PathSystem`
# MUST precede
# any user PATH element `BO_PathUser`
# in order to make collisions fail-fast and
# to defeat simple attempts at redirecting system commands as an attack vector.
#
# The user PATH element `BO_PathUser` comes LAST
# in order to make collisions fail-fast
# in favor of the project over the user.
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

# Projects will typically select a specific release of BriteOnyx
# Default it here with a self-contained copy for now
[[ -z "${BO_PathBriteOnyx}" ]] && export BO_PathBriteOnyx=${BO_Project}/BriteOnyx/bin

# Projects should modify PATH mostly by setting `BO_PathProject`
export BO_PathProject=${BO_Project}/bin:${BO_PathProjectAnaconda}

# Default system PATH element
[[ -z "${BO_PathOriginal}" ]] && export BO_PathOriginal=${PATH}
[[ -z "${BO_PathSystem}" ]] && export BO_PathSystem=${BO_PathOriginal}

# Currently no defaulting of the tool PATH element

# Default user PATH element
[[ -z "${BO_PathUser}" ]] && export BO_PathUser=${HOME}/bin

# This assemblage of `PATH`
# should remain fixed and invariant,
# except by modifying the elements properly
# as described above.
require_variable BO_PathBriteOnyx
require_variable BO_PathProject
require_variable BO_PathSystem
require_variable BO_PathTool
require_variable BO_PathUser
PATH=${BO_PathProject}
PATH+=:${BO_PathTool}
PATH+=:${BO_PathSystem}
PATH+=:${BO_PathBriteOnyx}
PATH+=:${BO_PathUser}
export PATH

remembering BO_PathBriteOnyx
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


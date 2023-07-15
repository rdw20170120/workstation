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
# Set paths, especially PATH

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
#
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

# Default system PATH element
[[ -z "${BO_PathNative}" ]] && export BO_PathNative=${PATH}
[[ -z "${BO_PathOriginal}" ]] && export BO_PathOriginal=${PATH}
[[ -z "${BO_PathSystem}" ]] && export BO_PathSystem=${BO_PathOriginal}

# TODO: REFACTOR: Move this to an appropriate script
export BO_PathNeovim=${HOME}/opt/Neovim/0.9.0/bin

# Most system-level modifications to `PATH`
# should happen to `BO_PathTool`
# Remember:  Order MATTERS!
BO_PathTool=
[[ -n "${BO_PathAnacondaBase}" ]] && BO_PathTool+=:${BO_PathAnacondaBase}
[[ -n "${BO_PathHomebrew}" ]] && BO_PathTool+=:${BO_PathHomebrew}
[[ -n "${BO_PathKrew}" ]] && BO_PathTool+=:${BO_PathKrew}
[[ -n "${BO_PathNeovim}" ]] && BO_PathTool+=:${BO_PathNeovim}
export BO_PathTool

# Default user PATH element
[[ -z "${BO_PathUser}" ]] && export BO_PathUser=${HOME}/bin

# This assemblage of `PATH`
# should remain fixed and invariant,
# except by modifying the elements properly
# as described above.
# NOTE:  `BO_PathProject` is absent here at the system level, by design
PATH=${BO_PathTool}
PATH+=:${BO_PathSystem}
PATH+=:${BO_PathBriteOnyxSystem}
PATH+=:${BO_PathUser}
export PATH

: << 'DisabledContent'
DisabledContent


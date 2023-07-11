#!/usr/bin/env false
# NOTE:  This file is intended to be sourced into a Bash shell.
################################################################################
# Configure paths, especially PATH

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

# Projects should modify PATH mostly by setting `BO_PathProject`
[[ -z "${BO_PathProject}" ]] && export BO_PathProject=

# Remember variants of the system `PATH`
[[ -z "${BO_PathNative}" ]] && export BO_PathNative=${PATH}
[[ -z "${BO_PathOriginal}" ]] && export BO_PathOriginal=${PATH}
export BO_PathSystem=${BO_PathOriginal}

# TODO: REFACTOR: Move this to an appropriate script
export BO_PathNeovim=${HOME}/opt/Neovim/0.9.0/bin

# Most system-level modifications to `PATH`
# should happen to `BO_PathTool`
# Remember:  Order MATTERS!
BO_PathTool=
[[ -d "${BO_PathAnaconda}" ]] && BO_PathTool+=:${BO_PathAnaconda}
[[ -d "${BO_PathHomebrew}" ]] && BO_PathTool+=:${BO_PathHomebrew}
[[ -d "${BO_PathKrew}" ]] && BO_PathTool+=:${BO_PathKrew}
[[ -d "${BO_PathNeovim}" ]] && BO_PathTool+=:${BO_PathNeovim}
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

: << 'DisabledContent'
DisabledContent


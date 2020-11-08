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
    return Script(
        [
            source_header(),
            """# NOTE: We MUST NOT EVER 'exit' during BriteOnyx bootstrap or activation
####################################################################################################
# NOTE: Uncomment the following two lines for debugging
# set -o verbose
# set -o xtrace
# TODO: SOMEDAY: Add inverse commands to isolate debugging

####################################################################################################
# Verify pre-conditions

[[   -z "$BO_Home"        ]] && echo 'FATAL: Missing $BO_Home'                && return 63
[[ ! -d "$BO_Home"        ]] && echo "FATAL: Missing directory '$BO_Home'"    && return 63
[[   -z "$BO_Project"     ]] && echo 'FATAL: Missing $BO_Project'             && return 63
[[ ! -d "$BO_Project"     ]] && echo "FATAL: Missing directory '$BO_Project'" && return 63
[[   -z "$BO_HomePackage" ]] && echo 'FATAL: Missing $BO_HomePackage'         && return 63
[[   -z "$BO_PathSystem"  ]] && echo 'FATAL: Missing $BO_PathSystem'          && return 63

Dir=$BO_Home/activation
[[ ! -d "${Dir}" ]] && echo "FATAL: Missing directory '${Dir}'" && return 63

####################################################################################################
# Configure environment for Linux

Script=${Dir}/activate.src
[[ ! -f "${Script}" ]] && echo "FATAL: Missing script '${Script}'" && return 63

source ${Script}

Status=$?
[[ ${Status} -ne 0 ]] && echo "FATAL: Exit code ${Status} at '$0':$LINENO" && return ${Status}

####################################################################################################
# Verify post-conditions

[[ -z "$BO_E_Config"  ]] && echo 'FATAL: Missing $BO_E_Config'  && return 63
[[ -z "$BO_E_Ok"      ]] && echo 'FATAL: Missing $BO_E_Ok'      && return "$BO_E_Config"
[[ -z "$BO_PathLinux" ]] && echo 'FATAL: Missing $BO_PathLinux' && return "$BO_E_Config"

####################################################################################################
# Configure environment for Python on Linux

DirPVE=$BO_Project/PVE
export BO_PathProject=$BO_PathProject:${DirPVE}/bin
export BO_PathPython=$BO_Home/invocation/Python

PATH=${BO_PathProject}
PATH=$PATH:${BO_PathPython}
PATH=$PATH:${BO_PathLinux}
PATH=$PATH:${BO_PathSystem}
export PATH

####################################################################################################
# Configure PIP_DOWNLOAD_CACHE

if [[ -z "$PIP_DOWNLOAD_CACHE" ]]; then
  echo 'WARN: Missing $PIP_DOWNLOAD_CACHE'
  [[ -z "$PIP_DOWNLOAD_CACHE" ]] && [[ -n "$TMPDIR" ]] && export PIP_DOWNLOAD_CACHE="$TMPDIR/pip"
  [[ -z "$PIP_DOWNLOAD_CACHE" ]] && echo 'FATAL: Missing $PIP_DOWNLOAD_CACHE' && return 63
  echo "INFO: Remembering PIP_DOWNLOAD_CACHE='$PIP_DOWNLOAD_CACHE'"
fi
[[ ! -d "$PIP_DOWNLOAD_CACHE" ]] && mkdir -p "$PIP_DOWNLOAD_CACHE"
[[ ! -d "$PIP_DOWNLOAD_CACHE" ]] && echo "FATAL: Missing directory '$PIP_DOWNLOAD_CACHE'" && return 63

####################################################################################################
# Configure Python virtual environment (PVE)

export PIP_REQUIRE_VIRTUALENV=true
export PIP_RESPECT_VIRTUALENV=true

Script=${DirPVE}/bin/activate
if [[ ! -f "${Script}" ]]; then
  # If the virtual environment does not already exist, create it
  # TODO: This code assumes that the Python virtual environment package is
  # already installed, but it may not be.  Eventually we should handle that,
  # either with a more-specific message or by actually installing it.
  echo "WARN: Creating Python virtual environment (PVE) in '${DirPVE}'"
  echo "WARN: This requires the 'python-virtualenv' package to have been installed"
  virtualenv "${DirPVE}"
  Status=$?
  [[ ${Status} -ne 0 ]] && echo "FATAL: Exit code ${Status} at '$0':$LINENO" && return ${Status}
fi

[[ ! -d "${DirPVE}" ]] && echo "FATAL: Missing directory '${DirPVE}'" && return 63
[[ ! -f "${Script}" ]] && echo "FATAL: Missing script '${Script}'" && return 63

source ${Script}

Status=$?
[[ ${Status} -ne 0 ]] && echo "FATAL: Exit code ${Status} at '$0':$LINENO" && return ${Status}

[[ -z "$VIRTUAL_ENV" ]] && echo 'FATAL: Missing $VIRTUAL_ENV' && return 63
export PYTHONHOME=$VIRTUAL_ENV
[[ -z "$PYTHONHOME"  ]] && echo 'FATAL: Missing $PYTHONHOME'  && return 63

echo "INFO: Activated Python virtual environment (PVE) in '${DirPVE}'"
echo "INFO: Found '$(python --version 2>&1)' at '$(which python)'"
""",
            disabled_content_footer(),
        ]
    )


VISITOR_MAP = VisitorMap(parent_map=script_bash.VISITOR_MAP)


def render(target_directory, target_file):
    script_bash.render(build(), VISITOR_MAP, target_directory, target_file)


""" Disabled content
"""

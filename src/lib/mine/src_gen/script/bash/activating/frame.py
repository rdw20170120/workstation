#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.frame import *

# Project modules   (relative references, NOT packaged, in project)
from .element import *
from .material import *


def header_activation(config):
    return [
        shebang_sourced(),
        comment(
            "Intended to be executed in a Bash shell via `source` during activation."
        ),
        no(set_("-o errexit", "-o nounset")),
        set_("-o pipefail", "+o verbose", "+o xtrace"),
        eol(),
        tracing_in_header(config),
        no(trap("...", "EXIT")),
        rule(),
    ]


"""DisabledContent
"""

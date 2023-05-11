#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    css_class = "support"
    page = Html5(css_class, "HowTo cut-and-paste")
    page.add(
        htmltags.p[
            "TODO: Describe how cut-and-paste is constrained within exam environment.",
        ],
    )
    page.add(
        htmltags.p[
            """TODO: Cut-and-paste is forbidden and blocked into and out of the exam environment, so as
to protect the integrity of the exam.""",
        ],
    )
    page.add(
        htmltags.p[
            "TODO: Cut-and-paste does not work ",
            emphasis("ACROSS"),
            " machines, but only ",
            emphasis("WITHIN"),
            " individual machines.  Cut-and-paste is an application or operating-system function.",
        ],
    )
    page.add(
        htmltags.p[
            """TODO: Cut-and-paste is mostly unnecessary for a system administrator since they routinely
make use of appropriate features of such tools as Bash and SSH.  The entire exam can be completed
using the web browser and terminal of the client machine, without directly logging in to any of the
server consoles (use SSH from a client shell instead).""",
        ],
    )
    page.render(PAGE_CUT_AND_PASTE)


if __name__ == "__main__":
    sys.exit(main())

""" Disabled content
"""

#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    css_class = "support"
    page = Html5(css_class, "Why some tasks undo others")
    page.add(
        htmltags.p[
            """TODO: Describe how the exam is constrained to execute tasks mostly in order, because we
are managing a database which is inherently stateful.""",
        ],
    )
    page.add(
        htmltags.p[
            """TODO: Describe how the system/database administrator role routinely involves doing and
undoing changes to systems/databases as deployment needs shift over time.  This exam involves such
changes over a much more significant timeframe than just the few hours of exam duration.""",
        ],
    )
    page.render(PAGE_UNDO)


if __name__ == "__main__":
    sys.exit(main())

""" Disabled content
"""

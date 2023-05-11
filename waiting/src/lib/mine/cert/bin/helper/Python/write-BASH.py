#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    css_class = "support"
    page = Html5(css_class, "HowTo use Bash")
    page.add(
        htmltags.p[
            "TODO: Describe how to use Bash command-line completion, editing, and history",
        ],
    )
    page.render(PAGE_Bash)


if __name__ == "__main__":
    sys.exit(main())

""" Disabled content
"""

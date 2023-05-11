#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    css_class = "support"
    page = Html5(css_class, "HowTo begin and end your exam session")
    page.add(
        htmltags.p["TODO: Describe how the exam session begins and ends",],
    )
    page.render(PAGE_SESSION)


if __name__ == "__main__":
    sys.exit(main())

""" Disabled content
"""

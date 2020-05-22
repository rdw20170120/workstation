#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    css_class = 'support'
    page = Html5(css_class, 'HowTo use BASH')
    page.add(htmltags.p[
        'TODO: Describe how to use BASH command-line completion, editing, and history',
    ],)
    page.render(PAGE_BASH)


if __name__ == '__main__':
    sys.exit(main())

""" Disabled content
"""


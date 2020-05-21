#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    css_class = 'support'
    page = Html5(css_class, 'HowTo use the exam user interface (UI)')
    page.add(htmltags.p[
        'TODO: Describe how the PSI/Hatsize user interface works for the examinee',
    ],)
    page.render(PAGE_UI)


if __name__ == '__main__':
    sys.exit(main())

""" Disabled content
"""


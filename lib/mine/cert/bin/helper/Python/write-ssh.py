#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    css_class = 'support'
    page = Html5(css_class, 'HowTo use SSH')
    page.add(htmltags.p[
        'TODO: Describe how the examinee should use ',
        literal('ssh'),
        ' to access the various machines within the exam environment.'
    ],)
    page.render(PAGE_SSH)


if __name__ == '__main__':
    sys.exit(main())

""" Disabled content
"""


#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    css_class = 'support'
    page = Html5(css_class, 'HowTo manage keyboard focus')
    page.add(htmltags.p[
        '''TODO: Describe how keyboard focus is managed within the exam environment by clicking the
mouse on the containing windows.  Note that there are several machine windows available within the
exam environment presented within your local web browser.''',
    ],)
    page.add(htmltags.p[
        '''TODO: Describe how managing keyboard focus is mostly unnecessary because the exam can be
easily completed from the client machine using its web browser and shell windows.''',
    ],)
    page.render(PAGE_FOCUS)


if __name__ == '__main__':
    sys.exit(main())

""" Disabled content
"""


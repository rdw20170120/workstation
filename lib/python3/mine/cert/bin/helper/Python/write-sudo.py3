#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    username = get_machine_username()

    css_class = 'support'
    page = Html5(css_class, 'HowTo be superuser')
    page.add(htmltags.p[
        'TODO:  Describe how the examinee should follow the best practice of ',
        emphasis('rarely-to-never'),
        ' using the ',
        literal('root'),
        ' account directly to exercise superuser privileges.',
    ],)
    page.add(htmltags.p[
        'TODO:  Describe how the examinee should use their own ',
        literal(username),
        ' account throughout the exam.',
    ],)
    page.add(htmltags.p[
        'TODO:  Describe how the examinee should use ',
        literal('sudo'),
        ' during the exam to gain superuser privileges, rather than attempting to login as ',
        literal('root'),
        '.',
    ],)
    page.render(PAGE_SUDO)


if __name__ == '__main__':
    sys.exit(main())

""" Disabled content
"""


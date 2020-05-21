#!/usr/bin/env python

"""
setup.py will call the setups of each step:
"""

import os
import sys


def main():
    os.system(
        'python step01_setup.py'
    )
    os.system(
        'python step02_setup.py'
    )
    os.system(
        'python step03_setup.py'
    )
    os.system(
        'python step04_setup.py'
    )
    os.system(
        'python step05_setup.py'
    )
    os.system(
        'python step06_setup.py'
    )
    os.system(
        'python step07_setup.py'
    )


if __name__ == '__main__':
    sys.exit(main())

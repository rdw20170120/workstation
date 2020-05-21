#!/usr/bin/env python

"""
answer.py will do the following tasks:

1. Creates a file
"""

import sys
from certtools import args_parse, debug


class Q():
    args = args_parse(args=sys.argv)
    file_name = args.seg1


def main():
    # Creating file
    with open(Q.file_name, 'w') as f:
        f.write('EI000\n')
    debug('File Created')


if __name__ == '__main__':
    sys.exit(main())

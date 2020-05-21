#!/usr/bin/env python

"""
setup.py will do the following tasks:

1. Creates a directory if not exists.
2. Deletes the file if exists.
"""

import os
import sys
from certtools import args_parse, debug


class Q():
    args = args_parse(args=sys.argv)
    file_name = args.seg1


def main():
    dir = os.path.dirname(Q.file_name)
    # Creating folder if not exist
    if not os.path.exists(dir):
        os.makedirs(dir)
        debug('Folder created')
    # Deleting file if exists
    elif os.path.exists(Q.file_name):
        os.remove(Q.file_name)
        debug('File removed')


if __name__ == '__main__':
    sys.exit(main())

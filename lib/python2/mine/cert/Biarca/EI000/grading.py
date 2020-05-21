#!/usr/bin/env python

"""
grading.py will do the following tasks:

1. Checks for the file existence.
"""

import sys
from certtools import args_parse
from certtools.couchbase.utils import common, checks


class Q():
    args = args_parse(args=sys.argv)
    file_name = args.seg1


def main():
    # Checking the file existence.
    score, msg = checks.ck000(Q.file_name)
    common.score_check(score, "CK000", msg)


if __name__ == '__main__':
    sys.exit(main())

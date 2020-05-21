#!/usr/bin/env python

import sys
import argparse


def args_parse(args):
    parser = argparse.ArgumentParser()
    if not args[0].startswith('--'):
        keys = args[1:]

    args = [key.split('=')[0] for key in keys]
    [parser.add_argument(a) for a in args]
    return parser.parse_args(keys)


def debug(msg):
    args = args_parse(args=sys.argv)
    if hasattr(args, 'debug') and args.debug in ['y', '1', 'true']:
        print(msg)


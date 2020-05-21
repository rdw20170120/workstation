''' generator support functionality
'''

# TODO:  import itertools
import sys

from project_euler.solution.math import is_even

_pseudo_infinite_range_limit = sys.maxsize

# TODO:  FIX:  Despite use of generators, it seems that I am instantiating the
# full pseudo-infinite sequence in some cases.  This consumes massive RAM, and
# could easily crash the host.  A lesser limit of about 300,000 items seems to
# consume about half of my physical RAM (1/2 of 8 GB = 4 GB).  That is enough
# to notice, but not enough to actually impair my machine.
_pseudo_infinite_range_limit = 300000

def even(items):
    '''Return the "items" that have even values (a multiple of 2).'''
    return (i for i in items if is_even(i))

def infinite(start=0):
    '''Return an infinite counting sequence, optionally starting at "start".
    '''
    # TODO:  return itertools.count(start)
    return pseudo_infinite(start)

def pseudo_infinite(start=0):
    '''Return a pseudo-infinite sequence, optionally starting at "start".
    
       Real length of sequence is subject to Python limits.
    '''
    return range(start, _pseudo_infinite_range_limit)

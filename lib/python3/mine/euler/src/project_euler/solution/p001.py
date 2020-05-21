''' Project Euler Problem 1 solution elements'''

from project_euler.solution.math import is_multiple_of

def is_desired_multiple(natural):
    '''Is "natural" number a desired multiple (of 3 or 5)?'''
    if 0 == natural:
        return False
    else:
        return is_multiple_of(3, natural) or is_multiple_of(5, natural)

def desired_multiples_below(natural):
    '''Return the desired multiples below the "natural" number.'''
    return [n for n in range(natural) if is_desired_multiple(n)]

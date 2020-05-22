''' math support functionality
'''

def is_even(value):
    '''Is "value" even (a multiple of 2)?'''
    return 0 == value % 2

def is_multiple_of(small, natural):
    '''Is "natural" number a multiple of "small"?'''
    return True if 0 == natural else 0 == natural % small

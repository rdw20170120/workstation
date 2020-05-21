''' math tests
'''

import nose.tools

from project_euler.solution.math import is_even
from project_euler.solution.math import is_multiple_of

def test_is_even():
    '''Test is_even().'''
    nose.tools.ok_(    is_even(0))
    nose.tools.ok_(not is_even(1))
    nose.tools.ok_(    is_even(2))
    nose.tools.ok_(not is_even(3))
    nose.tools.ok_(    is_even(4))

def test_is_multiple_of_three():
    '''Test given definition of multiples of three.'''
    nose.tools.ok_(    is_multiple_of(3, 0))
    nose.tools.ok_(not is_multiple_of(3, 1))
    nose.tools.ok_(not is_multiple_of(3, 2))
    nose.tools.ok_(    is_multiple_of(3, 3))
    nose.tools.ok_(not is_multiple_of(3, 4))
    nose.tools.ok_(not is_multiple_of(3, 5))
    nose.tools.ok_(    is_multiple_of(3, 6))
    nose.tools.ok_(not is_multiple_of(3, 7))
    nose.tools.ok_(not is_multiple_of(3, 8))
    nose.tools.ok_(    is_multiple_of(3, 9))

def test_is_multiple_of_five():
    '''Test given definition of multiples of five.'''
    nose.tools.ok_(    is_multiple_of(5, 0))
    nose.tools.ok_(not is_multiple_of(5, 1))
    nose.tools.ok_(not is_multiple_of(5, 2))
    nose.tools.ok_(not is_multiple_of(5, 3))
    nose.tools.ok_(not is_multiple_of(5, 4))
    nose.tools.ok_(    is_multiple_of(5, 5))
    nose.tools.ok_(not is_multiple_of(5, 6))
    nose.tools.ok_(not is_multiple_of(5, 7))
    nose.tools.ok_(not is_multiple_of(5, 8))
    nose.tools.ok_(not is_multiple_of(5, 9))

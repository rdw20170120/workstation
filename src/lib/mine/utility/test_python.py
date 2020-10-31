#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
import keyword
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.my_assert import assert_equal
from utility.my_assert import assert_in
# Co-located modules (relative references, NOT packaged, in project)


def test_kwlist():
    # For Python 3.6.9
    assert assert_equal(len(keyword.kwlist), 33)
    assert assert_in('False', keyword.kwlist)
    assert assert_in('None', keyword.kwlist)
    assert assert_in('True', keyword.kwlist)
    assert assert_in('and', keyword.kwlist)
    assert assert_in('as', keyword.kwlist)
    assert assert_in('assert', keyword.kwlist)
    assert assert_in('break', keyword.kwlist)
    assert assert_in('class', keyword.kwlist)
    assert assert_in('continue', keyword.kwlist)
    assert assert_in('def', keyword.kwlist)
    assert assert_in('del', keyword.kwlist)
    assert assert_in('elif', keyword.kwlist)
    assert assert_in('else', keyword.kwlist)
    assert assert_in('except', keyword.kwlist)
    assert assert_in('finally', keyword.kwlist)
    assert assert_in('for', keyword.kwlist)
    assert assert_in('from', keyword.kwlist)
    assert assert_in('global', keyword.kwlist)
    assert assert_in('if', keyword.kwlist)
    assert assert_in('import', keyword.kwlist)
    assert assert_in('in', keyword.kwlist)
    assert assert_in('is', keyword.kwlist)
    assert assert_in('lambda', keyword.kwlist)
    assert assert_in('nonlocal', keyword.kwlist)
    assert assert_in('not', keyword.kwlist)
    assert assert_in('or', keyword.kwlist)
    assert assert_in('pass', keyword.kwlist)
    assert assert_in('raise', keyword.kwlist)
    assert assert_in('return', keyword.kwlist)
    assert assert_in('try', keyword.kwlist)
    assert assert_in('while', keyword.kwlist)
    assert assert_in('with', keyword.kwlist)
    assert assert_in('yield', keyword.kwlist)

'''DisabledContent
'''


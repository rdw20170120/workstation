#!/usr/bin/env false
"""TODO: Write

TODO: Generate tests
NOTE: There is little value in testing "composed" methods,
e.g., those consisting of 'return [...]'.
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises
# Library modules    (absolute references, NOT packaged, in project)
from utility.my_assert import assert_equal
# Co-located modules (relative references, NOT packaged, in project)
from .renderer import Renderer
from .source import my_visitor_map
from .structure import *


s = Renderer(my_visitor_map)._serialize

will_squash = (None, '', (), [])
wont_squash = (False, True, 0, 0.0, 0j, ' ', 'Test', {})

def test_bt():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(bt()), '``')
    assert assert_equal(s(bt(None)), '``')
    assert assert_equal(s(bt('')), '``')
    assert assert_equal(s(bt('Test')), '`Test`')
    assert assert_equal(s(bt('Test', '123')), '`Test123`')

def test_dq():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(dq()), '""')
    assert assert_equal(s(dq(None)), '""')
    assert assert_equal(s(dq('')), '""')
    assert assert_equal(s(dq('Test')), '"Test"')
    assert assert_equal(s(dq('Test', '123')), '"Test123"')

def test_eol():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(eol()), '\n')
    with raises(TypeError): eol(None)

def test_line():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(line()), '\n')
    assert assert_equal(s(line(None)), '\n')
    assert assert_equal(s(line('Test')), 'Test\n')

def test_sq():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(sq()), "''")
    assert assert_equal(s(sq(None)), "''")
    assert assert_equal(s(sq('')), "''")
    assert assert_equal(s(sq('Test')), "'Test'")
    assert assert_equal(s(sq('Test', '123')), "'Test123'")

def test_squashed_01():
    assert assert_equal(squashed(False), False)

def test_squashed_02():
    assert assert_equal(squashed(True), True)

def test_squashed_03():
    assert assert_equal(squashed(0), 0)

def test_squashed_04():
    assert assert_equal(squashed(0.0), 0.0)

def test_squashed_05():
    assert assert_equal(squashed(0j), 0j)

def test_squashed_06():
    assert assert_equal(squashed(' '), ' ')

def test_squashed_07():
    assert assert_equal(squashed('Test'), 'Test')

def test_squashed_08():
    assert assert_equal(squashed({}), {})

def test_squashed_09():
    assert assert_equal(squashed(None), None)

def test_squashed_10():
    assert assert_equal(squashed(''), None)

def test_squashed_11():
    assert assert_equal(squashed(()), None)

def test_squashed_12():
    assert assert_equal(squashed((None)), None)

def test_squashed_13():
    assert assert_equal(squashed((None, )), None)

def test_squashed_14():
    assert assert_equal(squashed((None, None)), None)

def test_squashed_15():
    assert assert_equal(squashed([None]), None)

def test_squashed_16():
    assert assert_equal(squashed([None, None]), None)

def test_squashed_17():
    for i in will_squash:
        for j in wont_squash:
            assert assert_equal(squashed((i, j)), j)
            assert assert_equal(squashed([i, j]), j)

def test_squashed_18():
    for i in wont_squash:
        for j in will_squash:
            assert assert_equal(squashed((i, j)), i)
            assert assert_equal(squashed([i, j]), i)

'''DisabledContent
'''


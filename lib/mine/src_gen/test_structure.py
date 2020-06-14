#!/usr/bin/env false
"""
"""
from pytest import raises

from .source    import visitor_map
from .structure import * 
from .renderer  import Renderer


# NOTE: There is little value in testing "composed" methods,
# e.g., those consisting of 'return [...]'.
# TODO: Generate tests

s = Renderer(visitor_map)._serialize

will_squash = (None, '', (), [])
wont_squash = (False, True, 0, 0.0, 0j, ' ', 'Test', {})

def test_bt():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert s(bt()) == '``'
    assert s(bt(None)) == '``'
    assert s(bt('')) == '``'
    assert s(bt('Test')) == '`Test`'
    assert s(bt('Test', '123')) == '`Test123`'

def test_dq():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert s(dq()) == '""'
    assert s(dq(None)) == '""'
    assert s(dq('')) == '""'
    assert s(dq('Test')) == '"Test"'
    assert s(dq('Test', '123')) == '"Test123"'

def test_eol():
    # TODO: Break up tests into individual test methods
    assert s(eol()) == '\n'
    with raises(TypeError): eol(None)

def test_line():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert s(line()) == '\n'
    assert s(line(None)) == '\n'
    assert s(line('Test')) == 'Test\n'

def test_sq():
    # TODO: Expand tests for full pattern
    # TODO: Break up tests into individual test methods
    assert s(sq()) == "''"
    assert s(sq(None)) == "''"
    assert s(sq('')) == "''"
    assert s(sq('Test')) == "'Test'"
    assert s(sq('Test', '123')) == "'Test123'"

def test_squashed_01():
    assert squashed(False) is False

def test_squashed_02():
    assert squashed(True) is True

def test_squashed_03():
    assert squashed(0) == 0

def test_squashed_04():
    assert squashed(0.0) == 0.0

def test_squashed_05():
    assert squashed(0j) == 0j

def test_squashed_06():
    assert squashed(' ') == ' '

def test_squashed_07():
    assert squashed('Test') == 'Test'

def test_squashed_08():
    assert squashed({}) == {}

def test_squashed_09():
    assert squashed(None) is None

def test_squashed_10():
    assert squashed('') is None

def test_squashed_11():
    assert squashed(()) is None

def test_squashed_12():
    assert squashed((None)) is None

def test_squashed_13():
    assert squashed((None, )) is None

def test_squashed_14():
    assert squashed((None, None)) is None

def test_squashed_15():
    assert squashed([None]) is None

def test_squashed_16():
    assert squashed([None, None]) is None

def test_squashed_17():
    for i in will_squash:
        for j in wont_squash:
            assert squashed((i, j)) == j
            assert squashed([i, j]) == j

def test_squashed_18():
    for i in wont_squash:
        for j in will_squash:
            assert squashed((i, j)) == i
            assert squashed([i, j]) == i

'''DisabledContent
'''


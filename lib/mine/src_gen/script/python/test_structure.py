#!/usr/bin/env false
"""
"""
from pytest import raises

from ...renderer import Renderer
from ..source    import visitor_map
from ..structure import * 


# NOTE: There is little value in testing "composed" methods,
# e.g., those consisting of 'return [...]'.
# TODO: Generate tests
# TODO: Expand tests for full pattern

s = Renderer(visitor_map)._serialize

def test_command_01():
    assert s(command('Test')) == 'Test'

def test_command_02():
    assert s(command('Test', None)) == 'Test'

def test_command_03():
    assert s(command('Test', '')) == 'Test'

def test_command_04():
    assert s(command('Test', '123')) == 'Test 123'

def test_comment_01():
    assert s(comment()) == '#\n'

def test_comment_02():
    assert s(comment(None)) == '#\n'

def test_comment_03():
    assert s(comment('')) == '#\n'

def test_comment_04():
    assert s(comment('Test')) == '# Test\n'

def test_comment_05():
    assert s(comment('Test', None)) == '# Test\n'

def test_comment_06():
    assert s(comment('Test', '')) == '# Test\n'

def test_comment_06():
    assert s(comment('Test', '123')) == '# Test123\n'

def test_shebang_cat():
    assert s(shebang_cat()) == '#!/usr/bin/env cat\n'

def test_shebang_false():
    assert s(shebang_false()) == '#!/usr/bin/env false\n'

def test_shebang_thru_env_01():
    with raises(AssertionError):
        shebang_thru_env(None)

def test_shebang_thru_env_02():
    with raises(AssertionError):
        shebang_thru_env('')

def test_shebang_thru_env_03():
    assert s(shebang_thru_env('Test')) == '#!/usr/bin/env Test\n'

'''DisabledContent
'''


#!/usr/bin/env false
"""TODO: Write

TODO: Generate tests
TODO: Expand tests for full pattern
NOTE: There is little value in testing "composed" methods,
e.g., those consisting of 'return [...]'.
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises
# Library modules    (absolute references, NOT packaged, in project)
from utility import my_assert as is_
# Co-located modules (relative references, NOT packaged, in project)
from ...renderer import Renderer
from ..source import my_visitor_map
from ..structure import * 


s = Renderer(my_visitor_map)._serialize

def test_command_01():
    assert is_.equal(s(command('Test')), 'Test')

def test_command_02():
    assert is_.equal(s(command('Test', None)), 'Test')

def test_command_03():
    assert is_.equal(s(command('Test', '')), 'Test')

def test_command_04():
    assert is_.equal(s(command('Test', '123')), 'Test 123')

def test_comment_01():
    assert is_.equal(s(comment()), '#\n')

def test_comment_02():
    assert is_.equal(s(comment(None)), '#\n')

def test_comment_03():
    assert is_.equal(s(comment('')), '#\n')

def test_comment_04():
    assert is_.equal(s(comment('Test')), '# Test\n')

def test_comment_05():
    assert is_.equal(s(comment('Test', None)), '# Test\n')

def test_comment_06():
    assert is_.equal(s(comment('Test', '')), '# Test\n')

def test_comment_06():
    assert is_.equal(s(comment('Test', '123')), '# Test123\n')

def test_shebang_cat():
    assert is_.equal(s(shebang_cat()), '#!/usr/bin/env cat\n')

def test_shebang_false():
    assert is_.equal(s(shebang_false()), '#!/usr/bin/env false\n')

def test_shebang_thru_env_01():
    with raises(AssertionError): shebang_thru_env(None)

def test_shebang_thru_env_02():
    assert is_.equal(s(shebang_thru_env('')), '#!/usr/bin/env\n')

def test_shebang_thru_env_03():
    assert is_.equal(s(shebang_thru_env('Test')), '#!/usr/bin/env Test\n')

'''DisabledContent
'''


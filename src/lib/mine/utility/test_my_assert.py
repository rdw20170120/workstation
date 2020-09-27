#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises
# Library modules    (absolute references, NOT packaged, in project)
from utility.my_assert import assert_absolute_directory
from utility.my_assert import assert_absolute_file
from utility.my_assert import assert_absolute_path
from utility.my_assert import assert_equal
from utility.my_assert import assert_existing_absolute_path
from utility.my_assert import assert_instance
from utility.my_assert import assert_not_instance
# Co-located modules (relative references, NOT packaged, in project)


this_file = Path(__file__)
this_directory = this_file.parent

def test_assert_absolute_directory():
    assert assert_absolute_directory(this_directory)
    with raises(AssertionError):
        assert assert_absolute_directory(this_file)

def test_assert_absolute_file():
    with raises(AssertionError):
        assert assert_absolute_file(this_directory)
    assert assert_absolute_file(this_file)

def test_assert_absolute_path():
    assert assert_absolute_path(this_directory)
    assert assert_absolute_path(this_file)

def test_assert_equal():
    assert assert_equal(None, None)
    assert assert_equal('', '')
    assert assert_equal('Test', 'Test')

def test_assert_existing_absolute_path():
    assert assert_existing_absolute_path(this_directory)
    assert assert_existing_absolute_path(this_file)

def test_assert_instance():
    assert assert_instance(None, type(None))

    with raises(AssertionError) as info:
        assert assert_instance(None, str)
    a = str(info.value)
    assert "Value is None" in a
    assert "<class 'str'>" in a

    assert assert_instance('', str)

    assert assert_instance(None, (type(None), str))
    assert assert_instance('', (type(None), str))
    assert assert_instance('Test', (type(None), str))

def test_assert_not_instance():
    assert assert_not_instance(None, str)
    assert assert_not_instance(None, (bool, float, int, str))

'''DisabledContent
'''


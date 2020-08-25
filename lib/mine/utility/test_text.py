#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.my_assert import assert_equal
from utility.text import dict_from_string
from utility.text import string_without_prefix
from utility.text import string_without_suffix
# Co-located modules (relative references, NOT packaged, in project)


def test_dict_from_string():
    # TODO: Test with other basic data types in list
    the_dict = {
        'first': -1.0, 'second': -1, 'third': 0, 'fourth': 1, 'fifth': 1.0,
        'sixth': False, 'seventh': True,
        'eighth': None,
        'ninth': '', 'tenth': 'test'
        }
    the_string = str(the_dict)
    assert assert_equal(dict_from_string(the_string), the_dict)

def test_string_without_prefix_for_all_none():
    assert assert_equal(string_without_prefix(None, None), None)

def test_string_without_prefix_for_empty_prefix():
    assert assert_equal(string_without_prefix('empty prefix', ''), 'empty prefix')

def test_string_without_prefix_for_empty_string():
    assert assert_equal(string_without_prefix('', 'empty string'), '')

def test_string_without_prefix_for_none_prefix():
    assert assert_equal(string_without_prefix('none prefix', None), 'none prefix')

def test_string_without_prefix_for_none_string():
    assert assert_equal(string_without_prefix(None, 'none string'), None)

def test_string_without_prefix_having_prefix():
    assert assert_equal(string_without_prefix('prefix on string', 'prefix'), ' on string')

def test_string_without_prefix_missing_prefix():
    assert assert_equal(string_without_prefix('missing prefix on string', 'prefix'), 'missing prefix on string')

def test_string_without_suffix_for_all_none():
    assert assert_equal(string_without_suffix(None, None), None)

def test_string_without_suffix_for_empty_suffix():
    assert assert_equal(string_without_suffix('empty suffix', ''), 'empty suffix')

def test_string_without_suffix_for_empty_string():
    assert assert_equal(string_without_suffix('', 'empty string'), '')

def test_string_without_suffix_for_none_suffix():
    assert assert_equal(string_without_suffix('none suffix', None), 'none suffix')

def test_string_without_suffix_for_none_string():
    assert assert_equal(string_without_suffix(None, 'none string'), None)

def test_string_without_suffix_having_suffix():
    assert assert_equal(string_without_suffix('string having suffix', 'suffix'), 'string having ')

def test_string_without_suffix_missing_suffix():
    assert assert_equal(string_without_suffix('missing suffix on string', 'suffix'), 'missing suffix on string')

'''DisabledContent
'''


#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility import my_assert as is_
from utility.text import dict_from_string
from utility.text import replace_last
from utility.text import string_without_prefix
from utility.text import string_without_suffix
# Co-located modules (relative references, NOT packaged, in project)


def test_dict_from_string():
    # TODO: Test with other basic data types
    the_dict = {
        'first': -1.0, 'second': -1, 'third': 0, 'fourth': 1, 'fifth': 1.0,
        'sixth': False, 'seventh': True,
        'eighth': None,
        'ninth': '', 'tenth': 'test'
        }
    the_string = str(the_dict)
    assert is_.equal(dict_from_string(the_string), the_dict)

def test_replace_last():
    assert is_.equal(replace_last(None, None, None), None)
    assert is_.equal(replace_last(None, '', None), None)
    assert is_.equal(replace_last(None, 'Test', None), None)
    assert is_.equal(replace_last('', None, None), '')
    assert is_.equal(replace_last('', '', None), '')
    assert is_.equal(replace_last('', 'Test', None), '')
    assert is_.equal(replace_last('Test', None, None), 'Test')
    assert is_.equal(replace_last('Test', '', None), 'Test')
    assert is_.equal(replace_last('Test', 'Test', None), '')
    assert is_.equal(replace_last('Test', 'T', 'Z'), 'Zest')
    assert is_.equal(replace_last('Test', 's', 'x'), 'Text')
    assert is_.equal(replace_last('Test', 't', 's'), 'Tess')
    assert is_.equal(replace_last('Test', 'Te', 'Li'), 'List')
    assert is_.equal(replace_last('Test', 'es', 'ha'), 'That')
    assert is_.equal(replace_last('Test', 'st', 'es'), 'Tees')

def test_string_without_prefix_for_all_none():
    assert is_.equal(string_without_prefix(None, None), None)

def test_string_without_prefix_for_empty_prefix():
    assert is_.equal(string_without_prefix('empty prefix', ''), 'empty prefix')

def test_string_without_prefix_for_empty_string():
    assert is_.equal(string_without_prefix('', 'empty string'), '')

def test_string_without_prefix_for_none_prefix():
    assert is_.equal(string_without_prefix('none prefix', None), 'none prefix')

def test_string_without_prefix_for_none_string():
    assert is_.equal(string_without_prefix(None, 'none string'), None)

def test_string_without_prefix_having_prefix():
    assert is_.equal(string_without_prefix('prefix on string', 'prefix'), ' on string')

def test_string_without_prefix_missing_prefix():
    assert is_.equal(string_without_prefix('missing prefix on string', 'prefix'), 'missing prefix on string')

def test_string_without_suffix_for_all_none():
    assert is_.equal(string_without_suffix(None, None), None)

def test_string_without_suffix_for_empty_suffix():
    assert is_.equal(string_without_suffix('empty suffix', ''), 'empty suffix')

def test_string_without_suffix_for_empty_string():
    assert is_.equal(string_without_suffix('', 'empty string'), '')

def test_string_without_suffix_for_none_suffix():
    assert is_.equal(string_without_suffix('none suffix', None), 'none suffix')

def test_string_without_suffix_for_none_string():
    assert is_.equal(string_without_suffix(None, 'none string'), None)

def test_string_without_suffix_having_suffix():
    assert is_.equal(string_without_suffix('string having suffix', 'suffix'), 'string having ')

def test_string_without_suffix_missing_suffix():
    assert is_.equal(string_without_suffix('missing suffix on string', 'suffix'), 'missing suffix on string')

'''DisabledContent
'''


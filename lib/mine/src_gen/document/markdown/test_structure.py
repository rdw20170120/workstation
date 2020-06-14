#!/usr/bin/env false
"""
"""
from pytest import raises

from .source     import visitor_map
from .structure  import * 
from ...renderer import Renderer


# NOTE: There is little value in testing "composed" methods,
# e.g., those consisting of 'return [...]'.
# TODO: Generate tests

s = Renderer(visitor_map)._serialize

def test_header():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): header()
    with raises(AssertionError): header(None)
    with raises(AssertionError): header('')
    assert s(header('Test')) == '# Test\n'
    with raises(TypeError): header('Test', None)
    with raises(TypeError): header('Test', '')
    with raises(TypeError): header('Test', '123')
    with raises(TypeError): header('Test', level=None)
    with raises(TypeError): header('Test', level='')
    with raises(TypeError): header('Test', level='123')
    with raises(AssertionError): header('Test', level=0)
    assert s(header('Test', level=6)) == '###### Test\n'
    with raises(AssertionError): header('Test', level=7)

def test_h1():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): h1()
    with raises(AssertionError): h1(None)
    with raises(AssertionError): h1('')
    assert s(h1('Test')) == '# Test\n'
    with raises(TypeError): h1('Test', None)

def test_h2():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): h2()
    with raises(AssertionError): h2(None)
    with raises(AssertionError): h2('')
    assert s(h2('Test')) == '## Test\n'
    with raises(TypeError): h2('Test', None)

def test_numbered_list_item():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): numbered_list_item()
    with raises(AssertionError): numbered_list_item(None)
    with raises(AssertionError): numbered_list_item('')
    assert s(numbered_list_item('Test')) == '1. Test\n'
    with raises(TypeError): numbered_list_item('Test', None)
    with raises(TypeError): numbered_list_item('Test', '')
    with raises(TypeError): numbered_list_item('Test', '123')
    with raises(AssertionError): numbered_list_item('Test', level=-1)
    assert s(numbered_list_item('Test', level=9)) == 9 * 3 * ' ' + '1. Test\n'
    with raises(AssertionError): numbered_list_item('Test', level=10)

def test_nli0():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): nli0()
    with raises(AssertionError): nli0(None)
    with raises(AssertionError): nli0('')
    assert s(nli0('Test')) == '1. Test\n'
    with raises(TypeError): nli0('Test', None)

def test_note():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        note()
    with raises(AssertionError):
        note(None)
    with raises(AssertionError):
        note('')
    assert s(note('Test')) == 'NOTE: Test\n'
    with raises(TypeError):
        note('Test', None)

def test_table_header():
    # TODO: Break up tests into individual test methods
    with raises(AssertionError): table_header()
    with raises(AssertionError): table_header(None)
    with raises(AssertionError): table_header('')
    assert s(table_header('Test')) == '|Test|\n'
    assert s(table_header('Test', None)) == '|Test|\n'
    assert s(table_header('Test', '')) == '|Test|\n'
    assert s(table_header('Test', '123')) == '|Test|123|\n'

def test_table_row():
    # TODO: Break up tests into individual test methods
    with raises(AssertionError): table_row()
    with raises(AssertionError): table_row(None)
    with raises(AssertionError): table_row('')
    assert s(table_row('Test')) == '|Test|\n'
    assert s(table_row('Test', None)) == '|Test|\n'
    assert s(table_row('Test', '')) == '|Test|\n'
    assert s(table_row('Test', '123')) == '|Test|123|\n'

def test_table_ruler():
    # TODO: Break up tests into individual test methods
    with raises(AssertionError): table_ruler()
    with raises(AssertionError): table_ruler(None)
    with raises(AssertionError): table_ruler('')
    assert s(table_ruler('Test')) == '|Test|\n'
    assert s(table_ruler('Test', None)) == '|Test|\n'
    assert s(table_ruler('Test', '')) == '|Test|\n'
    assert s(table_ruler('Test', '123')) == '|Test|123|\n'

'''DisabledContent
'''


#!/bin/false

from pathlib import Path

from .filesystem import file_name_has_extension
from .filesystem import file_name_has_suffix
from .filesystem import split_file_name

def test_file_name_has_extension():
    assert not file_name_has_extension('name', '.ext')
    assert file_name_has_extension('name.ext', '.ext')
    assert not file_name_has_extension(Path('name'), '.ext')
    assert file_name_has_extension(Path('name.ext'), '.ext')

def test_file_name_has_suffix():
    assert not file_name_has_suffix('name', '.ext')
    assert file_name_has_suffix('name.ext', '.ext')
    assert not file_name_has_suffix(Path('name'), '.ext')
    assert file_name_has_suffix(Path('name.ext'), '.ext')
    assert file_name_has_suffix(Path('name-stuff.ext'), '-stuff.ext')

def test_split_file_name_having_double_extension():
    n, e = split_file_name('name.zzz.ext')
    assert n == 'name'
    assert e == '.zzz.ext'

def test_split_file_name_having_extension():
    n, e = split_file_name('name.ext')
    assert n == 'name'
    assert e == '.ext'

def test_split_file_name_missing_extension():
    n, e = split_file_name('name')
    assert n == 'name'
    assert e == ''


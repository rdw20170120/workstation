#!/bin/false

from pathlib import Path

from .filesystem import name_has_extension
from .filesystem import split_file_name

def test_name_has_extension():
    assert not name_has_extension('name', '.ext')
    assert name_has_extension('name.ext', '.ext')
    assert not name_has_extension(Path('name'), '.ext')
    assert name_has_extension(Path('name.ext'), '.ext')

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


#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .filesystem import basename_has_suffix
from .filesystem import split_basename
from .filesystem import split_pathname


def test_basename_has_suffix():
    assert not basename_has_suffix('name', '.ext')
    assert basename_has_suffix('name.ext', '.ext')
    assert not basename_has_suffix(Path('name'), '.ext')
    assert basename_has_suffix(Path('name.ext'), '.ext')
    assert basename_has_suffix(Path('name-stuff.ext'), '-stuff.ext')

def test_split_basename():
    n, e = split_basename('name')
    assert n == 'name'
    assert e == ''

    n, e = split_basename('name.ext')
    assert n == 'name'
    assert e == '.ext'

    n, e = split_basename('name.zzz.ext')
    assert n == 'name'
    assert e == '.zzz.ext'

def test_split_pathname():
    p, b = split_pathname('')
    assert p == Path('.')
    assert b == ''

    p, b = split_pathname('a/b/c')
    assert p == Path('a/b')
    assert b == 'c'

    p, b = split_pathname('a/b/c/name.ext')
    assert p == Path('a/b/c')
    assert b == 'name.ext'

'''DisabledContent
'''


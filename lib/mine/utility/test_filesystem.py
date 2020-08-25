#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.filesystem import basename_has_suffix
from utility.filesystem import split_basename
from utility.filesystem import split_pathname
from utility.my_assert import assert_equal
from utility.my_assert import assert_false
from utility.my_assert import assert_true
# Co-located modules (relative references, NOT packaged, in project)


def test_basename_has_suffix():
    assert assert_false(basename_has_suffix('name', '.ext'))
    assert assert_true(basename_has_suffix('name.ext', '.ext'))
    assert assert_false(basename_has_suffix(Path('name'), '.ext'))
    assert assert_true(basename_has_suffix(Path('name.ext'), '.ext'))
    assert assert_true(basename_has_suffix(Path('name-stuff.ext'), '-stuff.ext'))

def test_split_basename():
    n, e = split_basename('name')
    assert assert_equal(n, 'name')
    assert assert_equal(e, '')

    n, e = split_basename('name.ext')
    assert assert_equal(n, 'name')
    assert assert_equal(e, '.ext')

    n, e = split_basename('name.zzz.ext')
    assert assert_equal(n, 'name')
    assert assert_equal(e, '.zzz.ext')

def test_split_pathname():
    p, b = split_pathname('')
    assert assert_equal(p, Path('.'))
    assert assert_equal(b, '')

    p, b = split_pathname('a/b/c')
    assert assert_equal(p, Path('a/b'))
    assert assert_equal(b, 'c')

    p, b = split_pathname('a/b/c/name.ext')
    assert assert_equal(p, Path('a/b/c'))
    assert assert_equal(b, 'name.ext')

'''DisabledContent
'''


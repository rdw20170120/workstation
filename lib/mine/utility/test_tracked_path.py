#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
from pathlib import PosixPath
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .tracked_path import TrackedPath


def test_path():
    assert Path() is not None
    with raises(TypeError):
        Path(None)

    a = Path('')
    assert a is not None
    assert a.__fspath__() == '.'
    assert repr(a) == "PosixPath('.')"
    assert str(a) == '.'
    assert not a.is_absolute()

    a = Path('Test')
    assert a is not None
    assert a.__fspath__() == 'Test'
    assert repr(a) == "PosixPath('Test')"
    assert str(a) == 'Test'
    assert not a.is_absolute()

    a = Path('/Test')
    assert a is not None
    assert a.__fspath__() == '/Test'
    assert repr(a) == "PosixPath('/Test')"
    assert str(a) == '/Test'
    assert a.is_absolute()

    b = a / Path('123')
    assert b is not None
    assert b.__fspath__() == '/Test/123'
    assert repr(b) == "PosixPath('/Test/123')"
    assert str(b) == '/Test/123'
    assert b.is_absolute()

def test_tracked_path():
    with raises(TypeError):
        TrackedPath()
    with raises(TypeError):
        TrackedPath(None)
    with raises(AssertionError):
        TrackedPath(None, None)
    with raises(AssertionError):
        TrackedPath(None, None, None)
    with raises(AssertionError):
        TrackedPath('Test', 'Test', 'Test')
    with raises(AssertionError):
        TrackedPath('Test', 'Test', Path())
    with raises(AssertionError):
        TrackedPath('Test', Path(), 'Test')
    with raises(AssertionError):
        TrackedPath('Test', Path(), Path())
    with raises(AssertionError):
        TrackedPath('Test', '123', 'abc')

    a = TrackedPath('Test', '/123')
    assert a is not None
    assert a == PosixPath('/123')
    assert a.__fspath__() == '/123'
    assert (repr(a)
        == "TrackedPath('Test', PosixPath('/123'), PosixPath('.'))")
    assert str(a) == "Test '.'"

    b = TrackedPath('Test', '/123', 'abc')
    assert b is not None
    assert b == PosixPath('/123/abc')
    assert b.__fspath__() == '/123/abc'
    assert (repr(b)
        == "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))")
    assert str(b) == "Test 'abc'"

    c = Path('/123/abc/xyz')
    d = b.for_path(c)
    assert d is not None
    assert d == PosixPath('/123/abc/xyz')
    assert d.__fspath__() == '/123/abc/xyz'
    assert (repr(d)
        == "TrackedPath('Test', PosixPath('/123'), PosixPath('abc/xyz'))")
    assert str(d) == "Test 'abc/xyz'"

    e = d / 'def.ghi'
    assert e is not None
    assert e == PosixPath('/123/abc/xyz/def.ghi')
    assert e.__fspath__() == '/123/abc/xyz/def.ghi'
    assert (repr(e) ==
        "TrackedPath('Test', PosixPath('/123'), PosixPath('abc/xyz/def.ghi'))")
    assert str(e) == "Test 'abc/xyz/def.ghi'"

'''DisabledContent
'''


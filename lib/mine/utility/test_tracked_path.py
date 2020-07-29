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
    assert str(a) == a.__fspath__()
    assert a.for_log() == "Test '.'"
    assert a.top == a
    assert a.subpath == Path('.')
    assert a.basename == ''

    b = TrackedPath('Test', '/123', 'abc')
    assert b is not None
    assert b == PosixPath('/123/abc')
    assert b.__fspath__() == '/123/abc'
    assert (repr(b)
        == "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))")
    assert str(b) == b.__fspath__()
    assert b.for_log() == "Test 'abc'"
    assert b.top == a
    assert b.subpath == Path('.')
    assert b.basename == 'abc'

    c = Path('/123/abc/xyz')
    d = b.for_path(c)
    assert d is not None
    assert d == PosixPath('/123/abc/xyz')
    assert d.__fspath__() == '/123/abc/xyz'
    assert (repr(d)
        == "TrackedPath('Test', PosixPath('/123'), PosixPath('abc/xyz'))")
    assert str(d) == d.__fspath__()
    assert d.for_log() == "Test 'abc/xyz'"
    assert d.top == a
    assert d.subpath == Path('abc')
    assert d.basename == 'xyz'

    e = d / 'def.ghi'
    assert e is not None
    assert e == PosixPath('/123/abc/xyz/def.ghi')
    assert e.__fspath__() == '/123/abc/xyz/def.ghi'
    assert (repr(e) ==
        "TrackedPath('Test', PosixPath('/123'), PosixPath('abc/xyz/def.ghi'))")
    assert str(e) == e.__fspath__()
    assert e.for_log() == "Test 'abc/xyz/def.ghi'"
    assert e.top == a
    assert e.subpath == Path('abc/xyz')
    assert e.basename == 'def.ghi'

    f = b / None
    assert f is not None
    assert f == PosixPath('/123/abc')
    assert f.__fspath__() == '/123/abc'
    assert (repr(f) ==
        "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))")
    assert str(f) == f.__fspath__()
    assert f.for_log() == "Test 'abc'"
    assert f.top == a
    assert f.subpath == Path()
    assert f.basename == 'abc'

    g = b / ''
    assert g is not None
    assert g == PosixPath('/123/abc')
    assert g.__fspath__() == '/123/abc'
    assert (repr(g) ==
        "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))")
    assert str(g) == g.__fspath__()
    assert g.for_log() == "Test 'abc'"
    assert g.top == a
    assert g.subpath == Path()
    assert g.basename == 'abc'

    h = b / Path()
    assert h is not None
    assert h == PosixPath('/123/abc')
    assert h.__fspath__() == '/123/abc'
    assert (repr(h) ==
        "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))")
    assert str(h) == h.__fspath__()
    assert h.for_log() == "Test 'abc'"
    assert h.top == a
    assert h.subpath == Path()
    assert h.basename == 'abc'

'''DisabledContent
'''


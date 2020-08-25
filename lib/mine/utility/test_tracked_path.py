#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
from pathlib import PosixPath
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises
# Library modules    (absolute references, NOT packaged, in project)
from utility.my_assert import assert_equal
from utility.my_assert import assert_absolute_path
from utility.my_assert import assert_relative_path
from utility.my_assert import assert_not_none
from utility.tracked_path import TrackedPath
# Co-located modules (relative references, NOT packaged, in project)


def test_path():
    assert assert_not_none(Path())
    with raises(TypeError): Path(None)

    a = Path('')
    assert assert_not_none(a)
    assert assert_equal(a.__fspath__(), '.')
    assert assert_equal(repr(a), "PosixPath('.')")
    assert assert_equal(str(a), '.')
    assert assert_relative_path(a)

    a = Path('Test')
    assert assert_not_none(a)
    assert assert_equal(a.__fspath__(), 'Test')
    assert assert_equal(repr(a), "PosixPath('Test')")
    assert assert_equal(str(a), 'Test')
    assert assert_relative_path(a)

    a = Path('/Test')
    assert assert_not_none(a)
    assert assert_equal(a.__fspath__(), '/Test')
    assert assert_equal(repr(a), "PosixPath('/Test')")
    assert assert_equal(str(a), '/Test')
    assert assert_absolute_path(a)

    b = a / Path('123')
    assert assert_not_none(b)
    assert assert_equal(b.__fspath__(), '/Test/123')
    assert assert_equal(repr(b), "PosixPath('/Test/123')")
    assert assert_equal(str(b), '/Test/123')
    assert assert_absolute_path(b)

def test_tracked_path():
    with raises(TypeError): TrackedPath()
    with raises(TypeError): TrackedPath(None)
    with raises(AssertionError): TrackedPath(None, None)
    with raises(AssertionError): TrackedPath(None, None, None)
    with raises(AssertionError): TrackedPath('Test', 'Test', 'Test')
    with raises(AssertionError): TrackedPath('Test', 'Test', Path())
    with raises(AssertionError): TrackedPath('Test', Path(), 'Test')
    with raises(AssertionError): TrackedPath('Test', Path(), Path())
    with raises(AssertionError): TrackedPath('Test', '123', 'abc')

    a = TrackedPath('Test', '/123')
    assert assert_not_none(a)
    assert assert_equal(a, PosixPath('/123'))
    assert assert_equal(a.__fspath__(), '/123')
    assert assert_equal(repr(a), "TrackedPath('Test', PosixPath('/123'), PosixPath('.'))")
    assert assert_equal(str(a), a.__fspath__())
    assert assert_equal(a.for_log(), "'Test' path '.'")
    assert assert_absolute_path(a.top)
    assert assert_equal(a.top, a)
    assert assert_relative_path(a.subpath)
    assert assert_equal(a.subpath, Path('.'))
    assert assert_equal(a.basename, '')

    b = TrackedPath('Test', '/123', 'abc')
    assert assert_not_none(b)
    assert assert_equal(b, PosixPath('/123/abc'))
    assert assert_equal(b.__fspath__(), '/123/abc')
    assert assert_equal(repr(b), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))")
    assert assert_equal(str(b), b.__fspath__())
    assert assert_equal(b.for_log(), "'Test' path 'abc'")
    assert assert_absolute_path(b.top)
    assert assert_equal(b.top, a)
    assert assert_relative_path(b.subpath)
    assert assert_equal(b.subpath, Path('.'))
    assert assert_equal(b.basename, 'abc')

    c = Path('/123/abc/xyz')
    d = b.for_path(c)
    assert assert_not_none(d)
    assert assert_equal(d, PosixPath('/123/abc/xyz'))
    assert assert_equal(d.__fspath__(), '/123/abc/xyz')
    assert assert_equal(repr(d), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc/xyz'))")
    assert assert_equal(str(d), d.__fspath__())
    assert assert_equal(d.for_log(), "'Test' path 'abc/xyz'")
    assert assert_absolute_path(d.top)
    assert assert_equal(d.top, a)
    assert assert_relative_path(d.subpath)
    assert assert_equal(d.subpath, Path('abc'))
    assert assert_equal(d.basename, 'xyz')

    e = d / 'def.ghi'
    assert assert_not_none(e)
    assert assert_equal(e, PosixPath('/123/abc/xyz/def.ghi'))
    assert assert_equal(e.__fspath__(), '/123/abc/xyz/def.ghi')
    assert assert_equal(repr(e), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc/xyz/def.ghi'))")
    assert assert_equal(str(e), e.__fspath__())
    assert assert_equal(e.for_log(), "'Test' path 'abc/xyz/def.ghi'")
    assert assert_absolute_path(e.top)
    assert assert_equal(e.top, a)
    assert assert_relative_path(e.subpath)
    assert assert_equal(e.subpath, Path('abc/xyz'))
    assert assert_equal(e.basename, 'def.ghi')

    f = b / None
    assert assert_not_none(f)
    assert assert_equal(f, PosixPath('/123/abc'))
    assert assert_equal(f.__fspath__(), '/123/abc')
    assert assert_equal(repr(f), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))")
    assert assert_equal(str(f), f.__fspath__())
    assert assert_equal(f.for_log(), "'Test' path 'abc'")
    assert assert_absolute_path(f.top)
    assert assert_equal(f.top, a)
    assert assert_relative_path(f.subpath)
    assert assert_equal(f.subpath, Path())
    assert assert_equal(f.basename, 'abc')

    g = b / ''
    assert assert_not_none(g)
    assert assert_equal(g, PosixPath('/123/abc'))
    assert assert_equal(g.__fspath__(), '/123/abc')
    assert assert_equal(repr(g), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))")
    assert assert_equal(str(g), g.__fspath__())
    assert assert_equal(g.for_log(), "'Test' path 'abc'")
    assert assert_absolute_path(g.top)
    assert assert_equal(g.top, a)
    assert assert_relative_path(g.subpath)
    assert assert_equal(g.subpath, Path())
    assert assert_equal(g.basename, 'abc')

    h = b / Path()
    assert assert_not_none(h)
    assert assert_equal(h, PosixPath('/123/abc'))
    assert assert_equal(h.__fspath__(), '/123/abc')
    assert assert_equal(repr(h), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))")
    assert assert_equal(str(h), h.__fspath__())
    assert assert_equal(h.for_log(), "'Test' path 'abc'")
    assert assert_absolute_path(h.top)
    assert assert_equal(h.top, a)
    assert assert_relative_path(h.subpath)
    assert assert_equal(h.subpath, Path())
    assert assert_equal(h.basename, 'abc')

'''DisabledContent
'''


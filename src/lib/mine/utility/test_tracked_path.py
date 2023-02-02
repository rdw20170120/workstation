#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path
from pathlib import PosixPath

# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_
from utility import my_assert_pathname as pn_is_
from utility.tracked_path import TrackedPath

# Project modules   (relative references, NOT packaged, in project)


def test_path():
    assert is_.not_none(Path())
    with raises(TypeError):
        Path(None)

    a = Path("")
    assert is_.not_none(a)
    assert is_.equal(a.__fspath__(), ".")
    assert is_.equal(repr(a), "PosixPath('.')")
    assert is_.equal(str(a), ".")
    assert pn_is_.relative_path(a)

    a = Path("Test")
    assert is_.not_none(a)
    assert is_.equal(a.__fspath__(), "Test")
    assert is_.equal(repr(a), "PosixPath('Test')")
    assert is_.equal(str(a), "Test")
    assert pn_is_.relative_path(a)

    a = Path("/Test")
    assert is_.not_none(a)
    assert is_.equal(a.__fspath__(), "/Test")
    assert is_.equal(repr(a), "PosixPath('/Test')")
    assert is_.equal(str(a), "/Test")
    assert pn_is_.absolute_path(a)

    b = a / Path("123")
    assert is_.not_none(b)
    assert is_.equal(b.__fspath__(), "/Test/123")
    assert is_.equal(repr(b), "PosixPath('/Test/123')")
    assert is_.equal(str(b), "/Test/123")
    assert pn_is_.absolute_path(b)


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
        TrackedPath("Test", "Test", "Test")
    with raises(AssertionError):
        TrackedPath("Test", "Test", Path())
    with raises(AssertionError):
        TrackedPath("Test", Path(), "Test")
    with raises(AssertionError):
        TrackedPath("Test", Path(), Path())
    with raises(AssertionError):
        TrackedPath("Test", "123", "abc")

    a = TrackedPath("Test", "/123")
    assert is_.not_none(a)
    assert is_.equal(a, PosixPath("/123"))
    assert is_.equal(a.__fspath__(), "/123")
    assert is_.equal(
        repr(a), "TrackedPath('Test', PosixPath('/123'), PosixPath('.'))"
    )
    assert is_.equal(str(a), a)
    assert is_.equal(str(a), a.__fspath__())
    assert is_.equal(a.for_log(), "'Test' path '.'")
    assert pn_is_.absolute_path(a.top)
    assert is_.equal(a.top, a)
    assert pn_is_.relative_path(a.subpath)
    assert is_.equal(a.subpath, Path("."))
    assert is_.equal(a.basename, "")
    with raises(ValueError):
        a.parent

    b = TrackedPath("Test", "/123", "abc")
    assert is_.not_none(b)
    assert is_.equal(b, PosixPath("/123/abc"))
    assert is_.equal(b.__fspath__(), "/123/abc")
    assert is_.equal(
        repr(b), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))"
    )
    assert is_.equal(str(b), b)
    assert is_.equal(str(b), b.__fspath__())
    assert is_.equal(b.for_log(), "'Test' path 'abc'")
    assert pn_is_.absolute_path(b.top)
    assert is_.equal(b.top, a)
    assert pn_is_.relative_path(b.subpath)
    assert is_.equal(b.subpath, Path("."))
    assert is_.equal(b.basename, "abc")
    assert is_.equal(b.parent, a)

    c = Path("/123/abc/xyz")
    d = b.for_path(c)
    assert is_.not_none(d)
    assert is_.equal(d, PosixPath("/123/abc/xyz"))
    assert is_.equal(d.__fspath__(), "/123/abc/xyz")
    assert is_.equal(
        repr(d), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc/xyz'))"
    )
    assert is_.equal(str(d), d)
    assert is_.equal(str(d), d.__fspath__())
    assert is_.equal(d.for_log(), "'Test' path 'abc/xyz'")
    assert pn_is_.absolute_path(d.top)
    assert is_.equal(d.top, a)
    assert pn_is_.relative_path(d.subpath)
    assert is_.equal(d.subpath, Path("abc"))
    assert is_.equal(d.basename, "xyz")
    assert is_.equal(d.parent, b)

    e = d / "def.ghi"
    assert is_.not_none(e)
    assert is_.equal(e, PosixPath("/123/abc/xyz/def.ghi"))
    assert is_.equal(e.__fspath__(), "/123/abc/xyz/def.ghi")
    assert is_.equal(
        repr(e),
        "TrackedPath('Test', PosixPath('/123'), PosixPath('abc/xyz/def.ghi'))",
    )
    assert is_.equal(str(e), e)
    assert is_.equal(str(e), e.__fspath__())
    assert is_.equal(e.for_log(), "'Test' path 'abc/xyz/def.ghi'")
    assert pn_is_.absolute_path(e.top)
    assert is_.equal(e.top, a)
    assert pn_is_.relative_path(e.subpath)
    assert is_.equal(e.subpath, Path("abc/xyz"))
    assert is_.equal(e.basename, "def.ghi")
    assert is_.equal(e.parent, d)

    f = b / None
    assert is_.not_none(f)
    assert is_.equal(f, PosixPath("/123/abc"))
    assert is_.equal(f.__fspath__(), "/123/abc")
    assert is_.equal(
        repr(f), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))"
    )
    assert is_.equal(str(f), f)
    assert is_.equal(str(f), f.__fspath__())
    assert is_.equal(f.for_log(), "'Test' path 'abc'")
    assert pn_is_.absolute_path(f.top)
    assert is_.equal(f.top, a)
    assert pn_is_.relative_path(f.subpath)
    assert is_.equal(f.subpath, Path())
    assert is_.equal(f.basename, "abc")
    assert is_.equal(f.parent, a)

    g = b / ""
    assert is_.not_none(g)
    assert is_.equal(g, PosixPath("/123/abc"))
    assert is_.equal(g.__fspath__(), "/123/abc")
    assert is_.equal(
        repr(g), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))"
    )
    assert is_.equal(str(g), g.__fspath__())
    assert is_.equal(g.for_log(), "'Test' path 'abc'")
    assert pn_is_.absolute_path(g.top)
    assert is_.equal(g.top, a)
    assert pn_is_.relative_path(g.subpath)
    assert is_.equal(g.subpath, Path())
    assert is_.equal(g.basename, "abc")
    assert is_.equal(g.parent, a)

    h = b / Path()
    assert is_.not_none(h)
    assert is_.equal(h, PosixPath("/123/abc"))
    assert is_.equal(h.__fspath__(), "/123/abc")
    assert is_.equal(
        repr(h), "TrackedPath('Test', PosixPath('/123'), PosixPath('abc'))"
    )
    assert is_.equal(str(h), h)
    assert is_.equal(str(h), h.__fspath__())
    assert is_.equal(h.for_log(), "'Test' path 'abc'")
    assert pn_is_.absolute_path(h.top)
    assert is_.equal(h.top, a)
    assert pn_is_.relative_path(h.subpath)
    assert is_.equal(h.subpath, Path())
    assert is_.equal(h.basename, "abc")
    assert is_.equal(h.parent, a)


"""DisabledContent
"""

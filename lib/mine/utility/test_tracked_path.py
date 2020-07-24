#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .tracked_path import TrackedPath


def test_path():
    assert Path() is not None
    with raises(TypeError):
        Path(None)
    assert Path("") is not None
    assert Path("Test") is not None

def test_tracked_path():
    with raises(TypeError):
        TrackedPath()
    with raises(TypeError):
        TrackedPath(None)
    with raises(TypeError):
        TrackedPath(None, None)
    with raises(AssertionError):
        TrackedPath(None, None, None)

    assert TrackedPath("Test", "Test", "Test") is not None
    assert TrackedPath("Test", "Test", Path()) is not None
    assert TrackedPath("Test", Path(), "Test") is not None
    assert TrackedPath("Test", Path(), Path()) is not None

    a = TrackedPath("Test", "123", "abc")
    assert a.for_log == "Test path 'abc'"
    assert a.for_ref == "abc"
    assert a.__fspath__() == "123/abc"
    assert repr(a) == "TrackedPath('Test', PosixPath('123'), PosixPath('abc'))"
    assert str(a) == "123/abc"
    # TODO: Test combining with "/"

"""DisabledContent
    assert a. == ""
"""


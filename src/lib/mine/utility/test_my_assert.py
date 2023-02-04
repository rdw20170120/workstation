#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


def test_at_least():
    assert is_.at_least("", "")
    assert is_.at_least("Test", "")
    assert is_.at_least("Test", "Test")
    assert is_.at_least(-1, -1)
    assert is_.at_least(-1.0, -1.0)
    assert is_.at_least(0, -1)
    assert is_.at_least(0, -1.0)
    assert is_.at_least(0, 0)
    assert is_.at_least(0.0, 0.0)
    assert is_.at_least(1, 1)
    assert is_.at_least(1.0, 1.0)
    with raises(AssertionError):
        assert is_.at_least("", "Test")
    with raises(AssertionError):
        assert is_.at_least(0, 1)
    with raises(AssertionError):
        assert is_.at_least(0, 1.0)
    with raises(TypeError):
        assert is_.at_least(None, None)


def test_at_most():
    assert is_.at_most("", "")
    assert is_.at_most("", "Test")
    assert is_.at_most("Test", "Test")
    assert is_.at_most(-1, -1)
    assert is_.at_most(-1.0, -1.0)
    assert is_.at_most(0, 0)
    assert is_.at_most(0, 1)
    assert is_.at_most(0, 1.0)
    assert is_.at_most(0.0, 0.0)
    assert is_.at_most(1, 1)
    assert is_.at_most(1.0, 1.0)
    with raises(AssertionError):
        assert is_.at_most("Test", "")
    with raises(AssertionError):
        assert is_.at_most(0, -1)
    with raises(AssertionError):
        assert is_.at_most(0, -1.0)
    with raises(TypeError):
        assert is_.at_most(None, None)


def test_encoding_is_utf8():
    assert is_.encoding_is_utf8("UTF8")
    assert is_.encoding_is_utf8("utf-8")
    assert is_.encoding_is_utf8("utf_8")
    with raises(AssertionError):
        assert is_.encoding_is_utf8("")
    with raises(AssertionError):
        assert is_.encoding_is_utf8("Test")
    with raises(AssertionError):
        assert is_.encoding_is_utf8(0)
    with raises(AssertionError):
        assert is_.encoding_is_utf8(0.0)
    with raises(AssertionError):
        assert is_.encoding_is_utf8(None)
    with raises(TypeError):
        assert is_.encoding_is_utf8()


def test_equal():
    assert is_.equal("", "")
    assert is_.equal("Test", "Test")
    assert is_.equal(-1, -1)
    assert is_.equal(-1.0, -1.0)
    assert is_.equal(0, 0)
    assert is_.equal(0.0, 0.0)
    assert is_.equal(1, 1)
    assert is_.equal(1.0, 1.0)
    assert is_.equal(None, None)
    with raises(AssertionError):
        assert is_.equal(-1, 0)
    with raises(AssertionError):
        assert is_.equal(-1, 0)
    with raises(AssertionError):
        assert is_.equal(-1, 1)
    with raises(AssertionError):
        assert is_.equal(1, 0)


def test_greater():
    assert is_.greater("Test", "")
    assert is_.greater(0, -1)
    assert is_.greater(0, -1.0)
    with raises(AssertionError):
        assert is_.greater("", "")
    with raises(AssertionError):
        assert is_.greater("", "Test")
    with raises(AssertionError):
        assert is_.greater("Test", "Test")
    with raises(AssertionError):
        assert is_.greater(-1, -1)
    with raises(AssertionError):
        assert is_.greater(-1.0, -1.0)
    with raises(AssertionError):
        assert is_.greater(0, 0)
    with raises(AssertionError):
        assert is_.greater(0, 1)
    with raises(AssertionError):
        assert is_.greater(0, 1.0)
    with raises(AssertionError):
        assert is_.greater(0.0, 0.0)
    with raises(AssertionError):
        assert is_.greater(1, 1)
    with raises(AssertionError):
        assert is_.greater(1.0, 1.0)
    with raises(TypeError):
        assert is_.greater(None, None)


def test_identical():
    assert is_.identical("", "")
    assert is_.identical("Test", "Test")
    assert is_.identical(-1, -1)
    assert is_.identical(0, 0)
    assert is_.identical(0.0, 0.0)
    assert is_.identical(1, 1)
    assert is_.identical(1.0, 1.0)
    assert is_.identical(None, None)
    with raises(AssertionError):
        assert is_.identical(-1, 0)
    with raises(AssertionError):
        assert is_.identical(-1, 0)
    with raises(AssertionError):
        assert is_.identical(-1, 1)
    with raises(AssertionError):
        assert is_.identical(-1.0, -1.0)
    with raises(AssertionError):
        assert is_.identical(1, 0)


def test_instance():
    assert is_.instance(None, type(None))

    with raises(AssertionError) as info:
        assert is_.instance(None, str)
    a = str(info.value)
    assert "Value is None" in a
    assert "<class 'str'>" in a

    assert is_.instance("", str)

    assert is_.instance(None, (type(None), str))
    assert is_.instance("", (type(None), str))
    assert is_.instance("Test", (type(None), str))


def test_integer_at_least():
    assert is_.integer_at_least(-1, -1)
    assert is_.integer_at_least(0, -1)
    assert is_.integer_at_least(0, -1.0)
    assert is_.integer_at_least(0, 0)
    assert is_.integer_at_least(1, 1)
    with raises(AssertionError):
        assert is_.integer_at_least("", "")
    with raises(AssertionError):
        assert is_.integer_at_least("", "Test")
    with raises(AssertionError):
        assert is_.integer_at_least("Test", "")
    with raises(AssertionError):
        assert is_.integer_at_least("Test", "Test")
    with raises(AssertionError):
        assert is_.integer_at_least(-1.0, -1.0)
    with raises(AssertionError):
        assert is_.integer_at_least(0, 1)
    with raises(AssertionError):
        assert is_.integer_at_least(0, 1.0)
    with raises(AssertionError):
        assert is_.integer_at_least(0.0, 0.0)
    with raises(AssertionError):
        assert is_.integer_at_least(1.0, 1.0)
    with raises(AssertionError):
        assert is_.integer_at_least(None, None)


def test_integer_greater():
    assert is_.integer_greater(0, -1)
    assert is_.integer_greater(0, -1.0)
    with raises(AssertionError):
        assert is_.integer_greater("", "")
    with raises(AssertionError):
        assert is_.integer_greater("", "Test")
    with raises(AssertionError):
        assert is_.integer_greater("Test", "")
    with raises(AssertionError):
        assert is_.integer_greater("Test", "Test")
    with raises(AssertionError):
        assert is_.integer_greater(-1, -1)
    with raises(AssertionError):
        assert is_.integer_greater(-1.0, -1.0)
    with raises(AssertionError):
        assert is_.integer_greater(0, 0)
    with raises(AssertionError):
        assert is_.integer_greater(0, 1)
    with raises(AssertionError):
        assert is_.integer_greater(0, 1.0)
    with raises(AssertionError):
        assert is_.integer_greater(0.0, 0.0)
    with raises(AssertionError):
        assert is_.integer_greater(1, 1)
    with raises(AssertionError):
        assert is_.integer_greater(1.0, 1.0)
    with raises(AssertionError):
        assert is_.integer_greater(None, None)


def test_none():
    assert is_.none(None)
    with raises(AssertionError):
        assert is_.none("")
    with raises(AssertionError):
        assert is_.none("Test")
    with raises(AssertionError):
        assert is_.none(-1)
    with raises(AssertionError):
        assert is_.none(-1.0)
    with raises(AssertionError):
        assert is_.none(0)
    with raises(AssertionError):
        assert is_.none(0.0)
    with raises(AssertionError):
        assert is_.none(1)
    with raises(AssertionError):
        assert is_.none(1.0)
    with raises(TypeError):
        assert is_.none()


def test_not_equal():
    assert is_.not_equal(-1, 0)
    assert is_.not_equal(-1, 0)
    assert is_.not_equal(-1, 1)
    assert is_.not_equal(1, 0)
    with raises(AssertionError):
        assert is_.not_equal("", "")
    with raises(AssertionError):
        assert is_.not_equal("Test", "Test")
    with raises(AssertionError):
        assert is_.not_equal(-1, -1)
    with raises(AssertionError):
        assert is_.not_equal(-1.0, -1.0)
    with raises(AssertionError):
        assert is_.not_equal(0, 0)
    with raises(AssertionError):
        assert is_.not_equal(0.0, 0.0)
    with raises(AssertionError):
        assert is_.not_equal(1, 1)
    with raises(AssertionError):
        assert is_.not_equal(1.0, 1.0)
    with raises(AssertionError):
        assert is_.not_equal(None, None)


def test_not_instance():
    #   with raises(AssertionError):
    assert is_.not_instance(None, (bool, float, int, str))
    assert is_.not_instance(None, str)
    with raises(AssertionError):
        assert is_.not_instance("", (bool, float, int, str))
    with raises(AssertionError):
        assert is_.not_instance("Test", (bool, float, int, str))
    with raises(AssertionError):
        assert is_.not_instance(-1, (bool, float, int, str))
    with raises(AssertionError):
        assert is_.not_instance(-1.0, (bool, float, int, str))
    with raises(AssertionError):
        assert is_.not_instance(0, (bool, float, int, str))
    with raises(AssertionError):
        assert is_.not_instance(0.0, (bool, float, int, str))
    with raises(AssertionError):
        assert is_.not_instance(1, (bool, float, int, str))
    with raises(AssertionError):
        assert is_.not_instance(1.0, (bool, float, int, str))


"""DisabledContent
"""

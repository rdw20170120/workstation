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


def test_at_least_00():
    assert is_.at_least("", "")


def test_at_least_01():
    assert is_.at_least("Test", "")


def test_at_least_02():
    assert is_.at_least("Test", "Test")


def test_at_least_03():
    assert is_.at_least(-1, -1)


def test_at_least_04():
    assert is_.at_least(-1.0, -1.0)


def test_at_least_05():
    assert is_.at_least(0, -1)


def test_at_least_06():
    assert is_.at_least(0, -1.0)


def test_at_least_07():
    assert is_.at_least(0, 0)


def test_at_least_08():
    assert is_.at_least(0.0, 0.0)


def test_at_least_09():
    assert is_.at_least(1, 1)


def test_at_least_10():
    assert is_.at_least(1.0, 1.0)


def test_at_least_11():
    with raises(AssertionError):
        assert is_.at_least("", "Test")


def test_at_least_12():
    with raises(AssertionError):
        assert is_.at_least(0, 1)


def test_at_least_13():
    with raises(AssertionError):
        assert is_.at_least(0, 1.0)


def test_at_least_14():
    with raises(TypeError):
        assert is_.at_least(None, None)


def test_at_most_00():
    assert is_.at_most("", "")


def test_at_most_01():
    assert is_.at_most("", "Test")


def test_at_most_02():
    assert is_.at_most("Test", "Test")


def test_at_most_03():
    assert is_.at_most(-1, -1)


def test_at_most_04():
    assert is_.at_most(-1.0, -1.0)


def test_at_most_05():
    assert is_.at_most(0, 0)


def test_at_most_06():
    assert is_.at_most(0, 1)


def test_at_most_07():
    assert is_.at_most(0, 1.0)


def test_at_most_08():
    assert is_.at_most(0.0, 0.0)


def test_at_most_09():
    assert is_.at_most(1, 1)


def test_at_most_10():
    assert is_.at_most(1.0, 1.0)


def test_at_most_11():
    with raises(AssertionError):
        assert is_.at_most("Test", "")


def test_at_most_12():
    with raises(AssertionError):
        assert is_.at_most(0, -1)


def test_at_most_13():
    with raises(AssertionError):
        assert is_.at_most(0, -1.0)


def test_at_most_14():
    with raises(TypeError):
        assert is_.at_most(None, None)


def test_encoding_is_utf8_00():
    assert is_.encoding_is_utf8("UTF8")


def test_encoding_is_utf8_01():
    assert is_.encoding_is_utf8("utf-8")


def test_encoding_is_utf8_02():
    assert is_.encoding_is_utf8("utf_8")


def test_encoding_is_utf8_03():
    with raises(AssertionError):
        assert is_.encoding_is_utf8("")


def test_encoding_is_utf8_04():
    with raises(AssertionError):
        assert is_.encoding_is_utf8("Test")


def test_encoding_is_utf8_05():
    with raises(AssertionError):
        assert is_.encoding_is_utf8(0)


def test_encoding_is_utf8_06():
    with raises(AssertionError):
        assert is_.encoding_is_utf8(0.0)


def test_encoding_is_utf8_07():
    with raises(AssertionError):
        assert is_.encoding_is_utf8(None)


def test_encoding_is_utf8_08():
    with raises(TypeError):
        assert is_.encoding_is_utf8()


def test_equal_00():
    assert is_.equal("", "")


def test_equal_01():
    assert is_.equal("Test", "Test")


def test_equal_02():
    assert is_.equal(-1, -1)


def test_equal_03():
    assert is_.equal(-1.0, -1.0)


def test_equal_04():
    assert is_.equal(0, 0)


def test_equal_05():
    assert is_.equal(0.0, 0.0)


def test_equal_06():
    assert is_.equal(1, 1)


def test_equal_07():
    assert is_.equal(1.0, 1.0)


def test_equal_08():
    assert is_.equal(None, None)


def test_equal_09():
    with raises(AssertionError):
        assert is_.equal(-1, 0)


def test_equal_10():
    with raises(AssertionError):
        assert is_.equal(-1, 0)


def test_equal_11():
    with raises(AssertionError):
        assert is_.equal(-1, 1)


def test_equal_12():
    with raises(AssertionError):
        assert is_.equal(1, 0)


def test_greater_00():
    assert is_.greater("Test", "")


def test_greater_01():
    assert is_.greater(0, -1)


def test_greater_02():
    assert is_.greater(0, -1.0)


def test_greater_03():
    with raises(AssertionError):
        assert is_.greater("", "")


def test_greater_04():
    with raises(AssertionError):
        assert is_.greater("", "Test")


def test_greater_05():
    with raises(AssertionError):
        assert is_.greater("Test", "Test")


def test_greater_06():
    with raises(AssertionError):
        assert is_.greater(-1, -1)


def test_greater_07():
    with raises(AssertionError):
        assert is_.greater(-1.0, -1.0)


def test_greater_08():
    with raises(AssertionError):
        assert is_.greater(0, 0)


def test_greater_09():
    with raises(AssertionError):
        assert is_.greater(0, 1)


def test_greater_10():
    with raises(AssertionError):
        assert is_.greater(0, 1.0)


def test_greater_11():
    with raises(AssertionError):
        assert is_.greater(0.0, 0.0)


def test_greater_12():
    with raises(AssertionError):
        assert is_.greater(1, 1)


def test_greater_13():
    with raises(AssertionError):
        assert is_.greater(1.0, 1.0)


def test_greater_14():
    with raises(TypeError):
        assert is_.greater(None, None)


def test_identical_00():
    assert is_.identical("", "")


def test_identical_01():
    assert is_.identical("Test", "Test")


def test_identical_02():
    assert is_.identical(-1, -1)


def test_identical_03():
    assert is_.identical(0, 0)


def test_identical_04():
    assert is_.identical(0.0, 0.0)


def test_identical_05():
    assert is_.identical(1, 1)


def test_identical_06():
    assert is_.identical(1.0, 1.0)


def test_identical_07():
    assert is_.identical(None, None)


def test_identical_08():
    with raises(AssertionError):
        assert is_.identical(-1, 0)


def test_identical_09():
    with raises(AssertionError):
        assert is_.identical(-1, 0)


def test_identical_10():
    with raises(AssertionError):
        assert is_.identical(-1, 1)


def test_identical_11():
    with raises(AssertionError):
        assert is_.identical(-1.0, -1.0)


def test_identical_12():
    with raises(AssertionError):
        assert is_.identical(1, 0)


def test_instance_00():
    assert is_.instance(None, type(None))


def test_instance_01():
    with raises(AssertionError) as info:
        assert is_.instance(None, str)


def test_instance_02():
    a = str(info.value)
    assert "Value is None" in a
    assert "<class 'str'>" in a


def test_instance_00():
    assert is_.instance("", str)


def test_instance_01():
    assert is_.instance(None, (type(None), str))


def test_instance_02():
    assert is_.instance("", (type(None), str))


def test_instance_03():
    assert is_.instance("Test", (type(None), str))


def test_integer_at_least_00():
    assert is_.integer_at_least(-1, -1)


def test_integer_at_least_01():
    assert is_.integer_at_least(0, -1)


def test_integer_at_least_02():
    assert is_.integer_at_least(0, -1.0)


def test_integer_at_least_03():
    assert is_.integer_at_least(0, 0)


def test_integer_at_least_04():
    assert is_.integer_at_least(1, 1)


def test_integer_at_least_05():
    with raises(AssertionError):
        assert is_.integer_at_least("", "")


def test_integer_at_least_06():
    with raises(AssertionError):
        assert is_.integer_at_least("", "Test")


def test_integer_at_least_07():
    with raises(AssertionError):
        assert is_.integer_at_least("Test", "")


def test_integer_at_least_08():
    with raises(AssertionError):
        assert is_.integer_at_least("Test", "Test")


def test_integer_at_least_09():
    with raises(AssertionError):
        assert is_.integer_at_least(-1.0, -1.0)


def test_integer_at_least_10():
    with raises(AssertionError):
        assert is_.integer_at_least(0, 1)


def test_integer_at_least_11():
    with raises(AssertionError):
        assert is_.integer_at_least(0, 1.0)


def test_integer_at_least_12():
    with raises(AssertionError):
        assert is_.integer_at_least(0.0, 0.0)


def test_integer_at_least_13():
    with raises(AssertionError):
        assert is_.integer_at_least(1.0, 1.0)


def test_integer_at_least_14():
    with raises(AssertionError):
        assert is_.integer_at_least(None, None)


def test_integer_greater_00():
    assert is_.integer_greater(0, -1)


def test_integer_greater_01():
    assert is_.integer_greater(0, -1.0)


def test_integer_greater_02():
    with raises(AssertionError):
        assert is_.integer_greater("", "")


def test_integer_greater_03():
    with raises(AssertionError):
        assert is_.integer_greater("", "Test")


def test_integer_greater_04():
    with raises(AssertionError):
        assert is_.integer_greater("Test", "")


def test_integer_greater_05():
    with raises(AssertionError):
        assert is_.integer_greater("Test", "Test")


def test_integer_greater_06():
    with raises(AssertionError):
        assert is_.integer_greater(-1, -1)


def test_integer_greater_07():
    with raises(AssertionError):
        assert is_.integer_greater(-1.0, -1.0)


def test_integer_greater_08():
    with raises(AssertionError):
        assert is_.integer_greater(0, 0)


def test_integer_greater_09():
    with raises(AssertionError):
        assert is_.integer_greater(0, 1)


def test_integer_greater_10():
    with raises(AssertionError):
        assert is_.integer_greater(0, 1.0)


def test_integer_greater_11():
    with raises(AssertionError):
        assert is_.integer_greater(0.0, 0.0)


def test_integer_greater_12():
    with raises(AssertionError):
        assert is_.integer_greater(1, 1)


def test_integer_greater_13():
    with raises(AssertionError):
        assert is_.integer_greater(1.0, 1.0)


def test_integer_greater_14():
    with raises(AssertionError):
        assert is_.integer_greater(None, None)


def test_none_00():
    assert is_.none(None)


def test_none_01():
    with raises(AssertionError):
        assert is_.none("")


def test_none_02():
    with raises(AssertionError):
        assert is_.none("Test")


def test_none_03():
    with raises(AssertionError):
        assert is_.none(-1)


def test_none_04():
    with raises(AssertionError):
        assert is_.none(-1.0)


def test_none_05():
    with raises(AssertionError):
        assert is_.none(0)


def test_none_06():
    with raises(AssertionError):
        assert is_.none(0.0)


def test_none_07():
    with raises(AssertionError):
        assert is_.none(1)


def test_none_08():
    with raises(AssertionError):
        assert is_.none(1.0)


def test_none_09():
    with raises(TypeError):
        assert is_.none()


def test_not_equal_00():
    assert is_.not_equal(-1, 0)


def test_not_equal_01():
    assert is_.not_equal(-1, 0)


def test_not_equal_02():
    assert is_.not_equal(-1, 1)


def test_not_equal_03():
    assert is_.not_equal(1, 0)


def test_not_equal_04():
    with raises(AssertionError):
        assert is_.not_equal("", "")


def test_not_equal_05():
    with raises(AssertionError):
        assert is_.not_equal("Test", "Test")


def test_not_equal_06():
    with raises(AssertionError):
        assert is_.not_equal(-1, -1)


def test_not_equal_07():
    with raises(AssertionError):
        assert is_.not_equal(-1.0, -1.0)


def test_not_equal_08():
    with raises(AssertionError):
        assert is_.not_equal(0, 0)


def test_not_equal_09():
    with raises(AssertionError):
        assert is_.not_equal(0.0, 0.0)


def test_not_equal_10():
    with raises(AssertionError):
        assert is_.not_equal(1, 1)


def test_not_equal_11():
    with raises(AssertionError):
        assert is_.not_equal(1.0, 1.0)


def test_not_equal_12():
    with raises(AssertionError):
        assert is_.not_equal(None, None)


def test_not_instance_00():
    assert is_.not_instance(None, (bool, float, int, str))


def test_not_instance_01():
    assert is_.not_instance(None, str)


def test_not_instance_02():
    with raises(AssertionError):
        assert is_.not_instance("", (bool, float, int, str))


def test_not_instance_03():
    with raises(AssertionError):
        assert is_.not_instance("Test", (bool, float, int, str))


def test_not_instance_04():
    with raises(AssertionError):
        assert is_.not_instance(-1, (bool, float, int, str))


def test_not_instance_05():
    with raises(AssertionError):
        assert is_.not_instance(-1.0, (bool, float, int, str))


def test_not_instance_06():
    with raises(AssertionError):
        assert is_.not_instance(0, (bool, float, int, str))


def test_not_instance_07():
    with raises(AssertionError):
        assert is_.not_instance(0.0, (bool, float, int, str))


def test_not_instance_08():
    with raises(AssertionError):
        assert is_.not_instance(1, (bool, float, int, str))


def test_not_instance_09():
    with raises(AssertionError):
        assert is_.not_instance(1.0, (bool, float, int, str))


"""DisabledContent
"""

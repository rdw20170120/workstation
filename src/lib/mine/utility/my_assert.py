#!/usr/bin/env false
"""My module for assertions.

The Python `assert` statement takes an optional message argument,
but it has to be specified on each statement.
When the message argument is absent
then the resulting AssertionError
has an empty message that completely fails to communicate.
I want messages on EVERY assertion
that consistently match the assertion logic,
so I choose to refactor the assertions implementation.
However, it appears that I cannot return both
the conditional logic test result (bool) and
the failed assertion message (str)
from the call to a single helper function.

Therefore, I have refactored
to a set of helper functions
that return `True`
when the assertion condition logic succeeds
and throw a custom AssertionError
with a good consistent message
when the assertion condition logic fails.

This preserves the observable behavior of the `assert` statements.
Since the `assert` statements
become a no-op during an optimized compilation,
all of these helper functions can still be optimized away.
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)


def assert_absolute_directory(path):
    result = path.is_absolute()
    if result: result = path.is_dir()
    if result: return result
    else:
        raise AssertionError(
            '{!r} is NOT an absolute directory'.format(
                path
            ))

def assert_absolute_file(path):
    result = path.is_absolute()
    if result: result = path.is_file()
    if result: return result
    else:
        raise AssertionError(
            '{!r} is NOT an absolute file'.format(
                path
            ))

def assert_absolute_path(path):
    result = path.is_absolute()
    if result: return result
    else:
        raise AssertionError(
            '{!r} is NOT an absolute path'.format(
                path
            ))

def assert_encoding_is_utf8(encoding):
    result = (encoding in ('utf-8', 'UTF8'))
    if result: return result
    else:
        raise AssertionError(
            "Encoding {!r} is NOT a variant of UTF8".format(
                encoding
            ))

def assert_equal(actual_value, expected_value):
    """Assert that actual_value is equal to expected_value."""
    result = (actual_value == expected_value)
    if result: return result
    else:
        raise AssertionError(
            "{!r} does NOT equal {!r}".format(
                actual_value, expected_value
            ))

def assert_equal_or_greater(actual_value, expected_value):
    """Assert that actual_value is equal to or greater than expected_value."""
    result = (actual_value >= expected_value)
    if result: return result
    else:
        raise AssertionError(
            "{!r} is LESS than {!r}".format(
                actual_value, expected_value
            ))

def assert_existing_absolute_path(path):
    result = path.is_absolute()
    if result: result = path.exists()
    if result: return result
    else:
        raise AssertionError(
            '{!r} is NOT an existing absolute path'.format(
                path
            ))

def assert_false(actual_value):
    result = not bool(actual_value)
    if result: return result
    else:
        raise AssertionError(
            'Value is {!r}, INSTEAD of {!r}'.format(
                actual_value, False
            ))

def assert_greater(actual_value, lower_limit):
    """Assert that actual_value is greater than lower_limit."""
    result = (actual_value > lower_limit)
    if result: return result
    else:
        raise AssertionError(
            "{!r} is LESS than or EQUAL to {!r}".format(
                actual_value, lower_limit
            ))

def assert_in(actual_value, expected_values):
    result = (actual_value in expected_values)
    if result: return result
    else:
        raise AssertionError(
            'Value is {!r}, NOT IN {!r}'.format(
                actual_value, expected_values
            ))

def assert_instance(actual_value, expected_types):
    result = isinstance(actual_value, expected_types)
    if result: return result
    else:
        raise AssertionError(
            'Value is {!r}, INSTEAD of {!r}'.format(
                actual_value, expected_types
            ))

def assert_integer_equal_or_greater(actual_value, expected_value):
    """Assert that actual_value is an integer equal to or greater than expected_value."""
    result = isinstance(actual_value, int)
    if result: result = (actual_value >= expected_value)
    if result: return result
    else:
        raise AssertionError(
            "{!r} is NOT an INTEGER, or is LESS than {!r}".format(
                actual_value, expected_value
            ))

def assert_integer_greater(actual_value, lower_limit):
    """Assert that actual_value is an integer greater than lower_limit."""
    result = isinstance(actual_value, int)
    if result: result = (actual_value > lower_limit)
    if result: return result
    else:
        raise AssertionError(
            "{!r} is NOT an INTEGER, or is LESS than or EQUAL to {!r}".format(
                actual_value, lower_limit
            ))

def assert_is(actual_value, expected_value):
    """Assert that actual_value is identical to expected_value."""
    result = (actual_value is expected_value)
    if result: return result
    else:
        raise AssertionError(
            "{!r} is NOT identical to {!r}".format(
                actual_value, expected_value
            ))

def assert_none(value):
    return assert_is(value, None)

def assert_nonempty_string(value):
    return assert_instance(value, str) and assert_not_equal(value, '')

def assert_not(actual_value, expected_value):
    """Assert that actual_value is NOT identical to expected_value."""
    result = (actual_value is not expected_value)
    if result: return result
    else:
        raise AssertionError(
            "{!r} is IDENTICAL to {!r}".format(
                actual_value, expected_value
            ))

def assert_not_equal(actual_value, expected_value):
    """Assert that actual_value is NOT equal to expected_value."""
    result = (actual_value != expected_value)
    if result: return result
    else:
        raise AssertionError(
            "{!r} EQUALS {!r}".format(
                actual_value, expected_value
            ))

def assert_not_instance(actual_value, expected_types):
    result = not isinstance(actual_value, expected_types)
    if result: return result
    else:
        raise AssertionError(
            'Value is {!r}, which is one of DISALLOWED {!r}'.format(
                actual_value, expected_types
            ))

def assert_not_none(value):
    return assert_not(value, None)

def assert_relative_path(path):
    result = not path.is_absolute()
    if result: return result
    else:
        raise AssertionError(
            '{!r} is NOT a relative path'.format(
                path
            ))

def assert_range(actual_value, lower_limit, higher_limit):
    """Assert that actual_value is within range (inclusive)."""
    result = (lower_limit <= actual_value <= higher_limit)
    if result: return result
    else:
        raise AssertionError(
            "{!r} is OUTSIDE RANGE of {!r} to {!r} inclusive".format(
                actual_value, lower_limit, higher_limit
            ))

def assert_true(actual_value):
    result = bool(actual_value)
    if result: return result
    else:
        raise AssertionError(
            'Value is {!r}, INSTEAD of {!r}'.format(
                actual_value, True
            ))

'''DisabledContent
# TODO: Rewrite following implementations in favor of new style above

def has_type(actual_value, expected_type):
    return isinstance(actual_value, expected_type)

def has_type_message(actual_value, expected_type):
    return "Value is of type '{0}', instead of type '{1}'".format(
        type(actual_value), expected_type
        )

def assert_is_less_than(smallerName, smallerValue, biggerName, biggerValue):
    return smallerValue <= biggerValue

def assert_is_less_than_message(smallerName, smallerValue, biggerName, biggerValue):
    return "{0} '{1}' must be less than (or equal to) {2} '{3}'".format(
        smallerName, smallerValue, biggerName, biggerValue
        )

def unrecognized_message(actual_value, unexpected_kind, name):
    return "Value '{0}' is an unrecognized {1} of '{2}'".format(actual_value, name, unexpected_kind)
'''


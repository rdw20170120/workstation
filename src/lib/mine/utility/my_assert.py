#!/usr/bin/env false
"""My module for assertions.

The Python `assert` statement takes an optional message argument,
but it has to be specified on each statement.
When the message argument is absent
then the resulting AssertionError
has an empty message that completely fails to communicate.
I want messages on EVERY assertion
that consistently match the assertion logic,
so I chose to refactor the assertions implementation.
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
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)


def at_least(actual_value, expected_value):
    """Assert that actual_value is at least expected_value."""
    result = actual_value >= expected_value
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} is LESS than {!r}".format(actual_value, expected_value)
        )


def at_most(actual_value, expected_value):
    """Assert that actual_value is expected_value at most."""
    result = actual_value <= expected_value
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} is GREATER than {!r}".format(actual_value, expected_value)
        )


def encoding_is_utf8(encoding):
    # TODO: Add tests for complete list of variants
    # TODO: Add handling for both string and enum versions
    result = encoding in ("utf_8", "utf-8", "UTF8")
    if result:
        return result
    else:
        raise AssertionError("Encoding {!r} is NOT a variant of UTF8".format(encoding))


def equal(actual_value, expected_value):
    """Assert that actual_value is equal to expected_value."""
    result = actual_value == expected_value
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} does NOT equal {!r}".format(actual_value, expected_value)
        )


def false(actual_value):
    result = not bool(actual_value)
    if result:
        return result
    else:
        raise AssertionError(
            "Value is {!r}, INSTEAD of {!r}".format(actual_value, False)
        )


def greater(actual_value, lower_limit):
    """Assert that actual_value is greater than lower_limit."""
    result = actual_value > lower_limit
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} is LESS than or EQUAL to {!r}".format(actual_value, lower_limit)
        )


def identical(actual_value, expected_value):
    """Assert that actual_value is identical to expected_value."""
    result = actual_value is expected_value
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} is NOT identical to {!r}".format(actual_value, expected_value)
        )


def in_(actual_value, expected_values):
    result = actual_value in expected_values
    if result:
        return result
    else:
        raise AssertionError(
            "Value is {!r}, NOT IN {!r}".format(actual_value, expected_values)
        )


def instance(actual_value, expected_types):
    result = isinstance(actual_value, expected_types)
    if result:
        return result
    else:
        raise AssertionError(
            "Value is {!r}, INSTEAD of {!r}".format(actual_value, expected_types)
        )


def integer_at_least(actual_value, expected_value):
    """Assert that actual_value is an integer of at least expected_value."""
    result = isinstance(actual_value, int)
    if result:
        result = actual_value >= expected_value
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} is NOT an INTEGER, or is LESS than {!r}".format(
                actual_value, expected_value
            )
        )


def integer_greater(actual_value, lower_limit):
    """Assert that actual_value is an integer greater than lower_limit."""
    result = isinstance(actual_value, int)
    if result:
        result = actual_value > lower_limit
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} is NOT an INTEGER, or is LESS than or EQUAL to {!r}".format(
                actual_value, lower_limit
            )
        )


def none(value):
    return identical(value, None)


def nonempty_string(value):
    return instance(value, str) and not_equal(value, "")


def not_(actual_value, expected_value):
    """Assert that actual_value is NOT identical to expected_value."""
    result = actual_value is not expected_value
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} is IDENTICAL to {!r}".format(actual_value, expected_value)
        )


def not_equal(actual_value, expected_value):
    """Assert that actual_value is NOT equal to expected_value."""
    result = actual_value != expected_value
    if result:
        return result
    else:
        raise AssertionError("{!r} EQUALS {!r}".format(actual_value, expected_value))


def not_in(actual_value, expected_values):
    result = actual_value not in expected_values
    if result:
        return result
    else:
        raise AssertionError(
            "Value is {!r}, IN {!r}".format(actual_value, expected_values)
        )


def not_instance(actual_value, expected_types):
    result = not isinstance(actual_value, expected_types)
    if result:
        return result
    else:
        raise AssertionError(
            "Value is {!r}, which is one of DISALLOWED {!r}".format(
                actual_value, expected_types
            )
        )


def not_none(value):
    return not_(value, None)


def range(actual_value, lower_limit, higher_limit):
    """Assert that actual_value is within range (inclusive)."""
    result = lower_limit <= actual_value <= higher_limit
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} is OUTSIDE RANGE of {!r} to {!r} inclusive".format(
                actual_value, lower_limit, higher_limit
            )
        )


def true(actual_value):
    result = bool(actual_value)
    if result:
        return result
    else:
        raise AssertionError(
            "Value is {!r}, INSTEAD of {!r}".format(actual_value, True)
        )


"""DisabledContent
"""

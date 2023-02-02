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


def absolute_directory(path):
    result = path.is_absolute()
    if result:
        result = path.is_dir()
    if result:
        return result
    else:
        raise AssertionError("{!r} is NOT an absolute directory".format(path))


def absolute_file(path):
    result = path.is_absolute()
    if result:
        result = path.is_file()
    if result:
        return result
    else:
        raise AssertionError("{!r} is NOT an absolute file".format(path))


def existing_absolute_path(path):
    result = path.is_absolute()
    if result:
        result = path.exists()
    if result:
        return result
    else:
        raise AssertionError(
            "{!r} is NOT an existing absolute path".format(path)
        )


"""DisabledContent
"""

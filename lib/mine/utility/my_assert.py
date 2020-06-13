#!/bin/false
"""My module for managing assertions."""

def has_type(actual_value, expected_type):
    """Return whether actual_value has expected_type"""
    return isinstance(actual_value, expected_type)

def has_type_message(actual_value, expected_type):
    return "Value is of type '{0}', instead of type '{1}'".format(
        type(actual_value), expected_type
        )

def is_less_than(smallerName, smallerValue, biggerName, biggerValue):
    return smallerValue <= biggerValue

def is_less_than_message(smallerName, smallerValue, biggerName, biggerValue):
    return "{0} '{1}' must be less than (or equal to) {2} '{3}'".format(
        smallerName, smallerValue, biggerName, biggerValue
        )

def unrecognized_message(actual_value, unexpected_kind, name):
    """Return message for unrecognized actual_value of unexpected_kind described by name"""
    return "Value '{0}' is an unrecognized {1} of '{2}'".format(actual_value, name, unexpected_kind)


''' Disabled content
'''


from my_assert import unrecognized_message


class UnrecognizedValueError(ValueError):
    def __init__(self, actual_value, unexpected_kind, name):
        super(ValueError, self).__init__(
            unrecognized_message(actual_value, unexpected_kind, name)
        )


""" Disabled content
"""

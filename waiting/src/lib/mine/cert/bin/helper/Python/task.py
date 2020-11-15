import sys
import throw_out_your_templates

from my_instruction import get_output
from my_instruction import htmltags
from my_instruction import print_output
from webpage import Html5


class Task(Html5):
    def __init__(self, identifier, description):
        super(Task, self).__init__(
            "task", "Task {0} - {1}".format(identifier, description)
        )

    def _step_header(self, number, description):
        return htmltags.h2("step")[
            "Step {0} - {1}".format(number, description)
        ]

    def add_step_header(self, number, description):
        return self.add(self._step_header(number, description))


""" Disabled content
"""

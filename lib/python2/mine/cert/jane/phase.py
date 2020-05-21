"""
    Simple enum that represents the phases of exam processing.
"""

from enum import Enum


class Phase(Enum):
    """Simple enum that represents all of the valid exam phases."""

    instruction = 1
    prepare = 2
    initialize = 3
    began = 4
    answer = 5
    ended = 6
    answered = 7
    grade = 8
    graded = 9
    score = 10
    scored = 11
    unanswer = 12
    final = 13

    @classmethod
    def names(cls):
        """Simple method that returns a list of all phase names"""
        return list(cls.__members__)

    def ignored(self):
        """Simple method that indicates whether the phase will be ignored
        during processing."""
        return self in (Phase.instruction, Phase.prepare)

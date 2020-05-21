#!/bin/false

from .queue import TaskQueue

def test_queue():
    assert TaskQueue() is not None


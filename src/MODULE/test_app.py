#!/usr/bin/env false
"""
"""
from pathlib import Path

from .app import MyApp

def test_MyApp():
    assert MyApp(Path()) is not None

'''DisabledContent
'''


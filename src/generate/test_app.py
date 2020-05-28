#!/bin/false

from pathlib import Path

from .app import ContentGeneratorApp

def test_ContentGeneratorApp():
    assert ContentGeneratorApp(Path(), Path()) is not None


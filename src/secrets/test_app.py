#!/bin/false

from pathlib import Path

from .app import SecretsManagerApp

def test_SecretsManagerApp():
    assert SecretsManagerApp(Path()) is not None


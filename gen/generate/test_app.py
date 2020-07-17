#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from   pathlib import Path
import sys
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .app import ContentGeneratorApp


def test_ContentGeneratorApp():
    assert ContentGeneratorApp(Path()) is not None

def test_sys_getdefaultencoding():
    assert sys.getdefaultencoding() == 'utf-8'

def test_sys_getfilesystemencoding():
    assert sys.getfilesystemencoding() == 'utf-8'

def test_sys_stderr_encoding ():
    assert sys.stderr.encoding == 'UTF8'

def test_sys_stdin_encoding ():
    assert sys.stdin.encoding is None

def test_sys_stdout_encoding ():
    assert sys.stdout.encoding == 'UTF8'

'''DisabledContent
'''


#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
import sys
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility import my_assert as is_
# Co-located modules (relative references, NOT packaged, in project)
from .app import MyApp


def test_app():
    assert is_.not_none(MyApp(Path(), Path()))

def test_sys_getdefaultencoding():
    assert is_.encoding_is_utf8(sys.getdefaultencoding())

def test_sys_getfilesystemencoding():
    assert is_.encoding_is_utf8(sys.getfilesystemencoding())

def test_sys_stderr_encoding ():
    assert is_.encoding_is_utf8(sys.stderr.encoding)

def test_sys_stdin_encoding ():
    assert is_.none(sys.stdin.encoding)

def test_sys_stdout_encoding ():
    assert is_.encoding_is_utf8(sys.stdout.encoding)

'''DisabledContent
'''


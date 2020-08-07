#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from   pathlib import Path
import sys
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .app import MyApp


def _encoding_is_utf8(encoding):
    return encoding == 'utf-8' or encoding == 'UTF8'

def test_app():
    assert MyApp(Path(), Path()) is not None

def test_sys_getdefaultencoding():
    assert _encoding_is_utf8(sys.getdefaultencoding())

def test_sys_getfilesystemencoding():
    assert _encoding_is_utf8(sys.getfilesystemencoding())

def test_sys_stderr_encoding ():
    assert _encoding_is_utf8(sys.stderr.encoding)

def test_sys_stdin_encoding ():
    assert sys.stdin.encoding is None

def test_sys_stdout_encoding ():
    assert _encoding_is_utf8(sys.stdout.encoding)

'''DisabledContent
'''


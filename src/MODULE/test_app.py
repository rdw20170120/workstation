#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
import sys
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .app import MyApp


def test_MyApp():
    assert MyApp(None) is not None

def test_sys_getdefaultencoding():
    assert sys.getdefaultencoding() == 'utf-8'

def test_sys_getfilesystemencoding():
    assert sys.getfilesystemencoding() == 'utf-8'

def test_sys_stderr_encoding ():
    assert sys.stderr.encoding == 'utf-8'

def test_sys_stdin_encoding ():
    assert sys.stdin.encoding is None

def test_sys_stdout_encoding ():
    assert sys.stdout.encoding == 'utf-8'

'''DisabledContent
'''


#!/usr/bin/env false
"""
"""
from .source     import visitor_map
from ..structure import *


###############################################################################

def disabled_content_footer():
    return [
        line(),
        "'''", 'DisabledContent', eol(),
        "'''", eol(),
        line(),
    ]

def library_module_header():
    return [
        shebang_false(),
        '"""', eol(),
        '"""', eol(),
    ]

def main_module_header():
    return [
        shebang_false(),
        '"""', eol(),
        '"""', eol(),
    ]

def package_module_header():
    return [
        shebang_false(),
        line(),
    ]

def script_module_header():
    return [
        shebang_python3(),
        '"""', eol(),
        '"""', eol(),
    ]

###############################################################################

def shebang_python3():
    return shebang_thru_env('python3')

'''DisabledContent
'''


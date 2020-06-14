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

def python_script_header():
    return [
        shebang_python3(),
        '"""', eol(),
        '"""', eol(),
        line(),
    ]

###############################################################################

def shebang_python3():
    return shebang_thru_env('python3')


''' Disabled content
'''


from .python_source    import visitor_map
from .script_structure import *


###############################################################################

def python_script_header():
    return [
        shebang_python3(),
        note('Intended to be executed directly by the user.'),
    ]

###############################################################################

def shebang_python3():
    return shebang_thru_env('python3')


''' Disabled content
'''


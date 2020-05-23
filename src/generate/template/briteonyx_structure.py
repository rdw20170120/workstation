# from .briteonyx_script import visitor_map
from .bash_structure import *
from .bash_structure import _Command


def source_script(file_name):
    return [
        assign(vn('Script'), file_name), eol(),
        require_script(dq(vr('Script'))), or_(), failed(), or_(), return_last_status(), eol(),
        source(dq(vr('Script'))), or_(), failed(), or_(), return_last_status(), eol(),
    ]

####################################################################################################
""" Disabled content
####################################################################################################

class _BoLogInfo(_Command):
    def __init__(self, *elements):
        _Command.__init__(self, 'boLogInfo', dq(elements))

def bo_log_info(*elements):
    return _BoLogInfo(*elements)

####################################################################################################

class _Failed(_Command):
    def __init__(self):
        _Command.__init__(self, 'boFailed', dq('$0'), dq('$LINENO'), '$?')

def failed():
    return _Failed()

####################################################################################################

class _Log(_Command):
    def __init__(self, command, *elements):
        _Command.__init__(self, command, dq(elements))

def log_debug(*elements):
    return _Log('logDebug', *elements)

def log_error(*elements):
    return _Log('logError', *elements)

def log_fatal(*elements):
    return _Log('_logFatal', *elements)

def log_info(*elements):
    return _Log('logInfo', *elements)

def log_warn(*elements):
    return _Log('logWarn', *elements)

####################################################################################################

class _BoRequireDirectory(_Command):
    def __init__(self, directory_name):
        _Command.__init__(self, 'boDirectoryRequire', directory_name)

def require_directory(directory_name):
    return _BoRequireDirectory(dq(directory_name))

####################################################################################################

class _BoRequireScript(_Command):
    def __init__(self, file_name):
        _Command.__init__(self, 'boScriptRequire', file_name)

def require_script(file_name):
    return _BoRequireScript(file_name)

####################################################################################################

class _BoRequireVariable(_Command):
    def __init__(self, variable_name):
        _Command.__init__(self, 'boVariableRequire', variable_name)

def require_variable(variable_name):
    return _BoRequireVariable(variable_name)

####################################################################################################

class _BoTraceVariable(_Command):
    def __init__(self, variable_name):
        _Command.__init__(self, 'boTraceVariable', variable_name)

def trace_variable(variable_name):
    return _BoTraceVariable(variable_name)

####################################################################################################

def execution_trace():
    return [
        string_is_not_null(vr('BO_Trace')),
        and_(),
        echo_trace('Executing ', sq(vr('BASH_SOURCE'))),
        eol(),
    ]

"""


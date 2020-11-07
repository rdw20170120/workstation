#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
import ast
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility import my_assert as is_
# Co-located modules (relative references, NOT packaged, in project)


def dict_from_string(the_string):
    if the_string is None: return None
    assert is_.instance(the_string, str)
    result = ast.literal_eval(the_string)
    assert is_.instance(result, dict)
    return result

def replace_last(the_string, find, replace):
    if the_string is None: return None
    if find is None: return the_string
    result = the_string
    i = the_string.rfind(find)
    if i >= 0:
        if replace is None:
            result = the_string[0:i] + the_string[i + len(find):]
        else:
            result = the_string[0:i] + replace + the_string[i + len(find):]
    return result

def string_without_prefix(the_string, the_prefix):
    if the_string is None: return None
    if the_prefix is None: return the_string
    if the_string.startswith(the_prefix): return the_string[len(the_prefix):]
    else: return the_string

def string_without_suffix(the_string, the_suffix):
    if the_string is None: return None
    if the_suffix is None: return the_string
    if the_string.endswith(the_suffix):
        length = len(the_string) - len(the_suffix)
        return the_string[0:length]
    else: return the_string

'''DisabledContent
'''


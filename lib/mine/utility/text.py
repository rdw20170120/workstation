#!/bin/false

import ast

def dict_from_string(the_string):
    if the_string is None: return None
    assert isinstance(the_string, str)
    result = ast.literal_eval(the_string)
    assert isinstance(result, dict)
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


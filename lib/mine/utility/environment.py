#!/usr/bin/env false
"""
TODO: REVIEW: this module against its siblings.
"""
from os import environ


def get(key):
    return environ[key]

def has(key):
    return key in environ

def put(key, value):
    environ[key] = value

'''DisabledContent
'''


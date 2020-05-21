#!/bin/false

import os

def get(key):
    return os.environ[key]

def put(key, value):
    os.environ[key] = value


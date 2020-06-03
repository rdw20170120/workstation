#!/bin/false

from os import environ

def get(key):
    return environ[key]

def put(key, value):
    environ[key] = value


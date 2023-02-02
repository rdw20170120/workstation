#!/usr/bin/env false
"""Manipulate filesystem pathnames, but WITHOUT manipulating the filesystem itself."""
# Internal packages (absolute references, distributed with Python)
from logging import getLogger
from pathlib import Path
from pathlib import PurePath

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


log = getLogger(__name__)


def basename_has_suffix(path_, suffix):
    assert is_.instance(suffix, str)
    return str(path_).endswith(suffix)


def split_basename(path_):
    parent, basename = split_path(path_)
    name = PurePath(basename)
    suffixes = ""
    while True:
        suffix, name = name.suffix, name.stem
        if not suffix:
            break
        suffixes = suffix + suffixes
        name = PurePath(name)
    return str(name), suffixes


def split_path(path_):
    if not isinstance(path_, Path):
        path_ = PurePath(path_)
    return path_.parent, path_.name


"""DisabledContent
"""


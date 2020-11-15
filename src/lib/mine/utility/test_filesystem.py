#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility.filesystem import basename_has_suffix
from utility.filesystem import split_basename
from utility.filesystem import split_path
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


def test_basename_has_suffix():
    assert is_.false(basename_has_suffix("name", ".ext"))
    assert is_.true(basename_has_suffix("name.ext", ".ext"))
    assert is_.false(basename_has_suffix(Path("name"), ".ext"))
    assert is_.true(basename_has_suffix(Path("name.ext"), ".ext"))
    assert is_.true(basename_has_suffix(Path("name-stuff.ext"), "-stuff.ext"))


def test_split_basename():
    n, e = split_basename("name")
    assert is_.equal(n, "name")
    assert is_.equal(e, "")

    n, e = split_basename("name.ext")
    assert is_.equal(n, "name")
    assert is_.equal(e, ".ext")

    n, e = split_basename("name.zzz.ext")
    assert is_.equal(n, "name")
    assert is_.equal(e, ".zzz.ext")


def test_split_path():
    p, b = split_path("")
    assert is_.equal(p, Path("."))
    assert is_.equal(b, "")

    p, b = split_path("a/b/c")
    assert is_.equal(p, Path("a/b"))
    assert is_.equal(b, "c")

    p, b = split_path("a/b/c/name.ext")
    assert is_.equal(p, Path("a/b/c"))
    assert is_.equal(b, "name.ext")


"""DisabledContent
"""

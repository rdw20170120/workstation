#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility.pathname import basename_has_suffix
from utility.pathname import split_basename
from utility.pathname import split_path
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


def test_basename_has_suffix_00():
    assert is_.false(basename_has_suffix("name", ".ext"))


def test_basename_has_suffix_01():
    assert is_.true(basename_has_suffix("name.ext", ".ext"))


def test_basename_has_suffix_02():
    assert is_.false(basename_has_suffix(Path("name"), ".ext"))


def test_basename_has_suffix_03():
    assert is_.true(basename_has_suffix(Path("name.ext"), ".ext"))


def test_basename_has_suffix_04():
    assert is_.true(basename_has_suffix(Path("name-stuff.ext"), "-stuff.ext"))


def test_split_basename_00():
    n, e = split_basename("name")
    assert is_.equal(n, "name")
    assert is_.equal(e, "")


def test_split_basename_01():
    n, e = split_basename("name.ext")
    assert is_.equal(n, "name")
    assert is_.equal(e, ".ext")


def test_split_basename_02():
    n, e = split_basename("name.zzz.ext")
    assert is_.equal(n, "name")
    assert is_.equal(e, ".zzz.ext")


def test_split_path_00():
    p, b = split_path("")
    assert is_.equal(p, Path("."))
    assert is_.equal(b, "")


def test_split_path_01():
    p, b = split_path("a/b/c")
    assert is_.equal(p, Path("a/b"))
    assert is_.equal(b, "c")


def test_split_path_02():
    p, b = split_path("a/b/c/name.ext")
    assert is_.equal(p, Path("a/b/c"))
    assert is_.equal(b, "name.ext")


"""DisabledContent
"""

#!/usr/bin/env false
"""Test corresponding source-generation module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# from pytest import fixture
# from pytest import mark
# from pytest import param
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from src_gen.common import *
from src_gen.script.material import *
from src_gen.renderer import Renderer
from utility import my_assert as is_

# from utility import my_assert_filesystem as fs_is_
# from utility import my_assert_pathname as pn_is_
# Project modules   (relative references, NOT packaged, in project)
from .frame import *
from .material import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


# TODO: def test_import_():
# TODO: def test_import_from():


def test_shebang_cat():
    assert is_.equal(s(shebang_cat()), "#!/usr/bin/env cat\n")


def test_shebang_false():
    assert is_.equal(s(shebang_false()), "#!/usr/bin/env false\n")


def test_shebang_thru_env_01():
    with raises(AssertionError):
        shebang_thru_env(None)


def test_shebang_thru_env_02():
    assert is_.equal(s(shebang_thru_env("")), "#!/usr/bin/env\n")


def test_shebang_thru_env_03():
    assert is_.equal(s(shebang_thru_env("Test")), "#!/usr/bin/env Test\n")


"""DisabledContent
"""

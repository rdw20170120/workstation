#!/usr/bin/env false
"""Test corresponding source-generation module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from src_gen.common import *
from src_gen.renderer import Renderer
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .material import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_command_01():
    assert is_.equal(s(command("Test")), "Test")


def test_command_02():
    assert is_.equal(s(command("Test", None)), "Test")


def test_command_03():
    assert is_.equal(s(command("Test", "")), "Test")


def test_command_04():
    assert is_.equal(s(command("Test", "123")), "Test 123")


def test_comment_01():
    assert is_.equal(s(comment()), "#\n")


def test_comment_02():
    assert is_.equal(s(comment(None)), "#\n")


def test_comment_03():
    assert is_.equal(s(comment("")), "#\n")


def test_comment_04():
    assert is_.equal(s(comment("Test")), "# Test\n")


def test_comment_05():
    assert is_.equal(s(comment("Test", None)), "# Test\n")


def test_comment_06():
    assert is_.equal(s(comment("Test", "")), "# Test\n")


def test_comment_07():
    assert is_.equal(s(comment("Test", "123")), "# Test123\n")


def test_indent():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(indent()), 4 * " ")
    with raises(TypeError):
        indent(None)
    assert is_.equal(s(indent(-1)), -1 * 4 * " ")
    assert is_.equal(s(indent(0)), 0 * 4 * " ")
    assert is_.equal(s(indent(1)), 1 * 4 * " ")
    assert is_.equal(s(indent(2)), 2 * 4 * " ")
    assert is_.equal(s(indent(9)), 9 * 4 * " ")


def test_no():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(no()), "# NO: \n")
    assert is_.equal(s(no(None)), "# NO: \n")
    assert is_.equal(s(no("")), "# NO: \n")
    assert is_.equal(s(no("Test")), "# NO: Test\n")
    assert is_.equal(s(no("Test", None)), "# NO: Test\n")
    assert is_.equal(s(no("Test", "")), "# NO: Test\n")
    assert is_.equal(s(no("Test", "123")), "# NO: Test123\n")


def test_note():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(note()), "# NOTE: \n")
    assert is_.equal(s(note(None)), "# NOTE: \n")
    assert is_.equal(s(note("")), "# NOTE: \n")
    assert is_.equal(s(note("Test")), "# NOTE: Test\n")
    assert is_.equal(s(note("Test", None)), "# NOTE: Test\n")
    assert is_.equal(s(note("Test", "")), "# NOTE: Test\n")
    assert is_.equal(s(note("Test", "123")), "# NOTE: Test123\n")


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


# TDDO: def test_x():

"""DisabledContent
"""

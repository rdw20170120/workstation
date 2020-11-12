#!/usr/bin/env false
"""Generate all Markdown documents."""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from src_gen.document.markdown.source import generate as gen
from src_gen.document.markdown.structure import *

# Co-located modules (relative references, NOT packaged, in project)


def _document():
    return [
        h1("TODO"),
    ]


def _generate_bin(dir_):
    sub = Path("bin")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("bin", "lib")
    gen(_document(), dir_, sub, "README.md")


def _generate_briteonyx(dir_):
    sub = Path("BriteOnyx")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("BriteOnyx", "bin")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("BriteOnyx", "bin", "lib")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("BriteOnyx", "doc")
    gen(_document(), dir_, sub, "HowTo-activate_this_project.md")
    gen(_document(), dir_, sub, "HowTo-execute_application.md")
    gen(_document(), dir_, sub, "HowTo-install-packages.md")
    gen(_document(), dir_, sub, "HowTo-setup-AWS_CLI.md")
    gen(
        _document(),
        dir_,
        sub,
        "HowTo-setup-Python_virtual_environment.md",
    )
    gen(_document(), dir_, sub, "HowTo-setup-source_control.md")
    gen(_document(), dir_, sub, "HowTo-setup-workstation.md")
    gen(_document(), dir_, sub, "HowTo-test.md")
    gen(_document(), dir_, sub, "README.md")
    gen(_document(), dir_, sub, "project_initiation.md")


def _generate_doc(dir_):
    sub = Path("doc")
    gen(_document(), dir_, sub, "README.md")


def _generate_home(dir_):
    sub = Path("home")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("home", ".ssh")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("home", "Linux")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("home", "bin")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("home", "bin", "lib")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("home", "macOS")
    gen(_document(), dir_, sub, "README.md")


def _generate_others(dir_):
    sub = Path("cfg")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("cfg", "sample")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("out")
    gen(_document(), dir_, sub, "README.md")


def _generate_project(dir_):
    sub = Path(".")
    gen(_document(), dir_, sub, "README.md")
    gen(_document(), dir_, sub, "TODO.md")


def _generate_src(dir_):
    sub = Path("src")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("src", "app")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("src", "gen")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("src", "lib")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("src", "lib", "mine")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("src", "lib", "mine", "src_gen")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("src", "lib", "mine", "throw_out_your_templates")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("src", "lib", "mine", "utility")
    gen(_document(), dir_, sub, "README.md")
    sub = Path("src", "lib", "third_party")
    gen(_document(), dir_, sub, "README.md")


def generate(directory):
    _generate_bin(directory)
    _generate_briteonyx(directory)
    _generate_doc(directory)
    _generate_home(directory)
    _generate_others(directory)
    _generate_project(directory)
    _generate_src(directory)


"""DisabledContent
"""

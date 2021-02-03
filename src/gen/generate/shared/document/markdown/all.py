#!/usr/bin/env false
"""Generate all shared Markdown documents."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.document.markdown.complete import generate_document as document

# Project modules   (relative references, NOT packaged, in project)


def _generate_bin(dir_):
    sub = dir_
    document(sub, "README.md")
    sub = dir_ / "lib"
    document(sub, "README.md")


def _generate_briteonyx(dir_):
    sub = dir_
    document(sub, "README.md")
    sub = dir_ / "bin"
    document(sub, "README.md")
    sub = sub / "lib"
    document(sub, "README.md")
    sub = dir_ / "doc"
    document(sub, "HowTo-activate_this_project.md")
    document(sub, "HowTo-execute_application.md")
    document(sub, "HowTo-setup-Python_virtual_environment.md")
    document(sub, "HowTo-setup-source_control.md")
    document(sub, "HowTo-setup-workstation.md")
    document(sub, "HowTo-test.md")
    document(sub, "README.md")
    document(sub, "project_initiation.md")


def _generate_doc(dir_):
    sub = dir_
    document(sub, "README.md")


def _generate_project(dir_):
    sub = dir_
    document(sub, "HowTo-use_this_project.md")
    document(sub, "LICENSE.md")
    document(sub, "README.md")
    document(sub, "TODO.md")
    sub = dir_ / "cfg"
    document(sub, "README.md")
    sub = sub / "sample"
    document(sub, "README.md")
    sub = dir_ / "out"
    document(sub, "README.md")


def _generate_src(dir_):
    sub = dir_
    document(sub, "README.md")
    sub = dir_ / "app"
    document(sub, "README.md")
    sub = dir_ / "gen"
    document(sub, "README.md")
    sub = dir_ / "lib"
    document(sub, "README.md")
    _generate_mine(sub / "mine")
    _generate_third_party(sub / "third_party")


def _generate_mine(dir_):
    sub = dir_
    document(sub, "README.md")
    sub = dir_ / "src_gen"
    document(sub, "README.md")
    sub = dir_ / "throw_out_your_templates"
    document(sub, "README.md")
    sub = dir_ / "utility"
    document(sub, "README.md")


def _generate_third_party(dir_):
    sub = dir_
    document(sub, "README.md")


def generate(directory):
    _generate_bin(directory / "bin")
    _generate_briteonyx(directory / "BriteOnyx")
    _generate_doc(directory / "doc")
    _generate_project(directory)
    _generate_src(directory / "src")


"""DisabledContent
"""

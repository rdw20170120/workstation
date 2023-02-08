#!/usr/bin/env false
"""Generate all custom source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.markdown.complete import document
from src_gen.briteonyx.complete import executed
from src_gen.briteonyx.complete import sourced
from src_gen.bash.complete import activation
from src_gen.python.complete import generator
from src_gen.python.complete import library
from src_gen.python.complete import main
from src_gen.python.complete import package
from src_gen.python.complete import script
from src_gen.python.complete import suite
from utility.config import Config
from src_gen.bash.source import generate as bash
from src_gen.briteonyx.source import generate as briteonyx
from src_gen.markdown.source import generate as markdown
from src_gen.python.source import generate as python

# Project modules   (relative references, NOT packaged, in project)


def _generate_bin(dir_):
    sub = dir_
    briteonyx(executed(), sub, "sync_on_macOS")
    sub = dir_ / "lib"
    briteonyx(activation(), sub, "configure-Anaconda.bash")
    briteonyx(activation(), sub, "declare.bash")


def _generate_home(dir_):
    sub = dir_ / ".ssh"
    markdown(document(), sub, "README.md")
    sub = dir_ / "Linux"
    markdown(document(), sub, "README.md")
    sub = dir_ / "bin"
    bash(executed(), sub, "24-bit-color.sh")
    bash(executed(), sub, "clone_from_GitHub_by_Rob")
    bash(executed(), sub, "clone_from_GitHub_by_TextNow")
    bash(executed(), sub, "clone_from_GitHub_by_others")
    bash(executed(), sub, "clone_from_GitLab_by_Rob")
    bash(executed(), sub, "clone_from_GitLab_by_SWA")
    bash(executed(), sub, "clone_from_GitLab_by_Yum")
    bash(executed(), sub, "clone_from_GitLab_by_others")
    bash(executed(), sub, "git_config_user_Me_at_SWA")
    bash(executed(), sub, "git_config_user_Me_at_TextNow")
    bash(executed(), sub, "git_config_user_Me_at_home")
    bash(executed(), sub, "grep_stable_projects_for_all_phrases")
    bash(executed(), sub, "grep_stable_projects_for_phrase")
    bash(executed(), sub, "secure")
    sub = dir_ / "bin" / "lib"
    bash(sourced(), sub, "declare-git.bash")
    sub = dir_ / "macOS"
    markdown(document(), sub, "README.md")
    sub = dir_ / "macOS" / "bin"
    bash(executed(), sub, "homebrew-install")
    bash(executed(), sub, "homebrew-list")
    bash(executed(), sub, "homebrew-populate")
    bash(executed(), sub, "homebrew-update")
    bash(executed(), sub, "homebrew-upgrade")
    bash(executed(), sub, "homebrew-uninstall")
    markdown(document(), sub, "README.md")


def _generate_src(dir_):
    sub = dir_
    _generate_src_app(sub / "app")


def _generate_src_app(dir_):
    sub = dir_ / Config().application_name
    sub = dir_ / Config().application_name / "task"
    python(package(), sub, "__init__.py")
    python(library(), sub, "bootstrap.py")
    python(library(), sub, "mapping.py")
    python(library(), sub, "scan_directory.py")
    python(suite(), sub, "test_mapping.py")
    python(suite(), sub, "test_task.py")


def generate(directory):
    # NOTE: Typically,
    # there should NOT exist
    # any custom Bash scripts.
    # Any Bash scripts
    # should be shared,
    # or they should be
    # BriteOnyx scripts
    # instead.
    _generate_bin(directory / "bin")
    _generate_home(directory / "home")
    _generate_src(directory / "src")


"""DisabledContent
"""

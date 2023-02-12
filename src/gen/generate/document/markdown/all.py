#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.document.markdown.complete import *
from src_gen.document.markdown.source import generate as markdown
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)


def _generate(dir_):
    _generate_bin(dir_ / "bin")
    _generate_briteonyx(dir_ / "BriteOnyx")
    _generate_cfg(dir_ / "cfg")
    _generate_doc(dir_ / "doc")
    _generate_home(dir_ / "home")
    _generate_out(dir_ / "out")
    _generate_src(dir_ / "src")
    markdown(document(), dir_, "HowTo-use_this_project.md")
    markdown(document(), dir_, "LICENSE.md")
    markdown(document(), dir_, "README.md")
    markdown(document(), dir_, "TODO.md")


def _generate_bin(dir_):
    _generate_bin_lib(dir_ / "lib")
    markdown(document(), dir_, "README.md")


def _generate_bin_lib(dir_):
    markdown(document(), dir_, "README.md")


def _generate_briteonyx(dir_):
    _generate_briteonyx_bin(dir_ / "bin")
    _generate_briteonyx_doc(dir_ / "doc")
    markdown(document(), dir_, "README.md")


def _generate_briteonyx_bin(dir_):
    _generate_briteonyx_bin_lib(dir_ / "lib")
    markdown(document(), dir_, "README.md")


def _generate_briteonyx_bin_lib(dir_):
    markdown(document(), dir_, "README.md")


def _generate_briteonyx_doc(dir_):
    markdown(document(), dir_, "HowTo-activate_this_project.md")
    markdown(document(), dir_, "HowTo-execute_application.md")
    markdown(document(), dir_, "HowTo-install-OpenJDK-15.md")
    markdown(document(), dir_, "HowTo-install-packages.md")
    markdown(document(), dir_, "HowTo-setup-AWS_CLI.md")
    markdown(document(), dir_, "HowTo-setup-source_control.md")
    markdown(document(), dir_, "HowTo-setup-workstation.md")
    markdown(document(), dir_, "HowTo-test.md")
    markdown(document(), dir_, "HowTo-use-Anaconda.md")
    markdown(document(), dir_, "HowTo-use-Homebrew.md")
    markdown(document(), dir_, "HowTo-use-Vim.md")
    markdown(document(), dir_, "README.md")
    markdown(document(), dir_, "project_initiation.md")
    markdown(document(), dir_, "testssl.md")


def _generate_cfg(dir_):
    _generate_cfg_sample(dir_ / "sample")
    markdown(document(), dir_, "README.md")


def _generate_cfg_sample(dir_):
    markdown(document(), dir_, "README.md")


def _generate_doc(dir_):
    markdown(document(), dir_, "README.md")


def _generate_home(dir_):
    _generate_home_bin(dir_ / "bin")
    _generate_home_linux(dir_ / "Linux")
    _generate_home_macos(dir_ / "macOS")
    _generate_home_ssh(dir_ / ".ssh")
    markdown(document(), dir_, "README.md")


def _generate_home_bin(dir_):
    _generate_home_bin_lib(dir_ / "lib")
    markdown(document(), dir_, "README.md")


def _generate_home_bin_lib(dir_):
    markdown(document(), dir_, "README.md")


def _generate_home_linux(dir_):
    markdown(document(), dir_, "README.md")


def _generate_home_macos(dir_):
    _generate_home_macos_bin(dir_ / "bin")
    markdown(document(), dir_, "README.md")


def _generate_home_macos_bin(dir_):
    markdown(document(), dir_, "README.md")


def _generate_home_ssh(dir_):
    markdown(document(), dir_, "README.md")


def _generate_out(dir_):
    markdown(document(), dir_, "README.md")


def _generate_src(dir_):
    _generate_src_app(dir_ / "app")
    _generate_src_gen(dir_ / "gen")
    _generate_src_lib(dir_ / "lib")
    markdown(document(), dir_, "README.md")


def _generate_src_app(dir_):
    _generate_src_app_name(dir_ / Config().application_name)
    markdown(document(), dir_, "README.md")


def _generate_src_app_name(dir_):
    _generate_src_app_name_task(dir_ / "task")
    markdown(document(), dir_, "README.md")


def _generate_src_app_name_task(dir_):
    pass


def _generate_src_gen(dir_):
    _generate_src_gen_generate(dir_ / "generate")
    markdown(document(), dir_, "README.md")


def _generate_src_gen_generate(dir_):
    _generate_src_gen_generate_custom(dir_ / "custom")
    _generate_src_gen_generate_shared(dir_ / "shared")


def _generate_src_gen_generate_custom(dir_):
    pass


def _generate_src_gen_generate_shared(dir_):
    _generate_src_gen_generate_shared_briteonyx(dir_ / "briteonyx")


def _generate_src_gen_generate_shared_briteonyx(dir_):
    pass


def _generate_src_lib(dir_):
    _generate_src_lib_mine(dir_ / "mine")
    _generate_src_lib_third_party(dir_ / "third_party")
    markdown(document(), dir_, "README.md")


def _generate_src_lib_mine(dir_):
    _generate_src_lib_mine_aws(dir_ / "aws")
    _generate_src_lib_mine_src_gen(dir_ / "src_gen")
    _generate_src_lib_mine_task(dir_ / "task")
    _generate_src_lib_mine_templates(dir_ / "throw_out_your_templates")
    _generate_src_lib_mine_utility(dir_ / "utility")
    markdown(document(), dir_, "README.md")


def _generate_src_lib_mine_aws(dir_):
    markdown(document(), dir_, "README.md")


def _generate_src_lib_mine_src_gen(dir_):
    _generate_src_lib_mine_src_gen_document(dir_ / "document")
    _generate_src_lib_mine_src_gen_script(dir_ / "script")
    markdown(document(), dir_, "README.md")


def _generate_src_lib_mine_src_gen_document(dir_):
    _generate_src_lib_mine_src_gen_document_markdown(dir_ / "markdown")


def _generate_src_lib_mine_src_gen_document_markdown(dir_):
    pass


def _generate_src_lib_mine_src_gen_script(dir_):
    _generate_src_lib_mine_src_gen_script_bash(dir_ / "bash")
    _generate_src_lib_mine_src_gen_script_python(dir_ / "python")


def _generate_src_lib_mine_src_gen_script_bash(dir_):
    _generate_src_lib_mine_src_gen_script_bash_briteonyx(dir_ / "briteonyx")


def _generate_src_lib_mine_src_gen_script_bash_briteonyx(dir_):
    pass


def _generate_src_lib_mine_src_gen_script_python(dir_):
    pass


def _generate_src_lib_mine_task(dir_):
    markdown(document(), dir_, "README.md")


def _generate_src_lib_mine_templates(dir_):
    markdown(document(), dir_, "README.md")


def _generate_src_lib_mine_utility(dir_):
    markdown(document(), dir_, "README.md")


def _generate_src_lib_third_party(dir_):
    markdown(document(), dir_, "README.md")


def generate(directory):
    _generate(directory)


"""DisabledContent
"""

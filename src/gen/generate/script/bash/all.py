#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.complete import *
from src_gen.script.bash.render import generate as bash
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)
from .activating.all import generate as generate_activating
from .briteonyx.all import generate as generate_briteonyx


def _generate(dir_):
    _generate_bin(dir_ / "bin")
    _generate_briteonyx(dir_ / "BriteOnyx")
    _generate_cfg(dir_ / "cfg")
    _generate_doc(dir_ / "doc")
    _generate_home(dir_ / "home")
    _generate_out(dir_ / "home")
    _generate_src(dir_ / "src")


def _generate_bin(dir_):
    _generate_bin_lib(dir_ / "lib")


def _generate_bin_lib(dir_):
    pass


def _generate_briteonyx(dir_):
    _generate_briteonyx_bin(dir_ / "bin")
    _generate_briteonyx_doc(dir_ / "doc")


def _generate_briteonyx_bin(dir_):
    _generate_briteonyx_bin_lib(dir_ / "lib")


def _generate_briteonyx_bin_lib(dir_):
    pass


def _generate_briteonyx_doc(dir_):
    pass


def _generate_cfg(dir_):
    _generate_cfg_sample(dir_ / "sample")


def _generate_cfg_sample(dir_):
    pass


def _generate_doc(dir_):
    pass


def _generate_home(dir_):
    _generate_home_bin(dir_ / "bin")
    _generate_home_linux(dir_ / "Linux")
    _generate_home_macos(dir_ / "macOS")
    _generate_home_ssh(dir_ / ".ssh")


def _generate_home_bin(dir_):
    _generate_home_bin_lib(dir_ / "lib")
    bash(executed(), dir_, "24-bit-color.sh")
    bash(executed(), dir_, "clone_from_GitHub_by_Rob")
    bash(executed(), dir_, "clone_from_GitHub_by_TextNow")
    bash(executed(), dir_, "clone_from_GitHub_by_others")
    bash(executed(), dir_, "clone_from_GitLab_by_Rob")
    bash(executed(), dir_, "clone_from_GitLab_by_SWA")
    bash(executed(), dir_, "clone_from_GitLab_by_Yum")
    bash(executed(), dir_, "clone_from_GitLab_by_others")
    bash(executed(), dir_, "git_config_user_Me_at_SWA")
    bash(executed(), dir_, "git_config_user_Me_at_TextNow")
    bash(executed(), dir_, "git_config_user_Me_at_home")
    bash(executed(), dir_, "grep_stable_projects_for_all_phrases")
    bash(executed(), dir_, "grep_stable_projects_for_phrase")
    bash(executed(), dir_, "secure")


def _generate_home_bin_lib(dir_):
    bash(sourced(), dir_, "declare-git.bash")


def _generate_home_linux(dir_):
    pass


def _generate_home_macos(dir_):
    _generate_home_macos_bin(dir_ / "bin")


def _generate_home_macos_bin(dir_):
    bash(executed(), dir_, "homebrew-install")
    bash(executed(), dir_, "homebrew-list")
    bash(executed(), dir_, "homebrew-populate")
    bash(executed(), dir_, "homebrew-update")
    bash(executed(), dir_, "homebrew-upgrade")
    bash(executed(), dir_, "homebrew-uninstall")


def _generate_home_ssh(dir_):
    pass


def _generate_out(dir_):
    pass


def _generate_src(dir_):
    _generate_src_app(dir_ / "app")
    _generate_src_gen(dir_ / "gen")
    _generate_src_lib(dir_ / "lib")


def _generate_src_app(dir_):
    _generate_src_app_name(dir_ / Config().application_name)


def _generate_src_app_name(dir_):
    _generate_src_app_name_task(dir_ / "task")


def _generate_src_app_name_task(dir_):
    pass


def _generate_src_gen(dir_):
    _generate_src_gen_generate(dir_ / "generate")


def _generate_src_gen_generate(dir_):
    pass


def _generate_src_lib(dir_):
    _generate_src_lib_mine(dir_ / "mine")
    _generate_src_lib_third_party(dir_ / "third_party")


def _generate_src_lib_mine(dir_):
    _generate_src_lib_mine_aws(dir_ / "aws")
    _generate_src_lib_mine_src_gen(dir_ / "src_gen")
    _generate_src_lib_mine_task(dir_ / "task")
    _generate_src_lib_mine_templates(dir_ / "throw_out_your_templates")
    _generate_src_lib_mine_utility(dir_ / "utility")


def _generate_src_lib_mine_aws(dir_):
    pass


def _generate_src_lib_mine_aws(dir_):
    pass


def _generate_src_lib_mine_src_gen(dir_):
    _generate_src_lib_mine_src_gen_document(dir_ / "document")
    _generate_src_lib_mine_src_gen_script(dir_ / "script")


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
    pass


def _generate_src_lib_mine_templates(dir_):
    pass


def _generate_src_lib_mine_utility(dir_):
    pass


def _generate_src_lib_third_party(dir_):
    pass


def generate(directory):
    _generate(directory)
    generate_activating(directory)
    generate_briteonyx(directory)


"""DisabledContent
"""

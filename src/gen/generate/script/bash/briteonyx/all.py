#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.briteonyx.complete import *
from src_gen.script.bash.briteonyx.render import generate as briteonyx
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)


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
    briteonyx(executed(), dir_, "app-run")
    briteonyx(executed(), dir_, "show_maybe_missed_source")
    briteonyx(executed(), dir_, "sync_on_macOS")
    briteonyx(executed(), dir_, "tool-report")


def _generate_bin_lib(dir_):
    briteonyx(sourced(), dir_, "configure-Anaconda.bash")
    briteonyx(sourced(), dir_, "declare.bash")


def _generate_briteonyx(dir_):
    _generate_briteonyx_bin(dir_ / "bin")
    _generate_briteonyx_doc(dir_ / "doc")


def _generate_briteonyx_bin(dir_):
    _generate_briteonyx_bin_lib(dir_ / "lib")
    briteonyx(executed(), dir_, "all-capture")
    briteonyx(executed(), dir_, "all-check")
    briteonyx(executed(), dir_, "anaconda-capture")
    briteonyx(executed(), dir_, "anaconda-check")
    briteonyx(executed(), dir_, "anaconda-create")
    briteonyx(executed(), dir_, "anaconda-destroy")
    briteonyx(executed(), dir_, "anaconda-populate")
    briteonyx(executed(), dir_, "anaconda-report")
    briteonyx(executed(), dir_, "anaconda-upgrade")
    briteonyx(executed(), dir_, "env-capture")
    briteonyx(executed(), dir_, "env-check")
    briteonyx(executed(), dir_, "env-report")
    briteonyx(executed(), dir_, "gen-run")
    briteonyx(executed(), dir_, "prj-clean")
    briteonyx(executed(), dir_, "prj-wipe")
    briteonyx(executed(), dir_, "py-2to3")
    briteonyx(executed(), dir_, "py-capture")
    briteonyx(executed(), dir_, "py-check")
    briteonyx(executed(), dir_, "py-compile")
    briteonyx(executed(), dir_, "py-format")
    briteonyx(executed(), dir_, "py-report")
    briteonyx(executed(), dir_, "sig-check")
    briteonyx(executed(), dir_, "sig-make")
    briteonyx(executed(), dir_, "test-run")
    briteonyx(executed(), dir_, "tool-capture")
    briteonyx(executed(), dir_, "tool-check")


def _generate_briteonyx_bin_lib(dir_):
    briteonyx(sourced(), dir_, "alias.bash")


def _generate_briteonyx_doc(dir_):
    pass


def _generate_cfg(dir_):
    _generate_cfg_sample(dir_ / "sample")


def _generate_cfg_sample(dir_):
    briteonyx(sourced(), dir_, "alias.bash")
    briteonyx(sourced(), dir_, "context.bash")


def _generate_doc(dir_):
    pass


def _generate_home(dir_):
    _generate_home_bin(dir_ / "bin")
    _generate_home_linux(dir_ / "Linux")
    _generate_home_macos(dir_ / "macOS")
    _generate_home_ssh(dir_ / ".ssh")


def _generate_home_bin(dir_):
    _generate_home_bin_lib(dir_ / "lib")


def _generate_home_bin_lib(dir_):
    pass


def _generate_home_linux(dir_):
    pass


def _generate_home_macos(dir_):
    _generate_home_macos_bin(dir_ / "bin")


def _generate_home_macos_bin(dir_):
    pass


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


"""DisabledContent
"""

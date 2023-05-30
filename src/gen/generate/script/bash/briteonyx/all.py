#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.briteonyx.complete import *
from src_gen.script.bash.briteonyx.render import generate as briteonyx

# Project modules   (relative references, NOT packaged, in project)


def _generate(config, dir_):
    _generate_bin(config, dir_ / "bin")
    _generate_briteonyx(config, dir_ / "BriteOnyx")
    _generate_cfg(config, dir_ / "cfg")
    _generate_doc(dir_ / "doc")
    _generate_home(dir_ / "home")
    _generate_out(dir_ / "home")
    _generate_src(config, dir_ / "src")
    briteonyx(sourced(config), dir_, "alias.bash")
    briteonyx(sourced(config), dir_, "context.bash")


def _generate_bin(config, dir_):
    _generate_bin_lib(config, dir_ / "lib")
    briteonyx(executed(config), dir_, "anaconda-populate")
    briteonyx(executed(config), dir_, "app-run")
    briteonyx(executed(config), dir_, "show_maybe_missed_source")
    briteonyx(executed(config), dir_, "sync_workstation")
    briteonyx(executed(config), dir_, "tool-report")


def _generate_bin_lib(config, dir_):
    briteonyx(sourced(config), dir_, "declare.bash")


def _generate_briteonyx(config, dir_):
    _generate_briteonyx_bin(config, dir_ / "bin")
    _generate_briteonyx_doc(dir_ / "doc")


def _generate_briteonyx_bin(config, dir_):
    _generate_briteonyx_bin_lib(config, dir_ / "lib")
    briteonyx(executed(config), dir_, "all-capture")
    briteonyx(executed(config), dir_, "all-check")
    briteonyx(executed(config), dir_, "anaconda-capture")
    briteonyx(executed(config), dir_, "anaconda-check")
    briteonyx(executed(config), dir_, "anaconda-create")
    briteonyx(executed(config), dir_, "anaconda-destroy")
    briteonyx(executed(config), dir_, "anaconda-report")
    briteonyx(executed(config), dir_, "anaconda-upgrade")
    briteonyx(executed(config), dir_, "env-capture")
    briteonyx(executed(config), dir_, "env-check")
    briteonyx(executed(config), dir_, "env-report")
    briteonyx(executed(config), dir_, "gen-run")
    briteonyx(executed(config), dir_, "prj-clean")
    briteonyx(executed(config), dir_, "prj-wipe")
    briteonyx(executed(config), dir_, "py-2to3")
    briteonyx(executed(config), dir_, "py-capture")
    briteonyx(executed(config), dir_, "py-check")
    briteonyx(executed(config), dir_, "py-compile")
    briteonyx(executed(config), dir_, "py-format")
    briteonyx(executed(config), dir_, "py-report")
    briteonyx(executed(config), dir_, "sig-check")
    briteonyx(executed(config), dir_, "sig-make")
    briteonyx(executed(config), dir_, "test-run")
    briteonyx(executed(config), dir_, "tool-capture")
    briteonyx(executed(config), dir_, "tool-check")


def _generate_briteonyx_bin_lib(config, dir_):
    briteonyx(sourced(config), dir_, "alias.bash")
    briteonyx(sourced(config), dir_, "configure_Anaconda.bash")
    briteonyx(sourced(config), dir_, "configure_Python.bash")
    briteonyx(sourced(config), dir_, "initialize_Anaconda.bash")
    briteonyx(sourced(config), dir_, "maybe_create_Anaconda_environment.bash")


def _generate_briteonyx_doc(dir_):
    pass


def _generate_cfg(config, dir_):
    _generate_cfg_sample(config, dir_ / "sample")


def _generate_cfg_sample(config, dir_):
    briteonyx(sourced(config), dir_, "alias.bash")
    briteonyx(sourced(config), dir_, "context.bash")


def _generate_doc(dir_):
    pass


def _generate_home(dir_):
    _generate_home_bin(dir_ / "bin")
    _generate_home_darwin(dir_ / "Darwin")
    _generate_home_linux(dir_ / "Linux")
    _generate_home_ssh(dir_ / ".ssh")


def _generate_home_bin(dir_):
    _generate_home_bin_lib(dir_ / "lib")


def _generate_home_bin_lib(dir_):
    pass


def _generate_home_darwin(dir_):
    _generate_home_darwin_bin(dir_ / "bin")


def _generate_home_darwin_bin(dir_):
    pass


def _generate_home_linux(dir_):
    pass


def _generate_home_ssh(dir_):
    pass


def _generate_out(dir_):
    pass


def _generate_src(config, dir_):
    _generate_src_app(config, dir_ / "app")
    _generate_src_gen(dir_ / "gen")
    _generate_src_lib(dir_ / "lib")


def _generate_src_app(config, dir_):
    _generate_src_app_name(dir_ / config.application_name)


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


def generate(config, directory):
    _generate(config, directory)


"""DisabledContent
"""

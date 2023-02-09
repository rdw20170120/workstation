#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)


def _generate(dir_):
    bash(activate(), dir_, "activate.bash")
    markdown(document(), dir_, "HowTo-use_this_project.md")
    markdown(document(), dir_, "LICENSE.md")
    markdown(document(), dir_, "README.md")
    markdown(document(), dir_, "TODO.md")
    _generate_bin(dir_ / "bin")
    _generate_briteonyx(dir_ / "BriteOnyx")
    _generate_cfg(dir_ / "cfg")
    _generate_doc(dir_ / "doc")
    _generate_home(dir_ / "home")
    _generate_out(dir_ / "home")
    _generate_src(dir_ / "src")


def _generate_bin(dir_):
    markdown(document(), dir_, "README.md")
    briteonyx(executed(), dir_, "app-run")
    briteonyx(executed(), dir_, "show_maybe_missed_source")
    briteonyx(executed(), dir_, "sync_on_macOS")
    briteonyx(executed(), dir_, "tool-report")
    _generate_bin_lib(dir_ / "lib")


def _generate_bin_lib(dir_):
    markdown(document(), dir_, "README.md")
    activating(sourced(), dir_, "configure-Anaconda.bash")
    activating(sourced(), dir_, "declare.bash")


def _generate_briteonyx(dir_):
    markdown(document(), dir_, "README.md")
    _generate_briteonyx_bin(dir_ / "bin")
    _generate_briteonyx_doc(dir_ / "doc")


def _generate_briteonyx_bin(dir_):
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
    markdown(document(), dir_, "README.md")
    python(script(), dir_, "avro-print")
    python(script(), dir_, "extensions")
    python(script(), dir_, "list")
    python(script(), dir_, "parquet-print")
    _generate_briteonyx_bin_lib(dir_ / "lib")


def _generate_briteonyx_bin_lib(dir_):
    activating(sourced(), dir_, "configure-Python.bash")
    activating(sourced(), dir_, "declare-base.bash")
    activating(sourced(), dir_, "declare-common.bash")
    activating(sourced(), dir_, "declare-log4bash.bash")
    activating(sourced(), dir_, "declare-require.bash")
    activating(sourced(), dir_, "declare.bash")
    activating(sourced(), dir_, "set_path.bash")
    briteonyx(sourced(), dir_, "alias.bash")
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
    markdown(document(), dir_, "README.md")
    _generate_cfg_sample(dir_ / "sample")


def _generate_cfg_sample(dir_):
    activating(sourced(), dir_, "alias.bash")
    activating(sourced(), dir_, "context.bash")
    markdown(document(), dir_, "README.md")


def _generate_doc(dir_):
    markdown(document(), dir_, "README.md")


def _generate_home(dir_):
    markdown(document(), dir_, "README.md")
    _generate_home_bin(dir_ / "bin")
    _generate_home_bin_lib(dir_ / "lib")
    _generate_home_linux(dir_ / "Linux")
    _generate_home_macos(dir_ / "macOS")
    _generate_home_macos_bin(dir_ / "bin")
    _generate_home_ssh(dir_ / ".ssh")


def _generate_home_bin(dir_):
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
    markdown(document(), dir_, "README.md")


def _generate_home_linux(dir_):
    markdown(document(), dir_, "README.md")


def _generate_home_macos(dir_):
    markdown(document(), dir_, "README.md")


def _generate_home_macos_bin(dir_):
    bash(executed(), dir_, "homebrew-install")
    bash(executed(), dir_, "homebrew-list")
    bash(executed(), dir_, "homebrew-populate")
    bash(executed(), dir_, "homebrew-update")
    bash(executed(), dir_, "homebrew-upgrade")
    bash(executed(), dir_, "homebrew-uninstall")
    markdown(document(), dir_, "README.md")


def _generate_home_ssh(dir_):
    markdown(document(), dir_, "README.md")


def _generate_out(dir_):
    markdown(document(), dir_, "README.md")


def _generate_src(dir_):
    _generate_src_app(dir_ / "app")
    _generate_src_gen(dir_ / "gen")
    _generate_src_lib(dir_ / "lib")


def _generate_src_app(dir_):
    markdown(document(), dir_, "README.md")
    _generate_src_app_name(dir_ / Config().application_name)


def _generate_src_app_name(dir_):
    markdown(document(), dir_, "README.md")
    python(library(), dir_, "app.py")
    python(library(), dir_, "config.py")
    python(main(), dir_, "__main__.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "conftest.py")
    python(suite(), dir_, "test_app.py")
    python(suite(), dir_, "test_config.py")
    _generate_src_app_name_task(dir_ / "task")


def _generate_src_app_name_task(dir_):
    python(package(), dir_, "__init__.py")
    python(library(), dir_, "bootstrap.py")
    python(library(), dir_, "mapping.py")
    python(library(), dir_, "scan_directory.py")
    python(suite(), dir_, "test_mapping.py")
    python(suite(), dir_, "test_task.py")


def _generate_src_gen(dir_):
    markdown(document(), dir_, "README.md")
    _generate_src_gen_generate(dir_ / "generate")


def _generate_src_gen_generate(dir_):
    python(library(), dir_, "app.py")
    python(library(), dir_, "config.py")
    python(main(), dir_, "__main__.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "conftest.py")
    python(suite(), dir_, "test_app.py")
    python(suite(), dir_, "test_config.py")
    _generate_src_gen_generate_custom(dir_ / "custom")
    _generate_src_gen_generate_shared(dir_ / "shared")


def _generate_src_gen_generate_custom(dir_):
    python(library(), dir_, "all.py")
    python(package(), dir_, "__init__.py")


def _generate_src_gen_generate_shared(dir_):
    python(library(), dir_, "all.py")
    python(package(), dir_, "__init__.py")
    _generate_src_gen_generate_shared_briteonyx(dir_ / "briteonyx")


def _generate_src_gen_generate_shared_briteonyx(dir_):
    python(generator(), dir_, "activate.py")
    python(generator(), dir_, "alias.py")
    python(generator(), dir_, "configure_python.py")
    python(generator(), dir_, "declare.py")
    python(generator(), dir_, "declare_base.py")
    python(generator(), dir_, "declare_common.py")
    python(generator(), dir_, "declare_log4bash.py")
    python(generator(), dir_, "declare_require.py")
    python(generator(), dir_, "set_path.py")
    python(package(), dir_, "__init__.py")


def _generate_src_lib(dir_):
    _generate_src_lib_mine(dir_ / "mine")
    _generate_src_lib_third_party(dir_ / "third_party")


def _generate_src_lib_mine(dir_):
    _generate_src_lib_mine_aws(dir_ / "aws")
    _generate_src_lib_mine_src_gen(dir_ / "src_gen")
    _generate_src_lib_mine_task(dir_ / "task")
    _generate_src_lib_mine_templates(dir_ / "throw_out_your_templates")
    _generate_src_lib_mine_utility(dir_ / "utility")
    markdown(document(), dir_, "README.md")


def _generate_src_lib_mine_aws(dir_):
    markdown(document(), dir_, "README.md")


def _generate_src_lib_mine_aws(dir_):
    python(library(), dir_, "ec2.py")
    python(library(), dir_, "s3.py")
    python(library(), dir_, "service.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_ec2.py")
    python(suite(), dir_, "test_s3.py")
    python(suite(), dir_, "test_service.py")


def _generate_src_lib_mine_src_gen(dir_):
    markdown(document(), dir_, "README.md")
    python(library(), dir_, "renderer.py")
    python(library(), dir_, "source.py")
    python(library(), dir_, "structure.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_renderer.py")
    python(suite(), dir_, "test_source.py")
    python(suite(), dir_, "test_structure.py")
    _generate_src_lib_mine_src_gen_document(dir_ / "document")
    _generate_src_lib_mine_src_gen_script(dir_ / "script")


def _generate_src_lib_mine_src_gen_document(dir_):
    python(package(), dir_, "__init__.py")
    _generate_src_lib_mine_src_gen_document_markdown(dir_ / "markdown")


def _generate_src_lib_mine_src_gen_document_markdown(dir_):
    python(library(), dir_, "complete.py")
    python(library(), dir_, "source.py")
    python(library(), dir_, "structure.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_complete.py")
    python(suite(), dir_, "test_source.py")
    python(suite(), dir_, "test_structure.py")


def _generate_src_lib_mine_src_gen_script(dir_):
    python(library(), dir_, "source.py")
    python(library(), dir_, "structure.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_source.py")
    python(suite(), dir_, "test_structure.py")
    _generate_src_lib_mine_src_gen_script_bash(dir_ / "bash")
    _generate_src_lib_mine_src_gen_script_python(dir_ / "python")


def _generate_src_lib_mine_src_gen_script_bash(dir_):
    python(library(), dir_, "complete.py")
    python(library(), dir_, "source.py")
    python(library(), dir_, "structure.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_complete.py")
    python(suite(), dir_, "test_source.py")
    python(suite(), dir_, "test_structure.py")
    _generate_src_lib_mine_src_gen_script_bash_briteonyx(dir_ / "briteonyx")


def _generate_src_lib_mine_src_gen_script_bash_briteonyx(dir_):
    python(library(), dir_, "complete.py")
    python(library(), dir_, "source.py")
    python(library(), dir_, "structure.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_complete.py")
    python(suite(), dir_, "test_source.py")
    python(suite(), dir_, "test_structure.py")


def _generate_src_lib_mine_src_gen_script_python(dir_):
    python(library(), dir_, "complete.py")
    python(library(), dir_, "source.py")
    python(library(), dir_, "structure.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_complete.py")
    python(suite(), dir_, "test_source.py")
    python(suite(), dir_, "test_structure.py")


def _generate_src_lib_mine_task(dir_):
    markdown(document(), dir_, "README.md")
    python(library(), dir_, "config.py")
    python(library(), dir_, "delete_file.py")
    python(library(), dir_, "exception.py")
    python(library(), dir_, "queue.py")
    python(library(), dir_, "task.py")
    python(library(), dir_, "task_manager.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "conftest.py")
    python(suite(), dir_, "test_config.py")
    python(suite(), dir_, "test_exception.py")
    python(suite(), dir_, "test_queue.py")
    python(suite(), dir_, "test_task.py")
    python(suite(), dir_, "test_task_manager.py")


def _generate_src_lib_mine_templates(dir_):
    markdown(document(), dir_, "README.md")
    python(library(), dir_, "section_1.py")
    python(library(), dir_, "section_2.py")
    python(library(), dir_, "section_3.py")
    python(library(), dir_, "section_4.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_section_1.py")
    python(suite(), dir_, "test_section_2.py")
    python(suite(), dir_, "test_section_3.py")
    python(suite(), dir_, "test_section_4.py")


def _generate_src_lib_mine_utility(dir_):
    markdown(document(), dir_, "README.md")
    python(library(), dir_, "color_log_formatter.py")
    python(library(), dir_, "config.py")
    python(library(), dir_, "environment.py")
    python(library(), dir_, "filesystem.py")
    python(library(), dir_, "my_assert.py")
    python(library(), dir_, "my_logging.py")
    python(library(), dir_, "my_math.py")
    python(library(), dir_, "my_terminal.py")
    python(library(), dir_, "my_time.py")
    python(library(), dir_, "processing.py")
    python(library(), dir_, "singleton_application.py")
    python(library(), dir_, "text.py")
    python(library(), dir_, "tracked_path.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "conftest.py")
    python(suite(), dir_, "test_color_log_formatter.py")
    python(suite(), dir_, "test_config.py")
    python(suite(), dir_, "test_environment.py")
    python(suite(), dir_, "test_filesystem.py")
    python(suite(), dir_, "test_my_assert.py")
    python(suite(), dir_, "test_my_math.py")
    python(suite(), dir_, "test_my_time.py")
    python(suite(), dir_, "test_python.py")
    python(suite(), dir_, "test_singleton_application.py")
    python(suite(), dir_, "test_text.py")
    python(suite(), dir_, "test_tracked_path.py")


def _generate_src_lib_third_party(dir_):
    markdown(document(), dir_, "README.md")


def generate(directory):
    _generate(directory)


"""DisabledContent
"""

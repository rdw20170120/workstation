#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
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
from .briteonyx.activate import build as activate


def _generate(dir_):
    sub = dir_
    bash(activate(), sub, "activate.bash")
    markdown(document(), sub, "HowTo-use_this_project.md")
    markdown(document(), sub, "LICENSE.md")
    markdown(document(), sub, "README.md")
    markdown(document(), sub, "TODO.md")
    sub = dir_ / "out"
    markdown(document(), sub, "README.md")


def _generate_bin(dir_):
    sub = dir_
    markdown(document(), sub, "README.md")
    briteonyx(executed(), sub, "app-run")
    briteonyx(executed(), sub, "show_maybe_missed_source")
    briteonyx(executed(), sub, "tool-report")
    sub = dir_ / "lib"
    markdown(document(), sub, "README.md")


def _generate_briteonyx(dir_):
    sub = dir_
    markdown(document(), sub, "README.md")
    sub = dir_ / "bin"
    briteonyx(executed(), sub, "dep-capture")
    briteonyx(executed(), sub, "dep-check")
    briteonyx(executed(), sub, "dep-reinstall")
    briteonyx(executed(), sub, "dep-report")
    briteonyx(executed(), sub, "dep-upgrade")
    briteonyx(executed(), sub, "sig-check")
    briteonyx(executed(), sub, "sig-make")
    python(script(), sub, "avro-print")
    python(script(), sub, "extensions")
    python(script(), sub, "list")
    python(script(), sub, "parquet-print")
    markdown(document(), sub, "README.md")
    briteonyx(executed(), sub, "all-capture")
    briteonyx(executed(), sub, "all-check")
    briteonyx(executed(), sub, "env-capture")
    briteonyx(executed(), sub, "env-check")
    briteonyx(executed(), sub, "env-report")
    briteonyx(executed(), sub, "gen-run")
    briteonyx(executed(), sub, "prj-clean")
    briteonyx(executed(), sub, "prj-wipe")
    briteonyx(executed(), sub, "py-2to3")
    briteonyx(executed(), sub, "py-capture")
    briteonyx(executed(), sub, "py-check")
    briteonyx(executed(), sub, "py-compile")
    briteonyx(executed(), sub, "py-reformat")
    briteonyx(executed(), sub, "py-report")
    briteonyx(executed(), sub, "test-run")
    briteonyx(executed(), sub, "tool-capture")
    briteonyx(executed(), sub, "tool-check")
    sub = dir_ / "bin" / "lib"
    markdown(document(), sub, "README.md")
    bash(activation(), sub, "alias.bash")
    bash(activation(), sub, "configure-Python.bash")
    bash(activation(), sub, "declare.bash")
    bash(activation(), sub, "declare-base.bash")
    bash(activation(), sub, "declare-common.bash")
    bash(activation(), sub, "declare-log4bash.bash")
    bash(activation(), sub, "declare-require.bash")
    bash(activation(), sub, "set_path.bash")
    sub = dir_ / "doc"
    markdown(document(), sub, "HowTo-activate_this_project.md")
    markdown(document(), sub, "HowTo-execute_application.md")
    markdown(document(), sub, "HowTo-install-OpenJDK-15.md")
    markdown(document(), sub, "HowTo-install-packages.md")
    markdown(document(), sub, "HowTo-setup-AWS_CLI.md")
    markdown(document(), sub, "HowTo-setup-source_control.md")
    markdown(document(), sub, "HowTo-setup-workstation.md")
    markdown(document(), sub, "HowTo-test.md")
    markdown(document(), sub, "HowTo-use-Anaconda.md")
    markdown(document(), sub, "HowTo-use-Homebrew.md")
    markdown(document(), sub, "HowTo-use-Vim.md")
    markdown(document(), sub, "README.md")
    markdown(document(), sub, "project_initiation.md")
    markdown(document(), sub, "testssl.md")


def _generate_cfg(dir_):
    sub = dir_
    markdown(document(), sub, "README.md")
    sub = dir_ / "sample"
    bash(activation(), sub, "alias.bash")
    bash(activation(), sub, "context.bash")
    markdown(document(), sub, "README.md")


def _generate_doc(dir_):
    sub = dir_
    markdown(document(), sub, "README.md")


def _generate_src(dir_):
    sub = dir_
    _generate_src_app(sub / "app")
    _generate_src_gen(sub / "gen")
    markdown(document(), sub, "README.md")
    sub = dir_ / "lib"
    _generate_src_lib_mine(sub / "mine")
    _generate_src_lib_third_party(sub / "third_party")
    markdown(document(), sub, "README.md")


def _generate_src_app(dir_):
    sub = dir_
    markdown(document(), sub, "README.md")
    sub = dir_ / Config().application_name
    markdown(document(), sub, "README.md")
    python(library(), sub, "app.py")
    python(library(), sub, "config.py")
    python(main(), sub, "__main__.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "conftest.py")
    python(suite(), sub, "test_app.py")
    python(suite(), sub, "test_config.py")


def _generate_src_gen(dir_):
    sub = dir_
    markdown(document(), sub, "README.md")
    sub = dir_ / "generate"
    python(library(), sub, "app.py")
    python(library(), sub, "config.py")
    python(main(), sub, "__main__.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "conftest.py")
    python(suite(), sub, "test_app.py")
    python(suite(), sub, "test_config.py")
    sub = dir_ / "generate" / "custom"
    python(package(), sub, "__init__.py")
    python(library(), sub, "all.py")
    sub = dir_ / "generate" / "shared"
    python(library(), sub, "all.py")
    python(package(), sub, "__init__.py")
    sub = dir_ / "generate" / "shared" / "briteonyx"
    python(generator(), sub, "activate.py")
    python(generator(), sub, "alias.py")
    python(generator(), sub, "configure_python.py")
    python(generator(), sub, "declare.py")
    python(generator(), sub, "declare_base.py")
    python(generator(), sub, "declare_common.py")
    python(generator(), sub, "declare_log4bash.py")
    python(generator(), sub, "declare_require.py")
    python(generator(), sub, "set_path.py")
    python(package(), sub, "__init__.py")


def _generate_src_lib(dir_):
    sub = dir_ / "mine"
    _generate_src_lib_mine_aws(sub / "aws")
    _generate_src_lib_mine_src_gen(sub / "src_gen")
    _generate_src_lib_mine_task(sub / "task")
    _generate_src_lib_mine_templates(sub / "throw_out_your_templates")
    _generate_src_lib_mine_utility(sub / "utility")


def _generate_src_lib_mine(dir_):
    sub = dir_
    markdown(document(), sub, "README.md")
    sub = dir_ / "aws"
    markdown(document(), sub, "README.md")
    sub = dir_ / "src_gen"
    markdown(document(), sub, "README.md")
    sub = dir_ / "task"
    markdown(document(), sub, "README.md")
    sub = dir_ / "throw_out_your_templates"
    markdown(document(), sub, "README.md")
    sub = dir_ / "utility"
    markdown(document(), sub, "README.md")


def _generate_src_lib_mine_aws(dir_):
    sub = dir_
    python(library(), sub, "ec2.py")
    python(library(), sub, "s3.py")
    python(library(), sub, "service.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "test_ec2.py")
    python(suite(), sub, "test_s3.py")
    python(suite(), sub, "test_service.py")


def _generate_src_lib_mine_src_gen(dir_):
    sub = dir_
    python(library(), sub, "renderer.py")
    python(library(), sub, "source.py")
    python(library(), sub, "structure.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "test_renderer.py")
    python(suite(), sub, "test_source.py")
    python(suite(), sub, "test_structure.py")
    sub = dir_ / "document"
    python(package(), sub, "__init__.py")
    sub = dir_ / "document" / "markdown"
    python(library(), sub, "complete.py")
    python(library(), sub, "source.py")
    python(library(), sub, "structure.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "test_complete.py")
    python(suite(), sub, "test_source.py")
    python(suite(), sub, "test_structure.py")
    sub = dir_ / "script"
    python(library(), sub, "source.py")
    python(library(), sub, "structure.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "test_source.py")
    python(suite(), sub, "test_structure.py")
    sub = dir_ / "script" / "bash"
    python(library(), sub, "complete.py")
    python(library(), sub, "source.py")
    python(library(), sub, "structure.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "test_complete.py")
    python(suite(), sub, "test_source.py")
    python(suite(), sub, "test_structure.py")
    sub = dir_ / "script" / "bash" / "briteonyx"
    python(library(), sub, "complete.py")
    python(library(), sub, "source.py")
    python(library(), sub, "structure.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "test_complete.py")
    python(suite(), sub, "test_source.py")
    python(suite(), sub, "test_structure.py")
    sub = dir_ / "script" / "python"
    python(library(), sub, "complete.py")
    python(library(), sub, "source.py")
    python(library(), sub, "structure.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "test_complete.py")
    python(suite(), sub, "test_source.py")
    python(suite(), sub, "test_structure.py")


def _generate_src_lib_mine_task(dir_):
    sub = dir_
    python(library(), sub, "config.py")
    python(library(), sub, "delete_file.py")
    python(library(), sub, "exception.py")
    python(library(), sub, "queue.py")
    python(library(), sub, "task.py")
    python(library(), sub, "task_manager.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "conftest.py")
    python(suite(), sub, "test_config.py")
    python(suite(), sub, "test_exception.py")
    python(suite(), sub, "test_queue.py")
    python(suite(), sub, "test_task.py")
    python(suite(), sub, "test_task_manager.py")


def _generate_src_lib_mine_templates(dir_):
    sub = dir_
    python(library(), sub, "section_1.py")
    python(library(), sub, "section_2.py")
    python(library(), sub, "section_3.py")
    python(library(), sub, "section_4.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "test_section_1.py")
    python(suite(), sub, "test_section_2.py")
    python(suite(), sub, "test_section_3.py")
    python(suite(), sub, "test_section_4.py")


def _generate_src_lib_mine_utility(dir_):
    sub = dir_
    python(library(), sub, "color_log_formatter.py")
    python(library(), sub, "config.py")
    python(library(), sub, "environment.py")
    python(library(), sub, "filesystem.py")
    python(library(), sub, "my_assert.py")
    python(library(), sub, "my_logging.py")
    python(library(), sub, "my_math.py")
    python(library(), sub, "my_terminal.py")
    python(library(), sub, "my_time.py")
    python(library(), sub, "processing.py")
    python(library(), sub, "singleton_application.py")
    python(library(), sub, "text.py")
    python(library(), sub, "tracked_path.py")
    python(package(), sub, "__init__.py")
    python(suite(), sub, "conftest.py")
    python(suite(), sub, "test_color_log_formatter.py")
    python(suite(), sub, "test_config.py")
    python(suite(), sub, "test_environment.py")
    python(suite(), sub, "test_filesystem.py")
    python(suite(), sub, "test_my_assert.py")
    python(suite(), sub, "test_my_math.py")
    python(suite(), sub, "test_my_time.py")
    python(suite(), sub, "test_python.py")
    python(suite(), sub, "test_singleton_application.py")
    python(suite(), sub, "test_text.py")
    python(suite(), sub, "test_tracked_path.py")


def _generate_src_lib_third_party(dir_):
    sub = dir_
    markdown(document(), sub, "README.md")


def generate(directory):
    _generate(directory)
    _generate_bin(directory / "bin")
    _generate_briteonyx(directory / "BriteOnyx")
    _generate_cfg(directory / "cfg")
    _generate_doc(directory / "doc")
    _generate_src(directory / "src")


"""DisabledContent
"""

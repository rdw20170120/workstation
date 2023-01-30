#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.document.markdown.complete import generate_document as document
from src_gen.script.bash.briteonyx.complete import (
    generate_executed as executed,
)
from src_gen.script.bash.briteonyx.complete import generate_sourced as sourced
from src_gen.script.bash.complete import generate_activation as activation
from src_gen.script.python.complete import generate_generator as generator
from src_gen.script.python.complete import generate_library as library
from src_gen.script.python.complete import generate_main as main
from src_gen.script.python.complete import generate_package as package
from src_gen.script.python.complete import generate_script as script
from src_gen.script.python.complete import generate_test as test
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)
from .script.bash.activate import generate as generate_activate
from .script.bash.alias import generate as generate_alias
from .script.bash.configure_python import generate as generate_configure_python
from .script.bash.declare import generate as generate_declare
from .script.bash.declare_base import generate as generate_declare_base
from .script.bash.declare_common import generate as generate_declare_common
from .script.bash.declare_log4bash import generate as generate_declare_log4bash
from .script.bash.declare_require import generate as generate_declare_require
from .script.bash.set_path import generate as generate_set_path


def _generate(dir_):
    sub = dir_
    activation(sub, "alias.bash")
    activation(sub, "context.bash")
    document(sub, "HowTo-use_this_project.md")
    document(sub, "LICENSE.md")
    document(sub, "README.md")
    document(sub, "TODO.md")
    generate_activate(sub)
    sub = dir_ / "out"
    document(sub, "README.md")


def _generate_bin(dir_):
    sub = dir_
    document(sub, "README.md")
    executed(sub, "app-run")
    executed(sub, "show_maybe_missed_source")
    executed(sub, "tool-report")
    sub = dir_ / "lib"
    document(sub, "README.md")


def _generate_briteonyx(dir_):
    sub = dir_
    document(sub, "README.md")
    sub = dir_ / "bin"
    document(sub, "README.md")
    executed(sub, "all-capture")
    executed(sub, "all-check")
    # executed(sub, "dep-capture")
    # executed(sub, "dep-check")
    # executed(sub, "dep-reinstall")
    # executed(sub, "dep-report")
    # executed(sub, "dep-upgrade")
    executed(sub, "env-capture")
    executed(sub, "env-check")
    executed(sub, "env-report")
    executed(sub, "gen-run")
    executed(sub, "prj-clean")
    executed(sub, "prj-wipe")
    executed(sub, "py-2to3")
    executed(sub, "py-capture")
    executed(sub, "py-check")
    executed(sub, "py-compile")
    executed(sub, "py-reformat")
    executed(sub, "py-report")
    # executed(sub, "sig-check")
    # executed(sub, "sig-make")
    executed(sub, "test-run")
    executed(sub, "tool-capture")
    executed(sub, "tool-check")
    # script(sub, "avro-print")
    # script(sub, "extensions")
    # script(sub, "list")
    # script(sub, "parquet-print")
    sub = dir_ / "bin" / "lib"
    document(sub, "README.md")
    generate_alias(sub)
    generate_configure_python(sub)
    generate_declare(sub)
    generate_declare_base(sub)
    generate_declare_common(sub)
    generate_declare_log4bash(sub)
    generate_declare_require(sub)
    generate_set_path(sub)
    sub = dir_ / "doc"
    document(sub, "HowTo-activate_this_project.md")
    document(sub, "HowTo-execute_application.md")
    document(sub, "HowTo-install-OpenJDK-15.md")
    document(sub, "HowTo-install-packages.md")
    document(sub, "HowTo-setup-AWS_CLI.md")
    document(sub, "HowTo-setup-source_control.md")
    document(sub, "HowTo-setup-workstation.md")
    document(sub, "HowTo-test.md")
    document(sub, "HowTo-use-Anaconda.md")
    document(sub, "HowTo-use-Homebrew.md")
    document(sub, "HowTo-use-Vim.md")
    document(sub, "README.md")
    document(sub, "project_initiation.md")
    document(sub, "testssl.md")


def _generate_cfg(dir_):
    sub = dir_
    document(sub, "README.md")
    sub = dir_ / "sample"
    activation(sub, "alias.bash")
    activation(sub, "context.bash")
    document(sub, "README.md")


def _generate_doc(dir_):
    sub = dir_
    document(sub, "README.md")


def _generate_mine(dir_):
    sub = dir_
    document(sub, "README.md")
    sub = dir_ / "aws"
    document(sub, "README.md")
    sub = dir_ / "src_gen"
    document(sub, "README.md")
    sub = dir_ / "task"
    document(sub, "README.md")
    sub = dir_ / "throw_out_your_templates"
    document(sub, "README.md")
    sub = dir_ / "utility"
    document(sub, "README.md")


def _generate_src(dir_):
    sub = dir_
    document(sub, "README.md")
    _generate_src_app(dir_ / "app")
    _generate_src_gen(dir_ / "gen")
    document(sub, "README.md")
    sub = dir_ / "lib"
    document(sub, "README.md")
    _generate_mine(sub / "mine")
    _generate_third_party(sub / "third_party")


def _generate_src_app(dir_):
    sub = dir_
    document(sub, "README.md")
    sub = dir_ / Config().application_name
    document(sub, "README.md")
    library(sub, "app.py")
    library(sub, "config.py")
    main(sub, "__main__.py")
    package(sub, "__init__.py")
    test(sub, "conftest.py")
    test(sub, "test_app.py")
    test(sub, "test_config.py")


def _generate_src_gen(dir_):
    sub = dir_
    document(sub, "README.md")
    sub = dir_ / "generate"
    package(sub, "__init__.py")
    main(sub, "__main__.py")
    library(sub, "app.py")
    library(sub, "config.py")
    test(sub, "conftest.py")
    test(sub, "test_app.py")
    test(sub, "test_config.py")
    _generate_src_gen_custom(sub / "custom")
    _generate_src_gen_shared(sub / "shared")


def _generate_src_gen_custom(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "all.py")
    sub = dir_ / "document"
    package(sub, "__init__.py")
    library(sub, "all.py")
    sub = dir_ / "document" / "markdown"
    package(sub, "__init__.py")
    library(sub, "all.py")
    sub = dir_ / "script"
    package(sub, "__init__.py")
    library(sub, "all.py")
    sub = dir_ / "script" / "bash"
    package(sub, "__init__.py")
    library(sub, "all.py")
    sub = dir_ / "script" / "bash" / "briteonyx"
    package(sub, "__init__.py")
    library(sub, "all.py")
    sub = dir_ / "script" / "python"
    package(sub, "__init__.py")
    library(sub, "all.py")


def _generate_src_gen_shared(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "all.py")
    sub = dir_ / "document"
    package(sub, "__init__.py")
    library(sub, "all.py")
    sub = dir_ / "document" / "markdown"
    package(sub, "__init__.py")
    library(sub, "all.py")
    sub = dir_ / "script"
    package(sub, "__init__.py")
    library(sub, "all.py")
    _generate_src_gen_shared_bash(sub / "bash")
    _generate_src_gen_shared_briteonyx(sub / "bash" / "briteonyx")
    _generate_src_gen_shared_python(sub / "python")


def _generate_src_gen_shared_bash(dir_):
    sub = dir_
    package(sub, "__init__.py")
    generator(sub, "activate.py")
    generator(sub, "alias.py")
    generator(sub, "all.py")
    generator(sub, "configure_python.py")
    generator(sub, "declare.py")
    generator(sub, "declare_base.py")
    generator(sub, "declare_common.py")
    generator(sub, "declare_log4bash.py")
    generator(sub, "declare_require.py")
    generator(sub, "set_path.py")


def _generate_src_gen_shared_briteonyx(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "all.py")


def _generate_src_gen_shared_python(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "all.py")


def _generate_src_lib(dir_):
    sub = dir_ / "mine"
    _generate_src_lib_aws(sub / "aws")
    _generate_src_lib_src_gen(sub / "src_gen")
    _generate_src_lib_task(sub / "task")
    _generate_src_lib_templates(sub / "throw_out_your_templates")
    _generate_src_lib_utility(sub / "utility")


def _generate_src_lib_aws(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "ec2.py")
    library(sub, "s3.py")
    library(sub, "service.py")
    test(sub, "test_ec2.py")
    test(sub, "test_s3.py")
    test(sub, "test_service.py")


def _generate_src_lib_src_gen(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "renderer.py")
    library(sub, "source.py")
    library(sub, "structure.py")
    test(sub, "test_renderer.py")
    test(sub, "test_source.py")
    test(sub, "test_structure.py")
    sub = dir_ / "document"
    package(sub, "__init__.py")
    sub = dir_ / "document" / "markdown"
    package(sub, "__init__.py")
    library(sub, "complete.py")
    library(sub, "source.py")
    library(sub, "structure.py")
    test(sub, "test_complete.py")
    test(sub, "test_source.py")
    test(sub, "test_structure.py")
    sub = dir_ / "script"
    package(sub, "__init__.py")
    library(sub, "source.py")
    library(sub, "structure.py")
    test(sub, "test_source.py")
    test(sub, "test_structure.py")
    sub = dir_ / "script" / "bash"
    package(sub, "__init__.py")
    library(sub, "complete.py")
    library(sub, "source.py")
    library(sub, "structure.py")
    test(sub, "test_complete.py")
    test(sub, "test_source.py")
    test(sub, "test_structure.py")
    sub = dir_ / "script" / "bash" / "briteonyx"
    package(sub, "__init__.py")
    library(sub, "complete.py")
    library(sub, "source.py")
    library(sub, "structure.py")
    test(sub, "test_complete.py")
    test(sub, "test_source.py")
    test(sub, "test_structure.py")
    sub = dir_ / "script" / "python"
    package(sub, "__init__.py")
    library(sub, "complete.py")
    library(sub, "source.py")
    library(sub, "structure.py")
    test(sub, "test_complete.py")
    test(sub, "test_source.py")
    test(sub, "test_structure.py")


def _generate_src_lib_task(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "config.py")
    test(sub, "conftest.py")
    library(sub, "exception.py")
    library(sub, "delete_file.py")
    library(sub, "queue.py")
    library(sub, "task.py")
    library(sub, "task_manager.py")
    test(sub, "test_config.py")
    test(sub, "test_exception.py")
    test(sub, "test_queue.py")
    test(sub, "test_task.py")
    test(sub, "test_task_manager.py")


def _generate_src_lib_templates(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "section_1.py")
    library(sub, "section_2.py")
    library(sub, "section_3.py")
    library(sub, "section_4.py")
    test(sub, "test_section_1.py")
    test(sub, "test_section_2.py")
    test(sub, "test_section_3.py")
    test(sub, "test_section_4.py")


def _generate_src_lib_utility(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "color_log_formatter.py")
    library(sub, "config.py")
    test(sub, "conftest.py")
    library(sub, "environment.py")
    library(sub, "filesystem.py")
    library(sub, "my_assert.py")
    library(sub, "my_logging.py")
    library(sub, "my_math.py")
    library(sub, "my_terminal.py")
    library(sub, "my_time.py")
    library(sub, "processing.py")
    library(sub, "singleton_application.py")
    test(sub, "test_color_log_formatter.py")
    test(sub, "test_config.py")
    test(sub, "test_environment.py")
    test(sub, "test_filesystem.py")
    test(sub, "test_my_assert.py")
    test(sub, "test_my_math.py")
    test(sub, "test_my_time.py")
    test(sub, "test_python.py")
    test(sub, "test_singleton_application.py")
    test(sub, "test_text.py")
    test(sub, "test_tracked_path.py")
    library(sub, "text.py")
    library(sub, "tracked_path.py")


def _generate_third_party(dir_):
    sub = dir_
    document(sub, "README.md")


def generate(directory):
    _generate(directory)
    _generate_bin(directory / "bin")
    _generate_briteonyx(directory / "BriteOnyx")
    _generate_cfg(directory / "cfg")
    _generate_doc(directory / "doc")
    _generate_src(directory / "src")


"""DisabledContent
"""

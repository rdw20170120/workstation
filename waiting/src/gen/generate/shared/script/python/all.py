#!/usr/bin/env false
"""Generate all custom Python scripts."""
# TODO: Add method for test module
# TODO: Add method for module to generate one source file
# TODO: Add method for module to generate many source files
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.python.complete import generate_generator as generator
from src_gen.script.python.complete import generate_library as library
from src_gen.script.python.complete import generate_main as main
from src_gen.script.python.complete import generate_package as package
from src_gen.script.python.complete import generate_script as script
from src_gen.script.python.complete import generate_test as test
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)


def _generate_briteonyx(dir_):
    sub = dir_ / "bin"


#   script(sub, "avro-print")
#   script(sub, "extensions")
#   script(sub, "list")
#   script(sub, "parquet-print")


def _generate_src(dir_):
    sub = dir_
    _generate_src_app(sub / "app" / Config().application_name)
    _generate_src_gen(sub / "gen" / "generate")
    _generate_src_lib(sub / "lib")


def _generate_src_app(dir_):
    sub = dir_
    package(sub, "__init__.py")
    main(sub, "__main__.py")
    library(sub, "app.py")
    library(sub, "config.py")
    test(sub, "conftest.py")
    test(sub, "test_app.py")
    test(sub, "test_config.py")


def _generate_src_gen(dir_):
    sub = dir_
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


def generate(directory):
    _generate_briteonyx(directory / "BriteOnyx")
    _generate_src(directory / "src")


"""DisabledContent
"""

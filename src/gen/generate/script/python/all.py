#!/usr/bin/env false
"""Generate all Python scripts."""
# TODO: Add method for test module
# TODO: Add method for module to generate one source file
# TODO: Add method for module to generate many source files
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path

# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from src_gen.script.python.source import generate as gen
from src_gen.script.python.structure import *

# Co-located modules (relative references, NOT packaged, in project)


def _generate_app(dir_):
    sub = Path("src", "app", "MODULE")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_main(), dir_, sub, "__main__.py")
    gen(_library(), dir_, sub, "app.py")
    gen(_library(), dir_, sub, "config.py")
    gen(_library(), dir_, sub, "test_app.py")
    gen(_library(), dir_, sub, "test_config.py")
    sub = Path("src", "app", "MODULE", "task")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "bootstrap.py")
    gen(_library(), dir_, sub, "mapping.py")
    gen(_library(), dir_, sub, "scan_directory.py")
    gen(_library(), dir_, sub, "test_mapping.py")
    gen(_library(), dir_, sub, "test_task.py")


def _generate_bin(dir_):
    sub = Path("bin")


def _generate_briteonyx(dir_):
    sub = Path("BriteOnyx", "bin")
    gen(_script(), dir_, sub, "avro-print")
    gen(_script(), dir_, sub, "extensions")
    gen(_script(), dir_, sub, "list")
    gen(_script(), dir_, sub, "parquet-print")


def _generate_gen(dir_):
    sub = Path("src", "gen", "generate")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_main(), dir_, sub, "__main__.py")
    gen(_library(), dir_, sub, "app.py")
    gen(_library(), dir_, sub, "config.py")
    gen(_library(), dir_, sub, "test_app.py")
    gen(_library(), dir_, sub, "test_config.py")
    sub = Path("src", "gen", "generate", "document")
    gen(_package(), dir_, sub, "__init__.py")
    sub = Path("src", "gen", "generate", "document", "markdown")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "all.py")
    sub = Path("src", "gen", "generate", "script")
    gen(_package(), dir_, sub, "__init__.py")
    sub = Path("src", "gen", "generate", "script", "bash")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "all.py")
    gen(_library(), dir_, sub, "activate.py")
    gen(_library(), dir_, sub, "set_path.py")
    sub = Path("src", "gen", "generate", "script", "bash", "briteonyx")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "all.py")
    sub = Path("src", "gen", "generate", "script", "python")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "all.py")


def _generate_lib(dir_):
    _generate_lib_aws(dir_)
    _generate_lib_src_gen(dir_)
    _generate_lib_task(dir_)
    _generate_lib_utility(dir_)


def _generate_lib_aws(dir_):
    sub = Path("src", "lib", "mine", "aws")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "ec2.py")
    gen(_library(), dir_, sub, "s3.py")
    gen(_library(), dir_, sub, "service.py")
    gen(_library(), dir_, sub, "test_ec2.py")
    gen(_library(), dir_, sub, "test_s3.py")
    gen(_library(), dir_, sub, "test_service.py")


def _generate_lib_src_gen(dir_):
    sub = Path("src", "lib", "mine", "src_gen")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "renderer.py")
    gen(_library(), dir_, sub, "source.py")
    gen(_library(), dir_, sub, "structure.py")
    gen(_library(), dir_, sub, "test_structure.py")
    sub = Path("src", "lib", "mine", "src_gen", "document")
    gen(_package(), dir_, sub, "__init__.py")
    sub = Path("src", "lib", "mine", "src_gen", "document", "markdown")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "source.py")
    gen(_library(), dir_, sub, "structure.py")
    gen(_library(), dir_, sub, "test_structure.py")
    sub = Path("src", "lib", "mine", "src_gen", "script")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "source.py")
    gen(_library(), dir_, sub, "structure.py")
    gen(_library(), dir_, sub, "test_structure.py")
    sub = Path("src", "lib", "mine", "src_gen", "script", "bash")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "source.py")
    gen(_library(), dir_, sub, "structure.py")
    gen(_library(), dir_, sub, "test_structure.py")
    sub = Path("src", "lib", "mine", "src_gen", "script", "bash", "briteonyx")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "source.py")
    gen(_library(), dir_, sub, "structure.py")
    gen(_library(), dir_, sub, "test_structure.py")
    sub = Path("src", "lib", "mine", "src_gen", "script", "python")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "source.py")
    gen(_library(), dir_, sub, "structure.py")
    gen(_library(), dir_, sub, "test_structure.py")
    sub = Path("src", "lib", "mine", "throw_out_your_templates")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "section_1.py")
    gen(_library(), dir_, sub, "section_2.py")
    gen(_library(), dir_, sub, "section_3.py")
    gen(_library(), dir_, sub, "section_4.py")


def _generate_lib_task(dir_):
    sub = Path("src", "lib", "mine", "task")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "exception.py")
    gen(_library(), dir_, sub, "delete_file.py")
    gen(_library(), dir_, sub, "queue.py")
    gen(_library(), dir_, sub, "task.py")
    gen(_library(), dir_, sub, "task_manager.py")
    gen(_library(), dir_, sub, "test_queue.py")
    gen(_library(), dir_, sub, "test_task.py")


def _generate_lib_utility(dir_):
    sub = Path("src", "lib", "mine", "utility")
    gen(_package(), dir_, sub, "__init__.py")
    gen(_library(), dir_, sub, "color_log_formatter.py")
    gen(_library(), dir_, sub, "config.py")
    gen(_library(), dir_, sub, "environment.py")
    gen(_library(), dir_, sub, "filesystem.py")
    gen(_library(), dir_, sub, "math.py")
    gen(_library(), dir_, sub, "my_assert.py")
    gen(_library(), dir_, sub, "my_logging.py")
    gen(_library(), dir_, sub, "my_terminal.py")
    gen(_library(), dir_, sub, "my_time.py")
    gen(_library(), dir_, sub, "processing.py")
    gen(_library(), dir_, sub, "singleton_application.py")
    gen(_library(), dir_, sub, "test_config.py")
    gen(_library(), dir_, sub, "test_filesystem.py")
    gen(_library(), dir_, sub, "test_math.py")
    gen(_library(), dir_, sub, "test_my_assert.py")
    gen(_library(), dir_, sub, "test_my_time.py")
    gen(_library(), dir_, sub, "test_text.py")
    gen(_library(), dir_, sub, "test_tracked_path.py")
    gen(_library(), dir_, sub, "text.py")
    gen(_library(), dir_, sub, "tracked_path.py")


def _library():
    return [
        library_header(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def _main():
    return [
        main_header(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def _package():
    return [
        package_header(),
        line(),
    ]


def _script():
    return [
        script_header(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def generate(directory):
    _generate_app(directory)
    _generate_bin(directory)
    _generate_briteonyx(directory)
    _generate_gen(directory)
    _generate_lib(directory)


"""DisabledContent
"""

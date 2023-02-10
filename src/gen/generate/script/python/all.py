#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.python.complete import *
from src_gen.script.python.source import generate as python
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


def _generate_bin_lib(dir_):
    pass


def _generate_briteonyx(dir_):
    _generate_briteonyx_bin(dir_ / "bin")
    _generate_briteonyx_doc(dir_ / "doc")


def _generate_briteonyx_bin(dir_):
    python(script(), dir_, "avro-print")
    python(script(), dir_, "extensions")
    python(script(), dir_, "list")
    python(script(), dir_, "parquet-print")
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
    _generate_home_bin_lib(dir_ / "lib")
    _generate_home_linux(dir_ / "Linux")
    _generate_home_macos(dir_ / "macOS")
    _generate_home_macos_bin(dir_ / "bin")
    _generate_home_ssh(dir_ / ".ssh")


def _generate_home_bin(dir_):
    pass


def _generate_home_bin_lib(dir_):
    pass


def _generate_home_linux(dir_):
    pass


def _generate_home_macos(dir_):
    pass


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
    python(library(), dir_, "app.py")
    python(library(), dir_, "config.py")
    python(main(), dir_, "__main__.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "conftest.py")
    python(suite(), dir_, "test_app.py")
    python(suite(), dir_, "test_config.py")


def _generate_src_app_name_task(dir_):
    python(library(), dir_, "bootstrap.py")
    python(library(), dir_, "mapping.py")
    python(library(), dir_, "scan_directory.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_mapping.py")
    python(suite(), dir_, "test_task.py")


def _generate_src_gen(dir_):
    _generate_src_gen_generate(dir_ / "generate")


def _generate_src_gen_generate(dir_):
    _generate_src_gen_generate_custom(dir_ / "custom")
    _generate_src_gen_generate_shared(dir_ / "shared")
    python(library(), dir_, "app.py")
    python(library(), dir_, "config.py")
    python(main(), dir_, "__main__.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "conftest.py")
    python(suite(), dir_, "test_app.py")
    python(suite(), dir_, "test_config.py")


def _generate_src_gen_generate_custom(dir_):
    python(library(), dir_, "all.py")
    python(package(), dir_, "__init__.py")


def _generate_src_gen_generate_shared(dir_):
    _generate_src_gen_generate_shared_briteonyx(dir_ / "briteonyx")
    python(library(), dir_, "all.py")
    python(package(), dir_, "__init__.py")


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


def _generate_src_lib_mine_aws(dir_):
    pass


def _generate_src_lib_mine_aws(dir_):
    python(library(), dir_, "ec2.py")
    python(library(), dir_, "s3.py")
    python(library(), dir_, "service.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_ec2.py")
    python(suite(), dir_, "test_s3.py")
    python(suite(), dir_, "test_service.py")


def _generate_src_lib_mine_src_gen(dir_):
    _generate_src_lib_mine_src_gen_document(dir_ / "document")
    _generate_src_lib_mine_src_gen_script(dir_ / "script")
    python(library(), dir_, "renderer.py")
    python(library(), dir_, "source.py")
    python(library(), dir_, "structure.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_renderer.py")
    python(suite(), dir_, "test_source.py")
    python(suite(), dir_, "test_structure.py")


def _generate_src_lib_mine_src_gen_document(dir_):
    _generate_src_lib_mine_src_gen_document_markdown(dir_ / "markdown")
    python(package(), dir_, "__init__.py")


def _generate_src_lib_mine_src_gen_document_markdown(dir_):
    python(library(), dir_, "complete.py")
    python(library(), dir_, "source.py")
    python(library(), dir_, "structure.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_complete.py")
    python(suite(), dir_, "test_source.py")
    python(suite(), dir_, "test_structure.py")


def _generate_src_lib_mine_src_gen_script(dir_):
    _generate_src_lib_mine_src_gen_script_bash(dir_ / "bash")
    _generate_src_lib_mine_src_gen_script_python(dir_ / "python")
    python(library(), dir_, "source.py")
    python(library(), dir_, "structure.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_source.py")
    python(suite(), dir_, "test_structure.py")


def _generate_src_lib_mine_src_gen_script_bash(dir_):
    _generate_src_lib_mine_src_gen_script_bash_briteonyx(dir_ / "briteonyx")
    python(library(), dir_, "complete.py")
    python(library(), dir_, "source.py")
    python(library(), dir_, "structure.py")
    python(package(), dir_, "__init__.py")
    python(suite(), dir_, "test_complete.py")
    python(suite(), dir_, "test_source.py")
    python(suite(), dir_, "test_structure.py")


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
    pass


def generate(directory):
    _generate(directory)


"""DisabledContent
"""

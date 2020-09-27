#!/usr/bin/env false
"""Generate all Python scripts."""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from src_gen.script.python.source import generate as gen
from src_gen.script.python.structure import *
# Co-located modules (relative references, NOT packaged, in project)


def _generate_BriteOnyx(directory):
    sub = Path('BriteOnyx', 'bin')
    gen(_script(), directory, sub, 'avro-print')
    gen(_script(), directory, sub, 'extensions')
    gen(_script(), directory, sub, 'list')
    gen(_script(), directory, sub, 'parquet-print')

def _generate_app(directory):
    sub = Path('src', 'app', 'MODULE')
    gen(_package(), directory, sub, '__init__.py')
    gen(_main(), directory, sub, '__main__.py')
    gen(_library(), directory, sub, 'app.py')
    gen(_library(), directory, sub, 'config.py')
    gen(_library(), directory, sub, 'test_app.py')
    gen(_library(), directory, sub, 'test_config.py')
    sub = Path('src', 'app', 'MODULE', 'task')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'bootstrap.py')
    gen(_library(), directory, sub, 'mapping.py')
    gen(_library(), directory, sub, 'scan_directory.py')
    gen(_library(), directory, sub, 'test_mapping.py')
    gen(_library(), directory, sub, 'test_task.py')

def _generate_bin(directory):
    sub = Path('bin')

def _generate_gen(directory):
    sub = Path('src', 'gen', 'generate')
    gen(_package(), directory, sub, '__init__.py')
    gen(_main(), directory, sub, '__main__.py')
    gen(_library(), directory, sub, 'app.py')
    gen(_library(), directory, sub, 'config.py')
    gen(_library(), directory, sub, 'test_app.py')
    gen(_library(), directory, sub, 'test_config.py')
    sub = Path('src', 'gen', 'generate', 'document')
    gen(_package(), directory, sub, '__init__.py')
    sub = Path('src', 'gen', 'generate', 'document', 'markdown')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'all.py')
    sub = Path('src', 'gen', 'generate', 'script')
    gen(_package(), directory, sub, '__init__.py')
    sub = Path('src', 'gen', 'generate', 'script', 'bash')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'all.py')
    gen(_library(), directory, sub, 'activate.py')
    gen(_library(), directory, sub, 'set_path.py')
    sub = Path('src', 'gen', 'generate', 'script', 'bash', 'briteonyx')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'all.py')
    sub = Path('src', 'gen', 'generate', 'script', 'python')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'all.py')

def _generate_lib(directory):
    _generate_lib_aws(directory)
    _generate_lib_src_gen(directory)
    _generate_lib_task(directory)
    _generate_lib_utility(directory)

def _generate_lib_aws(directory):
    sub = Path('src', 'lib', 'mine', 'aws')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'ec2.py')
    gen(_library(), directory, sub, 's3.py')
    gen(_library(), directory, sub, 'service.py')
    gen(_library(), directory, sub, 'test_ec2.py')
    gen(_library(), directory, sub, 'test_s3.py')
    gen(_library(), directory, sub, 'test_service.py')

def _generate_lib_src_gen(directory):
    sub = Path('src', 'lib', 'mine', 'src_gen')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'renderer.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('src', 'lib', 'mine', 'src_gen', 'document')
    gen(_package(), directory, sub, '__init__.py')
    sub = Path('src', 'lib', 'mine', 'src_gen', 'document', 'markdown')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('src', 'lib', 'mine', 'src_gen', 'script')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('src', 'lib', 'mine', 'src_gen', 'script', 'bash')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('src', 'lib', 'mine', 'src_gen', 'script', 'bash', 'briteonyx')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('src', 'lib', 'mine', 'src_gen', 'script', 'python')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('src', 'lib', 'mine', 'throw_out_your_templates')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'section_1.py')
    gen(_library(), directory, sub, 'section_2.py')
    gen(_library(), directory, sub, 'section_3.py')
    gen(_library(), directory, sub, 'section_4.py')

def _generate_lib_task(directory):
    sub = Path('src', 'lib', 'mine', 'task')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'exception.py')
    gen(_library(), directory, sub, 'delete_file.py')
    gen(_library(), directory, sub, 'queue.py')
    gen(_library(), directory, sub, 'task.py')
    gen(_library(), directory, sub, 'task_manager.py')
    gen(_library(), directory, sub, 'test_queue.py')
    gen(_library(), directory, sub, 'test_task.py')

def _generate_lib_utility(directory):
    sub = Path('src', 'lib', 'mine', 'utility')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'color_log_formatter.py')
    gen(_library(), directory, sub, 'config.py')
    gen(_library(), directory, sub, 'environment.py')
    gen(_library(), directory, sub, 'filesystem.py')
    gen(_library(), directory, sub, 'math.py')
    gen(_library(), directory, sub, 'my_assert.py')
    gen(_library(), directory, sub, 'my_logging.py')
    gen(_library(), directory, sub, 'my_terminal.py')
    gen(_library(), directory, sub, 'my_time.py')
    gen(_library(), directory, sub, 'processing.py')
    gen(_library(), directory, sub, 'singleton_application.py')
    gen(_library(), directory, sub, 'test_config.py')
    gen(_library(), directory, sub, 'test_filesystem.py')
    gen(_library(), directory, sub, 'test_math.py')
    gen(_library(), directory, sub, 'test_my_assert.py')
    gen(_library(), directory, sub, 'test_my_time.py')
    gen(_library(), directory, sub, 'test_text.py')
    gen(_library(), directory, sub, 'test_tracked_path.py')
    gen(_library(), directory, sub, 'text.py')
    gen(_library(), directory, sub, 'tracked_path.py')

def _library():
    return [
        library_module_header(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def _main():
    return [
        main_module_header(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def _package():
    return [
        package_module_header(),
        line(),
    ]

def _script():
    return [
        script_module_header(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def generate(directory):
    _generate_BriteOnyx(directory)
    _generate_app(directory)
    _generate_bin(directory)
    _generate_gen(directory)
    _generate_lib(directory)

'''DisabledContent
'''


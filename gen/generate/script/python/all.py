#!/usr/bin/env false
"""
"""
from pathlib import Path

from src_gen.script.python.source    import generate as gen
from src_gen.script.python.structure import *


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
    ]

def _script():
    return [
        script_module_header(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def generate(directory):
    sub = Path('BriteOnyx', 'bin')
    gen(_script(), directory, sub, 'avro-print')
    gen(_script(), directory, sub, 'extensions')
    gen(_script(), directory, sub, 'list')
    sub = Path('gen', 'generate')
    gen(_package(), directory, sub, '__init__.py')
    gen(_main(), directory, sub, '__main__.py')
    gen(_library(), directory, sub, 'app.py')
    gen(_library(), directory, sub, 'config.py')
    gen(_library(), directory, sub, 'test_app.py')
    gen(_library(), directory, sub, 'test_config.py')
    sub = Path('gen', 'generate', 'document')
    gen(_package(), directory, sub, '__init__.py')
    sub = Path('gen', 'generate', 'document', 'markdown')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'all.py')
    sub = Path('gen', 'generate', 'script')
    gen(_package(), directory, sub, '__init__.py')
    sub = Path('gen', 'generate', 'script', 'bash')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'all.py')
    gen(_library(), directory, sub, 'project_activate_script.py')
    sub = Path('gen', 'generate', 'script', 'bash', 'briteonyx')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'all.py')
    sub = Path('gen', 'generate', 'script', 'python')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'all.py')
    sub = Path('gen', 'generate', 'utility')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'my_logging.py')
    gen(_library(), directory, sub, 'my_terminal.py')
    sub = Path('lib', 'mine', 'src_gen')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'renderer.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'src_gen', 'document')
    gen(_package(), directory, sub, '__init__.py')
    sub = Path('lib', 'mine', 'src_gen', 'document', 'markdown')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'src_gen', 'script')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'src_gen', 'script', 'bash')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'src_gen', 'script', 'bash', 'briteonyx')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'src_gen', 'script', 'python')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'source.py')
    gen(_library(), directory, sub, 'structure.py')
    gen(_library(), directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'throw_out_your_templates')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'section_1.py')
    gen(_library(), directory, sub, 'section_2.py')
    gen(_library(), directory, sub, 'section_3.py')
    gen(_library(), directory, sub, 'section_4.py')
    gen(_library(), directory, sub, 'test_section_1.py')
    gen(_library(), directory, sub, 'test_section_2.py')
    gen(_library(), directory, sub, 'test_section_3.py')
    gen(_library(), directory, sub, 'test_section_4.py')
    sub = Path('lib', 'mine', 'utility')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'environment.py')
    gen(_library(), directory, sub, 'filesystem.py')
    gen(_library(), directory, sub, 'math.py')
    gen(_library(), directory, sub, 'my_assert.py')
    gen(_library(), directory, sub, 'my_system.py')
    gen(_library(), directory, sub, 'my_time.py')
    gen(_library(), directory, sub, 'processing.py')
    gen(_library(), directory, sub, 'singleton_application.py')
    gen(_library(), directory, sub, 'test_environment.py')
    gen(_library(), directory, sub, 'test_filesystem.py')
    gen(_library(), directory, sub, 'test_math.py')
    gen(_library(), directory, sub, 'test_text.py')
    gen(_library(), directory, sub, 'test_time.py')
    gen(_library(), directory, sub, 'text.py')
    gen(_library(), directory, sub, 'time.py')
    sub = Path('src', 'MODULE')
    gen(_package(), directory, sub, '__init__.py')
    gen(_main(), directory, sub, '__main__.py')
    gen(_library(), directory, sub, 'app.py')
    gen(_library(), directory, sub, 'config.py')
    gen(_library(), directory, sub, 'test_app.py')
    gen(_library(), directory, sub, 'test_config.py')
    sub = Path('src', 'MODULE', 'task')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'bootstrap.py')
    gen(_library(), directory, sub, 'delete_file.py')
    gen(_library(), directory, sub, 'mapping.py')
    gen(_library(), directory, sub, 'queue.py')
    gen(_library(), directory, sub, 'scan_directory.py')
    gen(_library(), directory, sub, 'task.py')
    gen(_library(), directory, sub, 'task_manager.py')
    gen(_library(), directory, sub, 'test_mapping.py')
    gen(_library(), directory, sub, 'test_queue.py')
    gen(_library(), directory, sub, 'test_task.py')
    sub = Path('src', 'MODULE', 'utility')
    gen(_package(), directory, sub, '__init__.py')
    gen(_library(), directory, sub, 'my_logging.py')
    gen(_library(), directory, sub, 'my_terminal.py')

'''DisabledContent
'''


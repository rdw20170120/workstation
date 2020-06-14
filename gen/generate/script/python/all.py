#!/usr/bin/env false
"""
"""
from pathlib import Path

from throw_out_your_templates.section_3 import VisitorMap

from src_gen.script.python.source    import PythonSource
from src_gen.script.python.source    import visitor_map as parent_visitor_map
from src_gen.script.python.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _generate(content, target_directory, subdirectories, file_name):
    source = PythonSource(
        visitor_map,
        subdirectories, file_name,
        content
        )
    source.generate(target_directory)

def _library_module():
    return [
        library_module_header(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def _main_module():
    return [
        main_module_header(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def _package_module():
    return [
        package_module_header(),
    ]

def _script_module():
    return [
        script_module_header(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def generate(target_directory):
    sub = Path('BriteOnyx', 'bin')
    _generate(_script_module(), target_directory, sub, 'avro-print')
    _generate(_script_module(), target_directory, sub, 'extensions')
    _generate(_script_module(), target_directory, sub, 'list')
    sub = Path('gen', 'generate')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_main_module(), target_directory, sub, '__main__.py')
    _generate(_library_module(), target_directory, sub, 'app.py')
    _generate(_library_module(), target_directory, sub, 'config.py')
    _generate(_library_module(), target_directory, sub, 'test_app.py')
    _generate(_library_module(), target_directory, sub, 'test_config.py')
    sub = Path('gen', 'generate', 'document')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    sub = Path('gen', 'generate', 'document', 'markdown')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'all.py')
    sub = Path('gen', 'generate', 'script')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    sub = Path('gen', 'generate', 'script', 'bash')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'all.py')
    _generate(_library_module(), target_directory, sub, 'project_activate_script.py')
    sub = Path('gen', 'generate', 'script', 'bash', 'briteonyx')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'all.py')
    sub = Path('gen', 'generate', 'script', 'python')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'all.py')
    sub = Path('lib', 'mine', 'src_gen')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'renderer.py')
    _generate(_library_module(), target_directory, sub, 'source.py')
    _generate(_library_module(), target_directory, sub, 'structure.py')
    _generate(_library_module(), target_directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'src_gen', 'document')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    sub = Path('lib', 'mine', 'src_gen', 'document', 'markdown')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'source.py')
    _generate(_library_module(), target_directory, sub, 'structure.py')
    _generate(_library_module(), target_directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'src_gen', 'script')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'source.py')
    _generate(_library_module(), target_directory, sub, 'structure.py')
    _generate(_library_module(), target_directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'src_gen', 'script', 'bash')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'source.py')
    _generate(_library_module(), target_directory, sub, 'structure.py')
    _generate(_library_module(), target_directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'src_gen', 'script', 'bash', 'briteonyx')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'source.py')
    _generate(_library_module(), target_directory, sub, 'structure.py')
    _generate(_library_module(), target_directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'src_gen', 'script', 'python')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'source.py')
    _generate(_library_module(), target_directory, sub, 'structure.py')
    _generate(_library_module(), target_directory, sub, 'test_structure.py')
    sub = Path('lib', 'mine', 'throw_out_your_templates')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'section_1.py')
    _generate(_library_module(), target_directory, sub, 'section_2.py')
    _generate(_library_module(), target_directory, sub, 'section_3.py')
    _generate(_library_module(), target_directory, sub, 'section_4.py')
    _generate(_library_module(), target_directory, sub, 'test_section_1.py')
    _generate(_library_module(), target_directory, sub, 'test_section_2.py')
    _generate(_library_module(), target_directory, sub, 'test_section_3.py')
    _generate(_library_module(), target_directory, sub, 'test_section_4.py')
    sub = Path('lib', 'mine', 'utility')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'environment.py')
    _generate(_library_module(), target_directory, sub, 'filesystem.py')
    _generate(_library_module(), target_directory, sub, 'math.py')
    _generate(_library_module(), target_directory, sub, 'my_assert.py')
    _generate(_library_module(), target_directory, sub, 'my_system.py')
    _generate(_library_module(), target_directory, sub, 'my_time.py')
    _generate(_library_module(), target_directory, sub, 'processing.py')
    _generate(_library_module(), target_directory, sub, 'singleton_application.py')
    _generate(_library_module(), target_directory, sub, 'test_environment.py')
    _generate(_library_module(), target_directory, sub, 'test_filesystem.py')
    _generate(_library_module(), target_directory, sub, 'test_math.py')
    _generate(_library_module(), target_directory, sub, 'test_text.py')
    _generate(_library_module(), target_directory, sub, 'test_time.py')
    _generate(_library_module(), target_directory, sub, 'text.py')
    _generate(_library_module(), target_directory, sub, 'time.py')
    sub = Path('src', 'MODULE')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_main_module(), target_directory, sub, '__main__.py')
    _generate(_library_module(), target_directory, sub, 'app.py')
    _generate(_library_module(), target_directory, sub, 'config.py')
    _generate(_library_module(), target_directory, sub, 'test_app.py')
    _generate(_library_module(), target_directory, sub, 'test_config.py')
    sub = Path('src', 'MODULE', 'task')
    _generate(_package_module(), target_directory, sub, '__init__.py')
    _generate(_library_module(), target_directory, sub, 'bootstrap.py')
    _generate(_library_module(), target_directory, sub, 'delete_file.py')
    _generate(_library_module(), target_directory, sub, 'mapping.py')
    _generate(_library_module(), target_directory, sub, 'queue.py')
    _generate(_library_module(), target_directory, sub, 'scan_directory.py')
    _generate(_library_module(), target_directory, sub, 'task.py')
    _generate(_library_module(), target_directory, sub, 'task_manager.py')
    _generate(_library_module(), target_directory, sub, 'test_mapping.py')
    _generate(_library_module(), target_directory, sub, 'test_queue.py')
    _generate(_library_module(), target_directory, sub, 'test_task.py')

'''DisabledContent
    sub = Path('.')
    _generate(_script_module(), target_directory, sub, '')
'''


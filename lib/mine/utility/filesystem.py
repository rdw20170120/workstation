#!/usr/bin/env false
"""TODO: Write

TODO: REVIEW: this module against its siblings.
"""
# Internal packages  (absolute references, distributed with Python)
from os      import remove
from os.path import getsize
from pathlib import Path
from pathlib import PurePath
from shutil  import copy2
from shutil  import rmtree
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)


def clone_file(source_file, target_file):
    assert isinstance(source_file, Path)
    assert isinstance(target_file, Path)
    actual = copy2(source_file, target_file)
    assert actual == target_file

def concatenate_text_file(source_file, target_file, encoding=None):
    if encoding is None: encoding = 'utf_8'
    assert isinstance(source_file, Path)
    assert isinstance(target_file, Path)
    with target_file.open(
        encoding=encoding, mode='at', newline=None
        ) as writer:
        with source_file.open(
            encoding=encoding, mode='rt', newline=None
            ) as reader:
            for line in reader:
                writer.write(line)

def concatenate_text_files(target_file, source_files, encoding=None):
    if encoding is None: encoding = 'utf_8'
    assert isinstance(target_file, Path)
    assert isinstance(source_files, list)
    with target_file.open(
        encoding=encoding, mode='wt', newline=None
        ) as writer:
        for s in source_files:
            assert isinstance(s, Path)
            with s.open(
                encoding=encoding, mode='rt', newline=None
                ) as reader:
                for line in reader:
                    writer.write(line)

def delete_directory_tree(directory_path, force=False):
    assert isinstance(directory_path, Path)
    rmtree(directory_path, ignore_errors=force)

def delete_file(file_path):
    assert isinstance(file_path, Path)
    remove(file_path)

def file_name_has_extension(pathname, extension):
    assert isinstance(extension, str)
    if isinstance(pathname, str): pathname = Path(pathname)
    if isinstance(pathname, Path) or isinstance(pathname, PurePath):
        return pathname.suffix == extension
    else:
        raise ValueError(
            "Cannot file_name_has_extension('{}', '{}')".format(pathname, extension)
            )

def file_name_has_suffix(pathname, suffix):
    assert isinstance(suffix, str)
    if isinstance(pathname, str): pathname = Path(pathname)
    if isinstance(pathname, Path) or isinstance(pathname, PurePath):
        return str(pathname).endswith(suffix)
    else:
        raise ValueError(
            "Cannot file_name_has_suffix('{}', '{}')".format(pathname, suffix)
            )

def file_size(file_path):
    assert isinstance(file_path, Path)
    return getsize(file_path)

def split_file_name(file_path):
    if isinstance(file_path, str): file_path = PurePath(file_path)
    if isinstance(file_path, Path) or isinstance(file_path, PurePath):
        name = PurePath(file_path.name)
        suffixes = ''
        while True:
            suffix, name = name.suffix, name.stem
            if not suffix: break
            suffixes = suffix + suffixes
            name = PurePath(name)
        return name, suffixes
    else:
        raise ValueError("Cannot split_file_name('{}')".format(file_path))

def touch(file_path):
    if isinstance(file_path, str): file_path = PurePath(file_path)
    if isinstance(file_path, Path) or isinstance(file_path, PurePath):
        if not file_path.exists(): 
            with open(file_path,
                encoding=encoding, mode='wt', newline=None
                ) as f:
                f.write('')
        file_path.touch(exist_ok=True)
    else:
        raise ValueError("Cannot touch('{}')".format(file_path))

def read_binary_from_file(file_path):
    assert isinstance(file_path, Path)
    with open(file_path, mode='rb') as reader:
        result = reader.read()
        assert isinstance(result, bytes)
    return result

def read_text_from_file(file_path, encoding=None):
    if encoding is None: encoding = 'utf_8'
    assert isinstance(file_path, Path)
    with open(file_path,
        encoding=encoding, mode='rt', newline=None
        ) as reader:
        result = reader.read()
        assert isinstance(result, str)
    return result

def write_binary_into_file(file_path, binary_content):
    assert isinstance(file_path, Path)
    assert isinstance(binary_content, bytes)
    with open(file_path, mode='wb') as writer:
        count = writer.write(binary_content)
        assert count == len(binary_content)

def write_text_into_file(file_path, text_content, encoding=None):
    if encoding is None: encoding = 'utf_8'
    assert isinstance(file_path, Path)
    assert isinstance(text_content, str)
    with open(file_path,
        encoding=encoding, mode='wt', newline=None
        ) as writer:
        count = writer.write(text_content)
        assert count == len(text_content)

'''DisabledContent
'''


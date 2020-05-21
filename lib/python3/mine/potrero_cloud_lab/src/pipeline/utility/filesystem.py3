#!/bin/false

from os      import remove
from os.path import getsize
from pathlib import Path
from pathlib import PurePath
from shutil  import copy2
from shutil  import rmtree

# TODO: Convert to consistently use pathlib

def clone_file(source_file, target_file):
    assert isinstance(source_file, Path)
    assert isinstance(target_file, Path)
    actual = copy2(source_file, target_file)
    assert actual == target_file

def concatenate_text_file(source_file, target_file, encoding=None):
    assert isinstance(source_file, Path)
    assert isinstance(target_file, Path)
    if encoding is None: encoding = 'utf_8'
    with target_file.open(mode='at', encoding=encoding) as writer:
        with source_file.open(mode='rt', encoding=encoding) as reader:
            for line in reader:
                writer.write(line)

def delete_directory_tree(directory_path, force=False):
    assert isinstance(directory_path, Path)
    rmtree(directory_path, ignore_errors=force)

def delete_file(file_path):
    assert isinstance(file_path, Path)
    remove(file_path)

def file_size(file_path):
    assert isinstance(file_path, Path)
    return getsize(file_path)

def name_has_extension(pathname, extension):
    assert isinstance(extension, str)
    if isinstance(pathname, str): pathname = Path(pathname)
    if isinstance(pathname, Path) or isinstance(pathname, PurePath):
        return pathname.suffix == extension
    else:
        raise ValueError("Cannot name_has_extension('{}')".format(file_path))

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
        if file_path.exists(): file_path.touch(exist_ok=True)
        else:
            with open(file_path, 'wt') as f:
                f.write('')
    else:
        raise ValueError("Cannot touch('{}')".format(file_path))


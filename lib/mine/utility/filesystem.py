#!/usr/bin/env false
"""TODO: Write

TODO: REVIEW: this module against its siblings.
"""
# Internal packages  (absolute references, distributed with Python)
from logging import getLogger
from os      import remove
from os.path import getsize
from pathlib import Path
from pathlib import PurePath
from shutil  import copy2
from shutil  import rmtree
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)


log = getLogger(__name__)


def basename_has_suffix(pathname, suffix):
    assert isinstance(suffix, str)
    return str(pathname).endswith(suffix)

def clone_file(source_file, target_file):
    actual = copy2(source_file, target_file)
    assert actual == target_file

def concatenate_text_file(target_file, source_file, encoding=None):
    if encoding is None: encoding = 'utf_8'
    with target_file.open(
        encoding=encoding, mode='at', newline=None
        ) as writer:
        with source_file.open(
            encoding=encoding, mode='rt', newline=None
            ) as reader:
            for line in reader:
                log.debug(
                    "Concatenating to file '%s', encounter: %s",
                    target_file, line
                    )
                writer.write(line)

def concatenate_text_files(target_file, source_files, encoding=None):
    if encoding is None: encoding = 'utf_8'
    assert isinstance(source_files, list)
    with target_file.open(
        encoding=encoding, mode='wt', newline=None
        ) as writer:
        for s in source_files:
            with s.open(
                encoding=encoding, mode='rt', newline=None
                ) as reader:
                for line in reader:
                    writer.write(line)

def delete_directory_tree(directory_path, force=False):
    rmtree(directory_path, ignore_errors=force)

def delete_file(file_path):
    remove(file_path)

def file_size(file_path):
    return getsize(file_path)

def read_binary_from_file(file_path):
    with open(file_path, mode='rb') as reader:
        result = reader.read()
        assert isinstance(result, bytes)
    return result

def read_text_from_file(file_path, encoding=None):
    if encoding is None: encoding = 'utf_8'
    with open(file_path,
        encoding=encoding, mode='rt', newline=None
        ) as reader:
        result = reader.read()
        assert isinstance(result, str)
    return result

def split_basename(pathname):
    parent, basename = split_pathname(pathname)
    name = PurePath(basename)
    suffixes = ''
    while True:
        suffix, name = name.suffix, name.stem
        if not suffix: break
        suffixes = suffix + suffixes
        name = PurePath(name)
    return str(name), suffixes

def split_pathname(pathname):
    if not isinstance(pathname, Path): pathname = PurePath(pathname)
    return pathname.parent, pathname.name

def touch(file_path):
    if not isinstance(file_path, Path): file_path = PurePath(file_path)
    if not file_path.exists(): 
        with open(file_path,
            encoding=encoding, mode='wt', newline=None
            ) as f:
            f.write('')
    file_path.touch(exist_ok=True)

def write_binary_into_file(file_path, binary_content):
    assert isinstance(binary_content, bytes)
    with open(file_path, mode='wb') as writer:
        count = writer.write(binary_content)
        assert count == len(binary_content)

def write_text_into_file(file_path, text_content, encoding=None):
    if encoding is None: encoding = 'utf_8'
    assert isinstance(text_content, str)
    with open(file_path,
        encoding=encoding, mode='wt', newline=None
        ) as writer:
        count = writer.write(text_content)
        assert count == len(text_content)

'''DisabledContent
'''


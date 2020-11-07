#!/usr/bin/env false
"""TODO: Write

TODO: REVIEW: this module against its siblings.
"""
# Internal packages  (absolute references, distributed with Python)
from logging import getLogger
from os import link
from os import makedirs
from os import remove
from os.path import getsize
from os.path import isdir
from os.path import isfile
from pathlib import Path
from pathlib import PurePath
from shutil import copy2
from shutil import rmtree
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility import my_assert as is_
# Co-located modules (relative references, NOT packaged, in project)


log = getLogger(__name__)


def basename_has_suffix(path_, suffix):
    assert is_.instance(suffix, str)
    return str(path_).endswith(suffix)

def clone_file(source_file, target_file):
    assert is_.absolute_file(source_file)
    try:
        actual = copy2(str(source_file), str(target_file))
        assert is_.equal(actual, target_file)
    except BaseException:
        log.error('Failed to clone file %s to %s',
            source_file, target_file
            )
        raise

def concatenate_text_file(target_file, source_file, encoding=None):
    assert is_.absolute_file(source_file)
    if encoding is None: encoding = 'utf_8'
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
    assert is_.instance(source_files, list)
    with target_file.open(
        encoding=encoding, mode='wt', newline=None
        ) as writer:
        for s in source_files:
            assert is_.absolute_file(s)
            with s.open(
                encoding=encoding, mode='rt', newline=None
                ) as reader:
                for line in reader:
                    writer.write(line)

def create_directory(path_):
    try:
        makedirs(path_)
    except BaseException:
        log.error('Failed to create directory %s', path_)
        raise

def delete_directory(path_):
    try:
        rmtree(path_)
    except BaseException:
        log.error('Failed to delete directory %s', path_)
        raise

def delete_directory_tree(path_, force=False):
    try:
        rmtree(path_, ignore_errors=force)
    except BaseException:
        log.error('Failed to delete directory tree %s', path_)
        raise

def delete_file(file_):
    try:
        remove(file_)
    except BaseException:
        log.error('Failed to delete directory tree %s', path_)
        raise

def directory_exists(path_):
    result = isdir(path_)
    return result

def file_exists(path_name):
    result = isfile(path_name)
    return result

def file_size(file_):
    return getsize(file_)

def make_hard_link(new_path, existing_path):
    if isinstance(new_path, str): new_path = Path(new_path)
    assert is_.instance(new_path, Path)
    assert is_.absolute_path(new_path)
    assert is_.existing_absolute_path(existing_path)
    link(existing_path, new_path)
    # TODO: Added in Python 3.8
#   new_path.link_to(existing_path)

def maybe_create_directory(path_):
    if not directory_exists(path_): create_directory(path_)

def maybe_delete_directory(path_):
    if directory_exists(path_): delete_directory(path_)

def maybe_delete_file(path_):
    if file_exists(path_): delete_file(path_)

def read_binary_from_file(file_):
    with open(file_, mode='rb') as reader:
        result = reader.read()
        assert is_.instance(result, bytes)
    return result

def read_text_from_file(file_, encoding=None):
    if encoding is None: encoding = 'utf_8'
    with open(file_,
        encoding=encoding, mode='rt', newline=None
        ) as reader:
        result = reader.read()
        assert is_.instance(result, str)
    return result

def recreate_directory(path_):
    maybe_delete_directory(path_)
    create_directory(path_)

def split_basename(path_):
    parent, basename = split_path(path_)
    name = PurePath(basename)
    suffixes = ''
    while True:
        suffix, name = name.suffix, name.stem
        if not suffix: break
        suffixes = suffix + suffixes
        name = PurePath(name)
    return str(name), suffixes

def split_path(path_):
    if not isinstance(path_, Path): path_ = PurePath(path_)
    return path_.parent, path_.name

def touch(file_):
    try:
        if not isinstance(file_, Path):
            file_ = Path(file_)
        if not file_.exists():
            write_text_into_file(file_, '')
        file_.touch(exist_ok=True)
    except BaseException:
        log.error('Failed to touch file %s', file_)
        raise

def write_binary_into_file(file_, binary_content):
    assert is_.instance(binary_content, bytes)
    with open(file_, mode='wb') as writer:
        count = writer.write(binary_content)
        assert is_.equal(len(binary_content), count)

def write_text_into_file(file_, text_content, encoding=None):
    if encoding is None: encoding = 'utf_8'
    assert is_.instance(text_content, str)
    with open(file_,
        encoding=encoding, mode='wt', newline=None
        ) as writer:
        count = writer.write(text_content)
        assert is_.equal(len(text_content), count)

'''DisabledContent
'''


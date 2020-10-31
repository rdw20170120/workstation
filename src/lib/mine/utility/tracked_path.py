#!/usr/bin/env false
"""A path whose details are tracked in specific ways.

A tracked path has a filesystem path
consisting of a configured `top_directory`
concatenated with a `relative_path`.
When tracked in various ways such as in log files,
the tracked path is reported by its `relative_path`
and its `top_title` instead of its `top_directory`
(so that filesystem roots are abstracted out).
This makes it possible to keep track of a path
despite configuration differences across machines or over time.
The result is a stable reference suitable for comparisons.

A tracked path also has various metrics.
A primary metric is a record count, when relevant.

Tracked paths have various helpers to ease use
while enabling the consistent tracking of those metrics.
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
from shutil import rmtree
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.filesystem import split_path
from utility.my_assert import assert_absolute_directory
from utility.my_assert import assert_absolute_path
from utility.my_assert import assert_in
from utility.my_assert import assert_instance
from utility.my_assert import assert_not_instance
from utility.my_assert import assert_relative_path
# Co-located modules (relative references, NOT packaged, in project)


class TrackedPath(object):
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (other._title == self._title
                and other._path == self._path)
        elif isinstance(other, Path):
            return other == self.path
        else:
            return False

    def __fspath__(self):
        return str(self._path)

    def __getattr__(self, name):
        return getattr(self._path, name)

    def __init__(self, top_title, top_directory, relative_path=None):
        self._relative = relative_path
        self._title = top_title
        self._top = top_directory

        super().__init__()

        assert assert_instance(self._title, str)

        assert assert_not_instance(self._top, type(None))
        assert assert_not_instance(self._top, self.__class__)
        if not isinstance(self._top, Path): self._top = Path(self._top)
        assert assert_instance(self._top, Path)
        assert assert_absolute_path(self._top)
        if self._top.exists(): assert assert_absolute_directory(self._top)

        assert assert_not_instance(self._relative, self.__class__)
        if self._relative is None:
            # TODO: Use reference for current directory instead
            self._relative = Path('.')
        if not isinstance(self._relative, Path):
            self._relative = Path(self._relative)
        assert assert_instance(self._relative, Path)
        assert assert_relative_path(self._relative)
        self._subpath, self._basename = split_path(self._relative)

        self._path = self._top / self._relative
        assert assert_instance(self._path, Path)
        assert assert_absolute_path(self._path)

    def __repr__(self):
        return "{}({!r}, {!r}, {!r})".format(
            self.__class__.__name__,
            self._title, self._top, self._relative
            )

    def __str__(self):
        return self.__fspath__()

    def __truediv__(self, other):
        if other is None: other = Path()
        other = self._path / other
        return self.for_path(other)

    @property
    def basename(self):
        return self._basename

    def delete(self, force=False):
        if not self.exists(): return
        if self.is_dir():
            if force:
                rmtree(str(self), ignore_errors=force)
            else:
                self.rmdir()
        elif self.is_file():
            self.unlink()
        else:
            raise NotImplementedError(
                "Do not know how to delete {!r}".format(self)
                )

    def for_log(self):
        return "'{}' path '{}'".format(self._title, self._relative)

    def for_path(self, path):
        if not isinstance(path, Path): path = Path(path)
        relative = path.relative_to(self._top)
        return TrackedPath(self._title, self._top, relative)

    def open_for_binary_read(self, buffering=-1):
        return self._path.open(buffering=buffering, mode='br')

    def open_for_binary_write(self, buffering=-1):
        return self._path.open(buffering=buffering, mode='bw')

    def open_for_text_read(self,
        buffering=-1, encoding=None, errors=None, newline=None
        ):
        if encoding is None: encoding = 'utf_8'
        return self._path.open(
            buffering=buffering,
            encoding=encoding,
            errors=errors,
            mode='rt',
            newline=newline
            )

    def open_for_text_write(self,
        buffering=-1, encoding=None, errors=None, newline=None
        ):
        if encoding is None: encoding = 'utf_8'
        return self._path.open(
            buffering=buffering,
            encoding=encoding,
            errors=errors,
            mode='tw',
            newline=newline
            )

    @property
    def parent(self):
        return self.for_path(self._path.parent)

    @property
    def path(self):
        return self._path

    @property
    def relative(self):
        return self._relative

    @property
    def size(self):
        return self._path.stat().st_size

    def split_top(self):
        return self.top, self.subpath, self.basename

    @property
    def subpath(self):
        return self._subpath

    @property
    def top(self):
        return TrackedPath(self._title, self._top)

'''DisabledContent
'''


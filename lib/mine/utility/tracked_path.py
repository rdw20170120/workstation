#!/usr/bin/env false
"""A path whose details are tracked in specific ways.

A tracked path has a filesystem path
consisting of a configured `top_directory`
concatenated with a `relative_path`.
When tracked in various ways such as in log files,
the tracked path is reported by its `relative_path`
and its `top_name` instead of its `top_directory`
(so that filesystem roots are abstracted out).
This makes it possible to keep track of a path
despite configuration differences across machines or over time.
The result is a stable reference suitable for comparisons.

A tracked path also has various metrics.
A primary metric is a record count, when relevant.

Tracked paths have various helpers to ease use
while enabling the consistent tracking of those metrics.

TODO: Research how to best expose attributes of wrapped Path
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)


class TrackedPath(object):
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (other._name == self._name
                and other._path == self._path)
        elif isinstance(other, Path):
            return other == self.path
        else:
            return False

    def __fspath__(self):
        return str(self._path)

    def __getattr__(self, name):
        return getattr(self._path, name)

    def __init__(self, top_name, top_directory, relative_path=None):
        self._name = top_name
        self._relative = relative_path
        self._top = top_directory

        super().__init__()

        assert isinstance(self._name, str)

        if isinstance(self._top, str):
            self._top = Path(self._top)
        assert self._top.is_absolute()
        if self._top.exists(): assert self._top.is_dir()

        if self._relative is None:
            self._relative = Path('.')
        else:
            if isinstance(self._relative, str):
                self._relative = Path(self._relative)
            assert not self._relative.is_absolute()
        self._path = self._top / self._relative

    def __repr__(self):
        return "{}({!r}, {!r}, {!r})".format(
            self.__class__.__name__,
            self._name, self._top, self._relative
            )

    def __str__(self):
        return "{} '{}'".format(self._name, self._relative)

    def __truediv__(self, other):
        other = self._path / other
        return self.for_path(other)

    def exists(self):
        return self._path.exists()

    def for_path(self, path):
        if isinstance(path, str):
            path = Path(path)
        relative = path.relative_to(self._top)
        return TrackedPath(self._name, self._top, relative)

    def is_absolute(self):
        return self._path.is_absolute()

    def is_dir(self):
        return self._path.is_dir()

    def is_file(self):
        return self._path.is_file()

    @property
    def relative(self):
        return self._relative

    @property
    def path(self):
        return self._path


'''DisabledContent
'''


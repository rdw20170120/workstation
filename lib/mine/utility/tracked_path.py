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
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)


class TrackedPath(object):
    def __fspath__(self):
        return str(self._path)

    def __init__(self, top_name, top_directory, relative_path):
        super().__init__()

        if isinstance(relative_path, str):
            relative_path = Path(relative_path)
        assert isinstance(relative_path, Path)
        assert not relative_path.is_absolute()
        self._relative = relative_path

        if isinstance(top_directory, str):
            top_directory = Path(top_directory)
        assert isinstance(top_directory, Path)
        if top_directory.exists(): assert top_directory.is_dir()
        self._directory = top_directory

        assert isinstance(top_name, str)
        self._name = top_name

        self._path = self._directory / self._relative

    def __repr__(self):
        return "{}({!r}, {!r}, {!r})".format(
            self.__class__.__name__,
            self._name, self._directory, self._relative
            )

    def __str__(self):
        return self.__fspath__()

    @property
    def for_log(self):
        return "{} path '{}'".format(self._name, self._relative)

    @property
    def for_ref(self):
        return "{}".format(self._relative)

'''DisabledContent
'''


#!/usr/bin/python
# Manage files

import fnmatch
import glob
import os
import shutil


class FileManager(object):
    def copy_directory(self, source, target, pattern=None, flatten=False, maybe=False):
        # TODO: FIX: implement use of glob pattern
        for name in self.names_in_directory(source):
            next_source = os.path.join(source, name)
            next_target = os.path.join(target, name)
            try:
                if os.path.isdir(next_source):
                    if flatten:
                        next_target = target
                    self.create_directory(next_target)
                    self.copy_directory(
                        next_source, next_target, pattern, flatten, maybe
                    )
                else:
                    if self.name_matches(next_source, pattern):
                        self.copy_file(next_source, next_target, maybe)
            except (IOError, os.error) as e:
                print(
                    ('Cannot copy "%s"\n  to "%s"\n  because %s' % (source, target, e))
                )

    def copy_file(self, source, target, maybe=False):
        skip = maybe
        if skip:
            skip = os.path.exists(target)
        if not skip:
            print(('Copying file "%s"\n  to "%s"' % (source, target)))
            shutil.copyfile(source, target)

    def create_directory(self, directory):
        if not os.path.exists(directory):
            print(('Creating directory "%s"' % (directory,)))
            os.mkdir(directory)

    def list(self, directory, pattern=None):
        # TODO: FIX: implement use of glob pattern
        for current, directories, files in os.walk(directory):
            print(("Current ", current))
            print(("  Subdirectories", directories))
            print(("  Files", files))

    def names_in_directory(self, directory):
        return os.listdir(directory)

    def name_matches(self, name, pattern):
        if pattern is None:
            return True
        else:
            return fnmatch.fnmatch(name, pattern)


if __name__ == "__main__":

    def check_argument_count(arguments, minimum_count, maximum_count=None):
        try:
            if maximum_count is None:
                maximum_count = minimum_count
            count = len(arguments)
            if count < minimum_count:
                raise ValueError(
                    'Argument count "%d" is less than minimum "%d"!'
                    % (count, minimum_count)
                )
            if count > maximum_count:
                raise ValueError(
                    'Argument count "%d" is more than maximum "%d"!'
                    % (count, maximum_count)
                )
        except ValueError:
            print("Command-line arguments:")
            print((sys.argv))
            raise

    def help():
        print(
            """
Available commands:
    copy_flat <source> <target> [<glob>]
        Copy source directory tree flattened into single target directory
        Optionally filtering with glob pattern (see Python glob module)
    copy_tree <source> <target> [<glob>]
        Copy source directory tree to target directory tree
        Optionally filtering with glob pattern (see Python glob module)
    list <directory> [<glob>]
        List directory
        Optionally filtering with glob pattern (see Python glob module)
    maybe_copy_flat <source> <target> [<glob>]
        Maybe copy source directory tree flattened into single target directory
        Optionally filtering with glob pattern (see Python glob module)
        Skip existing files
    maybe_copy_tree <source> <target> [<glob>]
        Maybe copy source directory tree to target
        Optionally filtering with glob pattern (see Python glob module)
        Skip existing files
"""
        )

    import sys

    mgr = FileManager()
    check_argument_count(sys.argv, 2, 5)
    command = sys.argv[1]
    if "help" == command:
        help()
    elif "copy_flat" == command:
        check_argument_count(sys.argv, 4, 5)
        pattern = None
        if len(sys.argv) == 5:
            pattern = str(sys.argv[4])
        mgr.copy_directory(
            source=str(sys.argv[2]),
            target=str(sys.argv[3]),
            pattern=pattern,
            flatten=True,
            maybe=False,
        )
    elif "copy_tree" == command:
        check_argument_count(sys.argv, 4, 5)
        pattern = None
        if len(sys.argv) == 5:
            pattern = str(sys.argv[4])
        mgr.copy_directory(
            source=str(sys.argv[2]),
            target=str(sys.argv[3]),
            pattern=pattern,
            flatten=False,
            maybe=False,
        )
    elif "list" == command:
        check_argument_count(sys.argv, 3, 4)
        pattern = None
        if len(sys.argv) == 4:
            pattern = str(sys.argv[3])
        mgr.list(
            directory=str(sys.argv[2]),
            pattern=pattern,
        )
    elif "maybe_copy_flat" == command:
        check_argument_count(sys.argv, 4, 5)
        pattern = None
        if len(sys.argv) == 5:
            pattern = str(sys.argv[4])
        mgr.copy_directory(
            source=str(sys.argv[2]),
            target=str(sys.argv[3]),
            pattern=pattern,
            flatten=True,
            maybe=True,
        )
    elif "maybe_copy_tree" == command:
        check_argument_count(sys.argv, 4, 5)
        pattern = None
        if len(sys.argv) == 5:
            pattern = str(sys.argv[4])
        mgr.copy_directory(
            source=str(sys.argv[2]),
            target=str(sys.argv[3]),
            pattern=pattern,
            flatten=False,
            maybe=True,
        )
    else:
        raise ValueError('Command "%s" is unrecognized, try "help"!' % (command,))

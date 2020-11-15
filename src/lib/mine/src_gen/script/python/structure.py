#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.structure import *
from src_gen.script.source import my_visitor_map

# Project modules   (relative references, NOT packaged, in project)


###############################################################################


def shebang_python3():
    return shebang_thru_env("python3")


###############################################################################


def import_header_external():
    return [
        comment(
            "External packages (absolute references, NOT distributed with Python)"
        ),
    ]


def import_header_internal():
    return [
        comment(
            "Internal packages (absolute references, distributed with Python)"
        ),
    ]


def import_header_project():
    return [
        comment(
            "Project modules   (relative references, NOT packaged, in project)"
        ),
    ]


def import_header_library():
    return [
        comment(
            "Library modules   (absolute references, NOT packaged, in project)"
        ),
    ]


###############################################################################


class _Import(object):
    def __init__(self, package, as_):
        super().__init__()
        self.package = squashed(package)
        assert is_.not_none(self.package)
        self.as_ = squashed(as_)

    def __repr__(self):
        return "_Import({}, {})".format(self.package, self.as_)


@my_visitor_map.register(_Import)
def _visit_import(element, walker):
    walker.emit("import ")
    walker.walk(element.package)
    if element.as_ is not None:
        walker.emit(" as ")
        walker.walk(element.as_)
    walker.emit("\n")


def import_(package, as_=None):
    return _Import(package, as_)


class _ImportFrom(object):
    def __init__(self, package, item, as_):
        super().__init__()
        self.package = squashed(package)
        assert is_.not_none(self.package)
        self.item = squashed(item)
        assert is_.not_none(self.item)
        self.as_ = squashed(as_)

    def __repr__(self):
        return "_ImportFrom({}, {}, {})".format(
            self.package, self.item, self.as_
        )


@my_visitor_map.register(_ImportFrom)
def _visit_import_from(element, walker):
    walker.emit("from ")
    walker.walk(element.package)
    walker.emit(" import ")
    walker.walk(element.item)
    if element.as_ is not None:
        walker.emit(" as ")
        walker.walk(element.as_)
    walker.emit("\n")


def import_from(package, item, as_=None):
    return _ImportFrom(package, item, as_)


###############################################################################
def empty_imports():
    return [
        import_header_internal(),
        import_header_external(),
        import_header_library(),
        import_header_project(),
    ]


def test_imports():
    return [
        import_header_internal(),
        import_header_external(),
        import_from("pytest", "fixture"),
        import_from("pytest", "mark"),
        import_from("pytest", "param"),
        import_from("pytest", "raises"),
        import_header_library(),
        import_from("utility", "my_assert", "is_"),
        import_header_project(),
    ]


###############################################################################
def disabled_content_footer():
    return [
        line(),
        '"""DisabledContent',
        eol(),
        '"""',
        eol(),
        line(),
    ]


def library_header():
    return [
        shebang_false(),
        '"""TODO: Write',
        eol(),
        '"""',
        eol(),
        empty_imports(),
        line(),
        line(),
    ]


def main_header():
    return [
        shebang_false(),
        '"""TODO: Write',
        eol(),
        '"""',
        eol(),
        empty_imports(),
        line(),
        line(),
    ]


def package_header():
    return [
        shebang_false(),
        line(),
    ]


def script_header():
    return [
        shebang_python3(),
        '"""TODO: Write',
        eol(),
        line(),
        line("Intended to be executed directly by the user."),
        '"""',
        eol(),
        empty_imports(),
        line(),
        line(),
    ]


def test_header():
    return [
        shebang_false(),
        '"""Test corresponding module."""',
        eol(),
        test_imports(),
        line(),
        line(),
    ]


"""DisabledContent
"""

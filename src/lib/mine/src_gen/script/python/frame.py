#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)

def footer_for_disabled_content():
    return [
        line(),
        '"""DisabledContent',
        eol(),
        '"""',
        eol(),
        line(),
    ]


def header_for_generator():
    return [
        shebang_false(),
        '"""Generate script to TODO',
        eol(),
        '"""',
        eol(),
        imports_empty(),
        line(),
        line(),
    ]


def header_for_library():
    return [
        shebang_false(),
        '"""TODO: Write',
        eol(),
        '"""',
        eol(),
        imports_empty(),
        line(),
        line(),
    ]


def header_for_main():
    return [
        shebang_false(),
        '"""TODO: Write',
        eol(),
        '"""',
        eol(),
        imports_empty(),
        line(),
        line(),
    ]


def header_for_package():
    return [
        shebang_false(),
        line(),
    ]


def header_for_script():
    return [
        shebang_python3(),
        '"""TODO: Write',
        eol(),
        line(),
        line("Intended to be executed directly by the user."),
        '"""',
        eol(),
        imports_empty(),
        line(),
        line(),
    ]


def header_for_suite():
    return [
        shebang_false(),
        '"""Test corresponding module."""',
        eol(),
        imports_for_suite(),
        line(),
        line(),
    ]


def import_header_external():
    return [
        comment("External packages (absolute references, NOT distributed with Python)"),
    ]


def import_header_internal():
    return [
        comment("Internal packages (absolute references, distributed with Python)"),
    ]


def import_header_library():
    return [
        comment("Library modules   (absolute references, NOT packaged, in project)"),
    ]


def import_header_project():
    return [
        comment("Project modules   (relative references, NOT packaged, in project)"),
    ]


def imports_empty():
    return [
        import_header_internal(),
        import_header_external(),
        import_header_library(),
        import_header_project(),
    ]


def imports_for_suite():
    return [
        import_header_internal(),
        import_header_external(),
        import_from("pytest", "fixture"),
        import_from("pytest", "mark"),
        import_from("pytest", "param"),
        import_from("pytest", "raises"),
        import_header_library(),
        import_from("utility", "my_assert", "is_"),
        import_from("utility", "my_assert_filesystem", "fs_is_"),
        import_from("utility", "my_assert_pathname", "pn_is_"),
        import_header_project(),
    ]


"""DisabledContent
"""


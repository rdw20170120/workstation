#!/usr/bin/env false
"""Generate all Markdown documents."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.document.markdown.complete import generate_document as document

# Project modules   (relative references, NOT packaged, in project)


def _generate_doc(dir_):
    sub = dir_
    document(sub, "HowTo-install-OpenJDK-15.md")
    document(sub, "HowTo-use_Venafi-to_create_TLS_certificate.md")
    document(sub, "HowTo-use_Venafi-to_download_TLS_certificate.md")
    document(sub, "testssl.md")


def generate(directory):
    _generate_doc(directory / "doc")


"""DisabledContent
"""

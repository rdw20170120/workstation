#!/usr/bin/env false
"""Generate all BriteOnyx BASH scripts."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.briteonyx.complete import (
    generate_executed as executed,
)
from src_gen.script.bash.briteonyx.complete import generate_sourced as sourced

# Project modules   (relative references, NOT packaged, in project)


def _generate_bin(dir_):
    sub = dir_
    executed(sub, "bitnami-unpack_component")
    executed(sub, "certs-touch")
    executed(sub, "k8s-cluster-dev")
    executed(sub, "k8s-cluster-lab")
    executed(sub, "k8s-cluster-show")
    executed(sub, "k8s-secret-delete")
    executed(sub, "k8s-secret-describe")
    executed(sub, "k8s-secret-get-yaml")
    executed(sub, "k8s-secrets-list")
    executed(sub, "tls-analyze-java-log")
    executed(sub, "tls-test-via-java-class")
    executed(sub, "tls-test-via-kafka_topics")
    executed(sub, "tls-test-via-openssl")
    executed(sub, "testssl")
    _generate_bin_lib(sub / "lib")
    _generate_bin_test(sub / "test")


def _generate_bin_lib(dir_):
    sub = dir_
    sourced(sub, "declare-keytool.bash")
    sourced(sub, "declare-openssl-pkcs12.bash")
    sourced(sub, "declare-openssl-pkey.bash")
    sourced(sub, "declare-openssl-rsa.bash")
    sourced(sub, "declare-openssl-x509.bash")
    sourced(sub, "declare-openssl.bash")
    sourced(sub, "declare-security.bash")
    sourced(sub, "declare-venafi.bash")
    sourced(sub, "declare.bash")


def _generate_bin_test(dir_):
    sub = dir_
    executed(sub, "certs-process")
    executed(sub, "run-all")
    executed(sub, "bitnami-unpack_components")
    _generate_bin_test_dev(sub / "dev")
    _generate_bin_test_lab(sub / "lab")


def _generate_bin_test_dev(dir_):
    sub = dir_
    executed(sub, "certs-disassemble")
    executed(sub, "certs-generate")
    executed(sub, "certs-generate-keystore")
    executed(sub, "certs-generate-root")
    executed(sub, "certs-generate-truststore")
    executed(sub, "run-01")
    executed(sub, "run-02")
    executed(sub, "run-03")
    executed(sub, "run-04")
    executed(sub, "run-all")
    executed(sub, "secrets-fetch-some")
    executed(sub, "stores-create-Kafka_broker")


def _generate_bin_test_lab(dir_):
    sub = dir_
    executed(sub, "certs-disassemble")
    executed(sub, "run-01")
    executed(sub, "run-02")
    executed(sub, "run-03")
    executed(sub, "run-04")
    executed(sub, "run-all")
    executed(sub, "secrets-fetch-some")
    executed(sub, "secrets-push-fake")


def generate(directory):
    _generate_bin(directory / "bin")


"""DisabledContent
"""

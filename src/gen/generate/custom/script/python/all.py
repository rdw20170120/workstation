#!/usr/bin/env false
"""Generate all Python scripts."""
# TODO: Add method for test module
# TODO: Add method for module to generate one source file
# TODO: Add method for module to generate many source files
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.python.complete import generate_library as library
from src_gen.script.python.complete import generate_package as package
from src_gen.script.python.complete import generate_test as test
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)


def _generate_bin(dir_):
    sub = dir_


def _generate_src(dir_):
    sub = dir_
    _generate_src_app(sub / "app" / Config().application_name)
    _generate_src_gen(sub / "gen" / "generate")


def _generate_src_app(dir_):
    sub = dir_
    _generate_src_app_tls(sub / "tls")
    _generate_src_app_utility(sub / "utility")


def _generate_src_app_tls(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "development.py")
    library(sub, "laboratory.py")
    library(sub, "pkcs12_bundle.py")
    test(sub, "test_pkcs12_bundle.py")
    test(sub, "test_tool.py")


def _generate_src_app_utility(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "crypto.py")
    library(sub, "my_cryptography.py")
    library(sub, "my_keytool.py")
    library(sub, "my_kubectl.py")
    library(sub, "my_openssl.py")
    library(sub, "my_pem.py")
    test(sub, "test_commandlib.py")


def _generate_src_gen(dir_):
    sub = dir_ / "custom" / "document" / "markdown"
    library(sub, "tasks.py")


def _generate_waiting(dir_):
    sub = dir_ / "src" / "app" / "secrets"
    _generate_waiting_task(sub / "task")
    _generate_waiting_tls(sub / "tls")
    _generate_waiting_utility(sub / "utility")


def _generate_waiting_task(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "bootstrap.py")
    library(sub, "check_password.py")
    library(sub, "check_rsa_private_key_pem.py")
    library(sub, "check_rsa_public_key_pem.py")
    library(sub, "create_java_keystore.py")
    library(sub, "create_kubernetes_secret_for_java_keystores.py")
    library(sub, "delete_kubernetes_secret.py")
    library(sub, "describe_jks.py")
    library(sub, "describe_kubernetes_secret.py")
    library(sub, "describe_pfx.py")
    library(sub, "describe_pkcs12.py")
    library(sub, "describe_x509_pem.py")
    library(sub, "disassemble_jks.py")
    library(sub, "disassemble_pfx.py")
    library(sub, "disassemble_pkcs12.py")
    library(sub, "disassemble_venafi_pem.py")
    library(sub, "disassemble_venafi_pfx.py")
    library(sub, "get_kubernetes_secret.py")
    library(sub, "list_kubernetes_secrets.py")
    library(sub, "manage_secrets_for_machine.py")
    library(sub, "mapping.py")
    library(sub, "scan_configuration_directory.py")
    library(sub, "scan_secret_directory.py")
    library(sub, "task.py")
    test(sub, "test_mapping.py")
    test(sub, "test_task.py")


def _generate_waiting_tls(dir_):
    sub = dir_
    test(sub, "abstract_test_bundle.py")
    test(sub, "abstract_test_deploy_bundle.py")
    test(sub, "abstract_test_pkcs12_deploy_bundle.py")
    test(sub, "abstract_test_pkcs12_deploy_keystore.py")
    test(sub, "abstract_test_pkcs12_deploy_truststore.py")
    test(sub, "abstract_test_pkcs12_venafi_bundle.py")
    test(sub, "abstract_test_venafi_bundle.py")
    test(sub, "abstract_test_x509_pem_venafi_bundle.py")
    test(sub, "conftest.py")
    test(sub, "test_dev_kafka_broker_current_pkcs12_keystore.py")
    test(sub, "test_dev_kafka_broker_current_pkcs12_truststore.py")
    test(sub, "test_dev_kafka_broker_thru_20210430_pkcs12_venafi_bundle.py")
    test(sub, "test_dev_kafka_broker_thru_20210430_x509_pem_venafi_bundle.py")
    test(sub, "test_laptop_rwill253_thru_20210601_x509_pem_venafi_bundle.py")


def _generate_waiting_utility(dir_):
    sub = dir_
    library(sub, "java_keystore.py")
    library(sub, "kubernetes_secret.py")
    test(sub, "test_java_keystore.py")
    test(sub, "test_kubernetes_secret.py")


def generate(directory):
    _generate_bin(directory / "bin")
    _generate_src(directory / "src")
    _generate_waiting(directory / "waiting")


"""DisabledContent
"""

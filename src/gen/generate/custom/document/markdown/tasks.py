#!/usr/bin/env false
"""Generate tasks document."""
# Internal packages (absolute references, distributed with Python)
from enum import Enum

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.document.markdown.source import generate as gen
from src_gen.document.markdown.structure import *
from throw_out_your_templates.section_3 import VisitorMap
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


no_acls, with_acls = False, True
unverified, verified = False, True

Env = Enum(
    "Environment",
    {
        "n": "None",
        "w": "laptop",
        "d": "development",
        "s": "stage",
        "p": "production",
        "c": "CDO",
    },
)

lcl, dev, stg, prd, cdo = Env.w, Env.d, Env.s, Env.p, Env.c

cdo_to_prd = cdo, prd
dev_to_dev = dev, dev
lcl_to_dev = lcl, dev
lcl_to_lcl = lcl, lcl
lcl_to_none = lcl, None
prd_to_prd = prd, prd
stg_to_stg = stg, stg

Source = Enum(
    "CertificateSource", {"n": "None", "sg": "self-generated", "v": "Venafi"}
)

self, venafi = Source.sg, Source.v
unverified_venafi = venafi, unverified
verified_self = self, verified
verified_venafi = venafi, verified


def _application_environment(application, environment):
    assert is_.instance(application, str)
    if environment is None:
        return "None"
    assert is_.instance(environment, Env)
    return [environment, " ", application]


def _x509_description(certificate_source, verification):
    if verification is None:
        return "None"
    assert is_.instance(certificate_source, Source)
    assert is_.instance(verification, bool)
    if verification:
        verification = "host-verified"
    else:
        verification = "not host-verified"
    return [certificate_source, " ", verification]


def _phase_header():
    return [
        table_header(
            "Phase",
            "Client",
            "Server",
            "Client Certificate",
            "Server Certificate",
            "Using ACLs",
            "Incremental Goal",
        ),
    ]


def _phase_row(
    phase, using_kafka_acls, application, increment, connection, client, server
):
    if phase is None:
        phase = "TBD"
    assert is_.instance(increment, list)
    assert is_.instance(phase, str)
    assert is_.instance(using_kafka_acls, bool)
    client_certificate_source, client_verification = client
    client_environment, server_environment = connection
    if server is None:
        server_certificate_source, server_verification = None, None
    else:
        server_certificate_source, server_verification = server
    using_kafka_acls = "with ACLs" if using_kafka_acls else "no ACLs"
    return [
        table_row(
            phase,
            _application_environment(application, client_environment),
            _application_environment(application, server_environment),
            _x509_description(client_certificate_source, client_verification),
            _x509_description(server_certificate_source, server_verification),
            using_kafka_acls,
            increment,
        ),
    ]


def _phase_row_set(using_kafka_acls, highlight, client, server):
    handshake = "Verify TLS handshake"
    return [
        _phase_row(
            None,
            using_kafka_acls,
            "OpenSSL",
            ["Verify standalone ", highlight],
            connection=lcl_to_none,
            client=client,
            server=None,
        ),
        _phase_row(
            None,
            using_kafka_acls,
            "OpenSSL",
            [handshake, " using local OpenSSL ", highlight],
            connection=lcl_to_lcl,
            client=client,
            server=server,
        ),
        _phase_row(
            None,
            using_kafka_acls,
            "Kafka",
            [handshake, " using local Kafka ", highlight],
            connection=lcl_to_lcl,
            client=client,
            server=server,
        ),
        _phase_row(
            None,
            using_kafka_acls,
            "Kafka",
            [handshake, " using dev Kafka server ", highlight],
            connection=lcl_to_dev,
            client=client,
            server=server,
        ),
        _phase_row(
            None,
            using_kafka_acls,
            "Kafka",
            [handshake, " fully in dev ", highlight],
            connection=dev_to_dev,
            client=client,
            server=server,
        ),
        _phase_row(
            None,
            using_kafka_acls,
            "Kafka",
            [handshake, " fully in staging ", highlight],
            connection=stg_to_stg,
            client=client,
            server=server,
        ),
        _phase_row(
            None,
            using_kafka_acls,
            "Kafka",
            [handshake, " fully in production ", highlight],
            connection=prd_to_prd,
            client=client,
            server=server,
        ),
    ]


def _phase_ruler():
    return [
        table_ruler(
            "---",
            "---",
            "---",
            "---",
            "---",
            "---",
            "---",
        ),
    ]


def _phase_table():
    return [
        line(),
        s("Here is the plan laid out as a table."),
        line(),
        _phase_header(),
        _phase_ruler(),
        _phase_row_set(
            no_acls,
            "without host verification",
            client=unverified_venafi,
            server=unverified_venafi,
        ),
        _phase_row_set(
            with_acls,
            "with ACLs",
            client=unverified_venafi,
            server=unverified_venafi,
        ),
        _phase_row_set(
            no_acls,
            "with host verification",
            client=verified_venafi,
            server=verified_venafi,
        ),
        _phase_row_set(
            no_acls,
            "with self-generated client certificates",
            client=verified_self,
            server=verified_venafi,
        ),
        _phase_row(
            None,
            with_acls,
            "Kafka",
            ["Verify TLS handshake using CDO Kafka client"],
            connection=cdo_to_prd,
            client=verified_self,
            server=verified_venafi,
        ),
    ]


def build():
    return [
        h1("Tasks for securing Apache Kafka"),
        s(
            "As described in the README.md, security requires proper planning and implementation."
        ),
        s("Here is that security plan for our Apache Kafka clusters."),
        s(
            "Once proven, this plan will be extended to the rest of our OCDP implementation."
        ),
        s(
            "These are the phases (or milestones) for incrementally securing Kafka."
        ),
        s("The effort is incremental for two reasons."),
        line(),
        s(
            "First, security is difficult to get right because good security only works when everything is perfect."
        ),
        s("Therefore, we must make one change at a time and test well."),
        s("Second, we are building an automated solution."),
        s(
            "For each phase (milestone), we must build several new pieces of functionality or extend them to cover new scope."
        ),
        _phase_table(),
        line(),
        s(
            "John believes that we can implement Kafka Access Control Lists (ACLs) without host-verified TLS certificates from the clients."
        ),
        s("So we have reordered these phases to reflect such an approach."),
        s("We may reorder them further to test ACLs sooner."),
        s("."),
        line(),
        h2("Detailed subtasks"),
        line("TODO"),
        line(),
        note("This document was automatically generated."),
        s("Do NOT edit manually."),
        s(
            [
                "Edit the source in ",
                bt("src/gen/generate/document/markdown/tasks.py"),
                ".",
            ]
        ),
        line(),
    ]


def generate(directory):
    gen(build(), directory, "tasks.md")


"""DisabledContent
1. Consider whether using BASH, OpenSSL, Keystore Explorer, and the Java security tools are enough.
1. Convert each of the code snippets above into a reusable function, right-sized for this process.
1. Test certificates on my workstation.
   1. Document in detail how to create a TLS certificate using Venafi for my workstation.
   1. Create TLS certificate for my workstation using Venafi.
   1. Document in detail how to download a TLS certificate with trustchain from Venafi.
   1. Download certificate with trustchain for my workstation.
   1. Use OpenSSL to break out the pieces of the TLS certificate and trustchain for my workstation.
   1. Test 1a = Use OpenSSL to verify the certificate chain.
1. Test stores on my workstation.
   1. Use workstation certificate to create client stores (keystore & truststore).
   1. Use workstation certificate to create server stores (keystore & truststore).
   1. Test 1b = Use OpenSSL to verify client stores against server.
   1. Test 1c = Use OpenSSL to verify server stores against client.
1. Test TLS handshake on my workstation.
   1. Test 2 = Use OpenSSL to test client & server TLS handshake on workstation.
1. Test Kafka TLS handshake on my workstation.
   1. Test 3a = Deploy a Kafka server and client locally to test, without certificates.
   1. Push stores into Kubernetes for my workstation.
   1. Test 3b = Deploy a Kafka server and client locally to test, with certificates.
1. Test Kafka TLS handshake from my workstation to our dev servers.
   1. Test 4a = Deploy a Kafka client locally to connect to our dev Kafka servers, without certificates.
   1. Document in detail how to create TLS certificate(s) using Venafi for our Kafka dev servers.
   1. Create TLS certificate(s) for our Kafka dev servers using Venafi.
   1. Download TLS certificate(s) with trustchain for our Kafka dev servers.
   1. Use OpenSSL to break out the pieces of TLS certificate(s) and trustchain for our Kafka dev servers.
   1. Update stores for my workstation to include Kafka dev servers.
   1. Push stores into Kubernetes for my workstation.
   1. Create stores for our Kafka dev servers.
   1. Push stores into Kubernetes for our Kafka dev servers.
   1. Test 4b = Deploy a Kafka client locally to connect to our dev Kafka servers, with certificates.
1. Document in detail how to create a Kafka dev client TLS certificate using Venafi.
1. Create a TLS certificate for a Kafka dev client using Venafi.
1. Download certificate with trustchain for a Kafka dev client.
1. Use OpenSSL to break out the pieces of the TLS certificate and trustchain.

...

1. Test 5 = Deploy a Kafka client in dev that connects to the Kafka servers in dev.
1. Test 6 = Deploy a Kafka client & server in stage.
1. Mix in Hashicorp Vault to store the TLS certificates.
1. Have each team member create a TLS certificate for their workstation, mix it in, and test.
1. Test 7 = Deploy a Kafka client & server in production.
1. Test 8 = Deploy a real Kafka client at a CDO to connect to production Kafka server.

"""

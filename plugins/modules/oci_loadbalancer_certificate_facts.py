#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_loadbalancer_certificate_facts
short_description: Fetches details about one or multiple Certificate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Certificate resources in Oracle Cloud Infrastructure
    - Lists all SSL certificates bundles associated with a given load balancer.
version_added: "2.5"
options:
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer associated with the certificate bundles
              to be listed.
        type: str
        required: true
    name:
        description:
            - The name of the certificate whose details needs to be fetched.
            - Required to get a specific certificate.
        type: str
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List certificates
  oci_loadbalancer_certificate_facts:
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
certificates:
    description:
        - List of Certificate resources
    returned: on success
    type: complex
    contains:
        certificate_name:
            description:
                - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                  Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                  Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                - "Example: `example_certificate_bundle`"
            returned: on success
            type: string
            sample: example_certificate_bundle
        public_certificate:
            description:
                - The public certificate, in PEM format, that you received from your SSL certificate provider.
                - "Example:"
                -     -----BEGIN CERTIFICATE-----
                      MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG
                      A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE
                      MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl
                      YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw
                      ...
                      -----END CERTIFICATE-----
            returned: on success
            type: string
            sample: public_certificate_example
        ca_certificate:
            description:
                - The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.
                - "Example:"
                -     -----BEGIN CERTIFICATE-----
                      MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix
                      EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD
                      VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y
                      aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy
                      ...
                      -----END CERTIFICATE-----
            returned: on success
            type: string
            sample: ca_certificate_example
    sample: [{
        "certificate_name": "example_certificate_bundle",
        "public_certificate": "public_certificate_example",
        "ca_certificate": "ca_certificate_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "load_balancer_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_certificates,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            **optional_kwargs
        )


CertificateFactsHelperCustom = get_custom_class("CertificateFactsHelperCustom")


class ResourceFactsHelper(CertificateFactsHelperCustom, CertificateFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(load_balancer_id=dict(type="str", required=True), name=dict(type="str"),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="certificate",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(certificates=result)


if __name__ == "__main__":
    main()

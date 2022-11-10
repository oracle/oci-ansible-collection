#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_loadbalancer_ssl_cipher_suite_facts
short_description: Fetches details about one or multiple SslCipherSuite resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SslCipherSuite resources in Oracle Cloud Infrastructure
    - Lists all SSL cipher suites associated with the specified load balancer.
    - If I(name) is specified, the details of a single SslCipherSuite will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - The name of the SSL cipher suite to retrieve.
            - "example: `example_cipher_suite`"
            - Required to get a specific ssl_cipher_suite.
        type: str
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated load balancer.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific ssl_cipher_suite
  oci_loadbalancer_ssl_cipher_suite_facts:
    # required
    name: name_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: List ssl_cipher_suites
  oci_loadbalancer_ssl_cipher_suite_facts:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
ssl_cipher_suites:
    description:
        - List of SslCipherSuite resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - A friendly name for the SSL cipher suite. It must be unique and it cannot be changed.
                - "**Note:** The name of your user-defined cipher suite must not be the same as any of Oracle's predefined or
                            reserved SSL cipher suite names:"
                - "* oci-default-ssl-cipher-suite-v1
                  * oci-modern-ssl-cipher-suite-v1
                  * oci-compatible-ssl-cipher-suite-v1
                  * oci-wider-compatible-ssl-cipher-suite-v1
                  * oci-customized-ssl-cipher-suite"
                - "example: `example_cipher_suite`"
            returned: on success
            type: str
            sample: name_example
        ciphers:
            description:
                - A list of SSL ciphers the load balancer must support for HTTPS or SSL connections.
                - "The following ciphers are valid values for this property:"
                - "*  __TLSv1.2 ciphers__"
                - "       \\"AES128-GCM-SHA256\\"
                          \\"AES128-SHA256\\"
                          \\"AES256-GCM-SHA384\\"
                          \\"AES256-SHA256\\"
                          \\"DH-DSS-AES128-GCM-SHA256\\"
                          \\"DH-DSS-AES128-SHA256\\"
                          \\"DH-DSS-AES256-GCM-SHA384\\"
                          \\"DH-DSS-AES256-SHA256\\"
                          \\"DH-RSA-AES128-GCM-SHA256\\"
                          \\"DH-RSA-AES128-SHA256\\"
                          \\"DH-RSA-AES256-GCM-SHA384\\"
                          \\"DH-RSA-AES256-SHA256\\"
                          \\"DHE-DSS-AES128-GCM-SHA256\\"
                          \\"DHE-DSS-AES128-SHA256\\"
                          \\"DHE-DSS-AES256-GCM-SHA384\\"
                          \\"DHE-DSS-AES256-SHA256\\"
                          \\"DHE-RSA-AES128-GCM-SHA256\\"
                          \\"DHE-RSA-AES128-SHA256\\"
                          \\"DHE-RSA-AES256-GCM-SHA384\\"
                          \\"DHE-RSA-AES256-SHA256\\"
                          \\"ECDH-ECDSA-AES128-GCM-SHA256\\"
                          \\"ECDH-ECDSA-AES128-SHA256\\"
                          \\"ECDH-ECDSA-AES256-GCM-SHA384\\"
                          \\"ECDH-ECDSA-AES256-SHA384\\"
                          \\"ECDH-RSA-AES128-GCM-SHA256\\"
                          \\"ECDH-RSA-AES128-SHA256\\"
                          \\"ECDH-RSA-AES256-GCM-SHA384\\"
                          \\"ECDH-RSA-AES256-SHA384\\"
                          \\"ECDHE-ECDSA-AES128-GCM-SHA256\\"
                          \\"ECDHE-ECDSA-AES128-SHA256\\"
                          \\"ECDHE-ECDSA-AES256-GCM-SHA384\\"
                          \\"ECDHE-ECDSA-AES256-SHA384\\"
                          \\"ECDHE-RSA-AES128-GCM-SHA256\\"
                          \\"ECDHE-RSA-AES128-SHA256\\"
                          \\"ECDHE-RSA-AES256-GCM-SHA384\\"
                          \\"ECDHE-RSA-AES256-SHA384\\""
                - "*  __TLSv1 ciphers also supported by TLSv1.2__"
                - "       \\"AES128-SHA\\"
                          \\"AES256-SHA\\"
                          \\"CAMELLIA128-SHA\\"
                          \\"CAMELLIA256-SHA\\"
                          \\"DES-CBC3-SHA\\"
                          \\"DH-DSS-AES128-SHA\\"
                          \\"DH-DSS-AES256-SHA\\"
                          \\"DH-DSS-CAMELLIA128-SHA\\"
                          \\"DH-DSS-CAMELLIA256-SHA\\"
                          \\"DH-DSS-DES-CBC3-SHAv\\"
                          \\"DH-DSS-SEED-SHA\\"
                          \\"DH-RSA-AES128-SHA\\"
                          \\"DH-RSA-AES256-SHA\\"
                          \\"DH-RSA-CAMELLIA128-SHA\\"
                          \\"DH-RSA-CAMELLIA256-SHA\\"
                          \\"DH-RSA-DES-CBC3-SHA\\"
                          \\"DH-RSA-SEED-SHA\\"
                          \\"DHE-DSS-AES128-SHA\\"
                          \\"DHE-DSS-AES256-SHA\\"
                          \\"DHE-DSS-CAMELLIA128-SHA\\"
                          \\"DHE-DSS-CAMELLIA256-SHA\\"
                          \\"DHE-DSS-DES-CBC3-SHA\\"
                          \\"DHE-DSS-SEED-SHA\\"
                          \\"DHE-RSA-AES128-SHA\\"
                          \\"DHE-RSA-AES256-SHA\\"
                          \\"DHE-RSA-CAMELLIA128-SHA\\"
                          \\"DHE-RSA-CAMELLIA256-SHA\\"
                          \\"DHE-RSA-DES-CBC3-SHA\\"
                          \\"DHE-RSA-SEED-SHA\\"
                          \\"ECDH-ECDSA-AES128-SHA\\"
                          \\"ECDH-ECDSA-AES256-SHA\\"
                          \\"ECDH-ECDSA-DES-CBC3-SHA\\"
                          \\"ECDH-ECDSA-RC4-SHA\\"
                          \\"ECDH-RSA-AES128-SHA\\"
                          \\"ECDH-RSA-AES256-SHA\\"
                          \\"ECDH-RSA-DES-CBC3-SHA\\"
                          \\"ECDH-RSA-RC4-SHA\\"
                          \\"ECDHE-ECDSA-AES128-SHA\\"
                          \\"ECDHE-ECDSA-AES256-SHA\\"
                          \\"ECDHE-ECDSA-DES-CBC3-SHA\\"
                          \\"ECDHE-ECDSA-RC4-SHA\\"
                          \\"ECDHE-RSA-AES128-SHA\\"
                          \\"ECDHE-RSA-AES256-SHA\\"
                          \\"ECDHE-RSA-DES-CBC3-SHA\\"
                          \\"ECDHE-RSA-RC4-SHA\\"
                          \\"IDEA-CBC-SHA\\"
                          \\"KRB5-DES-CBC3-MD5\\"
                          \\"KRB5-DES-CBC3-SHA\\"
                          \\"KRB5-IDEA-CBC-MD5\\"
                          \\"KRB5-IDEA-CBC-SHA\\"
                          \\"KRB5-RC4-MD5\\"
                          \\"KRB5-RC4-SHA\\"
                          \\"PSK-3DES-EDE-CBC-SHA\\"
                          \\"PSK-AES128-CBC-SHA\\"
                          \\"PSK-AES256-CBC-SHA\\"
                          \\"PSK-RC4-SHA\\"
                          \\"RC4-MD5\\"
                          \\"RC4-SHA\\"
                          \\"SEED-SHA\\""
                - "example: `[\\"ECDHE-RSA-AES256-GCM-SHA384\\",\\"ECDHE-ECDSA-AES256-GCM-SHA384\\",\\"ECDHE-RSA-AES128-GCM-SHA256\\"]`"
            returned: on success
            type: list
            sample: []
    sample: [{
        "name": "name_example",
        "ciphers": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SslCipherSuiteFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "name",
        ]

    def get_required_params_for_list(self):
        return [
            "load_balancer_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ssl_cipher_suite,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            name=self.module.params.get("name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_ssl_cipher_suites,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            **optional_kwargs
        )


SslCipherSuiteFactsHelperCustom = get_custom_class("SslCipherSuiteFactsHelperCustom")


class ResourceFactsHelper(
    SslCipherSuiteFactsHelperCustom, SslCipherSuiteFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(name=dict(type="str"), load_balancer_id=dict(type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ssl_cipher_suite",
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

    module.exit_json(ssl_cipher_suites=result)


if __name__ == "__main__":
    main()

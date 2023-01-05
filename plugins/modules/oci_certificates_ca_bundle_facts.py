#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_certificates_ca_bundle_facts
short_description: Fetches details about a CaBundle resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a CaBundle resource in Oracle Cloud Infrastructure
    - Gets a ca-bundle bundle.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ca_bundle_id:
        description:
            - The OCID of the CA bundle.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific ca_bundle
  oci_certificates_ca_bundle_facts:
    # required
    ca_bundle_id: "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
ca_bundle:
    description:
        - CaBundle resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the CA bundle.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A user-friendly name for the CA bundle. Names are unique within a compartment. Valid characters include uppercase or lowercase letters,
                  numbers, hyphens, underscores, and periods.
            returned: on success
            type: str
            sample: name_example
        ca_bundle_pem:
            description:
                - Certificates (in PEM format) in the CA bundle. Can be of arbitrary length.
            returned: on success
            type: str
            sample: ca_bundle_pem_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "ca_bundle_pem": "ca_bundle_pem_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.certificates import CertificatesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CaBundleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "ca_bundle_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ca_bundle,
            ca_bundle_id=self.module.params.get("ca_bundle_id"),
        )


CaBundleFactsHelperCustom = get_custom_class("CaBundleFactsHelperCustom")


class ResourceFactsHelper(CaBundleFactsHelperCustom, CaBundleFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            ca_bundle_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ca_bundle",
        service_client_class=CertificatesClient,
        namespace="certificates",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(ca_bundle=result)


if __name__ == "__main__":
    main()

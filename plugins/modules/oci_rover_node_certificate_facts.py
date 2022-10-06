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
module: oci_rover_node_certificate_facts
short_description: Fetches details about a RoverNodeCertificate resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a RoverNodeCertificate resource in Oracle Cloud Infrastructure
    - Get the certificate for a rover node
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    rover_node_id:
        description:
            - Unique RoverNode identifier
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific rover_node_certificate
  oci_rover_node_certificate_facts:
    # required
    rover_node_id: "ocid1.rovernode.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
rover_node_certificate:
    description:
        - RoverNodeCertificate resource
    returned: on success
    type: complex
    contains:
        certificate:
            description:
                - The certificate that can be installed on a client to do TLS communication to the node
            returned: on success
            type: str
            sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    sample: {
        "certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.rover import RoverNodeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoverNodeCertificateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "rover_node_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_node_certificate,
            rover_node_id=self.module.params.get("rover_node_id"),
        )


RoverNodeCertificateFactsHelperCustom = get_custom_class(
    "RoverNodeCertificateFactsHelperCustom"
)


class ResourceFactsHelper(
    RoverNodeCertificateFactsHelperCustom, RoverNodeCertificateFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(rover_node_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="rover_node_certificate",
        service_client_class=RoverNodeClient,
        namespace="rover",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(rover_node_certificate=result)


if __name__ == "__main__":
    main()

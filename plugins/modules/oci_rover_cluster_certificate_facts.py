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
module: oci_rover_cluster_certificate_facts
short_description: Fetches details about a RoverClusterCertificate resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a RoverClusterCertificate resource in Oracle Cloud Infrastructure
    - Get the certificate for a rover cluster
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    rover_cluster_id:
        description:
            - Unique RoverCluster identifier
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific rover_cluster_certificate
  oci_rover_cluster_certificate_facts:
    # required
    rover_cluster_id: "ocid1.rovercluster.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
rover_cluster_certificate:
    description:
        - RoverClusterCertificate resource
    returned: on success
    type: complex
    contains:
        certificate:
            description:
                - The certificate that can be installed on a client to do TLS communication to the cluster
            returned: on success
            type: str
            sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    sample: {
        "certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.rover import RoverClusterClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoverClusterCertificateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "rover_cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_cluster_certificate,
            rover_cluster_id=self.module.params.get("rover_cluster_id"),
        )


RoverClusterCertificateFactsHelperCustom = get_custom_class(
    "RoverClusterCertificateFactsHelperCustom"
)


class ResourceFactsHelper(
    RoverClusterCertificateFactsHelperCustom, RoverClusterCertificateFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(rover_cluster_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="rover_cluster_certificate",
        service_client_class=RoverClusterClient,
        namespace="rover",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(rover_cluster_certificate=result)


if __name__ == "__main__":
    main()

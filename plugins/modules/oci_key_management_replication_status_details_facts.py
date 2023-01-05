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
module: oci_key_management_replication_status_details_facts
short_description: Fetches details about a ReplicationStatusDetails resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ReplicationStatusDetails resource in Oracle Cloud Infrastructure
    - When a vault has a replica, each operation on the vault or its resources, such as
      keys, is replicated and has an associated replicationId. Replication status provides
      details about whether the operation associated with the given replicationId has been
      successfully applied across replicas.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    replication_id:
        description:
            - replicationId associated with an operation on a resource
        type: str
        aliases: ["id"]
        required: true
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific replication_status_details
  oci_key_management_replication_status_details_facts:
    # required
    replication_id: "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

"""

RETURN = """
replication_status_details:
    description:
        - ReplicationStatusDetails resource
    returned: on success
    type: complex
    contains:
        replica_details:
            description:
                - The value to assign to the replica_details property of this Vault.
            returned: on success
            type: complex
            contains:
                region:
                    description:
                        - The replica region
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                status:
                    description:
                        - Replication status associated with a replicationId
                    returned: on success
                    type: str
                    sample: REPLICATING
    sample: {
        "replica_details": [{
            "region": "us-phoenix-1",
            "status": "REPLICATING"
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.key_management import KmsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReplicationStatusDetailsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "replication_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication_status,
            replication_id=self.module.params.get("replication_id"),
        )


ReplicationStatusDetailsFactsHelperCustom = get_custom_class(
    "ReplicationStatusDetailsFactsHelperCustom"
)


class ResourceFactsHelper(
    ReplicationStatusDetailsFactsHelperCustom, ReplicationStatusDetailsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            replication_id=dict(aliases=["id"], type="str", required=True),
            service_endpoint=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="replication_status_details",
        service_client_class=KmsManagementClient,
        namespace="key_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(replication_status_details=result)


if __name__ == "__main__":
    main()

#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_key_management_vault_replica_facts
short_description: Fetches details about one or multiple VaultReplica resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VaultReplica resources in Oracle Cloud Infrastructure
    - Lists the replicas for a vault
    - As a provisioning operation, this call is subject to a Key Management limit that applies to
      the total number of requests across all provisioning write operations. Key Management might
      throttle this call to reject an otherwise valid request when the total rate of provisioning
      write operations exceeds 10 requests per second for a given tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vault_id:
        description:
            - The OCID of the vault.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order. The default
              order for `TIMECREATED` is descending. The default order for `DISPLAYNAME`
              is ascending.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List vault_replicas
  oci_key_management_vault_replica_facts:
    # required
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
vault_replicas:
    description:
        - List of VaultReplica resources
    returned: on success
    type: complex
    contains:
        crypto_endpoint:
            description:
                - The vault replica's crypto endpoint
            returned: on success
            type: str
            sample: crypto_endpoint_example
        management_endpoint:
            description:
                - The vault replica's management endpoint
            returned: on success
            type: str
            sample: management_endpoint_example
        region:
            description:
                - Region to which vault is replicated to
            returned: on success
            type: str
            sample: us-phoenix-1
        status:
            description:
                - "The value to assign to the status property of this VaultReplicaSummary. Allowed values for this property are: 'CREATING', 'CREATED',
                  'DELETING', 'DELETED', 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'."
            returned: on success
            type: str
            sample: CREATING
    sample: [{
        "crypto_endpoint": "crypto_endpoint_example",
        "management_endpoint": "management_endpoint_example",
        "region": "us-phoenix-1",
        "status": "CREATING"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.key_management import KmsVaultClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VaultReplicaFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "vault_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_vault_replicas,
            vault_id=self.module.params.get("vault_id"),
            **optional_kwargs
        )


VaultReplicaFactsHelperCustom = get_custom_class("VaultReplicaFactsHelperCustom")


class ResourceFactsHelper(VaultReplicaFactsHelperCustom, VaultReplicaFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            vault_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vault_replica",
        service_client_class=KmsVaultClient,
        namespace="key_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(vault_replicas=result)


if __name__ == "__main__":
    main()

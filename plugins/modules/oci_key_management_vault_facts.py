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
module: oci_key_management_vault_facts
short_description: Fetches details about one or multiple Vault resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Vault resources in Oracle Cloud Infrastructure
    - Lists the vaults in the specified compartment.
    - As a provisioning operation, this call is subject to a Key Management limit that applies to
      the total number of requests across all provisioning read operations. Key Management might
      throttle this call to reject an otherwise valid request when the total rate of provisioning
      read operations exceeds 10 requests per second for a given tenancy.
    - If I(vault_id) is specified, the details of a single Vault will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vault_id:
        description:
            - The OCID of the vault.
            - Required to get a specific vault.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple vaults.
        type: str
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific vault
  oci_key_management_vault_facts:
    # required
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"

- name: List vaults
  oci_key_management_vault_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
vaults:
    description:
        - List of Vault resources
    returned: on success
    type: complex
    contains:
        time_of_deletion:
            description:
                - "An optional property to indicate when to delete the vault, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        wrappingkey_id:
            description:
                - The OCID of the vault's wrapping key.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.wrappingkey.oc1..xxxxxxEXAMPLExxxxxx"
        replica_details:
            description:
                - The value to assign to the replica_details property of this Vault.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                replication_id:
                    description:
                        - ReplicationId associated with a vault operation
                    returned: on success
                    type: str
                    sample: "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        is_primary:
            description:
                - The value to assign to the is_primary property of this Vault.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        compartment_id:
            description:
                - The OCID of the compartment that contains this vault.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        crypto_endpoint:
            description:
                - The service endpoint to perform cryptographic operations against. Cryptographic operations include
                  L(Encrypt,https://docs.cloud.oracle.com/api/#/en/key/latest/EncryptedData/Encrypt),
                  L(Decrypt,https://docs.cloud.oracle.com/api/#/en/key/latest/DecryptedData/Decrypt),
                  and L(GenerateDataEncryptionKey,https://docs.cloud.oracle.com/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey) operations.
            returned: on success
            type: str
            sample: crypto_endpoint_example
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name for the vault. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the vault.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The vault's current lifecycle state.
                - "Example: `DELETED`"
            returned: on success
            type: str
            sample: CREATING
        management_endpoint:
            description:
                - "The service endpoint to perform management operations against. Management operations include \\"Create,\\" \\"Update,\\" \\"List,\\"
                  \\"Get,\\" and \\"Delete\\" operations."
            returned: on success
            type: str
            sample: management_endpoint_example
        time_created:
            description:
                - The date and time this vault was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                - "Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vault_type:
            description:
                - The type of vault. Each type of vault stores the key with different
                  degrees of isolation and has different options and pricing.
            returned: on success
            type: str
            sample: VIRTUAL_PRIVATE
    sample: [{
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "wrappingkey_id": "ocid1.wrappingkey.oc1..xxxxxxEXAMPLExxxxxx",
        "replica_details": {
            "replication_id": "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_primary": true,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "crypto_endpoint": "crypto_endpoint_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "management_endpoint": "management_endpoint_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "vault_type": "VIRTUAL_PRIVATE"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.key_management import KmsVaultClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VaultFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "vault_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vault, vault_id=self.module.params.get("vault_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_vaults,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VaultFactsHelperCustom = get_custom_class("VaultFactsHelperCustom")


class ResourceFactsHelper(VaultFactsHelperCustom, VaultFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            vault_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vault",
        service_client_class=KmsVaultClient,
        namespace="key_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(vaults=result)


if __name__ == "__main__":
    main()

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
module: oci_key_management_vault
short_description: Manage a Vault resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a Vault resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new vault. The type of vault you create determines key placement, pricing, and
      available options. Options include storage isolation, a dedicated service endpoint instead
      of a shared service endpoint for API calls, and either a dedicated hardware security module
      (HSM) or a multitenant HSM.
    - As a provisioning operation, this call is subject to a Key Management limit that applies to
      the total number of requests across all provisioning write operations. Key Management might
      throttle this call to reject an otherwise valid request when the total rate of provisioning
      write operations exceeds 10 requests per second for a given tenancy.
    - "This resource has the following action operations in the M(oracle.oci.oci_key_management_vault_actions) module: cancel_vault_deletion,
      change_compartment, create_vault_replica, delete_vault_replica, schedule_vault_deletion."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment where you want to create this vault.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    vault_type:
        description:
            - The type of vault to create. Each type of vault stores the key with different degrees of isolation and has different options and pricing.
            - Required for create using I(state=present).
        type: str
        choices:
            - "VIRTUAL_PRIVATE"
            - "DEFAULT"
    vault_id:
        description:
            - The OCID of the vault.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name for the vault. It does not have to be unique, and it is changeable.
              Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    state:
        description:
            - The state of the Vault.
            - Use I(state=present) to create or update a Vault.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create vault
  oci_key_management_vault:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    vault_type: VIRTUAL_PRIVATE
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update vault
  oci_key_management_vault:
    # required
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update vault using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_key_management_vault:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

"""

RETURN = """
vault:
    description:
        - Details of the Vault resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        time_of_deletion:
            description:
                - "An optional property to indicate when to delete the vault, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
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
        wrappingkey_id:
            description:
                - The OCID of the vault's wrapping key.
            returned: on success
            type: str
            sample: "ocid1.wrappingkey.oc1..xxxxxxEXAMPLExxxxxx"
        replica_details:
            description:
                - The value to assign to the replica_details property of this Vault.
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
            returned: on success
            type: bool
            sample: true
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "crypto_endpoint": "crypto_endpoint_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "management_endpoint": "management_endpoint_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "vault_type": "VIRTUAL_PRIVATE",
        "wrappingkey_id": "ocid1.wrappingkey.oc1..xxxxxxEXAMPLExxxxxx",
        "replica_details": {
            "replication_id": "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_primary": true
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.key_management import KmsVaultClient
    from oci.key_management.models import CreateVaultDetails
    from oci.key_management.models import UpdateVaultDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VaultHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(VaultHelperGen, self).get_possible_entity_types() + [
            "vault",
            "vaults",
            "keyManagementvault",
            "keyManagementvaults",
            "vaultresource",
            "vaultsresource",
            "keymanagement",
        ]

    def get_module_resource_id_param(self):
        return "vault_id"

    def get_module_resource_id(self):
        return self.module.params.get("vault_id")

    def get_get_fn(self):
        return self.client.get_vault

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_vault, vault_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vault, vault_id=self.module.params.get("vault_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_vaults, **kwargs)

    def get_create_model_class(self):
        return CreateVaultDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_vault,
            call_fn_args=(),
            call_fn_kwargs=dict(create_vault_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateVaultDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_vault,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vault_id=self.module.params.get("vault_id"),
                update_vault_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


VaultHelperCustom = get_custom_class("VaultHelperCustom")


class ResourceHelper(VaultHelperCustom, VaultHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            vault_type=dict(type="str", choices=["VIRTUAL_PRIVATE", "DEFAULT"]),
            vault_id=dict(aliases=["id"], type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vault",
        service_client_class=KmsVaultClient,
        namespace="key_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

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
module: oci_key_management_key_version
short_description: Manage a KeyVersion resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a KeyVersion resource in Oracle Cloud Infrastructure
    - For I(state=present), generates a new L(KeyVersion,https://docs.cloud.oracle.com/api/#/en/key/release/KeyVersion/) resource that provides new
      cryptographic
      material for a master encryption key. The key must be in an `ENABLED` state to be rotated.
    - As a management operation, this call is subject to a Key Management limit that applies to the total number
      of requests across all  management write operations. Key Management might throttle this call to reject an
      otherwise valid request when the total rate of management write operations exceeds 10 requests per second
      for a given tenancy.
    - "This resource has the following action operations in the M(oci_key_version_actions) module: cancel_key_version_deletion, schedule_key_version_deletion."
version_added: "2.5"
options:
    key_id:
        description:
            - The OCID of the key.
        type: str
        required: true
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
    state:
        description:
            - The state of the KeyVersion.
            - Use I(state=present) to create a KeyVersion.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create key_version
  oci_key_management_key_version:
    key_id: ocid1.key.oc1..xxxxxxEXAMPLExxxxxx
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

"""

RETURN = """
key_version:
    description:
        - Details of the KeyVersion resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains this key version.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        id:
            description:
                - The OCID of the key version.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        key_id:
            description:
                - The OCID of the key associated with this key version.
            returned: on success
            type: string
            sample: ocid1.key.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The key version's current lifecycle state.
                - "Example: `ENABLED`"
            returned: on success
            type: string
            sample: ENABLED
        origin:
            description:
                - The source of the key material. When this value is `INTERNAL`, Key Management
                  created the key material. When this value is `EXTERNAL`, the key material
                  was imported from an external source.
            returned: on success
            type: string
            sample: INTERNAL
        time_created:
            description:
                - The date and time this key version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                - "Example: \\"2018-04-03T21:10:29.600Z\\""
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the key version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-04-03T21:10:29.600Z
        vault_id:
            description:
                - The OCID of the vault that contains this key version.
            returned: on success
            type: string
            sample: ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ENABLED",
        "origin": "INTERNAL",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_of_deletion": "2019-04-03T21:10:29.600Z",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.key_management import KmsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KeyVersionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get and list"""

    def get_get_fn(self):
        return self.client.get_key_version

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_key_version,
            key_id=self.module.params.get("key_id"),
            key_version_id=self.module.params.get("key_version_id"),
        )

    def list_resources(self):
        required_list_method_params = [
            "key_id",
        ]

        optional_list_method_params = []

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_key_versions, **kwargs
        )

    def create_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_key_version,
            call_fn_args=(),
            call_fn_kwargs=dict(key_id=self.module.params.get("key_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )


KeyVersionHelperCustom = get_custom_class("KeyVersionHelperCustom")


class ResourceHelper(KeyVersionHelperCustom, KeyVersionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            key_id=dict(type="str", required=True),
            service_endpoint=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="key_version",
        service_client_class=KmsManagementClient,
        namespace="key_management",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

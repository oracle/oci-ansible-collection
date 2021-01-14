#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_blockstorage_boot_volume_kms_key
short_description: Manage a BootVolumeKmsKey resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a BootVolumeKmsKey resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    boot_volume_id:
        description:
            - The OCID of the boot volume.
        type: str
        aliases: ["id"]
        required: true
    kms_key_id:
        description:
            - The OCID of the new Key Management key to assign to protect the specified volume.
              This key has to be a valid Key Management key, and policies must exist to allow the user and the Block Volume service to access this key.
              If you specify the same OCID as the previous key's OCID, the Block Volume service will use it to regenerate a volume encryption key.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the BootVolumeKmsKey.
            - Use I(state=present) to update an existing a BootVolumeKmsKey.
            - Use I(state=absent) to delete a BootVolumeKmsKey.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update boot_volume_kms_key
  oci_blockstorage_boot_volume_kms_key:
    boot_volume_id: ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx
    kms_key_id: ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete boot_volume_kms_key
  oci_blockstorage_boot_volume_kms_key:
    boot_volume_id: ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
boot_volume_kms_key:
    description:
        - Details of the BootVolumeKmsKey resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        kms_key_id:
            description:
                - The OCID of the Key Management key assigned to this volume. If the volume is not using Key Management, then the `kmsKeyId` will be a null
                  string.
            returned: on success
            type: string
            sample: ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core import BlockstorageClient
    from oci.core.models import UpdateBootVolumeKmsKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BootVolumeKmsKeyHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and delete"""

    def get_module_resource_id_param(self):
        return "boot_volume_id"

    def get_module_resource_id(self):
        return self.module.params.get("boot_volume_id")

    def get_get_fn(self):
        return self.client.get_boot_volume_kms_key

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_boot_volume_kms_key,
            boot_volume_id=self.module.params.get("boot_volume_id"),
        )

    def get_update_model_class(self):
        return UpdateBootVolumeKmsKeyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_boot_volume_kms_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                boot_volume_id=self.module.params.get("boot_volume_id"),
                update_boot_volume_kms_key_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_boot_volume_kms_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                boot_volume_id=self.module.params.get("boot_volume_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


BootVolumeKmsKeyHelperCustom = get_custom_class("BootVolumeKmsKeyHelperCustom")


class ResourceHelper(BootVolumeKmsKeyHelperCustom, BootVolumeKmsKeyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            boot_volume_id=dict(aliases=["id"], type="str", required=True),
            kms_key_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="boot_volume_kms_key",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

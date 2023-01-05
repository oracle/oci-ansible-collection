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
module: oci_blockstorage_volume_kms_key
short_description: Manage a VolumeKmsKey resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a VolumeKmsKey resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    kms_key_id:
        description:
            - The OCID of the new Key Management key to assign to protect the specified volume.
              This key has to be a valid Key Management key, and policies must exist to allow the user and the Block Volume service to access this key.
              If you specify the same OCID as the previous key's OCID, the Block Volume service will use it to regenerate a volume encryption key.
            - This parameter is updatable.
        type: str
    volume_id:
        description:
            - The OCID of the volume.
        type: str
        aliases: ["id"]
        required: true
    state:
        description:
            - The state of the VolumeKmsKey.
            - Use I(state=present) to update an existing a VolumeKmsKey.
            - Use I(state=absent) to delete a VolumeKmsKey.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update volume_kms_key
  oci_blockstorage_volume_kms_key:
    # required
    volume_id: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete volume_kms_key
  oci_blockstorage_volume_kms_key:
    # required
    volume_id: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
volume_kms_key:
    description:
        - Details of the VolumeKmsKey resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        kms_key_id:
            description:
                - The OCID of the Key Management key assigned to this volume. If the volume is not using Key Management, then the `kmsKeyId` will be a null
                  string.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core import BlockstorageClient
    from oci.core.models import UpdateVolumeKmsKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeKmsKeyHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and delete"""

    def get_possible_entity_types(self):
        return super(VolumeKmsKeyHelperGen, self).get_possible_entity_types() + [
            "volumekmskey",
            "volumekmskeys",
            "corevolumekmskey",
            "corevolumekmskeys",
            "volumekmskeyresource",
            "volumekmskeysresource",
            "kmskey",
            "kmskeys",
            "corekmskey",
            "corekmskeys",
            "kmskeyresource",
            "kmskeysresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "volume_id"

    def get_module_resource_id(self):
        return self.module.params.get("volume_id")

    def get_get_fn(self):
        return self.client.get_volume_kms_key

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_kms_key,
            volume_id=self.module.params.get("volume_id"),
        )

    def get_update_model_class(self):
        return UpdateVolumeKmsKeyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_volume_kms_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_id=self.module.params.get("volume_id"),
                update_volume_kms_key_details=update_details,
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
            call_fn=self.client.delete_volume_kms_key,
            call_fn_args=(),
            call_fn_kwargs=dict(volume_id=self.module.params.get("volume_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


VolumeKmsKeyHelperCustom = get_custom_class("VolumeKmsKeyHelperCustom")


class ResourceHelper(VolumeKmsKeyHelperCustom, VolumeKmsKeyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            kms_key_id=dict(type="str"),
            volume_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume_kms_key",
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

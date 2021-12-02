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
module: oci_blockstorage_boot_volume_backup
short_description: Manage a BootVolumeBackup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BootVolumeBackup resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new boot volume backup of the specified boot volume. For general information about boot volume backups,
      see L(Overview of Boot Volume Backups,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/bootvolumebackups.htm)
    - When the request is received, the backup object is in a REQUEST_RECEIVED state.
      When the data is imaged, it goes into a CREATING state.
      After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.
    - "This resource has the following action operations in the M(oracle.oci.oci_blockstorage_boot_volume_backup_actions) module: change_compartment, copy."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    boot_volume_id:
        description:
            - The OCID of the boot volume that needs to be backed up.
            - Required for create using I(state=present).
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    type:
        description:
            - The type of backup to create. If omitted, defaults to incremental.
        type: str
        choices:
            - "FULL"
            - "INCREMENTAL"
    boot_volume_backup_id:
        description:
            - The OCID of the boot volume backup.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the BootVolumeBackup.
            - Use I(state=present) to create or update a BootVolumeBackup.
            - Use I(state=absent) to delete a BootVolumeBackup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create boot_volume_backup
  oci_blockstorage_boot_volume_backup:
    # required
    boot_volume_id: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    type: FULL

- name: Update boot_volume_backup
  oci_blockstorage_boot_volume_backup:
    # required
    boot_volume_backup_id: "ocid1.bootvolumebackup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update boot_volume_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_boot_volume_backup:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Delete boot_volume_backup
  oci_blockstorage_boot_volume_backup:
    # required
    boot_volume_backup_id: "ocid1.bootvolumebackup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete boot_volume_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_boot_volume_backup:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
boot_volume_backup:
    description:
        - Details of the BootVolumeBackup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        boot_volume_id:
            description:
                - The OCID of the boot volume.
            returned: on success
            type: str
            sample: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the boot volume backup.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        expiration_time:
            description:
                - The date and time the volume backup will expire and be automatically deleted.
                  Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339). This parameter will always be present for backups that
                  were created automatically by a scheduled-backup policy. For manually created backups,
                  it will be absent, signifying that there is no expiration time and the backup will
                  last forever until manually deleted.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the boot volume backup.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        image_id:
            description:
                - The image OCID used to create the boot volume the backup is taken from.
            returned: on success
            type: str
            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_id:
            description:
                - The OCID of the Key Management master encryption assigned to the boot volume backup.
                  For more information about the Key Management service and encryption keys, see
                  L(Overview of Key Management,https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) and
                  L(Using Keys,https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm).
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of a boot volume backup.
            returned: on success
            type: str
            sample: CREATING
        size_in_gbs:
            description:
                - The size of the boot volume, in GBs.
            returned: on success
            type: int
            sample: 56
        source_boot_volume_backup_id:
            description:
                - The OCID of the source boot volume backup.
            returned: on success
            type: str
            sample: "ocid1.sourcebootvolumebackup.oc1..xxxxxxEXAMPLExxxxxx"
        source_type:
            description:
                - Specifies whether the backup was created manually, or via scheduled backup policy.
            returned: on success
            type: str
            sample: MANUAL
        time_created:
            description:
                - The date and time the boot volume backup was created. This is the time the actual point-in-time image
                  of the volume data was taken. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_request_received:
            description:
                - The date and time the request to create the boot volume backup was received. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        type:
            description:
                - The type of a volume backup.
            returned: on success
            type: str
            sample: FULL
        unique_size_in_gbs:
            description:
                - The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space
                  consumed on the boot volume and whether the backup is full or incremental.
            returned: on success
            type: int
            sample: 56
    sample: {
        "boot_volume_id": "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "display_name": "display_name_example",
        "expiration_time": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "size_in_gbs": 56,
        "source_boot_volume_backup_id": "ocid1.sourcebootvolumebackup.oc1..xxxxxxEXAMPLExxxxxx",
        "source_type": "MANUAL",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_request_received": "2013-10-20T19:20:30+01:00",
        "type": "FULL",
        "unique_size_in_gbs": 56
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
    from oci.core.models import CreateBootVolumeBackupDetails
    from oci.core.models import UpdateBootVolumeBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BootVolumeBackupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "boot_volume_backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("boot_volume_backup_id")

    def get_get_fn(self):
        return self.client.get_boot_volume_backup

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_boot_volume_backup,
            boot_volume_backup_id=self.module.params.get("boot_volume_backup_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["boot_volume_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_boot_volume_backups, **kwargs
        )

    def get_create_model_class(self):
        return CreateBootVolumeBackupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_boot_volume_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(create_boot_volume_backup_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateBootVolumeBackupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_boot_volume_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                boot_volume_backup_id=self.module.params.get("boot_volume_backup_id"),
                update_boot_volume_backup_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_boot_volume_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                boot_volume_backup_id=self.module.params.get("boot_volume_backup_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


BootVolumeBackupHelperCustom = get_custom_class("BootVolumeBackupHelperCustom")


class ResourceHelper(BootVolumeBackupHelperCustom, BootVolumeBackupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            boot_volume_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            type=dict(type="str", choices=["FULL", "INCREMENTAL"]),
            boot_volume_backup_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="boot_volume_backup",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

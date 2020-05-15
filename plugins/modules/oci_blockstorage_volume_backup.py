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
module: oci_blockstorage_volume_backup
short_description: Manage a VolumeBackup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VolumeBackup resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new backup of the specified volume. For general information about volume backups,
      see L(Overview of Block Volume Service Backups,https://docs.cloud.oracle.com/Content/Block/Concepts/blockvolumebackups.htm)
    - When the request is received, the backup object is in a REQUEST_RECEIVED state.
      When the data is imaged, it goes into a CREATING state.
      After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.
    - "This resource has the following action operations in the M(oci_volume_backup_actions) module: copy."
version_added: "2.5"
options:
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name for the volume backup. Does not have to be unique and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    type:
        description:
            - The type of backup to create. If omitted, defaults to INCREMENTAL.
        type: str
        choices:
            - "FULL"
            - "INCREMENTAL"
    volume_id:
        description:
            - The OCID of the volume that needs to be backed up.
            - Required for create using I(state=present).
        type: str
    volume_backup_id:
        description:
            - The OCID of the volume backup.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the VolumeBackup.
            - Use I(state=present) to create or update a VolumeBackup.
            - Use I(state=absent) to delete a VolumeBackup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create volume_backup
  oci_blockstorage_volume_backup:
    volume_id: ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update volume_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_volume_backup:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update volume_backup
  oci_blockstorage_volume_backup:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    volume_backup_id: ocid1.volumebackup.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete volume_backup
  oci_blockstorage_volume_backup:
    volume_backup_id: ocid1.volumebackup.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete volume_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_volume_backup:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
volume_backup:
    description:
        - Details of the VolumeBackup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains the volume backup.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name for the volume backup. Does not have to be unique and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        expiration_time:
            description:
                - The date and time the volume backup will expire and be automatically deleted.
                  Format defined by RFC3339. This parameter will always be present for backups that
                  were created automatically by a scheduled-backup policy. For manually created backups,
                  it will be absent, signifying that there is no expiration time and the backup will
                  last forever until manually deleted.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the volume backup.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of a volume backup.
            returned: on success
            type: string
            sample: CREATING
        size_in_gbs:
            description:
                - The size of the volume, in GBs.
            returned: on success
            type: int
            sample: 56
        size_in_mbs:
            description:
                - The size of the volume in MBs. The value must be a multiple of 1024.
                  This field is deprecated. Please use sizeInGBs.
            returned: on success
            type: int
            sample: 56
        source_type:
            description:
                - Specifies whether the backup was created manually, or via scheduled backup policy.
            returned: on success
            type: string
            sample: MANUAL
        source_volume_backup_id:
            description:
                - The OCID of the source volume backup.
            returned: on success
            type: string
            sample: ocid1.sourcevolumebackup.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the volume backup was created. This is the time the actual point-in-time image
                  of the volume data was taken. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_request_received:
            description:
                - The date and time the request to create the volume backup was received. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        type:
            description:
                - The type of a volume backup.
            returned: on success
            type: string
            sample: FULL
        unique_size_in_gbs:
            description:
                - The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space
                  consumed on the volume and whether the backup is full or incremental.
            returned: on success
            type: int
            sample: 56
        unique_size_in_mbs:
            description:
                - The size used by the backup, in MBs. It is typically smaller than sizeInMBs, depending on the space
                  consumed on the volume and whether the backup is full or incremental.
                  This field is deprecated. Please use uniqueSizeInGBs.
            returned: on success
            type: int
            sample: 56
        volume_id:
            description:
                - The OCID of the volume.
            returned: on success
            type: string
            sample: ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "expiration_time": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "size_in_gbs": 56,
        "size_in_mbs": 56,
        "source_type": "MANUAL",
        "source_volume_backup_id": "ocid1.sourcevolumebackup.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_request_received": "2013-10-20T19:20:30+01:00",
        "type": "FULL",
        "unique_size_in_gbs": 56,
        "unique_size_in_mbs": 56,
        "volume_id": "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core.models import CreateVolumeBackupDetails
    from oci.core.models import UpdateVolumeBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeBackupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "volume_backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("volume_backup_id")

    def get_get_fn(self):
        return self.client.get_volume_backup

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_backup,
            volume_backup_id=self.module.params.get("volume_backup_id"),
        )

    def list_resources(self):
        required_list_method_params = [
            "compartment_id",
        ]

        optional_list_method_params = [
            "volume_id",
            "display_name",
        ]

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
            self.client.list_volume_backups, **kwargs
        )

    def get_create_model_class(self):
        return CreateVolumeBackupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_volume_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(create_volume_backup_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateVolumeBackupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_volume_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_backup_id=self.module.params.get("volume_backup_id"),
                update_volume_backup_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_volume_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_backup_id=self.module.params.get("volume_backup_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


VolumeBackupHelperCustom = get_custom_class("VolumeBackupHelperCustom")


class ResourceHelper(VolumeBackupHelperCustom, VolumeBackupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            type=dict(type="str", choices=["FULL", "INCREMENTAL"]),
            volume_id=dict(type="str"),
            volume_backup_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume_backup",
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

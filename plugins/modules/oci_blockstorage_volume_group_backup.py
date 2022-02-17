#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_blockstorage_volume_group_backup
short_description: Manage a VolumeGroupBackup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VolumeGroupBackup resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new backup volume group of the specified volume group.
      For more information, see L(Volume Groups,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm).
    - "This resource has the following action operations in the M(oracle.oci.oci_blockstorage_volume_group_backup_actions) module: change_compartment, copy."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that will contain the volume group
              backup. This parameter is optional, by default backup will be created in
              the same compartment and source volume group.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
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
    volume_group_id:
        description:
            - The OCID of the volume group that needs to be backed up.
            - Required for create using I(state=present).
        type: str
    volume_group_backup_id:
        description:
            - The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the VolumeGroupBackup.
            - Use I(state=present) to create or update a VolumeGroupBackup.
            - Use I(state=absent) to delete a VolumeGroupBackup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create volume_group_backup
  oci_blockstorage_volume_group_backup:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    volume_group_id: "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    type: FULL

- name: Update volume_group_backup
  oci_blockstorage_volume_group_backup:
    # required
    volume_group_backup_id: "ocid1.volumegroupbackup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update volume_group_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_volume_group_backup:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Delete volume_group_backup
  oci_blockstorage_volume_group_backup:
    # required
    volume_group_backup_id: "ocid1.volumegroupbackup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete volume_group_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_volume_group_backup:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
volume_group_backup:
    description:
        - Details of the VolumeGroupBackup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains the volume group backup.
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
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        expiration_time:
            description:
                - The date and time the volume group backup will expire and be automatically deleted.
                  Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339). This parameter will always be present for volume group
                  backups that were created automatically by a scheduled-backup policy. For manually
                  created volume group backups, it will be absent, signifying that there is no expiration
                  time and the backup will last forever until manually deleted.
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
                - The OCID of the volume group backup.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of a volume group backup.
            returned: on success
            type: str
            sample: CREATING
        size_in_mbs:
            description:
                - The aggregate size of the volume group backup, in MBs.
            returned: on success
            type: int
            sample: 56
        size_in_gbs:
            description:
                - The aggregate size of the volume group backup, in GBs.
            returned: on success
            type: int
            sample: 56
        source_type:
            description:
                - Specifies whether the volume group backup was created manually, or via scheduled
                  backup policy.
            returned: on success
            type: str
            sample: MANUAL
        time_created:
            description:
                - The date and time the volume group backup was created. This is the time the actual point-in-time image
                  of the volume group data was taken. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_request_received:
            description:
                - The date and time the request to create the volume group backup was received. Format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        type:
            description:
                - The type of backup.
            returned: on success
            type: str
            sample: FULL
        unique_size_in_mbs:
            description:
                - The aggregate size used by the volume group backup, in MBs.
                - It is typically smaller than sizeInMBs, depending on the spaceconsumed
                  on the volume group and whether the volume backup is full or incremental.
            returned: on success
            type: int
            sample: 56
        unique_size_in_gbs:
            description:
                - The aggregate size used by the volume group backup, in GBs.
                - It is typically smaller than sizeInGBs, depending on the spaceconsumed
                  on the volume group and whether the volume backup is full or incremental.
            returned: on success
            type: int
            sample: 56
        volume_backup_ids:
            description:
                - OCIDs for the volume backups in this volume group backup.
            returned: on success
            type: list
            sample: []
        volume_group_id:
            description:
                - The OCID of the source volume group.
            returned: on success
            type: str
            sample: "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"
        source_volume_group_backup_id:
            description:
                - The OCID of the source volume group backup.
            returned: on success
            type: str
            sample: "ocid1.sourcevolumegroupbackup.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "expiration_time": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "size_in_mbs": 56,
        "size_in_gbs": 56,
        "source_type": "MANUAL",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_request_received": "2013-10-20T19:20:30+01:00",
        "type": "FULL",
        "unique_size_in_mbs": 56,
        "unique_size_in_gbs": 56,
        "volume_backup_ids": [],
        "volume_group_id": "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx",
        "source_volume_group_backup_id": "ocid1.sourcevolumegroupbackup.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core.models import CreateVolumeGroupBackupDetails
    from oci.core.models import UpdateVolumeGroupBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeGroupBackupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(VolumeGroupBackupHelperGen, self).get_possible_entity_types() + [
            "volumegroupbackup",
            "volumegroupbackups",
            "corevolumegroupbackup",
            "corevolumegroupbackups",
            "volumegroupbackupresource",
            "volumegroupbackupsresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "volume_group_backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("volume_group_backup_id")

    def get_get_fn(self):
        return self.client.get_volume_group_backup

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_group_backup,
            volume_group_backup_id=self.module.params.get("volume_group_backup_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["volume_group_id", "display_name"]

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
            self.client.list_volume_group_backups, **kwargs
        )

    def get_create_model_class(self):
        return CreateVolumeGroupBackupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_volume_group_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(create_volume_group_backup_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateVolumeGroupBackupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_volume_group_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_group_backup_id=self.module.params.get("volume_group_backup_id"),
                update_volume_group_backup_details=update_details,
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
            call_fn=self.client.delete_volume_group_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_group_backup_id=self.module.params.get("volume_group_backup_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


VolumeGroupBackupHelperCustom = get_custom_class("VolumeGroupBackupHelperCustom")


class ResourceHelper(VolumeGroupBackupHelperCustom, VolumeGroupBackupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            type=dict(type="str", choices=["FULL", "INCREMENTAL"]),
            volume_group_id=dict(type="str"),
            volume_group_backup_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume_group_backup",
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

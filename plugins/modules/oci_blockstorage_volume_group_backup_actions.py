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
module: oci_blockstorage_volume_group_backup_actions
short_description: Perform actions on a VolumeGroupBackup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a VolumeGroupBackup resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a volume group backup into a different compartment within the same tenancy.
      For information about moving resources between compartments,
      see L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=copy), creates a volume group backup copy in specified region. For general information about volume group backups,
      see L(Overview of Block Volume Service Backups,https://docs.cloud.oracle.com/Content/Block/Concepts/blockvolumebackups.htm)
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    volume_group_backup_id:
        description:
            - The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the volume group backup to.
            - Required for I(action=change_compartment).
        type: str
    destination_region:
        description:
            - The name of the destination region.
            - "Example: `us-ashburn-1`"
            - Required for I(action=copy).
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Applicable only for I(action=copy).
        type: str
        aliases: ["name"]
    kms_key_id:
        description:
            - The OCID of the Key Management key in the destination region which will be the master encryption key
              for the copied volume group backup.
              If you do not specify this attribute the volume group backup will be encrypted with the Oracle-provided encryption
              key when it is copied to the destination region.
            - For more information about the Key Management service and encryption keys, see
              L(Overview of Key Management,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm) and
              L(Using Keys,https://docs.cloud.oracle.com/Content/KeyManagement/Tasks/usingkeys.htm).
            - Applicable only for I(action=copy).
        type: str
    action:
        description:
            - The action to perform on the VolumeGroupBackup.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "copy"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on volume_group_backup
  oci_blockstorage_volume_group_backup_actions:
    # required
    volume_group_backup_id: "ocid1.volumegroupbackup.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action copy on volume_group_backup
  oci_blockstorage_volume_group_backup_actions:
    # required
    volume_group_backup_id: "ocid1.volumegroupbackup.oc1..xxxxxxEXAMPLExxxxxx"
    destination_region: us-phoenix-1
    action: copy

    # optional
    display_name: display_name_example
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"

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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.core import BlockstorageClient
    from oci.core.models import ChangeVolumeGroupBackupCompartmentDetails
    from oci.core.models import CopyVolumeGroupBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeGroupBackupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        copy
    """

    @staticmethod
    def get_module_resource_id_param():
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVolumeGroupBackupCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_volume_group_backup_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_group_backup_id=self.module.params.get("volume_group_backup_id"),
                change_volume_group_backup_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def copy(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CopyVolumeGroupBackupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.copy_volume_group_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_group_backup_id=self.module.params.get("volume_group_backup_id"),
                copy_volume_group_backup_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


VolumeGroupBackupActionsHelperCustom = get_custom_class(
    "VolumeGroupBackupActionsHelperCustom"
)


class ResourceHelper(
    VolumeGroupBackupActionsHelperCustom, VolumeGroupBackupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            volume_group_backup_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            destination_region=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            kms_key_id=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["change_compartment", "copy"]
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

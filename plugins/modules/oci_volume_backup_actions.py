#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_volume_backup_actions
short_description: Perform actions on a VolumeBackup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a VolumeBackup resource in Oracle Cloud Infrastructure
    - For I(action=copy), creates a volume backup copy in specified region. For general information about volume backups,
      see L(Overview of Block Volume Service Backups,https://docs.cloud.oracle.com/Content/Block/Concepts/blockvolumebackups.htm)
version_added: "2.5"
options:
    volume_backup_id:
        description:
            - The OCID of the volume backup.
        aliases: ["id"]
        required: true
    destination_region:
        description:
            - The name of the destination region.
            - "Example: `us-ashburn-1`"
        required: true
    display_name:
        description:
            - A user-friendly name for the volume backup. Does not have to be unique and it's changeable.
              Avoid entering confidential information.
        aliases: ["name"]
    action:
        description:
            - The action to perform on the VolumeBackup.
        required: true
        choices: ["copy"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action copy on volume_backup
  oci_volume_backup_actions:
    volume_backup_id: ocid1.volumebackup.oc1..xxxxxxEXAMPLExxxxxx
    destination_region: us-ashburn-1
    action: copy

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
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {Operations: {CostCenter: US}}
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
                  predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {Department: Finance}
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
        "defined_tags": {Operations: {CostCenter: US}},
        "display_name": "display_name_example",
        "expiration_time": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {Department: Finance},
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
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    convert_input_data_to_model_class,
)

try:
    from oci.core import BlockstorageClient
    from oci.core.models import CopyVolumeBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeBackupActionsHelperGen(OCIResourceHelperBase):
    """Supported actions: copy"""

    @staticmethod
    def get_module_resource_id_param():
        return "volume_backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("volume_backup_id")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_backup,
            volume_backup_id=self.module.params.get("volume_backup_id"),
        )

    def copy(self):
        action_details = convert_input_data_to_model_class(
            self.module.params, CopyVolumeBackupDetails
        )
        return oci_common_utils.call_with_backoff(
            self.client.copy_volume_backup,
            volume_backup_id=self.module.params.get("volume_backup_id"),
            copy_volume_backup_details=action_details,
        )


VolumeBackupActionsHelperCustom = get_custom_class("VolumeBackupActionsHelperCustom")


class ResourceHelper(VolumeBackupActionsHelperCustom, VolumeBackupActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            volume_backup_id=dict(aliases=["id"], type="str", required=True),
            destination_region=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            action=dict(type="str", required=True, choices=["copy"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume_backup",
        service_client_class=BlockstorageClient,
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

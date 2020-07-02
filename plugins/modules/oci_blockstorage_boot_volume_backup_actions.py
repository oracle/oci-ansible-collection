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
module: oci_blockstorage_boot_volume_backup_actions
short_description: Perform actions on a BootVolumeBackup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BootVolumeBackup resource in Oracle Cloud Infrastructure
    - For I(action=copy), creates a boot volume backup copy in specified region. For general information about volume backups,
      see L(Overview of Boot Volume Backups,https://docs.cloud.oracle.com/Content/Block/Concepts/bootvolumebackups.htm)
version_added: "2.9"
author: Oracle (@oracle)
options:
    boot_volume_backup_id:
        description:
            - The OCID of the boot volume backup.
        type: str
        aliases: ["id"]
        required: true
    destination_region:
        description:
            - The name of the destination region.
            - "Example: `us-ashburn-1`"
        type: str
        required: true
    display_name:
        description:
            - A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable.
              Avoid entering confidential information.
        type: str
        aliases: ["name"]
    action:
        description:
            - The action to perform on the BootVolumeBackup.
        type: str
        required: true
        choices:
            - "copy"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action copy on boot_volume_backup
  oci_blockstorage_boot_volume_backup_actions:
    boot_volume_backup_id: ocid1.bootvolumebackup.oc1..xxxxxxEXAMPLExxxxxx
    destination_region: us-ashburn-1
    action: copy

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
            type: string
            sample: ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment that contains the boot volume backup.
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
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {}
        display_name:
            description:
                - A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable.
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
                - The OCID of the boot volume backup.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        image_id:
            description:
                - The image OCID used to create the boot volume the backup is taken from.
            returned: on success
            type: string
            sample: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of a boot volume backup.
            returned: on success
            type: string
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
            type: string
            sample: ocid1.sourcebootvolumebackup.oc1..xxxxxxEXAMPLExxxxxx
        source_type:
            description:
                - Specifies whether the backup was created manually, or via scheduled backup policy.
            returned: on success
            type: string
            sample: MANUAL
        time_created:
            description:
                - The date and time the boot volume backup was created. This is the time the actual point-in-time image
                  of the volume data was taken. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_request_received:
            description:
                - The date and time the request to create the boot volume backup was received. Format defined by RFC3339.
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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.core import BlockstorageClient
    from oci.core.models import CopyBootVolumeBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BootVolumeBackupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        copy
    """

    @staticmethod
    def get_module_resource_id_param():
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

    def copy(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CopyBootVolumeBackupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.copy_boot_volume_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                boot_volume_backup_id=self.module.params.get("boot_volume_backup_id"),
                copy_boot_volume_backup_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


BootVolumeBackupActionsHelperCustom = get_custom_class(
    "BootVolumeBackupActionsHelperCustom"
)


class ResourceHelper(
    BootVolumeBackupActionsHelperCustom, BootVolumeBackupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            boot_volume_backup_id=dict(aliases=["id"], type="str", required=True),
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
        resource_type="boot_volume_backup",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

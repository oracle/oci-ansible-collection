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
module: oci_blockstorage_volume_group_actions
short_description: Perform actions on a VolumeGroup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a VolumeGroup resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a volume group into a different compartment within the same tenancy.
      For information about moving resources between compartments,
      see L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9"
author: Oracle (@oracle)
options:
    volume_group_id:
        description:
            - The Oracle Cloud ID (OCID) that uniquely identifies the volume group.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the volume group to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the VolumeGroup.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on volume_group
  oci_blockstorage_volume_group_actions:
    volume_group_id: "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
volume_group:
    description:
        - Details of the VolumeGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of the volume group.
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment that contains the volume group.
            returned: on success
            type: string
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
                - A user-friendly name for the volume group. Does not have to be
                  unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
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
                - The OCID for the volume group.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of a volume group.
            returned: on success
            type: string
            sample: PROVISIONING
        size_in_mbs:
            description:
                - The aggregate size of the volume group in MBs.
            returned: on success
            type: int
            sample: 56
        size_in_gbs:
            description:
                - The aggregate size of the volume group in GBs.
            returned: on success
            type: int
            sample: 56
        source_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - ""
                    returned: on success
                    type: string
                    sample: volumeGroupBackupId
                volume_group_backup_id:
                    description:
                        - The OCID of the volume group backup to restore from.
                    returned: on success
                    type: string
                    sample: "ocid1.volumegroupbackup.oc1..xxxxxxEXAMPLExxxxxx"
                volume_group_id:
                    description:
                        - The OCID of the volume group to clone from.
                    returned: on success
                    type: string
                    sample: "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"
                volume_ids:
                    description:
                        - OCIDs for the volumes in this volume group.
                    returned: on success
                    type: list
                    sample: []
        time_created:
            description:
                - The date and time the volume group was created. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        volume_ids:
            description:
                - OCIDs for the volumes in this volume group.
            returned: on success
            type: list
            sample: []
        is_hydrated:
            description:
                - Specifies whether the newly created cloned volume group's data has finished copying
                  from the source volume group or backup.
            returned: on success
            type: bool
            sample: true
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "size_in_mbs": 56,
        "size_in_gbs": 56,
        "source_details": {
            "type": "volumeGroupBackupId",
            "volume_group_backup_id": "ocid1.volumegroupbackup.oc1..xxxxxxEXAMPLExxxxxx",
            "volume_group_id": "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx",
            "volume_ids": []
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "volume_ids": [],
        "is_hydrated": true
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
    from oci.core.models import ChangeVolumeGroupCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeGroupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "volume_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("volume_group_id")

    def get_get_fn(self):
        return self.client.get_volume_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_group,
            volume_group_id=self.module.params.get("volume_group_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVolumeGroupCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_volume_group_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_group_id=self.module.params.get("volume_group_id"),
                change_volume_group_compartment_details=action_details,
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


VolumeGroupActionsHelperCustom = get_custom_class("VolumeGroupActionsHelperCustom")


class ResourceHelper(VolumeGroupActionsHelperCustom, VolumeGroupActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            volume_group_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume_group",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

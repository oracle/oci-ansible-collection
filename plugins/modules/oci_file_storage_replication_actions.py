#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_file_storage_replication_actions
short_description: Perform actions on a Replication resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Replication resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a replication and its replication target into a different compartment within the same tenancy.
      For information about moving resources between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    replication_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the replication.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to move the replication to. Also changes the
              replication target's compartment in the target region.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Replication.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on replication
  oci_file_storage_replication_actions:
    # required
    replication_id: "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
replication:
    description:
        - Details of the Replication resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the replication.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - "The availability domain that contains the replication. May be unset as a blank or `NULL` value.
                  Example: `Uocm:PHX-AD-2`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the replication.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the replication.
            returned: on success
            type: str
            sample: CREATING
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `My replication`"
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time the replication was created
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2021-01-04T20:01:29.100Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source file system.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the target file system.
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        replication_target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                  L(`ReplicationTarget`,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/ReplicationTarget).
            returned: on success
            type: str
            sample: "ocid1.replicationtarget.oc1..xxxxxxEXAMPLExxxxxx"
        replication_interval:
            description:
                - Duration in minutes between replication snapshots.
            returned: on success
            type: int
            sample: 56
        last_snapshot_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last snapshot that has been replicated completely.
                  Empty if the copy of the initial snapshot is not complete.
            returned: on success
            type: str
            sample: "ocid1.lastsnapshot.oc1..xxxxxxEXAMPLExxxxxx"
        recovery_point_time:
            description:
                - "The L(`snapshotTime`,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Snapshot/snapshotTime) of the most recent recoverable
                  replication snapshot
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                  Example: `2021-04-04T20:01:29.100Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        delta_status:
            description:
                - The current state of the snapshot during replication operations.
            returned: on success
            type: str
            sample: IDLE
        lifecycle_details:
            description:
                - Additional information about the current 'lifecycleState'.
            returned: on success
            type: str
            sample: lifecycle_details_example
        delta_progress:
            description:
                - Percentage progress of the current replication cycle.
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair
                   with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "replication_target_id": "ocid1.replicationtarget.oc1..xxxxxxEXAMPLExxxxxx",
        "replication_interval": 56,
        "last_snapshot_id": "ocid1.lastsnapshot.oc1..xxxxxxEXAMPLExxxxxx",
        "recovery_point_time": "2013-10-20T19:20:30+01:00",
        "delta_status": "IDLE",
        "lifecycle_details": "lifecycle_details_example",
        "delta_progress": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import ChangeReplicationCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReplicationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "replication_id"

    def get_module_resource_id(self):
        return self.module.params.get("replication_id")

    def get_get_fn(self):
        return self.client.get_replication

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication,
            replication_id=self.module.params.get("replication_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeReplicationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_replication_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                replication_id=self.module.params.get("replication_id"),
                change_replication_compartment_details=action_details,
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


ReplicationActionsHelperCustom = get_custom_class("ReplicationActionsHelperCustom")


class ResourceHelper(ReplicationActionsHelperCustom, ReplicationActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            replication_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="replication",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

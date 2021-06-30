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
module: oci_database_backup_destination_actions
short_description: Perform actions on a BackupDestination resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BackupDestination resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), move the backup destination and its dependent resources to the specified compartment.
      For more information, see
      L(Moving Database Resources to a Different Compartment,https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes).
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the resource to.
        type: str
        required: true
    backup_destination_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the BackupDestination.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on backup_destination
  oci_database_backup_destination_actions:
    compartment_id: "ocid.compartment.oc1..unique_ID"
    backup_destination_id: "ocid1.backupdestination.oc1..xxxxxxEXAMPLExxxxxx"
    action: "change_compartment"

"""

RETURN = """
backup_destination:
    description:
        - Details of the BackupDestination resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-provided name of the backup destination.
            returned: on success
            type: string
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - Type of the backup destination.
            returned: on success
            type: string
            sample: NFS
        associated_databases:
            description:
                - List of databases associated with the backup destination.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    returned: on success
                    type: string
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                db_name:
                    description:
                        - The display name of the database that is associated with the backup destination.
                    returned: on success
                    type: string
                    sample: db_name_example
        connection_string:
            description:
                - For a RECOVERY_APPLIANCE backup destination, the connection string for connecting to the Recovery Appliance.
            returned: on success
            type: string
            sample: connection_string_example
        vpc_users:
            description:
                - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.
            returned: on success
            type: list
            sample: []
        local_mount_point_path:
            description:
                - The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server
                  location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM
                  cluster nodes.
            returned: on success
            type: string
            sample: local_mount_point_path_example
        nfs_mount_type:
            description:
                - NFS Mount type for backup destination.
            returned: on success
            type: string
            sample: SELF_MOUNT
        nfs_server:
            description:
                - Host names or IP addresses for NFS Auto mount.
            returned: on success
            type: list
            sample: []
        nfs_server_export:
            description:
                - Specifies the directory on which to mount the file system
            returned: on success
            type: string
            sample: nfs_server_export_example
        lifecycle_state:
            description:
                - The current lifecycle state of the backup destination.
            returned: on success
            type: string
            sample: ACTIVE
        time_created:
            description:
                - The date and time the backup destination was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_details:
            description:
                - A descriptive text associated with the lifecycleState.
                  Typically contains additional displayable text
            returned: on success
            type: string
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "NFS",
        "associated_databases": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "db_name": "db_name_example"
        }],
        "connection_string": "connection_string_example",
        "vpc_users": [],
        "local_mount_point_path": "local_mount_point_path_example",
        "nfs_mount_type": "SELF_MOUNT",
        "nfs_server": [],
        "nfs_server_export": "nfs_server_export_example",
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import ChangeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackupDestinationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def __init__(self, *args, **kwargs):
        super(BackupDestinationActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "backup_destination_id"

    def get_module_resource_id(self):
        return self.module.params.get("backup_destination_id")

    def get_get_fn(self):
        return self.client.get_backup_destination

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backup_destination,
            backup_destination_id=self.module.params.get("backup_destination_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_backup_destination_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_compartment_details=action_details,
                backup_destination_id=self.module.params.get("backup_destination_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BackupDestinationActionsHelperCustom = get_custom_class(
    "BackupDestinationActionsHelperCustom"
)


class ResourceHelper(
    BackupDestinationActionsHelperCustom, BackupDestinationActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            backup_destination_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="backup_destination",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

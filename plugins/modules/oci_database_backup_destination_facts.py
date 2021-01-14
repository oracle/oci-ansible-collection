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
module: oci_database_backup_destination_facts
short_description: Fetches details about one or multiple BackupDestination resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BackupDestination resources in Oracle Cloud Infrastructure
    - Gets a list of backup destinations in the specified compartment.
    - If I(backup_destination_id) is specified, the details of a single BackupDestination will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    backup_destination_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
            - Required to get a specific backup_destination.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple backup_destinations.
        type: str
    type:
        description:
            - A filter to return only resources that match the given type of the Backup Destination.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List backup_destinations
  oci_database_backup_destination_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific backup_destination
  oci_database_backup_destination_facts:
    backup_destination_id: ocid1.backupdestination.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
backup_destinations:
    description:
        - List of BackupDestination resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackupDestinationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "backup_destination_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backup_destination,
            backup_destination_id=self.module.params.get("backup_destination_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "type",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_backup_destination,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


BackupDestinationFactsHelperCustom = get_custom_class(
    "BackupDestinationFactsHelperCustom"
)


class ResourceFactsHelper(
    BackupDestinationFactsHelperCustom, BackupDestinationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            backup_destination_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            type=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backup_destination",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(backup_destinations=result)


if __name__ == "__main__":
    main()

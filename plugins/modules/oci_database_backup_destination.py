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
module: oci_database_backup_destination
short_description: Manage a BackupDestination resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BackupDestination resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a backup destination.
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The user-provided name of the backup destination.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    type:
        description:
            - Type of the backup destination.
            - Required for create using I(state=present).
        type: str
        choices:
            - "NFS"
            - "RECOVERY_APPLIANCE"
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - This parameter is updatable.
        type: dict
    local_mount_point_path:
        description:
            - "**Deprecated.** The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS
              server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM
              cluster nodes.
              This field is deprecated. Use the mountTypeDetails field instead to specify the mount type for NFS."
            - This parameter is updatable.
            - Applicable when type is 'NFS'
        type: str
    mount_type_details:
        description:
            - ""
            - Applicable when type is 'NFS'
        type: dict
        suboptions:
            mount_type:
                description:
                    - Mount type for backup destination.
                type: str
                choices:
                    - "SELF_MOUNT"
                    - "AUTOMATED_MOUNT"
                default: "SELF_MOUNT"
            local_mount_point_path:
                description:
                    - The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server
                      location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM
                      cluster nodes.
                    - Required when mount_type is 'SELF_MOUNT'
                type: str
            nfs_server:
                description:
                    - IP addresses for NFS Auto mount.
                    - Required when mount_type is 'AUTOMATED_MOUNT'
                type: list
            nfs_server_export:
                description:
                    - Specifies the directory on which to mount the file system
                    - Required when mount_type is 'AUTOMATED_MOUNT'
                type: str
    connection_string:
        description:
            - The connection string for connecting to the Recovery Appliance.
            - This parameter is updatable.
            - Required when type is 'RECOVERY_APPLIANCE'
        type: str
    vpc_users:
        description:
            - The Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.
            - This parameter is updatable.
            - Required when type is 'RECOVERY_APPLIANCE'
        type: list
    backup_destination_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    nfs_mount_type:
        description:
            - NFS Mount type for backup destination.
            - This parameter is updatable.
        type: str
        choices:
            - "SELF_MOUNT"
            - "AUTOMATED_MOUNT"
    nfs_server:
        description:
            - IP addresses for NFS Auto mount.
            - This parameter is updatable.
        type: list
    nfs_server_export:
        description:
            - Specifies the directory on which to mount the file system
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the BackupDestination.
            - Use I(state=present) to create or update a BackupDestination.
            - Use I(state=absent) to delete a BackupDestination.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create backup_destination
  oci_database_backup_destination:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    type: RECOVERY_APPLIANCE
    connection_string: connection_string_example

- name: Update backup_destination using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_backup_destination:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    local_mount_point_path: local_mount_point_path_example
    connection_string: connection_string_example
    nfs_mount_type: SELF_MOUNT
    nfs_server_export: nfs_server_export_example

- name: Update backup_destination
  oci_database_backup_destination:
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    backup_destination_id: ocid1.backupdestination.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete backup_destination
  oci_database_backup_destination:
    backup_destination_id: ocid1.backupdestination.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete backup_destination using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_backup_destination:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient
    from oci.database.models import CreateBackupDestinationDetails
    from oci.database.models import UpdateBackupDestinationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackupDestinationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["type"]

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
            self.client.list_backup_destination, **kwargs
        )

    def get_create_model_class(self):
        return CreateBackupDestinationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_backup_destination,
            call_fn_args=(),
            call_fn_kwargs=dict(create_backup_destination_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateBackupDestinationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_backup_destination,
            call_fn_args=(),
            call_fn_kwargs=dict(
                backup_destination_id=self.module.params.get("backup_destination_id"),
                update_backup_destination_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_backup_destination,
            call_fn_args=(),
            call_fn_kwargs=dict(
                backup_destination_id=self.module.params.get("backup_destination_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


BackupDestinationHelperCustom = get_custom_class("BackupDestinationHelperCustom")


class ResourceHelper(BackupDestinationHelperCustom, BackupDestinationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            type=dict(type="str", choices=["NFS", "RECOVERY_APPLIANCE"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            local_mount_point_path=dict(type="str"),
            mount_type_details=dict(
                type="dict",
                options=dict(
                    mount_type=dict(
                        type="str",
                        default="SELF_MOUNT",
                        choices=["SELF_MOUNT", "AUTOMATED_MOUNT"],
                    ),
                    local_mount_point_path=dict(type="str"),
                    nfs_server=dict(type="list"),
                    nfs_server_export=dict(type="str"),
                ),
            ),
            connection_string=dict(type="str"),
            vpc_users=dict(type="list"),
            backup_destination_id=dict(aliases=["id"], type="str"),
            nfs_mount_type=dict(type="str", choices=["SELF_MOUNT", "AUTOMATED_MOUNT"]),
            nfs_server=dict(type="list"),
            nfs_server_export=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

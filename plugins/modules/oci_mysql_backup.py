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
module: oci_mysql_backup
short_description: Manage a Backup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Backup resource in Oracle Cloud Infrastructure
    - For I(state=present), create a backup of a DB System.
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - A user-supplied display name for the backup.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A user-supplied description for the backup.
            - This parameter is updatable.
        type: str
    backup_type:
        description:
            - The type of backup.
        type: str
        choices:
            - "FULL"
            - "INCREMENTAL"
    db_system_id:
        description:
            - The OCID of the DB System the Backup is associated with.
            - Required for create using I(state=present).
        type: str
    retention_in_days:
        description:
            - Number of days to retain this backup.
            - This parameter is updatable.
        type: int
    freeform_tags:
        description:
            - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    backup_id:
        description:
            - The OCID of the Backup
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the Backup.
            - Use I(state=present) to create or update a Backup.
            - Use I(state=absent) to delete a Backup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create backup
  oci_mysql_backup:
    db_system_id: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_backup:
    display_name: display_name_example
    description: description_example
    retention_in_days: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update backup
  oci_mysql_backup:
    display_name: display_name_example
    description: description_example
    backup_id: ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete backup
  oci_mysql_backup:
    backup_id: ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_backup:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
backup:
    description:
        - Details of the Backup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the backup itself
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-supplied display name for the backup.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - A user-supplied description for the backup.
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The time the backup record was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time at which the backup was updated.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The state of the backup.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: string
            sample: lifecycle_details_example
        backup_type:
            description:
                - The type of backup.
            returned: on success
            type: string
            sample: FULL
        creation_type:
            description:
                - If the backup was created automatically, or by a manual request.
            returned: on success
            type: string
            sample: MANUAL
        db_system_id:
            description:
                - The OCID of the DB System the backup is associated with.
            returned: on success
            type: string
            sample: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx
        backup_size_in_gbs:
            description:
                - The size of the backup in base-2 (IEC) gibibytes. (GiB).
            returned: on success
            type: int
            sample: 56
        retention_in_days:
            description:
                - Number of days to retain this backup.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_gbs:
            description:
                - Initial size of the data volume in GiBs.
            returned: on success
            type: int
            sample: 56
        mysql_version:
            description:
                - The MySQL server version of the DB System used for backup.
            returned: on success
            type: string
            sample: mysql_version_example
        shape_name:
            description:
                - The shape of the DB System used for backup.
            returned: on success
            type: string
            sample: shape_name_example
        freeform_tags:
            description:
                - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "backup_type": "FULL",
        "creation_type": "MANUAL",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_size_in_gbs": 56,
        "retention_in_days": 56,
        "data_storage_size_in_gbs": 56,
        "mysql_version": "mysql_version_example",
        "shape_name": "shape_name_example",
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
    from oci.mysql import DbBackupsClient
    from oci.mysql.models import CreateBackupDetails
    from oci.mysql.models import UpdateBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlBackupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("backup_id")

    def get_get_fn(self):
        return self.client.get_backup

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backup, backup_id=self.module.params.get("backup_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["backup_id", "db_system_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_backups, **kwargs)

    def get_create_model_class(self):
        return CreateBackupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(create_backup_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateBackupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                backup_id=self.module.params.get("backup_id"),
                update_backup_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(backup_id=self.module.params.get("backup_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlBackupHelperCustom = get_custom_class("MysqlBackupHelperCustom")


class ResourceHelper(MysqlBackupHelperCustom, MysqlBackupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            backup_type=dict(type="str", choices=["FULL", "INCREMENTAL"]),
            db_system_id=dict(type="str"),
            retention_in_days=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            backup_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="backup",
        service_client_class=DbBackupsClient,
        namespace="mysql",
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

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
module: oci_database_backup
short_description: Manage a Backup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a Backup resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new backup in the specified database based on the request parameters you provide. If you previously used RMAN or dbcli to
      configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your
      database. This means that you can no longer rely on your previously configured unmanaged backups to work.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - The user-friendly name for the backup. The name does not have to be unique.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    backup_id:
        description:
            - The backup L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the Backup.
            - Use I(state=present) to create a Backup.
            - Use I(state=absent) to delete a Backup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create backup
  oci_database_backup:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

- name: Delete backup
  oci_database_backup:
    # required
    backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_backup:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the backup. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        type:
            description:
                - The type of backup.
            returned: on success
            type: str
            sample: INCREMENTAL
        time_started:
            description:
                - The date and time the backup started.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - The date and time the backup was completed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        availability_domain:
            description:
                - The name of the availability domain where the database backup is stored.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        lifecycle_state:
            description:
                - The current state of the backup.
            returned: on success
            type: str
            sample: CREATING
        database_edition:
            description:
                - The Oracle Database edition of the DB system from which the database backup was taken.
            returned: on success
            type: str
            sample: STANDARD_EDITION
        database_size_in_gbs:
            description:
                - The size of the database in gigabytes at the time the backup was taken.
            returned: on success
            type: float
            sample: 1.2
        shape:
            description:
                - Shape of the backup's source database.
            returned: on success
            type: str
            sample: shape_example
        version:
            description:
                - Version of the backup's source database
            returned: on success
            type: str
            sample: version_example
        kms_key_id:
            description:
                - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "type": "INCREMENTAL",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "lifecycle_state": "CREATING",
        "database_edition": "STANDARD_EDITION",
        "database_size_in_gbs": 1.2,
        "shape": "shape_example",
        "version": "version_example",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(BackupHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(BackupHelperGen, self).get_possible_entity_types() + [
            "backup",
            "backups",
            "databasebackup",
            "databasebackups",
            "backupresource",
            "backupsresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("backup_id")

    def get_get_fn(self):
        return self.client.get_backup

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_backup, backup_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backup, backup_id=self.module.params.get("backup_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["database_id", "compartment_id"]

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
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(backup_id=self.module.params.get("backup_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BackupHelperCustom = get_custom_class("BackupHelperCustom")


class ResourceHelper(BackupHelperCustom, BackupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            database_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
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
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

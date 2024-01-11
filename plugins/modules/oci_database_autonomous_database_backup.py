#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_database_autonomous_database_backup
short_description: Manage an AutonomousDatabaseBackup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AutonomousDatabaseBackup resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Autonomous Database backup for the specified database based on the provided request parameters.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The user-friendly name for the backup. The name does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    autonomous_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database backup.
            - Required for create using I(state=present).
        type: str
    is_long_term_backup:
        description:
            - Indicates whether the backup is long-term
        type: bool
    backup_destination_details:
        description:
            - ""
        type: dict
        suboptions:
            type:
                description:
                    - Type of the database backup destination.
                type: str
                choices:
                    - "NFS"
                    - "RECOVERY_APPLIANCE"
                    - "OBJECT_STORE"
                    - "LOCAL"
                    - "DBRS"
                required: true
            id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
                type: str
            vpc_user:
                description:
                    - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery Appliance.
                type: str
            vpc_password:
                description:
                    - For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.
                type: str
            internet_proxy:
                description:
                    - Proxy URL to connect to object store.
                type: str
            dbrs_policy_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DBRS policy used for backup.
                type: str
    retention_period_in_days:
        description:
            - Retention period, in days, for long-term backups
            - This parameter is updatable.
        type: int
    autonomous_database_backup_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database backup.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the AutonomousDatabaseBackup.
            - Use I(state=present) to create or update an AutonomousDatabaseBackup.
            - Use I(state=absent) to delete an AutonomousDatabaseBackup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create autonomous_database_backup
  oci_database_autonomous_database_backup:
    # required
    autonomous_database_id: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    is_long_term_backup: true
    backup_destination_details:
      # required
      type: NFS

      # optional
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      vpc_user: vpc_user_example
      vpc_password: example-password
      internet_proxy: internet_proxy_example
      dbrs_policy_id: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    retention_period_in_days: 56

- name: Update autonomous_database_backup
  oci_database_autonomous_database_backup:
    # required
    autonomous_database_backup_id: "ocid1.autonomousdatabasebackup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    retention_period_in_days: 56

- name: Update autonomous_database_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_database_backup:
    # required
    display_name: display_name_example

    # optional
    retention_period_in_days: 56

- name: Delete autonomous_database_backup
  oci_database_autonomous_database_backup:
    # required
    autonomous_database_backup_id: "ocid1.autonomousdatabasebackup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete autonomous_database_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_database_backup:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
autonomous_database_backup:
    description:
        - Details of the AutonomousDatabaseBackup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database backup.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        autonomous_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database.
            returned: on success
            type: str
            sample: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"
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
        is_automatic:
            description:
                - Indicates whether the backup is user-initiated or automatic.
            returned: on success
            type: bool
            sample: true
        time_started:
            description:
                - The date and time the backup started.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - The date and time the backup completed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        database_size_in_tbs:
            description:
                - The size of the database in terabytes at the time the backup was taken.
            returned: on success
            type: float
            sample: 10
        lifecycle_state:
            description:
                - The current state of the backup.
            returned: on success
            type: str
            sample: CREATING
        is_restorable:
            description:
                - Indicates whether the backup can be used to restore the associated Autonomous Database.
            returned: on success
            type: bool
            sample: true
        key_store_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the key store.
            returned: on success
            type: str
            sample: "ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx"
        key_store_wallet_name:
            description:
                - The wallet name for Oracle Key Vault.
            returned: on success
            type: str
            sample: key_store_wallet_name_example
        kms_key_id:
            description:
                - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        vault_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                  L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_version_id:
            description:
                - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
                  versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
            returned: on success
            type: str
            sample: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
        retention_period_in_days:
            description:
                - Retention period, in days, for long-term backups
            returned: on success
            type: int
            sample: 56
        time_available_till:
            description:
                - Timestamp until when the backup will be available
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        db_version:
            description:
                - A valid Oracle Database version for Autonomous Database.
            returned: on success
            type: str
            sample: db_version_example
        size_in_tbs:
            description:
                - The backup size in terrabytes (TB).
            returned: on success
            type: float
            sample: 1.2
        backup_destination_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of the database backup destination.
                    returned: on success
                    type: str
                    sample: NFS
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                vpc_user:
                    description:
                        - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery Appliance.
                    returned: on success
                    type: str
                    sample: vpc_user_example
                vpc_password:
                    description:
                        - For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.
                    returned: on success
                    type: str
                    sample: example-password
                internet_proxy:
                    description:
                        - Proxy URL to connect to object store.
                    returned: on success
                    type: str
                    sample: internet_proxy_example
                dbrs_policy_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DBRS policy used for backup.
                    returned: on success
                    type: str
                    sample: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_database_id": "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "type": "INCREMENTAL",
        "is_automatic": true,
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "database_size_in_tbs": 10,
        "lifecycle_state": "CREATING",
        "is_restorable": true,
        "key_store_id": "ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx",
        "key_store_wallet_name": "key_store_wallet_name_example",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_version_id": "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx",
        "retention_period_in_days": 56,
        "time_available_till": "2013-10-20T19:20:30+01:00",
        "db_version": "db_version_example",
        "size_in_tbs": 1.2,
        "backup_destination_details": {
            "type": "NFS",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "vpc_user": "vpc_user_example",
            "vpc_password": "example-password",
            "internet_proxy": "internet_proxy_example",
            "dbrs_policy_id": "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateAutonomousDatabaseBackupDetails
    from oci.database.models import UpdateAutonomousDatabaseBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousDatabaseBackupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(AutonomousDatabaseBackupHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    def get_possible_entity_types(self):
        return super(
            AutonomousDatabaseBackupHelperGen, self
        ).get_possible_entity_types() + [
            "autonomousdatabasebackup",
            "autonomousdatabasebackups",
            "databaseautonomousdatabasebackup",
            "databaseautonomousdatabasebackups",
            "autonomousdatabasebackupresource",
            "autonomousdatabasebackupsresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "autonomous_database_backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("autonomous_database_backup_id")

    def get_get_fn(self):
        return self.client.get_autonomous_database_backup

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_database_backup,
            autonomous_database_backup_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_database_backup,
            autonomous_database_backup_id=self.module.params.get(
                "autonomous_database_backup_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["autonomous_database_id", "display_name"]

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
            self.client.list_autonomous_database_backups, **kwargs
        )

    def get_create_model_class(self):
        return CreateAutonomousDatabaseBackupDetails

    def get_exclude_attributes(self):
        return ["is_long_term_backup"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_autonomous_database_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_autonomous_database_backup_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAutonomousDatabaseBackupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_autonomous_database_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_backup_id=self.module.params.get(
                    "autonomous_database_backup_id"
                ),
                update_autonomous_database_backup_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_autonomous_database_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_backup_id=self.module.params.get(
                    "autonomous_database_backup_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AutonomousDatabaseBackupHelperCustom = get_custom_class(
    "AutonomousDatabaseBackupHelperCustom"
)


class ResourceHelper(
    AutonomousDatabaseBackupHelperCustom, AutonomousDatabaseBackupHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            autonomous_database_id=dict(type="str"),
            is_long_term_backup=dict(type="bool"),
            backup_destination_details=dict(
                type="dict",
                options=dict(
                    type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "NFS",
                            "RECOVERY_APPLIANCE",
                            "OBJECT_STORE",
                            "LOCAL",
                            "DBRS",
                        ],
                    ),
                    id=dict(type="str"),
                    vpc_user=dict(type="str"),
                    vpc_password=dict(type="str", no_log=True),
                    internet_proxy=dict(type="str"),
                    dbrs_policy_id=dict(type="str"),
                ),
            ),
            retention_period_in_days=dict(type="int"),
            autonomous_database_backup_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="autonomous_database_backup",
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

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
module: oci_recovery_protected_database
short_description: Manage a ProtectedDatabase resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ProtectedDatabase resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Protected Database.
    - "This resource has the following action operations in the M(oracle.oci.oci_recovery_protected_database_actions) module: change_compartment,
      fetch_protected_database_configuration."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_unique_name:
        description:
            - The dbUniqueName of the protected database in Recovery Service. You cannot change the unique name.
            - Required for create using I(state=present).
        type: str
    database_id:
        description:
            - The OCID of the protected database.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment that contains the protected database.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    change_rate:
        description:
            - The percentage of data changes that exist in the database between successive incremental backups.
        type: float
    compression_ratio:
        description:
            - The compression ratio of the protected database. The compression ratio represents the ratio of compressed block size to expanded block size.
        type: float
    display_name:
        description:
            - The protected database name. You can change the displayName. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    database_size:
        description:
            - "The size of the protected database. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than
              5TB."
            - This parameter is updatable.
        type: str
        choices:
            - "XS"
            - "S"
            - "M"
            - "L"
            - "XL"
            - "XXL"
            - "AUTO"
    database_size_in_gbs:
        description:
            - The size of the database, in gigabytes.
            - This parameter is updatable.
        type: int
    password:
        description:
            - "Password credential which can be used to connect to Protected Database.
              It must contain at least 2 uppercase, 2 lowercase, 2 numeric and 2 special characters.
              The special characters must be underscore (_), number sign (#) or hyphen (-). The password must not contain the username \\"admin\\", regardless
              of casing."
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    protection_policy_id:
        description:
            - The OCID of the protection policy associated with the protected database.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    recovery_service_subnets:
        description:
            - List of recovery service subnet resources associated with the protected database.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            recovery_service_subnet_id:
                description:
                    - The recovery service subnet OCID.
                type: str
                required: true
    is_redo_logs_shipped:
        description:
            - The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected
              database to Recovery Service.
              Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.
            - This parameter is updatable.
        type: bool
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
              us/iaas/Content/General/Concepts/resourcetags.htm)"
            - This parameter is updatable.
        type: dict
    protected_database_id:
        description:
            - The protected database OCID.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ProtectedDatabase.
            - Use I(state=present) to create or update a ProtectedDatabase.
            - Use I(state=absent) to delete a ProtectedDatabase.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create protected_database
  oci_recovery_protected_database:
    # required
    db_unique_name: db_unique_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    password: example-password
    protection_policy_id: "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    recovery_service_subnets:
    - # required
      recovery_service_subnet_id: "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    change_rate: 3.4
    compression_ratio: 3.4
    database_size: XS
    database_size_in_gbs: 56
    is_redo_logs_shipped: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update protected_database
  oci_recovery_protected_database:
    # required
    protected_database_id: "ocid1.protecteddatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    database_size: XS
    database_size_in_gbs: 56
    password: example-password
    protection_policy_id: "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    recovery_service_subnets:
    - # required
      recovery_service_subnet_id: "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx"
    is_redo_logs_shipped: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update protected_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_recovery_protected_database:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    database_size: XS
    database_size_in_gbs: 56
    password: example-password
    protection_policy_id: "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    recovery_service_subnets:
    - # required
      recovery_service_subnet_id: "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx"
    is_redo_logs_shipped: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete protected_database
  oci_recovery_protected_database:
    # required
    protected_database_id: "ocid1.protecteddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete protected_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_recovery_protected_database:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
protected_database:
    description:
        - Details of the ProtectedDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the protected database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The protected database name. You can change the displayName. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the protected database.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        db_unique_name:
            description:
                - The dbUniqueName for the protected database in Recovery Service. You cannot change the unique name.
            returned: on success
            type: str
            sample: db_unique_name_example
        vpc_user_name:
            description:
                - The virtual private catalog (VPC) user credentials that authenticates the protected database to access Recovery Service.
            returned: on success
            type: str
            sample: vpc_user_name_example
        database_size:
            description:
                - "The size of the protected database. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater
                  than 5TB."
            returned: on success
            type: str
            sample: XS
        protection_policy_id:
            description:
                - The OCID of the protection policy associated with the protected database.
            returned: on success
            type: str
            sample: "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx"
        recovery_service_subnets:
            description:
                - List of recovery service subnet resources associated with the protected database.
            returned: on success
            type: complex
            contains:
                recovery_service_subnet_id:
                    description:
                        - Recovery Service Subnet Identifier.
                    returned: on success
                    type: str
                    sample: "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx"
                lifecycle_state:
                    description:
                        - The current state of the Recovery Service Subnet.
                    returned: on success
                    type: str
                    sample: CREATING
        database_id:
            description:
                - The OCID of the protected database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        database_size_in_gbs:
            description:
                - The size of the database in GBs, in gigabytes.
            returned: on success
            type: int
            sample: 56
        change_rate:
            description:
                - The percentage of data changes that exist in the database between successive incremental backups.
            returned: on success
            type: float
            sample: 1.2
        compression_ratio:
            description:
                - The compression ratio of the protected database. The compression ratio represents the ratio of compressed block size to expanded block size.
            returned: on success
            type: float
            sample: 1.2
        is_redo_logs_shipped:
            description:
                - The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected
                  database to Recovery Service.
                  Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups.
                  For this to be effective, additional
                  configuration is needed on client side.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - "An RFC3339 formatted datetime string that indicates the created time for a protected database. For example: '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "An RFC3339 formatted datetime string that indicates the last updated time for a protected database. For example: '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Protected Database.
            returned: on success
            type: str
            sample: CREATING
        health:
            description:
                - "Indicates the protection status of the database. Allowed values are:
                   - HEALTHY
                   - WARNING
                   - ALERT"
                - "A 'HEALTHY' status indicates that Recovery Service can ensure database recovery to any point in time within the entire recovery window. The
                  potential data loss exposure since the last backup is:
                   - Less than 10 seconds, if Real-time data protection is enabled
                   - Less than 70 minutes if Real-time data protection is disabled"
                - "A 'WARNING' status indicates that Recovery Service can ensure database recovery within the current recovery window - 1 day. The potential
                  data loss exposure since the last backup is:
                   - Greater than 10 seconds, if Real-time data protection is enabled
                   - Greater than 60 minutes, if if Real-time data protection is disabled"
                - An 'ALERT' status indicates that Recovery Service cannot recover the database within the current recovery window.
            returned: on success
            type: str
            sample: PROTECTED
        is_read_only_resource:
            description:
                - Indicates whether the protected database is created by Recovery Service or created manually.
                  Set to <b>TRUE</b> for a service-defined protected database. When you enable the OCI-managed automatic backups option for a database and set
                  Recovery Service as the backup destination, then Recovery Service creates the associated protected database resource.
                  Set to <b>FALSE</b> for a user-defined protected database.
            returned: on success
            type: bool
            sample: true
        lifecycle_details:
            description:
                - Detailed description about the current lifecycle state of the protected database. For example, it can be used to provide actionable
                  information for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        health_details:
            description:
                - A message describing the current health of the protected database.
            returned: on success
            type: str
            sample: health_details_example
        metrics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                backup_space_used_in_gbs:
                    description:
                        - Backup storage space, in gigabytes, utilized by the protected database. Oracle charges for the total storage used.
                    returned: on success
                    type: float
                    sample: 3.4
                backup_space_estimate_in_gbs:
                    description:
                        - The estimated backup storage space, in gigabytes, required to meet the recovery window goal, including foot print and backups for the
                          protected database.
                    returned: on success
                    type: float
                    sample: 3.4
                unprotected_window_in_seconds:
                    description:
                        - This is the time window when there is data loss exposure. The point after which recovery is impossible unless additional redo is
                          available.
                          This is the time we received the last backup or last redo-log shipped.
                    returned: on success
                    type: float
                    sample: 3.4
                db_size_in_gbs:
                    description:
                        - The estimated space, in gigabytes, consumed by the protected database. The database size is based on the size of the data files in the
                          catalog, and does not include archive logs.
                    returned: on success
                    type: float
                    sample: 3.4
                is_redo_logs_enabled:
                    description:
                        - The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the
                          protected database to Recovery Service.
                          Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log
                          backups.
                    returned: on success
                    type: bool
                    sample: true
                retention_period_in_days:
                    description:
                        - The maximum number of days to retain backups for a protected database.
                    returned: on success
                    type: float
                    sample: 3.4
                current_retention_period_in_seconds:
                    description:
                        - Number of seconds backups are currently retained for this database.
                    returned: on success
                    type: float
                    sample: 3.4
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`. For more information, see L(Resource Tags,https://docs.oracle.com/en-
                  us/iaas/Content/General/Concepts/resourcetags.htm)"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "db_unique_name": "db_unique_name_example",
        "vpc_user_name": "vpc_user_name_example",
        "database_size": "XS",
        "protection_policy_id": "ocid1.protectionpolicy.oc1..xxxxxxEXAMPLExxxxxx",
        "recovery_service_subnets": [{
            "recovery_service_subnet_id": "ocid1.recoveryservicesubnet.oc1..xxxxxxEXAMPLExxxxxx",
            "lifecycle_state": "CREATING"
        }],
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "database_size_in_gbs": 56,
        "change_rate": 1.2,
        "compression_ratio": 1.2,
        "is_redo_logs_shipped": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "health": "PROTECTED",
        "is_read_only_resource": true,
        "lifecycle_details": "lifecycle_details_example",
        "health_details": "health_details_example",
        "metrics": {
            "backup_space_used_in_gbs": 3.4,
            "backup_space_estimate_in_gbs": 3.4,
            "unprotected_window_in_seconds": 3.4,
            "db_size_in_gbs": 3.4,
            "is_redo_logs_enabled": true,
            "retention_period_in_days": 3.4,
            "current_retention_period_in_seconds": 3.4
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.recovery import DatabaseRecoveryClient
    from oci.recovery.models import CreateProtectedDatabaseDetails
    from oci.recovery.models import UpdateProtectedDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectedDatabaseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ProtectedDatabaseHelperGen, self).get_possible_entity_types() + [
            "recoveryserviceprotecteddatabase",
            "recoveryserviceprotecteddatabases",
            "recoveryrecoveryserviceprotecteddatabase",
            "recoveryrecoveryserviceprotecteddatabases",
            "recoveryserviceprotecteddatabaseresource",
            "recoveryserviceprotecteddatabasesresource",
            "protecteddatabase",
            "protecteddatabases",
            "recoveryprotecteddatabase",
            "recoveryprotecteddatabases",
            "protecteddatabaseresource",
            "protecteddatabasesresource",
            "recovery",
        ]

    def get_module_resource_id_param(self):
        return "protected_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("protected_database_id")

    def get_get_fn(self):
        return self.client.get_protected_database

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_protected_database, protected_database_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_protected_database,
            protected_database_id=self.module.params.get("protected_database_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "protection_policy_id"]
        )

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
            self.client.list_protected_databases, **kwargs
        )

    def get_create_model_class(self):
        return CreateProtectedDatabaseDetails

    def get_exclude_attributes(self):
        return ["password"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_protected_database,
            call_fn_args=(),
            call_fn_kwargs=dict(create_protected_database_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateProtectedDatabaseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_protected_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                protected_database_id=self.module.params.get("protected_database_id"),
                update_protected_database_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_protected_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                protected_database_id=self.module.params.get("protected_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ProtectedDatabaseHelperCustom = get_custom_class("ProtectedDatabaseHelperCustom")


class ResourceHelper(ProtectedDatabaseHelperCustom, ProtectedDatabaseHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            db_unique_name=dict(type="str"),
            database_id=dict(type="str"),
            compartment_id=dict(type="str"),
            change_rate=dict(type="float"),
            compression_ratio=dict(type="float"),
            display_name=dict(aliases=["name"], type="str"),
            database_size=dict(
                type="str", choices=["XS", "S", "M", "L", "XL", "XXL", "AUTO"]
            ),
            database_size_in_gbs=dict(type="int"),
            password=dict(type="str", no_log=True),
            protection_policy_id=dict(type="str"),
            recovery_service_subnets=dict(
                type="list",
                elements="dict",
                options=dict(
                    recovery_service_subnet_id=dict(type="str", required=True)
                ),
            ),
            is_redo_logs_shipped=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            protected_database_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="protected_database",
        service_client_class=DatabaseRecoveryClient,
        namespace="recovery",
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

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
module: oci_psql_db_system_actions
short_description: Perform actions on a DbSystem resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DbSystem resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a database system from one compartment to another. When provided, If-Match is checked against ETag values of the
      resource.
    - For I(action=failover), runs a failover operation. Optionally, specify the desired AD for regions with three ADs.
    - For I(action=reset_master_user_password), resets the database system's master password.
    - For I(action=restart_db_instance_in), restarts the running database instance node.
    - For I(action=restore), restore the database system.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the database system should be moved.
            - Required for I(action=change_compartment).
        type: str
    password_details:
        description:
            - ""
            - Required for I(action=reset_master_user_password).
        type: dict
        suboptions:
            password:
                description:
                    - The database system password.
                    - Required when password_type is 'PLAIN_TEXT'
                type: str
            password_type:
                description:
                    - The password type.
                type: str
                choices:
                    - "PLAIN_TEXT"
                    - "VAULT_SECRET"
                required: true
            secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret where the password is stored.
                    - Required when password_type is 'VAULT_SECRET'
                type: str
            secret_version:
                description:
                    - The secret version of the stored password.
                    - Required when password_type is 'VAULT_SECRET'
                type: str
    db_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database instance node. This parameter is optional.
              If not set, an existing database instance node will be chosen based on availability.
            - Required for I(action=restart_db_instance_in).
        type: str
    restart_type:
        description:
            - The restart type for the database instance.
            - Required for I(action=restart_db_instance_in).
        type: str
        choices:
            - "NORMAL"
            - "NODE_REBOOT"
    db_system_id:
        description:
            - A unique identifier for the database system.
        type: str
        aliases: ["id"]
        required: true
    backup_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database system backup.
            - Required for I(action=restore).
        type: str
    ad:
        description:
            - The preferred AD for regions with three availability domains. This parameter is optional.
              If not set, the AD will be chosen based on availability.
            - Applicable only for I(action=failover)I(action=restore).
        type: str
    action:
        description:
            - The action to perform on the DbSystem.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "failover"
            - "reset_master_user_password"
            - "restart_db_instance_in"
            - "restore"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on db_system
  oci_psql_db_system_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action failover on db_system
  oci_psql_db_system_actions:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    action: failover

    # optional
    db_instance_id: "ocid1.dbinstance.oc1..xxxxxxEXAMPLExxxxxx"
    ad: Uocm:PHX-AD-1

- name: Perform action reset_master_user_password on db_system
  oci_psql_db_system_actions:
    # required
    password_details:
      # required
      password: example-password
      password_type: PLAIN_TEXT
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    action: reset_master_user_password

- name: Perform action restart_db_instance_in on db_system
  oci_psql_db_system_actions:
    # required
    db_instance_id: "ocid1.dbinstance.oc1..xxxxxxEXAMPLExxxxxx"
    restart_type: NORMAL
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    action: restart_db_instance_in

- name: Perform action restore on db_system
  oci_psql_db_system_actions:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
    action: restore

    # optional
    ad: Uocm:PHX-AD-1

"""

RETURN = """
db_system:
    description:
        - Details of the DbSystem resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - A unique identifier for the database system. Immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the database system. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A description of the database system.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the database system.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time that the database system was created, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time that the database system was updated, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the database system.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        admin_username:
            description:
                - The database system administrator username.
            returned: on success
            type: str
            sample: admin_username_example
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
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        system_type:
            description:
                - Type of the database system.
            returned: on success
            type: str
            sample: OCI_OPTIMIZED_STORAGE
        db_version:
            description:
                - The major and minor versions of the database system software.
            returned: on success
            type: str
            sample: db_version_example
        config_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the configuration associated with the database system.
            returned: on success
            type: str
            sample: "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx"
        shape:
            description:
                - "The name of the shape for the database instance.
                  Example: `VM.Standard.E4.Flex`"
            returned: on success
            type: str
            sample: shape_example
        instance_ocpu_count:
            description:
                - The total number of OCPUs available to each database instance node.
            returned: on success
            type: int
            sample: 56
        instance_memory_size_in_gbs:
            description:
                - The total amount of memory available to each database instance node, in gigabytes.
            returned: on success
            type: int
            sample: 56
        instance_count:
            description:
                - Count of instances, or nodes, in the database system.
            returned: on success
            type: int
            sample: 56
        instances:
            description:
                - The list of instances, or nodes, in the database system.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - A unique identifier for the database instance node. Immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - A user-friendly display name for the database instance node. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Description of the database instance node.
                    returned: on success
                    type: str
                    sample: description_example
                availability_domain:
                    description:
                        - The availability domain in which the database instance node is located.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                lifecycle_state:
                    description:
                        - The current state of the database instance node.
                    returned: on success
                    type: str
                    sample: CREATING
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                time_created:
                    description:
                        - The date and time that the database instance node was created, expressed in
                          L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time that the database instance node was updated, expressed in
                          L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        storage_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                system_type:
                    description:
                        - Type of the database system.
                    returned: on success
                    type: str
                    sample: OCI_OPTIMIZED_STORAGE
                is_regionally_durable:
                    description:
                        - Specifies if the block volume used for the database system is regional or AD-local.
                          If not specified, it will be set to false.
                          If `isRegionallyDurable` is set to true, `availabilityDomain` should not be specified.
                          If `isRegionallyDurable` is set to false, `availabilityDomain` must be specified.
                    returned: on success
                    type: bool
                    sample: true
                availability_domain:
                    description:
                        - Specifies the availability domain of AD-local storage.
                          If `isRegionallyDurable` is set to true, `availabilityDomain` should not be specified.
                          If `isRegionallyDurable` is set to false, `availabilityDomain` must be specified.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                iops:
                    description:
                        - Guaranteed input/output storage requests per second (IOPS) available to the database system.
                    returned: on success
                    type: int
                    sample: 56
        network_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the customer subnet associated with the database
                          system.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                primary_db_endpoint_private_ip:
                    description:
                        - Private IP in customer subnet. The value is optional.
                          If the IP is not provided, the IP will be chosen from the available IP addresses from the specified subnet.
                    returned: on success
                    type: str
                    sample: primary_db_endpoint_private_ip_example
                nsg_ids:
                    description:
                        - List of customer Network Security Group L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated
                          with the database system.
                    returned: on success
                    type: list
                    sample: []
        management_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                maintenance_window_start:
                    description:
                        - The start of the maintenance window.
                    returned: on success
                    type: str
                    sample: maintenance_window_start_example
                backup_policy:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        days_of_the_month:
                            description:
                                - Day of the month when the backup should start.
                                  To ensure that the backup runs monthly, the latest day of the month that you can use to schedule a backup is the the 28th day.
                            returned: on success
                            type: list
                            sample: []
                        kind:
                            description:
                                - The kind of backup policy.
                            returned: on success
                            type: str
                            sample: DAILY
                        retention_days:
                            description:
                                - How many days the data should be stored after the database system deletion.
                            returned: on success
                            type: int
                            sample: 56
                        days_of_the_week:
                            description:
                                - The day of the week that the backup starts.
                            returned: on success
                            type: list
                            sample: []
                        backup_start:
                            description:
                                - Hour of the day when the backup starts.
                            returned: on success
                            type: str
                            sample: backup_start_example
        source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                backup_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database system backup.
                    returned: on success
                    type: str
                    sample: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
                is_having_restore_config_overrides:
                    description:
                        - Deprecated. Don't use.
                    returned: on success
                    type: bool
                    sample: true
                source_type:
                    description:
                        - The source descriminator.
                    returned: on success
                    type: str
                    sample: BACKUP
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "admin_username": "admin_username_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "system_type": "OCI_OPTIMIZED_STORAGE",
        "db_version": "db_version_example",
        "config_id": "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx",
        "shape": "shape_example",
        "instance_ocpu_count": 56,
        "instance_memory_size_in_gbs": 56,
        "instance_count": 56,
        "instances": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "availability_domain": "Uocm:PHX-AD-1",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        }],
        "storage_details": {
            "system_type": "OCI_OPTIMIZED_STORAGE",
            "is_regionally_durable": true,
            "availability_domain": "Uocm:PHX-AD-1",
            "iops": 56
        },
        "network_details": {
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "primary_db_endpoint_private_ip": "primary_db_endpoint_private_ip_example",
            "nsg_ids": []
        },
        "management_policy": {
            "maintenance_window_start": "maintenance_window_start_example",
            "backup_policy": {
                "days_of_the_month": [],
                "kind": "DAILY",
                "retention_days": 56,
                "days_of_the_week": [],
                "backup_start": "backup_start_example"
            }
        },
        "source": {
            "backup_id": "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx",
            "is_having_restore_config_overrides": true,
            "source_type": "BACKUP"
        }
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
    from oci.psql import PostgresqlClient
    from oci.psql.models import ChangeDbSystemCompartmentDetails
    from oci.psql.models import FailoverDbSystemDetails
    from oci.psql.models import ResetMasterUserPasswordDetails
    from oci.psql.models import RestartDbInstanceInDbSystemDetails
    from oci.psql.models import RestoreDbSystemDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PsqlDbSystemActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        failover
        reset_master_user_password
        restart_db_instance_in
        restore
    """

    @staticmethod
    def get_module_resource_id_param():
        return "db_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_system_id")

    def get_get_fn(self):
        return self.client.get_db_system

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system,
            db_system_id=self.module.params.get("db_system_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDbSystemCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_db_system_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                change_db_system_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def failover(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, FailoverDbSystemDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.failover_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                failover_db_system_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def reset_master_user_password(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResetMasterUserPasswordDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reset_master_user_password,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                reset_master_user_password_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def restart_db_instance_in(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestartDbInstanceInDbSystemDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restart_db_instance_in_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                restart_db_instance_in_db_system_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def restore(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestoreDbSystemDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restore_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                restore_db_system_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


PsqlDbSystemActionsHelperCustom = get_custom_class("PsqlDbSystemActionsHelperCustom")


class ResourceHelper(PsqlDbSystemActionsHelperCustom, PsqlDbSystemActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            password_details=dict(
                type="dict",
                no_log=False,
                options=dict(
                    password=dict(type="str", no_log=True),
                    password_type=dict(
                        type="str",
                        required=True,
                        choices=["PLAIN_TEXT", "VAULT_SECRET"],
                    ),
                    secret_id=dict(type="str"),
                    secret_version=dict(type="str", no_log=True),
                ),
            ),
            db_instance_id=dict(type="str"),
            restart_type=dict(type="str", choices=["NORMAL", "NODE_REBOOT"]),
            db_system_id=dict(aliases=["id"], type="str", required=True),
            backup_id=dict(type="str"),
            ad=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "failover",
                    "reset_master_user_password",
                    "restart_db_instance_in",
                    "restore",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_system",
        service_client_class=PostgresqlClient,
        namespace="psql",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

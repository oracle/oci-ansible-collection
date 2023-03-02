#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_database_management_managed_database_actions
short_description: Perform actions on a ManagedDatabase resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagedDatabase resource in Oracle Cloud Infrastructure
    - For I(action=clone_sql_tuning_task), clones and runs a SQL tuning task in the database.
    - For I(action=drop_sql_tuning_task), drops a SQL tuning task and its related results from the database.
    - For I(action=start_sql_tuning_task), starts a SQL tuning task for a given set of SQL statements from the active session history top SQL statements.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    original_task_id:
        description:
            - The identifier of the SQL tuning task being cloned. This is not the
              L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
              It can be retrieved from the following endpoint
              L(ListSqlTuningAdvisorTasks,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database-
              management/latest/ManagedDatabase/ListSqlTuningAdvisorTasks).
            - Required for I(action=clone_sql_tuning_task).
        type: int
    task_id:
        description:
            - The identifier of the SQL tuning task being dropped. This is not the
              L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
              It can be retrieved from the following endpoint
              L(ListSqlTuningAdvisorTasks,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database-
              management/latest/ManagedDatabase/ListSqlTuningAdvisorTasks).
            - Required for I(action=drop_sql_tuning_task).
        type: int
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        aliases: ["id"]
        required: true
    task_name:
        description:
            - The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.
            - Required for I(action=clone_sql_tuning_task), I(action=start_sql_tuning_task).
        type: str
    task_description:
        description:
            - The description of the SQL tuning task.
            - Applicable only for I(action=clone_sql_tuning_task)I(action=start_sql_tuning_task).
        type: str
    credential_details:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            password_secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Secret
                      where the database password is stored.
                    - Required when sql_tuning_task_credential_type is 'SECRET'
                type: str
            sql_tuning_task_credential_type:
                description:
                    - The type of credential for the SQL tuning task.
                type: str
                choices:
                    - "SECRET"
                    - "PASSWORD"
                required: true
            username:
                description:
                    - The user name used to connect to the database.
                type: str
                required: true
            role:
                description:
                    - The role of the database user.
                type: str
                choices:
                    - "NORMAL"
                    - "SYSDBA"
                required: true
            password:
                description:
                    - The database user's password encoded using BASE64 scheme.
                    - Required when sql_tuning_task_credential_type is 'PASSWORD'
                type: str
    total_time_limit_in_minutes:
        description:
            - The time limit for running the SQL tuning task.
            - Required for I(action=start_sql_tuning_task).
        type: int
    scope:
        description:
            - The scope for the SQL tuning task. For LIMITED scope, the SQL profile recommendation
              is excluded, so the task is executed faster. For COMPREHENSIVE scope, the SQL profile recommendation
              is included.
            - Required for I(action=start_sql_tuning_task).
        type: str
        choices:
            - "LIMITED"
            - "COMPREHENSIVE"
    statement_time_limit_in_minutes:
        description:
            - The time limit per SQL statement (in minutes). This is for a task with the COMPREHENSIVE scope.
              The time limit per SQL statement should not be more than the total time limit.
            - Applicable only for I(action=start_sql_tuning_task).
        type: int
    sql_tuning_set:
        description:
            - ""
            - Applicable only for I(action=start_sql_tuning_task).
        type: dict
        suboptions:
            name:
                description:
                    - The name of the SQL tuning set.
                type: str
                required: true
            owner:
                description:
                    - The owner of the SQL tuning set.
                type: str
                required: true
    sql_details:
        description:
            - The details of the SQL statement on which tuning is performed.
              To obtain the details of the SQL statement, you must provide either the sqlTuningSet
              or the tuple of sqlDetails/timeStarted/timeEnded.
            - Applicable only for I(action=start_sql_tuning_task).
        type: list
        elements: dict
        suboptions:
            sql_id:
                description:
                    - The identifier of a SQL statement.
                type: str
                required: true
    time_started:
        description:
            - The start time of the period in which SQL statements are running.
            - Applicable only for I(action=start_sql_tuning_task).
        type: str
    time_ended:
        description:
            - The end time of the period in which SQL statements are running.
            - Applicable only for I(action=start_sql_tuning_task).
        type: str
    action:
        description:
            - The action to perform on the ManagedDatabase.
        type: str
        required: true
        choices:
            - "clone_sql_tuning_task"
            - "drop_sql_tuning_task"
            - "start_sql_tuning_task"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action clone_sql_tuning_task on managed_database
  oci_database_management_managed_database_actions:
    # required
    original_task_id: 56
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    task_name: task_name_example
    credential_details:
      # required
      password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
      sql_tuning_task_credential_type: SECRET
      username: username_example
      role: NORMAL
    action: clone_sql_tuning_task

    # optional
    task_description: task_description_example

- name: Perform action drop_sql_tuning_task on managed_database
  oci_database_management_managed_database_actions:
    # required
    task_id: 56
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    credential_details:
      # required
      password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
      sql_tuning_task_credential_type: SECRET
      username: username_example
      role: NORMAL
    action: drop_sql_tuning_task

- name: Perform action start_sql_tuning_task on managed_database
  oci_database_management_managed_database_actions:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    task_name: task_name_example
    credential_details:
      # required
      password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
      sql_tuning_task_credential_type: SECRET
      username: username_example
      role: NORMAL
    total_time_limit_in_minutes: 56
    scope: LIMITED
    action: start_sql_tuning_task

    # optional
    task_description: task_description_example
    statement_time_limit_in_minutes: 56
    sql_tuning_set:
      # required
      name: name_example
      owner: owner_example
    sql_details:
    - # required
      sql_id: "ocid1.sql.oc1..xxxxxxEXAMPLExxxxxx"
    time_started: time_started_example
    time_ended: time_ended_example

"""

RETURN = """
managed_database:
    description:
        - Details of the ManagedDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the Managed Database.
            returned: on success
            type: str
            sample: name_example
        database_type:
            description:
                - The type of Oracle Database installation.
            returned: on success
            type: str
            sample: EXTERNAL_SIDB
        database_sub_type:
            description:
                - The subtype of the Oracle Database. Indicates whether the database is a Container Database,
                  Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.
            returned: on success
            type: str
            sample: CDB
        deployment_type:
            description:
                - The infrastructure used to deploy the Oracle Database.
            returned: on success
            type: str
            sample: ONPREMISE
        management_option:
            description:
                - The management option used when enabling Database Management.
            returned: on success
            type: str
            sample: BASIC
        workload_type:
            description:
                - The workload type of the Autonomous Database.
            returned: on success
            type: str
            sample: OLTP
        is_cluster:
            description:
                - Indicates whether the Oracle Database is part of a cluster.
            returned: on success
            type: bool
            sample: true
        parent_container_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the parent Container Database
                  if Managed Database is a Pluggable Database.
            returned: on success
            type: str
            sample: "ocid1.parentcontainer.oc1..xxxxxxEXAMPLExxxxxx"
        managed_database_groups:
            description:
                - A list of Managed Database Groups that the Managed Database belongs to.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - The name of the Managed Database Group.
                    returned: on success
                    type: str
                    sample: name_example
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the Managed Database
                          Group resides.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external
                  DB system that this Managed Database is part of.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        storage_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the storage DB system.
            returned: on success
            type: str
            sample: "ocid1.storagesystem.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the Managed Database was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        database_status:
            description:
                - The status of the Oracle Database. Indicates whether the status of the database
                  is UP, DOWN, or UNKNOWN at the current time.
            returned: on success
            type: str
            sample: UP
        parent_container_name:
            description:
                - The name of the parent Container Database.
            returned: on success
            type: str
            sample: parent_container_name_example
        parent_container_compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
                  in which the parent Container Database resides, if the Managed Database
                  is a Pluggable Database (PDB).
            returned: on success
            type: str
            sample: "ocid1.parentcontainercompartment.oc1..xxxxxxEXAMPLExxxxxx"
        instance_count:
            description:
                - The number of Oracle Real Application Clusters (Oracle RAC) database instances.
            returned: on success
            type: int
            sample: 56
        instance_details:
            description:
                - The details of the Oracle Real Application Clusters (Oracle RAC) database instances.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The ID of the Oracle RAC database instance.
                    returned: on success
                    type: int
                    sample: 56
                name:
                    description:
                        - The name of the Oracle RAC database instance.
                    returned: on success
                    type: str
                    sample: name_example
                host_name:
                    description:
                        - The name of the host of the Oracle RAC database instance.
                    returned: on success
                    type: str
                    sample: host_name_example
                status:
                    description:
                        - The status of the Oracle RAC database instance.
                    returned: on success
                    type: str
                    sample: UP
        pdb_count:
            description:
                - The number of PDBs in the Container Database.
            returned: on success
            type: int
            sample: 56
        pdb_status:
            description:
                - The status of the PDB in the Container Database.
            returned: on success
            type: complex
            contains:
                status:
                    description:
                        - The status of the PDBs with this count.
                    returned: on success
                    type: str
                    sample: UP
                count:
                    description:
                        - The number of PDBs with this status.
                    returned: on success
                    type: int
                    sample: 56
        additional_details:
            description:
                - "The additional details specific to a type of database defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "database_type": "EXTERNAL_SIDB",
        "database_sub_type": "CDB",
        "deployment_type": "ONPREMISE",
        "management_option": "BASIC",
        "workload_type": "OLTP",
        "is_cluster": true,
        "parent_container_id": "ocid1.parentcontainer.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_database_groups": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "storage_system_id": "ocid1.storagesystem.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "database_status": "UP",
        "parent_container_name": "parent_container_name_example",
        "parent_container_compartment_id": "ocid1.parentcontainercompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_count": 56,
        "instance_details": [{
            "id": 56,
            "name": "name_example",
            "host_name": "host_name_example",
            "status": "UP"
        }],
        "pdb_count": 56,
        "pdb_status": [{
            "status": "UP",
            "count": 56
        }],
        "additional_details": {}
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
    from oci.database_management import SqlTuningClient
    from oci.database_management.models import CloneSqlTuningTaskDetails
    from oci.database_management.models import DropSqlTuningTaskDetails
    from oci.database_management.models import StartSqlTuningTaskDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedDatabaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        clone_sql_tuning_task
        drop_sql_tuning_task
        start_sql_tuning_task
    """

    @staticmethod
    def get_module_resource_id_param():
        return "managed_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_database_id")

    def get_get_fn(self):
        return self.client.get_managed_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_database,
            managed_database_id=self.module.params.get("managed_database_id"),
        )

    def clone_sql_tuning_task(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CloneSqlTuningTaskDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.clone_sql_tuning_task,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                clone_sql_tuning_task_details=action_details,
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

    def drop_sql_tuning_task(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DropSqlTuningTaskDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.drop_sql_tuning_task,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                drop_sql_tuning_task_details=action_details,
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

    def start_sql_tuning_task(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StartSqlTuningTaskDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_sql_tuning_task,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                start_sql_tuning_task_details=action_details,
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


ManagedDatabaseActionsHelperCustom = get_custom_class(
    "ManagedDatabaseActionsHelperCustom"
)


class ResourceHelper(
    ManagedDatabaseActionsHelperCustom, ManagedDatabaseActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            original_task_id=dict(type="int"),
            task_id=dict(type="int"),
            managed_database_id=dict(aliases=["id"], type="str", required=True),
            task_name=dict(type="str"),
            task_description=dict(type="str"),
            credential_details=dict(
                type="dict",
                required=True,
                options=dict(
                    password_secret_id=dict(type="str"),
                    sql_tuning_task_credential_type=dict(
                        type="str", required=True, choices=["SECRET", "PASSWORD"]
                    ),
                    username=dict(type="str", required=True),
                    role=dict(type="str", required=True, choices=["NORMAL", "SYSDBA"]),
                    password=dict(type="str", no_log=True),
                ),
            ),
            total_time_limit_in_minutes=dict(type="int"),
            scope=dict(type="str", choices=["LIMITED", "COMPREHENSIVE"]),
            statement_time_limit_in_minutes=dict(type="int"),
            sql_tuning_set=dict(
                type="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    owner=dict(type="str", required=True),
                ),
            ),
            sql_details=dict(
                type="list",
                elements="dict",
                options=dict(sql_id=dict(type="str", required=True)),
            ),
            time_started=dict(type="str"),
            time_ended=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "clone_sql_tuning_task",
                    "drop_sql_tuning_task",
                    "start_sql_tuning_task",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_database",
        service_client_class=SqlTuningClient,
        namespace="database_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

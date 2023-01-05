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
module: oci_database_management_managed_database_group_actions
short_description: Perform actions on a ManagedDatabaseGroup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagedDatabaseGroup resource in Oracle Cloud Infrastructure
    - For I(action=add_managed_database), adds a Managed Database to a specific Managed Database Group.
      After the database is added, it will be included in the
      management activities performed on the Managed Database Group.
    - For I(action=change_compartment), moves a Managed Database Group to a different compartment.
      The destination compartment must not have a Managed Database Group
      with the same name.
    - For I(action=remove_managed_database), removes a Managed Database from a Managed Database Group. Any management
      activities that are currently running on this database will continue to
      run to completion. However, any activities scheduled to run in the future
      will not be performed on this database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              compartment to which the Managed Database Group should be moved.
            - Required for I(action=change_compartment).
        type: str
    managed_database_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group.
        type: str
        aliases: ["id"]
        required: true
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
            - Required for I(action=add_managed_database), I(action=remove_managed_database).
        type: str
    action:
        description:
            - The action to perform on the ManagedDatabaseGroup.
        type: str
        required: true
        choices:
            - "add_managed_database"
            - "change_compartment"
            - "remove_managed_database"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action add_managed_database on managed_database_group
  oci_database_management_managed_database_group_actions:
    # required
    managed_database_group_id: "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx"
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_managed_database

- name: Perform action change_compartment on managed_database_group
  oci_database_management_managed_database_group_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    managed_database_group_id: "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action remove_managed_database on managed_database_group
  oci_database_management_managed_database_group_actions:
    # required
    managed_database_group_id: "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx"
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_managed_database

"""

RETURN = """
managed_database_group:
    description:
        - Details of the ManagedDatabaseGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the Managed Database Group.
            returned: on success
            type: str
            sample: name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The information specified by the user about the Managed Database Group.
            returned: on success
            type: str
            sample: description_example
        managed_databases:
            description:
                - A list of Managed Databases in the Managed Database Group.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - The name of the Managed Database.
                    returned: on success
                    type: str
                    sample: name_example
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the Managed Database
                          resides.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                deployment_type:
                    description:
                        - The infrastructure used to deploy the Oracle Database.
                    returned: on success
                    type: str
                    sample: ONPREMISE
                workload_type:
                    description:
                        - The workload type of the Autonomous Database.
                    returned: on success
                    type: str
                    sample: OLTP
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
                time_added:
                    description:
                        - The date and time the Managed Database was added to the group.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the Managed Database Group.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the Managed Database Group was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the Managed Database Group was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "name": "name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "managed_databases": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "deployment_type": "ONPREMISE",
            "workload_type": "OLTP",
            "database_type": "EXTERNAL_SIDB",
            "database_sub_type": "CDB",
            "time_added": "2013-10-20T19:20:30+01:00"
        }],
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.database_management import DbManagementClient
    from oci.database_management.models import (
        AddManagedDatabaseToManagedDatabaseGroupDetails,
    )
    from oci.database_management.models import (
        ChangeManagedDatabaseGroupCompartmentDetails,
    )
    from oci.database_management.models import (
        RemoveManagedDatabaseFromManagedDatabaseGroupDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedDatabaseGroupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_managed_database
        change_compartment
        remove_managed_database
    """

    @staticmethod
    def get_module_resource_id_param():
        return "managed_database_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_database_group_id")

    def get_get_fn(self):
        return self.client.get_managed_database_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_database_group,
            managed_database_group_id=self.module.params.get(
                "managed_database_group_id"
            ),
        )

    def add_managed_database(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddManagedDatabaseToManagedDatabaseGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_managed_database_to_managed_database_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_group_id=self.module.params.get(
                    "managed_database_group_id"
                ),
                add_managed_database_to_managed_database_group_details=action_details,
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeManagedDatabaseGroupCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_managed_database_group_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_group_id=self.module.params.get(
                    "managed_database_group_id"
                ),
                change_managed_database_group_compartment_details=action_details,
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

    def remove_managed_database(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveManagedDatabaseFromManagedDatabaseGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_managed_database_from_managed_database_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_group_id=self.module.params.get(
                    "managed_database_group_id"
                ),
                remove_managed_database_from_managed_database_group_details=action_details,
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


ManagedDatabaseGroupActionsHelperCustom = get_custom_class(
    "ManagedDatabaseGroupActionsHelperCustom"
)


class ResourceHelper(
    ManagedDatabaseGroupActionsHelperCustom, ManagedDatabaseGroupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            managed_database_group_id=dict(aliases=["id"], type="str", required=True),
            managed_database_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_managed_database",
                    "change_compartment",
                    "remove_managed_database",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_database_group",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

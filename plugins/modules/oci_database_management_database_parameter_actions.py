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
module: oci_database_management_database_parameter_actions
short_description: Perform actions on a DatabaseParameter resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DatabaseParameter resource in Oracle Cloud Infrastructure
    - "For I(action=change), changes database parameter values. There are two kinds of database
      parameters:
      - Dynamic parameters: They can be changed for the current Oracle
      Database instance. The changes take effect immediately.
      - Static parameters: They cannot be changed for the current instance.
      You must change these parameters and then restart the database before
      changes take effect.
      **Note:** If the instance is started using a text initialization
      parameter file, the parameter changes are applicable only for the
      current instance. You must update them manually to be passed to
      a future instance."
    - For I(action=reset), resets database parameter values to their default or startup values.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    change_parameters:
        description:
            - A list of database parameters and their values.
            - Required for I(action=change).
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - The parameter name.
                type: str
                required: true
            value:
                description:
                    - The parameter value.
                type: str
                required: true
            update_comment:
                description:
                    - A comment string to associate with the change in parameter value.
                      It cannot contain control characters or a line break.
                type: str
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        aliases: ["id"]
        required: true
    credentials:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            user_name:
                description:
                    - The database user name used to perform management activity.
                type: str
            password:
                description:
                    - The password for the database user name.
                type: str
            secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the user password.
                type: str
            role:
                description:
                    - The role of the database user. Indicates whether the database user is a normal user or sysdba.
                type: str
                choices:
                    - "NORMAL"
                    - "SYSDBA"
    scope:
        description:
            - The clause used to specify when the parameter change takes effect.
            - Use `MEMORY` to make the change in memory and affect it immediately.
              Use `SPFILE` to make the change in the server parameter file. The
              change takes effect when the database is next shut down and started
              up again. Use `BOTH` to make the change in memory and in the server
              parameter file. The change takes effect immediately and persists
              after the database is shut down and started up again.
        type: str
        choices:
            - "MEMORY"
            - "SPFILE"
            - "BOTH"
        required: true
    reset_parameters:
        description:
            - A list of database parameter names.
            - Required for I(action=reset).
        type: list
        elements: str
    action:
        description:
            - The action to perform on the DatabaseParameter.
        type: str
        required: true
        choices:
            - "change"
            - "reset"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change on database_parameter
  oci_database_management_database_parameter_actions:
    # required
    change_parameters:
    - # required
      name: name_example
      value: value_example

      # optional
      update_comment: update_comment_example
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    credentials:
      # optional
      user_name: user_name_example
      password: example-password
      secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
      role: NORMAL
    scope: MEMORY
    action: change

- name: Perform action reset on database_parameter
  oci_database_management_database_parameter_actions:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    credentials:
      # optional
      user_name: user_name_example
      password: example-password
      secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
      role: NORMAL
    scope: MEMORY
    reset_parameters: [ "reset_parameters_example" ]
    action: reset

"""

RETURN = """
update_database_parameters_result:
    description:
        - Details of the DatabaseParameter resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        status:
            description:
                - A map with the parameter name as key and its update status as value.
            returned: on success
            type: complex
            contains:
                status:
                    description:
                        - The status of the parameter update.
                    returned: on success
                    type: str
                    sample: SUCCEEDED
                error_code:
                    description:
                        - An error code that defines the failure or `null` if the parameter
                          was updated successfully.
                    returned: on success
                    type: str
                    sample: error_code_example
                error_message:
                    description:
                        - The error message indicating the reason for failure or `null` if
                          the parameter was updated successfully.
                    returned: on success
                    type: str
                    sample: error_message_example
    sample: {
        "status": {
            "status": "SUCCEEDED",
            "error_code": "error_code_example",
            "error_message": "error_message_example"
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
    from oci.database_management import DbManagementClient
    from oci.database_management.models import ChangeDatabaseParametersDetails
    from oci.database_management.models import ResetDatabaseParametersDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseParameterActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change
        reset
    """

    @staticmethod
    def get_module_resource_id_param():
        return "managed_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_database_id")

    def change(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDatabaseParametersDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_database_parameters,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                change_database_parameters_details=action_details,
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

    def reset(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResetDatabaseParametersDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reset_database_parameters,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                reset_database_parameters_details=action_details,
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


DatabaseParameterActionsHelperCustom = get_custom_class(
    "DatabaseParameterActionsHelperCustom"
)


class ResourceHelper(
    DatabaseParameterActionsHelperCustom, DatabaseParameterActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            change_parameters=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    value=dict(type="str", required=True),
                    update_comment=dict(type="str"),
                ),
            ),
            managed_database_id=dict(aliases=["id"], type="str", required=True),
            credentials=dict(
                type="dict",
                required=True,
                options=dict(
                    user_name=dict(type="str"),
                    password=dict(type="str", no_log=True),
                    secret_id=dict(type="str"),
                    role=dict(type="str", choices=["NORMAL", "SYSDBA"]),
                ),
            ),
            scope=dict(type="str", required=True, choices=["MEMORY", "SPFILE", "BOTH"]),
            reset_parameters=dict(type="list", elements="str"),
            action=dict(type="str", required=True, choices=["change", "reset"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_parameter",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

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
module: oci_database_tools_connection_actions
short_description: Perform actions on a DatabaseToolsConnection resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DatabaseToolsConnection resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the specified Database Tools connection to a different compartment in the same tenancy.
      For information about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=validate), validates the Database Tools connection details by establishing a connection to the database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to move the `DatabaseToolsConnection` to.
            - Required for I(action=change_compartment).
        type: str
    database_tools_connection_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a Database Tools connection.
        type: str
        aliases: ["id"]
        required: true
    type:
        description:
            - The `DatabaseToolsConnection` type.
            - Required for I(action=validate).
        type: str
        choices:
            - "ORACLE_DATABASE"
            - "MYSQL"
    action:
        description:
            - The action to perform on the DatabaseToolsConnection.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "validate"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on database_tools_connection
  oci_database_tools_connection_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_tools_connection_id: "ocid1.databasetoolsconnection.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action validate on database_tools_connection with type = ORACLE_DATABASE
  oci_database_tools_connection_actions:
    # required
    type: ORACLE_DATABASE

- name: Perform action validate on database_tools_connection with type = MYSQL
  oci_database_tools_connection_actions:
    # required
    type: MYSQL

"""

RETURN = """
database_tools_connection:
    description:
        - Details of the DatabaseToolsConnection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Tools connection.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the Database Tools
                  connection.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the Database Tools connection.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, this message can be used to provide actionable information for a resource
                  in the Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time the Database Tools connection was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the DatabaseToolsConnection was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        type:
            description:
                - The Database Tools connection type.
            returned: on success
            type: str
            sample: ORACLE_DATABASE
        related_resource:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                entity_type:
                    description:
                        - The resource entity type.
                    returned: on success
                    type: str
                    sample: MYSQLDBSYSTEM
                identifier:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the related resource.
                    returned: on success
                    type: str
                    sample: identifier_example
        connection_string:
            description:
                - The connection string used to connect to the MySQL Server.
            returned: on success
            type: str
            sample: connection_string_example
        user_name:
            description:
                - The user name.
            returned: on success
            type: str
            sample: user_name_example
        user_password:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                value_type:
                    description:
                        - The value type of the user password.
                    returned: on success
                    type: str
                    sample: SECRETID
                secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the user password.
                    returned: on success
                    type: str
                    sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        advanced_properties:
            description:
                - The advanced connection properties key-value pair (for example, `sslMode`).
            returned: on success
            type: dict
            sample: {}
        key_stores:
            description:
                - The CA certificate to verify the server's certificate and
                  the client private key and associated certificate required for client authentication.
            returned: on success
            type: complex
            contains:
                key_store_type:
                    description:
                        - The key store type.
                    returned: on success
                    type: str
                    sample: CLIENT_CERTIFICATE_PEM
                key_store_content:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        value_type:
                            description:
                                - The value type of the key store content.
                            returned: on success
                            type: str
                            sample: SECRETID
                        secret_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the key store.
                            returned: on success
                            type: str
                            sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
                key_store_password:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        value_type:
                            description:
                                - The value type of the key store password.
                            returned: on success
                            type: str
                            sample: SECRETID
                        secret_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the key store
                                  password.
                            returned: on success
                            type: str
                            sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Tools private endpoint used to access the
                  database in the customer VCN.
            returned: on success
            type: str
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "system_tags": {},
        "type": "ORACLE_DATABASE",
        "related_resource": {
            "entity_type": "MYSQLDBSYSTEM",
            "identifier": "identifier_example"
        },
        "connection_string": "connection_string_example",
        "user_name": "user_name_example",
        "user_password": {
            "value_type": "SECRETID",
            "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "advanced_properties": {},
        "key_stores": [{
            "key_store_type": "CLIENT_CERTIFICATE_PEM",
            "key_store_content": {
                "value_type": "SECRETID",
                "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "key_store_password": {
                "value_type": "SECRETID",
                "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
            }
        }],
        "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.database_tools import DatabaseToolsClient
    from oci.database_tools.models import (
        ChangeDatabaseToolsConnectionCompartmentDetails,
    )
    from oci.database_tools.models import ValidateDatabaseToolsConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseToolsConnectionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        validate
    """

    @staticmethod
    def get_module_resource_id_param():
        return "database_tools_connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_tools_connection_id")

    def get_get_fn(self):
        return self.client.get_database_tools_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_tools_connection,
            database_tools_connection_id=self.module.params.get(
                "database_tools_connection_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDatabaseToolsConnectionCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_database_tools_connection_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_tools_connection_id=self.module.params.get(
                    "database_tools_connection_id"
                ),
                change_database_tools_connection_compartment_details=action_details,
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

    def validate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ValidateDatabaseToolsConnectionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.validate_database_tools_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_tools_connection_id=self.module.params.get(
                    "database_tools_connection_id"
                ),
                validate_database_tools_connection_details=action_details,
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


DatabaseToolsConnectionActionsHelperCustom = get_custom_class(
    "DatabaseToolsConnectionActionsHelperCustom"
)


class ResourceHelper(
    DatabaseToolsConnectionActionsHelperCustom, DatabaseToolsConnectionActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            database_tools_connection_id=dict(
                aliases=["id"], type="str", required=True
            ),
            type=dict(type="str", choices=["ORACLE_DATABASE", "MYSQL"]),
            action=dict(
                type="str", required=True, choices=["change_compartment", "validate"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_tools_connection",
        service_client_class=DatabaseToolsClient,
        namespace="database_tools",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

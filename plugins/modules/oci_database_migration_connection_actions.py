#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_database_migration_connection_actions
short_description: Perform actions on a Connection resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Connection resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), used to change the Database Connection compartment.
    - For I(action=connection_diagnostics), perform connection test for a database connection.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for I(action=change_compartment).
        type: str
    connection_id:
        description:
            - The OCID of the database connection.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Connection.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "connection_diagnostics"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on connection
  oci_database_migration_connection_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action connection_diagnostics on connection
  oci_database_migration_connection_actions:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    action: connection_diagnostics

"""

RETURN = """
connection:
    description:
        - Details of the Connection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        host:
            description:
                - The IP Address of the host.
            returned: on success
            type: str
            sample: host_example
        port:
            description:
                - The port to be used for the connection.
            returned: on success
            type: int
            sample: 56
        database_name:
            description:
                - The name of the database being referenced.
            returned: on success
            type: str
            sample: database_name_example
        security_protocol:
            description:
                - Security Protocol to be used for the connection.
            returned: on success
            type: str
            sample: PLAIN
        ssl_mode:
            description:
                - SSL mode to be used for the connection.
            returned: on success
            type: str
            sample: DISABLED
        additional_attributes:
            description:
                - An array of name-value pair attribute entries.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the property entry.
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - The value of the property entry.
                    returned: on success
                    type: str
                    sample: value_example
        db_system_id:
            description:
                - The OCID of the database system being referenced.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        connection_type:
            description:
                - Defines the type of connection. For example, ORACLE.
            returned: on success
            type: str
            sample: MYSQL
        id:
            description:
                - The OCID of the connection being referenced.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A user-friendly description. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see Resource Tags. Example: {\\"Department\\": \\"Finance\\"}"
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        lifecycle_state:
            description:
                - The Connection's current lifecycle state.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - The message describing the current state of the connection's lifecycle in detail.
                  For example, can be used to provide actionable information for a connection in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time when this resource was created.
                  An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when this resource was updated.
                  An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vault_id:
            description:
                - OCI resource ID.
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        key_id:
            description:
                - The OCID of the key used in cryptographic operations.
            returned: on success
            type: str
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - OCI resource ID.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        ingress_ips:
            description:
                - List of ingress IP addresses from where to connect to this connection's privateIp.
            returned: on success
            type: complex
            contains:
                ingress_ip:
                    description:
                        - A Private Endpoint IPv4 or IPv6 Address created in the customer's subnet.
                    returned: on success
                    type: str
                    sample: ingress_ip_example
        nsg_ids:
            description:
                - An array of Network Security Group OCIDs used to define network access for Connections.
            returned: on success
            type: list
            sample: []
        username:
            description:
                - The username (credential) used when creating or updating this resource.
            returned: on success
            type: str
            sample: username_example
        password:
            description:
                - The password (credential) used when creating or updating this resource.
            returned: on success
            type: str
            sample: example-password
        replication_username:
            description:
                - The username (credential) used when creating or updating this resource.
            returned: on success
            type: str
            sample: replication_username_example
        replication_password:
            description:
                - The password (credential) used when creating or updating this resource.
            returned: on success
            type: str
            sample: example-password
        secret_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        technology_type:
            description:
                - "The type of MySQL source or target connection.
                  Example: OCI_MYSQL represents OCI MySQL HeatWave Database Service"
            returned: on success
            type: str
            sample: AMAZON_AURORA_MYSQL
        connection_string:
            description:
                - Connect descriptor or Easy Connect Naming method used to connect to a database.
            returned: on success
            type: str
            sample: connection_string_example
        database_id:
            description:
                - The OCID of the database being referenced.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        ssh_host:
            description:
                - Name of the host the SSH key is valid for.
            returned: on success
            type: str
            sample: ssh_host_example
        ssh_key:
            description:
                - Private SSH key string.
            returned: on success
            type: str
            sample: ssh_key_example
        ssh_user:
            description:
                - The username (credential) used when creating or updating this resource.
            returned: on success
            type: str
            sample: ssh_user_example
        ssh_sudo_location:
            description:
                - Sudo location
            returned: on success
            type: str
            sample: ssh_sudo_location_example
    sample: {
        "host": "host_example",
        "port": 56,
        "database_name": "database_name_example",
        "security_protocol": "PLAIN",
        "ssl_mode": "DISABLED",
        "additional_attributes": [{
            "name": "name_example",
            "value": "value_example"
        }],
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_type": "MYSQL",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "ingress_ips": [{
            "ingress_ip": "ingress_ip_example"
        }],
        "nsg_ids": [],
        "username": "username_example",
        "password": "example-password",
        "replication_username": "replication_username_example",
        "replication_password": "example-password",
        "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "technology_type": "AMAZON_AURORA_MYSQL",
        "connection_string": "connection_string_example",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "ssh_host": "ssh_host_example",
        "ssh_key": "ssh_key_example",
        "ssh_user": "ssh_user_example",
        "ssh_sudo_location": "ssh_sudo_location_example"
    }

diagnostics_result:
    description:
        - Details of the Connection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        result_type:
            description:
                - Type of the Result (i.e. Success or Failure).
            returned: on success
            type: str
            sample: SUCCEEDED
        error:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                code:
                    description:
                        - A short error code that defines the error, meant for programmatic parsing.
                    returned: on success
                    type: str
                    sample: code_example
                message:
                    description:
                        - A human-readable error string.
                    returned: on success
                    type: str
                    sample: message_example
                issue:
                    description:
                        - The text describing the root cause of the reported issue
                    returned: on success
                    type: str
                    sample: issue_example
                action:
                    description:
                        - The text describing the action required to fix the issue
                    returned: on success
                    type: str
                    sample: action_example
    sample: {
        "result_type": "SUCCEEDED",
        "error": {
            "code": "code_example",
            "message": "message_example",
            "issue": "issue_example",
            "action": "action_example"
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
    from oci.database_migration import DatabaseMigrationClient
    from oci.database_migration.models import ChangeConnectionCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        connection_diagnostics
    """

    @staticmethod
    def get_module_resource_id_param():
        return "connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("connection_id")

    def get_get_fn(self):
        return self.client.get_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_id=self.module.params.get("connection_id"),
        )

    def get_response_field_name(self, action):
        response_fields = dict(
            connection_diagnostics="diagnostics_result",
            change_compartment="connection",
        )
        return response_fields.get(action, "connection")

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeConnectionCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_connection_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connection_id=self.module.params.get("connection_id"),
                change_connection_compartment_details=action_details,
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

    def connection_diagnostics(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.connection_diagnostics,
            call_fn_args=(),
            call_fn_kwargs=dict(connection_id=self.module.params.get("connection_id"),),
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


ConnectionActionsHelperCustom = get_custom_class("ConnectionActionsHelperCustom")


class ResourceHelper(ConnectionActionsHelperCustom, ConnectionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            connection_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "connection_diagnostics"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connection",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

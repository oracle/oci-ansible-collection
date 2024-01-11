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
module: oci_database_console_connection
short_description: Manage a ConsoleConnection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a ConsoleConnection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new console connection to the specified database node.
      After the console connection has been created and is available,
      you connect to the console using SSH.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    public_key:
        description:
            - The SSH public key used to authenticate the console connection.
            - Required for create using I(state=present).
        type: str
    db_node_id:
        description:
            - The database node L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    console_connection_id:
        description:
            - The OCID of the console connection.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ConsoleConnection.
            - Use I(state=present) to create a ConsoleConnection.
            - Use I(state=absent) to delete a ConsoleConnection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create console_connection
  oci_database_console_connection:
    # required
    public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
    db_node_id: "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete console_connection
  oci_database_console_connection:
    # required
    db_node_id: "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx"
    console_connection_id: "ocid1.consoleconnection.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
console_connection:
    description:
        - Details of the ConsoleConnection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the console connection.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment to contain the console connection.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        db_node_id:
            description:
                - The OCID of the database node.
            returned: on success
            type: str
            sample: "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx"
        connection_string:
            description:
                - The SSH connection string for the console connection.
            returned: on success
            type: str
            sample: connection_string_example
        fingerprint:
            description:
                - The SSH public key fingerprint for the console connection.
            returned: on success
            type: str
            sample: fingerprint_example
        lifecycle_state:
            description:
                - The current state of the console connection.
            returned: on success
            type: str
            sample: ACTIVE
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "db_node_id": "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_string": "connection_string_example",
        "fingerprint": "fingerprint_example",
        "lifecycle_state": "ACTIVE"
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
    from oci.database import DatabaseClient
    from oci.database.models import CreateConsoleConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConsoleConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ConsoleConnectionHelperGen, self).get_possible_entity_types() + [
            "consoleconnection",
            "consoleconnections",
            "databaseconsoleconnection",
            "databaseconsoleconnections",
            "consoleconnectionresource",
            "consoleconnectionsresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "console_connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("console_connection_id")

    def get_get_fn(self):
        return self.client.get_console_connection

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_console_connection,
            console_connection_id=summary_model.id,
            db_node_id=self.module.params.get("db_node_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_console_connection,
            db_node_id=self.module.params.get("db_node_id"),
            console_connection_id=self.module.params.get("console_connection_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "db_node_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_console_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateConsoleConnectionDetails

    def get_exclude_attributes(self):
        return ["public_key"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_console_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_console_connection_details=create_details,
                db_node_id=self.module.params.get("db_node_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_console_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_node_id=self.module.params.get("db_node_id"),
                console_connection_id=self.module.params.get("console_connection_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ConsoleConnectionHelperCustom = get_custom_class("ConsoleConnectionHelperCustom")


class ResourceHelper(ConsoleConnectionHelperCustom, ConsoleConnectionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            public_key=dict(type="str"),
            db_node_id=dict(type="str", required=True),
            console_connection_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="console_connection",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

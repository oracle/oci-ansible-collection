#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connection_id:
        description:
            - The OCID of the database connection
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the compartment to move the resource to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Connection.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on connection
  oci_database_migration_connection_actions:
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
connection:
    description:
        - Details of the Connection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the resource
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID of the compartment
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_type:
            description:
                - Database connection type.
            returned: on success
            type: str
            sample: MANUAL
        display_name:
            description:
                - Database Connection display name identifier.
            returned: on success
            type: str
            sample: display_name_example
        database_id:
            description:
                - The OCID of the cloud database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        connect_descriptor:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                host:
                    description:
                        - Host of the connect descriptor.
                    returned: on success
                    type: str
                    sample: host_example
                port:
                    description:
                        - Port of the connect descriptor.
                    returned: on success
                    type: int
                    sample: 56
                database_service_name:
                    description:
                        - Database service name.
                    returned: on success
                    type: str
                    sample: database_service_name_example
                connect_string:
                    description:
                        - Connect string.
                    returned: on success
                    type: str
                    sample: connect_string_example
        credentials_secret_id:
            description:
                - OCID of the Secret in the OCI vault containing the Database Connection credentials.
            returned: on success
            type: str
            sample: "ocid1.credentialssecret.oc1..xxxxxxEXAMPLExxxxxx"
        certificate_tdn:
            description:
                - This name is the distinguished name used while creating the certificate on target database.
            returned: on success
            type: str
            sample: certificate_tdn_example
        ssh_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                host:
                    description:
                        - Name of the host the SSH key is valid for.
                    returned: on success
                    type: str
                    sample: host_example
                user:
                    description:
                        - SSH user
                    returned: on success
                    type: str
                    sample: user_example
                sudo_location:
                    description:
                        - Sudo location
                    returned: on success
                    type: str
                    sample: sudo_location_example
        admin_credentials:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                username:
                    description:
                        - Administrator username
                    returned: on success
                    type: str
                    sample: username_example
        private_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to contain the
                          private endpoint.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                vcn_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN where the Private Endpoint will be bound
                          to.
                    returned: on success
                    type: str
                    sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
                subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the customer's
                          subnet where the private endpoint VNIC will reside.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                id:
                    description:
                        - L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a previously created Private Endpoint.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        vault_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                compartment_id:
                    description:
                        - OCID of the compartment where the secret containing the credentials will be created.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                vault_id:
                    description:
                        - OCID of the vault
                    returned: on success
                    type: str
                    sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
                key_id:
                    description:
                        - OCID of the vault encryption key
                    returned: on success
                    type: str
                    sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the Connection resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information
                  for a resource in Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time the Connection resource was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time of the last Connection resource details update. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "database_type": "MANUAL",
        "display_name": "display_name_example",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "connect_descriptor": {
            "host": "host_example",
            "port": 56,
            "database_service_name": "database_service_name_example",
            "connect_string": "connect_string_example"
        },
        "credentials_secret_id": "ocid1.credentialssecret.oc1..xxxxxxEXAMPLExxxxxx",
        "certificate_tdn": "certificate_tdn_example",
        "ssh_details": {
            "host": "host_example",
            "user": "user_example",
            "sudo_location": "sudo_location_example"
        },
        "admin_credentials": {
            "username": "username_example"
        },
        "private_endpoint": {
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "vault_details": {
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
            "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
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


ConnectionActionsHelperCustom = get_custom_class("ConnectionActionsHelperCustom")


class ResourceHelper(ConnectionActionsHelperCustom, ConnectionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            connection_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

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

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
module: oci_database_migration_connection_facts
short_description: Fetches details about one or multiple Connection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Connection resources in Oracle Cloud Infrastructure
    - List all Database Connections.
    - If I(connection_id) is specified, the details of a single Connection will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connection_id:
        description:
            - The OCID of the database connection
            - Required to get a specific connection.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple connections.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.
              Default order for displayName is ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - The current state of the Database Migration Deployment.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific connection
  oci_database_migration_connection_facts:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: List connections
  oci_database_migration_connection_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: timeCreated
    sort_order: ASC
    lifecycle_state: CREATING

"""

RETURN = """
connections:
    description:
        - List of Connection resources
    returned: on success
    type: complex
    contains:
        connect_descriptor:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.credentialssecret.oc1..xxxxxxEXAMPLExxxxxx"
        certificate_tdn:
            description:
                - This name is the distinguished name used while creating the certificate on target database.
                - Returned for get operation
            returned: on success
            type: str
            sample: certificate_tdn_example
        ssh_details:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                username:
                    description:
                        - Administrator username
                    returned: on success
                    type: str
                    sample: username_example
        replication_credentials:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
        manual_database_sub_type:
            description:
                - Database manual connection subtype. This value can only be specified for manual connections.
            returned: on success
            type: str
            sample: ORACLE
        is_dedicated:
            description:
                - True if the Autonomous Connection is dedicated. Not provided for Non-Autonomous Connections.
            returned: on success
            type: bool
            sample: true
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
        nsg_ids:
            description:
                - An array of Network Security Group OCIDs used to define network access for Connections.
            returned: on success
            type: list
            sample: []
    sample: [{
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
        "replication_credentials": {
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "database_type": "MANUAL",
        "manual_database_sub_type": "ORACLE",
        "is_dedicated": true,
        "display_name": "display_name_example",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "nsg_ids": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_migration import DatabaseMigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "connection_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_id=self.module.params.get("connection_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_connections,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ConnectionFactsHelperCustom = get_custom_class("ConnectionFactsHelperCustom")


class ResourceFactsHelper(ConnectionFactsHelperCustom, ConnectionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            connection_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="connection",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(connections=result)


if __name__ == "__main__":
    main()

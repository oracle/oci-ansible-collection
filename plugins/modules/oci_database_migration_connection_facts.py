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
            - The OCID of the database connection.
            - Required to get a specific connection.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple connections.
        type: str
    technology_type:
        description:
            - The array of technology types.
        type: list
        elements: str
        choices:
            - "OCI_AUTONOMOUS_DATABASE"
            - "OCI_MYSQL"
            - "ORACLE_DATABASE"
            - "ORACLE_EXADATA"
            - "AMAZON_RDS_ORACLE"
            - "AMAZON_AURORA_MYSQL"
            - "AMAZON_RDS_MYSQL"
            - "AZURE_MYSQL"
            - "GOOGLE_CLOUD_SQL_MYSQL"
            - "MYSQL_SERVER"
    connection_type:
        description:
            - The array of connection types.
        type: list
        elements: str
        choices:
            - "MYSQL"
            - "ORACLE"
    source_connection_id:
        description:
            - The OCID of the source database connection.
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
    technology_type: [ "OCI_AUTONOMOUS_DATABASE" ]
    connection_type: [ "MYSQL" ]
    source_connection_id: "ocid1.sourceconnection.oc1..xxxxxxEXAMPLExxxxxx"
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
        host:
            description:
                - The IP Address of the host.
                - Returned for get operation
            returned: on success
            type: str
            sample: host_example
        port:
            description:
                - The port to be used for the connection.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        database_name:
            description:
                - The name of the database being referenced.
                - Returned for get operation
            returned: on success
            type: str
            sample: database_name_example
        security_protocol:
            description:
                - Security Protocol to be used for the connection.
                - Returned for get operation
            returned: on success
            type: str
            sample: PLAIN
        ssl_mode:
            description:
                - SSL mode to be used for the connection.
                - Returned for get operation
            returned: on success
            type: str
            sample: DISABLED
        additional_attributes:
            description:
                - An array of name-value pair attribute entries.
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        username:
            description:
                - The username (credential) used when creating or updating this resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: username_example
        password:
            description:
                - The password (credential) used when creating or updating this resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: example-password
        replication_username:
            description:
                - The username (credential) used when creating or updating this resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: replication_username_example
        replication_password:
            description:
                - The password (credential) used when creating or updating this resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: example-password
        secret_id:
            description:
                - The OCID of the resource being referenced.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_id:
            description:
                - The OCID of the resource being referenced.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        technology_type:
            description:
                - "The type of MySQL source or target connection.
                  Example: OCI_MYSQL represents OCI MySQL HeatWave Database Service"
                - Returned for get operation
            returned: on success
            type: str
            sample: AMAZON_AURORA_MYSQL
        connection_string:
            description:
                - Connect descriptor or Easy Connect Naming method used to connect to a database.
                - Returned for get operation
            returned: on success
            type: str
            sample: connection_string_example
        database_id:
            description:
                - The OCID of the database being referenced.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        ssh_host:
            description:
                - Name of the host the SSH key is valid for.
                - Returned for get operation
            returned: on success
            type: str
            sample: ssh_host_example
        ssh_key:
            description:
                - Private SSH key string.
                - Returned for get operation
            returned: on success
            type: str
            sample: ssh_key_example
        ssh_user:
            description:
                - The username (credential) used when creating or updating this resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: ssh_user_example
        ssh_sudo_location:
            description:
                - Sudo location
                - Returned for get operation
            returned: on success
            type: str
            sample: ssh_sudo_location_example
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
    sample: [{
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
        "ssh_sudo_location": "ssh_sudo_location_example",
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
            "technology_type",
            "connection_type",
            "source_connection_id",
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
            technology_type=dict(
                type="list",
                elements="str",
                choices=[
                    "OCI_AUTONOMOUS_DATABASE",
                    "OCI_MYSQL",
                    "ORACLE_DATABASE",
                    "ORACLE_EXADATA",
                    "AMAZON_RDS_ORACLE",
                    "AMAZON_AURORA_MYSQL",
                    "AMAZON_RDS_MYSQL",
                    "AZURE_MYSQL",
                    "GOOGLE_CLOUD_SQL_MYSQL",
                    "MYSQL_SERVER",
                ],
            ),
            connection_type=dict(
                type="list", elements="str", choices=["MYSQL", "ORACLE"]
            ),
            source_connection_id=dict(type="str"),
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

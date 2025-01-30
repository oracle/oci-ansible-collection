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
module: oci_database_migration_connection
short_description: Manage a Connection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Connection resource in Oracle Cloud Infrastructure
    - For I(state=present), create a Database Connection resource that contains the details to connect to either a Source or Target Database
      in the migration.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_migration_connection_actions) module: change_compartment,
      connection_diagnostics."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    technology_type:
        description:
            - "The type of MySQL source or target connection.
              Example: OCI_MYSQL represents OCI MySQL HeatWave Database Service"
            - Required for create using I(state=present).
        type: str
    connection_string:
        description:
            - Connect descriptor or Easy Connect Naming method used to connect to a database.
            - This parameter is updatable.
            - Applicable when connection_type is 'ORACLE'
        type: str
    wallet:
        description:
            - The wallet contents used to make connections to a database.  This
              attribute is expected to be base64 encoded.
            - This parameter is updatable.
            - Applicable when connection_type is 'ORACLE'
        type: str
    database_id:
        description:
            - The OCID of the database being referenced.
            - This parameter is updatable.
            - Applicable when connection_type is 'ORACLE'
        type: str
    ssh_host:
        description:
            - Name of the host the SSH key is valid for.
            - This parameter is updatable.
            - Applicable when connection_type is 'ORACLE'
        type: str
    ssh_key:
        description:
            - Private SSH key string.
            - This parameter is updatable.
            - Applicable when connection_type is 'ORACLE'
        type: str
    ssh_user:
        description:
            - The username (credential) used when creating or updating this resource.
            - This parameter is updatable.
            - Applicable when connection_type is 'ORACLE'
        type: str
    ssh_sudo_location:
        description:
            - Sudo location
            - This parameter is updatable.
            - Applicable when connection_type is 'ORACLE'
        type: str
    connection_type:
        description:
            - Defines the type of connection. For example, ORACLE.
            - Required for create using I(state=present), update using I(state=present) with connection_id present.
            - Applicable when connection_type is one of ['MYSQL', 'ORACLE']
        type: str
        choices:
            - "MYSQL"
            - "ORACLE"
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Applicable when connection_type is one of ['MYSQL', 'ORACLE']
        type: str
        aliases: ["name"]
    description:
        description:
            - A user-friendly description. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see Resource Tags. Example: {\\"Department\\": \\"Finance\\"}"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    vault_id:
        description:
            - OCI resource ID.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MYSQL', 'ORACLE']
        type: str
    key_id:
        description:
            - The OCID of the key used in cryptographic operations.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MYSQL', 'ORACLE']
        type: str
    subnet_id:
        description:
            - OCI resource ID.
            - This parameter is updatable.
        type: str
    nsg_ids:
        description:
            - An array of Network Security Group OCIDs used to define network access for Connections.
            - This parameter is updatable.
        type: list
        elements: str
    username:
        description:
            - The username (credential) used when creating or updating this resource.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MYSQL', 'ORACLE']
        type: str
    password:
        description:
            - The password (credential) used when creating or updating this resource.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when connection_type is one of ['MYSQL', 'ORACLE']
        type: str
    replication_username:
        description:
            - The username (credential) used when creating or updating this resource.
            - This parameter is updatable.
        type: str
    replication_password:
        description:
            - The password (credential) used when creating or updating this resource.
            - This parameter is updatable.
        type: str
    host:
        description:
            - The IP Address of the host.
            - This parameter is updatable.
            - Applicable when connection_type is 'MYSQL'
        type: str
    port:
        description:
            - The port to be used for the connection.
            - This parameter is updatable.
            - Applicable when connection_type is 'MYSQL'
        type: int
    database_name:
        description:
            - The name of the database being referenced.
            - This parameter is updatable.
            - Required when connection_type is 'MYSQL'
        type: str
    security_protocol:
        description:
            - Security Type for MySQL.
            - This parameter is updatable.
            - Required when connection_type is 'MYSQL'
        type: str
    ssl_mode:
        description:
            - SSL modes for MySQL.
            - This parameter is updatable.
            - Applicable when connection_type is 'MYSQL'
        type: str
    ssl_ca:
        description:
            - "Database Certificate - The base64 encoded content of mysql.pem file
              containing the server public key (for 1 and 2-way SSL)."
            - This parameter is updatable.
            - Applicable when connection_type is 'MYSQL'
        type: str
    ssl_crl:
        description:
            - "Certificates revoked by certificate authorities (CA).
              Server certificate must not be on this list (for 1 and 2-way SSL).
              Note: This is an optional and that too only applicable if TLS/MTLS option is selected."
            - This parameter is updatable.
            - Applicable when connection_type is 'MYSQL'
        type: str
    ssl_cert:
        description:
            - "Client Certificate - The base64 encoded content of client-cert.pem file
              containing the client public key (for 2-way SSL)."
            - This parameter is updatable.
            - Applicable when connection_type is 'MYSQL'
        type: str
    ssl_key:
        description:
            - "Client Key - The client-key.pem containing the client private key (for 2-way SSL)."
            - This parameter is updatable.
            - Applicable when connection_type is 'MYSQL'
        type: str
    additional_attributes:
        description:
            - An array of name-value pair attribute entries.
            - This parameter is updatable.
            - Applicable when connection_type is 'MYSQL'
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - The name of the property entry.
                    - Required when connection_type is 'MYSQL'
                type: str
                required: true
            value:
                description:
                    - The value of the property entry.
                    - Required when connection_type is 'MYSQL'
                type: str
                required: true
    db_system_id:
        description:
            - The OCID of the database system being referenced.
            - This parameter is updatable.
            - Applicable when connection_type is 'MYSQL'
        type: str
    connection_id:
        description:
            - The OCID of the database connection.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Connection.
            - Use I(state=present) to create or update a Connection.
            - Use I(state=absent) to delete a Connection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create connection with connection_type = MYSQL
  oci_database_migration_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: MYSQL

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password
    replication_username: replication_username_example
    replication_password: example-password
    host: host_example
    port: 56
    database_name: database_name_example
    security_protocol: security_protocol_example
    ssl_mode: ssl_mode_example
    ssl_ca: ssl_ca_example
    ssl_crl: ssl_crl_example
    ssl_cert: ssl_cert_example
    ssl_key: ssl_key_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create connection with connection_type = ORACLE
  oci_database_migration_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    technology_type: technology_type_example
    connection_type: ORACLE

    # optional
    connection_string: connection_string_example
    wallet: wallet_example
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    ssh_host: ssh_host_example
    ssh_key: ssh_key_example
    ssh_user: ssh_user_example
    ssh_sudo_location: ssh_sudo_location_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password
    replication_username: replication_username_example
    replication_password: example-password

- name: Update connection with connection_type = MYSQL
  oci_database_migration_connection:
    # required
    connection_type: MYSQL

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password
    replication_username: replication_username_example
    replication_password: example-password
    host: host_example
    port: 56
    database_name: database_name_example
    security_protocol: security_protocol_example
    ssl_mode: ssl_mode_example
    ssl_ca: ssl_ca_example
    ssl_crl: ssl_crl_example
    ssl_cert: ssl_cert_example
    ssl_key: ssl_key_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update connection with connection_type = ORACLE
  oci_database_migration_connection:
    # required
    connection_type: ORACLE

    # optional
    connection_string: connection_string_example
    wallet: wallet_example
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    ssh_host: ssh_host_example
    ssh_key: ssh_key_example
    ssh_user: ssh_user_example
    ssh_sudo_location: ssh_sudo_location_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password
    replication_username: replication_username_example
    replication_password: example-password

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = MYSQL
  oci_database_migration_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: MYSQL

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password
    replication_username: replication_username_example
    replication_password: example-password
    host: host_example
    port: 56
    database_name: database_name_example
    security_protocol: security_protocol_example
    ssl_mode: ssl_mode_example
    ssl_ca: ssl_ca_example
    ssl_crl: ssl_crl_example
    ssl_cert: ssl_cert_example
    ssl_key: ssl_key_example
    additional_attributes:
    - # required
      name: name_example
      value: value_example
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with connection_type = ORACLE
  oci_database_migration_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_type: ORACLE

    # optional
    connection_string: connection_string_example
    wallet: wallet_example
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    ssh_host: ssh_host_example
    ssh_key: ssh_key_example
    ssh_user: ssh_user_example
    ssh_sudo_location: ssh_sudo_location_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    username: username_example
    password: example-password
    replication_username: replication_username_example
    replication_password: example-password

- name: Delete connection
  oci_database_migration_connection:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_migration_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    from oci.database_migration import DatabaseMigrationClient
    from oci.database_migration.models import CreateConnectionDetails
    from oci.database_migration.models import UpdateConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ConnectionHelperGen, self).get_possible_entity_types() + [
            "odmsconnection",
            "odmsconnections",
            "databaseMigrationodmsconnection",
            "databaseMigrationodmsconnections",
            "odmsconnectionresource",
            "odmsconnectionsresource",
            "connection",
            "connections",
            "databaseMigrationconnection",
            "databaseMigrationconnections",
            "connectionresource",
            "connectionsresource",
            "databasemigration",
        ]

    def get_module_resource_id_param(self):
        return "connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("connection_id")

    def get_get_fn(self):
        return self.client.get_connection

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection, connection_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_id=self.module.params.get("connection_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateConnectionDetails

    def get_exclude_attributes(self):
        return ["ssl_crl", "wallet", "ssl_key", "ssl_ca", "ssl_cert"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(create_connection_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connection_id=self.module.params.get("connection_id"),
                update_connection_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(connection_id=self.module.params.get("connection_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ConnectionHelperCustom = get_custom_class("ConnectionHelperCustom")


class ResourceHelper(ConnectionHelperCustom, ConnectionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            technology_type=dict(type="str"),
            connection_string=dict(type="str"),
            wallet=dict(type="str"),
            database_id=dict(type="str"),
            ssh_host=dict(type="str"),
            ssh_key=dict(type="str", no_log=True),
            ssh_user=dict(type="str"),
            ssh_sudo_location=dict(type="str"),
            connection_type=dict(type="str", choices=["MYSQL", "ORACLE"]),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            vault_id=dict(type="str"),
            key_id=dict(type="str"),
            subnet_id=dict(type="str"),
            nsg_ids=dict(type="list", elements="str"),
            username=dict(type="str"),
            password=dict(type="str", no_log=True),
            replication_username=dict(type="str"),
            replication_password=dict(type="str", no_log=True),
            host=dict(type="str"),
            port=dict(type="int"),
            database_name=dict(type="str"),
            security_protocol=dict(type="str"),
            ssl_mode=dict(type="str"),
            ssl_ca=dict(type="str"),
            ssl_crl=dict(type="str"),
            ssl_cert=dict(type="str"),
            ssl_key=dict(type="str", no_log=True),
            additional_attributes=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    value=dict(type="str", required=True),
                ),
            ),
            db_system_id=dict(type="str"),
            connection_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

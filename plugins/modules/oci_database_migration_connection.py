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
module: oci_database_migration_connection
short_description: Manage a Connection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Connection resource in Oracle Cloud Infrastructure
    - For I(state=present), create a Database Connection resource that contains the details to connect to either a Source or Target Database
      in the migration.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_migration_connection_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - OCID of the compartment
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - Database Connection display name identifier.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    database_type:
        description:
            - Database connection type.
            - Required for create using I(state=present).
        type: str
        choices:
            - "MANUAL"
            - "AUTONOMOUS"
            - "USER_MANAGED_OCI"
    database_id:
        description:
            - The OCID of the cloud database. Required if the database connection type is Autonomous.
            - This parameter is updatable.
        type: str
    connect_descriptor:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            host:
                description:
                    - Host or IP address of the connect descriptor. Required if no connectString was specified.
                    - This parameter is updatable.
                type: str
            port:
                description:
                    - Port of the connect descriptor. Required if no connectString was specified.
                    - This parameter is updatable.
                type: int
            database_service_name:
                description:
                    - Database service name. Required if no connectString was specified.
                    - This parameter is updatable.
                type: str
            connect_string:
                description:
                    - "Connect String. Required if no host, port nor databaseServiceName were specified.
                      If a Private Endpoint was specified in the Connection, the host entry should be a valid IP address.
                      Supported formats:
                      Easy connect: <host>:<port>/<db_service_name>
                      Long format: (description= (address=(port=<port>)(host=<host>))(connect_data=(service_name=<db_service_name>)))"
                    - This parameter is updatable.
                type: str
    certificate_tdn:
        description:
            - This name is the distinguished name used while creating the certificate on target database. Requires a TLS wallet to be specified.
              Not required for source container database connections.
            - This parameter is updatable.
        type: str
    tls_wallet:
        description:
            - cwallet.sso containing containing the TCPS/SSL certificate; base64 encoded String. Not required for source container database connections.
            - This parameter is updatable.
        type: str
    tls_keystore:
        description:
            - keystore.jks file contents; base64 encoded String. Requires a TLS wallet to be specified. Not required for source container database connections.
            - This parameter is updatable.
        type: str
    ssh_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            host:
                description:
                    - Name of the host the SSH key is valid for.
                    - This parameter is updatable.
                type: str
            sshkey:
                description:
                    - Private SSH key string.
                    - This parameter is updatable.
                type: str
            user:
                description:
                    - SSH user
                    - This parameter is updatable.
                type: str
            sudo_location:
                description:
                    - Sudo location
                    - This parameter is updatable.
                type: str
    admin_credentials:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            username:
                description:
                    - Administrator username
                    - This parameter is updatable.
                type: str
            password:
                description:
                    - Administrator password
                    - This parameter is updatable.
                type: str
    private_endpoint:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            compartment_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to contain the
                      private endpoint.
                    - This parameter is updatable.
                type: str
            vcn_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN where the Private Endpoint will be bound to.
                    - This parameter is updatable.
                type: str
            subnet_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the customer's subnet where the private endpoint
                      VNIC
                      will reside.
                    - This parameter is updatable.
                type: str
    vault_details:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            compartment_id:
                description:
                    - OCID of the compartment where the secret containing the credentials will be created.
                    - This parameter is updatable.
                type: str
            vault_id:
                description:
                    - OCID of the vault
                    - This parameter is updatable.
                type: str
            key_id:
                description:
                    - OCID of the vault encryption key
                    - This parameter is updatable.
                type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    connection_id:
        description:
            - The OCID of the database connection
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
- name: Create connection
  oci_database_migration_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_type: MANUAL
    admin_credentials:
      # optional
      username: username_example
      password: example-password
    vault_details:
      # optional
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    connect_descriptor:
      # optional
      host: host_example
      port: 56
      database_service_name: database_service_name_example
      connect_string: connect_string_example
    certificate_tdn: certificate_tdn_example
    tls_wallet: tls_wallet_example
    tls_keystore: tls_keystore_example
    ssh_details:
      # optional
      host: host_example
      sshkey: sshkey_example
      user: user_example
      sudo_location: sudo_location_example
    private_endpoint:
      # optional
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update connection
  oci_database_migration_connection:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    connect_descriptor:
      # optional
      host: host_example
      port: 56
      database_service_name: database_service_name_example
      connect_string: connect_string_example
    certificate_tdn: certificate_tdn_example
    tls_wallet: tls_wallet_example
    tls_keystore: tls_keystore_example
    ssh_details:
      # optional
      host: host_example
      sshkey: sshkey_example
      user: user_example
      sudo_location: sudo_location_example
    admin_credentials:
      # optional
      username: username_example
      password: example-password
    private_endpoint:
      # optional
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    vault_details:
      # optional
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_migration_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    connect_descriptor:
      # optional
      host: host_example
      port: 56
      database_service_name: database_service_name_example
      connect_string: connect_string_example
    certificate_tdn: certificate_tdn_example
    tls_wallet: tls_wallet_example
    tls_keystore: tls_keystore_example
    ssh_details:
      # optional
      host: host_example
      sshkey: sshkey_example
      user: user_example
      sudo_location: sudo_location_example
    admin_credentials:
      # optional
      username: username_example
      password: example-password
    private_endpoint:
      # optional
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    vault_details:
      # optional
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

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
    OCIResourceHelperBase,
    get_custom_class,
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
        return [
            "admin_credentials.password",
            "tls_keystore",
            "tls_wallet",
            "ssh_details.sshkey",
        ]

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
            display_name=dict(aliases=["name"], type="str"),
            database_type=dict(
                type="str", choices=["MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI"]
            ),
            database_id=dict(type="str"),
            connect_descriptor=dict(
                type="dict",
                options=dict(
                    host=dict(type="str"),
                    port=dict(type="int"),
                    database_service_name=dict(type="str"),
                    connect_string=dict(type="str"),
                ),
            ),
            certificate_tdn=dict(type="str"),
            tls_wallet=dict(type="str"),
            tls_keystore=dict(type="str", no_log=True),
            ssh_details=dict(
                type="dict",
                options=dict(
                    host=dict(type="str"),
                    sshkey=dict(type="str", no_log=True),
                    user=dict(type="str"),
                    sudo_location=dict(type="str"),
                ),
            ),
            admin_credentials=dict(
                type="dict",
                options=dict(
                    username=dict(type="str"), password=dict(type="str", no_log=True)
                ),
            ),
            private_endpoint=dict(
                type="dict",
                options=dict(
                    compartment_id=dict(type="str"),
                    vcn_id=dict(type="str"),
                    subnet_id=dict(type="str"),
                ),
            ),
            vault_details=dict(
                type="dict",
                options=dict(
                    compartment_id=dict(type="str"),
                    vault_id=dict(type="str"),
                    key_id=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            connection_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

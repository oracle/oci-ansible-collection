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
module: oci_database_tools_connection
short_description: Manage a DatabaseToolsConnection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DatabaseToolsConnection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Database Tools connection.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_tools_connection_actions) module: change_compartment, validate."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the Database Tools connection.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Applicable when type is one of ['MYSQL', 'ORACLE_DATABASE']
        type: str
        aliases: ["name"]
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    type:
        description:
            - The DatabaseToolsConnection type.
            - Required for create using I(state=present), update using I(state=present) with database_tools_connection_id present.
        type: str
        choices:
            - "MYSQL"
            - "ORACLE_DATABASE"
    related_resource:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            entity_type:
                description:
                    - The resource entity type.
                    - This parameter is updatable.
                    - Applicable when type is one of ['MYSQL', 'ORACLE_DATABASE']
                type: str
                choices:
                    - "MYSQLDBSYSTEM"
                    - "AUTONOMOUSDATABASE"
                    - "DATABASE"
                    - "PLUGGABLEDATABASE"
            identifier:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the related resource.
                    - This parameter is updatable.
                    - Applicable when type is one of ['MYSQL', 'ORACLE_DATABASE']
                type: str
    connection_string:
        description:
            - The connection string used to connect to the MySQL Server.
            - This parameter is updatable.
        type: str
    user_name:
        description:
            - The user name.
            - This parameter is updatable.
        type: str
    user_password:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            value_type:
                description:
                    - The value type of the user password.
                type: str
                choices:
                    - "SECRETID"
                required: true
            secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the user password.
                type: str
                required: true
    advanced_properties:
        description:
            - The advanced connection properties key-value pair (e.g., `sslMode`).
            - This parameter is updatable.
        type: dict
    key_stores:
        description:
            - The CA certificate to verify the server's certificate and
              the client private key and associated certificate required for client authentication.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            key_store_type:
                description:
                    - The key store type.
                type: str
                choices:
                    - "CLIENT_CERTIFICATE_PEM"
                    - "CLIENT_PRIVATE_KEY_PEM"
                    - "CA_CERTIFICATE_PEM"
                    - "JAVA_KEY_STORE"
                    - "JAVA_TRUST_STORE"
                    - "PKCS12"
                    - "SSO"
            key_store_content:
                description:
                    - ""
                type: dict
                suboptions:
                    value_type:
                        description:
                            - The value type of the key store content.
                        type: str
                        choices:
                            - "SECRETID"
                        required: true
                    secret_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the key store.
                        type: str
            key_store_password:
                description:
                    - ""
                type: dict
                suboptions:
                    value_type:
                        description:
                            - The value type of the key store password.
                        type: str
                        choices:
                            - "SECRETID"
                        required: true
                    secret_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the key store
                              password.
                        type: str
    private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Tools private endpoint used to access the
              database in the customer VCN.
            - This parameter is updatable.
        type: str
    database_tools_connection_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a Database Tools connection.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DatabaseToolsConnection.
            - Use I(state=present) to create or update a DatabaseToolsConnection.
            - Use I(state=absent) to delete a DatabaseToolsConnection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create database_tools_connection with type = MYSQL
  oci_database_tools_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    type: MYSQL

    # optional
    display_name: display_name_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    related_resource:
      # optional
      entity_type: MYSQLDBSYSTEM
      identifier: identifier_example
    connection_string: connection_string_example
    user_name: user_name_example
    user_password:
      # required
      value_type: SECRETID
      secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    advanced_properties: null
    key_stores:
    - # optional
      key_store_type: CLIENT_CERTIFICATE_PEM
      key_store_content:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
      key_store_password:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create database_tools_connection with type = ORACLE_DATABASE
  oci_database_tools_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    type: ORACLE_DATABASE

    # optional
    display_name: display_name_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    related_resource:
      # optional
      entity_type: MYSQLDBSYSTEM
      identifier: identifier_example
    connection_string: connection_string_example
    user_name: user_name_example
    user_password:
      # required
      value_type: SECRETID
      secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    advanced_properties: null
    key_stores:
    - # optional
      key_store_type: CLIENT_CERTIFICATE_PEM
      key_store_content:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
      key_store_password:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update database_tools_connection with type = MYSQL
  oci_database_tools_connection:
    # required
    type: MYSQL

    # optional
    display_name: display_name_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    related_resource:
      # optional
      entity_type: MYSQLDBSYSTEM
      identifier: identifier_example
    connection_string: connection_string_example
    user_name: user_name_example
    user_password:
      # required
      value_type: SECRETID
      secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    advanced_properties: null
    key_stores:
    - # optional
      key_store_type: CLIENT_CERTIFICATE_PEM
      key_store_content:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
      key_store_password:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update database_tools_connection with type = ORACLE_DATABASE
  oci_database_tools_connection:
    # required
    type: ORACLE_DATABASE

    # optional
    display_name: display_name_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    related_resource:
      # optional
      entity_type: MYSQLDBSYSTEM
      identifier: identifier_example
    connection_string: connection_string_example
    user_name: user_name_example
    user_password:
      # required
      value_type: SECRETID
      secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    advanced_properties: null
    key_stores:
    - # optional
      key_store_type: CLIENT_CERTIFICATE_PEM
      key_store_content:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
      key_store_password:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update database_tools_connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = MYSQL
  oci_database_tools_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    type: MYSQL

    # optional
    display_name: display_name_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    related_resource:
      # optional
      entity_type: MYSQLDBSYSTEM
      identifier: identifier_example
    connection_string: connection_string_example
    user_name: user_name_example
    user_password:
      # required
      value_type: SECRETID
      secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    advanced_properties: null
    key_stores:
    - # optional
      key_store_type: CLIENT_CERTIFICATE_PEM
      key_store_content:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
      key_store_password:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update database_tools_connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = ORACLE_DATABASE
  oci_database_tools_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    type: ORACLE_DATABASE

    # optional
    display_name: display_name_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    related_resource:
      # optional
      entity_type: MYSQLDBSYSTEM
      identifier: identifier_example
    connection_string: connection_string_example
    user_name: user_name_example
    user_password:
      # required
      value_type: SECRETID
      secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    advanced_properties: null
    key_stores:
    - # optional
      key_store_type: CLIENT_CERTIFICATE_PEM
      key_store_content:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
      key_store_password:
        # required
        value_type: SECRETID

        # optional
        secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete database_tools_connection
  oci_database_tools_connection:
    # required
    database_tools_connection_id: "ocid1.databasetoolsconnection.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete database_tools_connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_tools_connection:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_tools import DatabaseToolsClient
    from oci.database_tools.models import CreateDatabaseToolsConnectionDetails
    from oci.database_tools.models import UpdateDatabaseToolsConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseToolsConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DatabaseToolsConnectionHelperGen, self
        ).get_possible_entity_types() + [
            "databasetoolsconnection",
            "databasetoolsconnections",
            "databaseToolsdatabasetoolsconnection",
            "databaseToolsdatabasetoolsconnections",
            "databasetoolsconnectionresource",
            "databasetoolsconnectionsresource",
            "databasetools",
        ]

    def get_module_resource_id_param(self):
        return "database_tools_connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_tools_connection_id")

    def get_get_fn(self):
        return self.client.get_database_tools_connection

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_tools_connection,
            database_tools_connection_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_tools_connection,
            database_tools_connection_id=self.module.params.get(
                "database_tools_connection_id"
            ),
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
            self.client.list_database_tools_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateDatabaseToolsConnectionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_database_tools_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_database_tools_connection_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDatabaseToolsConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_database_tools_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_tools_connection_id=self.module.params.get(
                    "database_tools_connection_id"
                ),
                update_database_tools_connection_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_database_tools_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_tools_connection_id=self.module.params.get(
                    "database_tools_connection_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseToolsConnectionHelperCustom = get_custom_class(
    "DatabaseToolsConnectionHelperCustom"
)


class ResourceHelper(
    DatabaseToolsConnectionHelperCustom, DatabaseToolsConnectionHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            type=dict(type="str", choices=["MYSQL", "ORACLE_DATABASE"]),
            related_resource=dict(
                type="dict",
                options=dict(
                    entity_type=dict(
                        type="str",
                        choices=[
                            "MYSQLDBSYSTEM",
                            "AUTONOMOUSDATABASE",
                            "DATABASE",
                            "PLUGGABLEDATABASE",
                        ],
                    ),
                    identifier=dict(type="str"),
                ),
            ),
            connection_string=dict(type="str"),
            user_name=dict(type="str"),
            user_password=dict(
                type="dict",
                no_log=False,
                options=dict(
                    value_type=dict(type="str", required=True, choices=["SECRETID"]),
                    secret_id=dict(type="str", required=True),
                ),
            ),
            advanced_properties=dict(type="dict"),
            key_stores=dict(
                type="list",
                elements="dict",
                no_log=False,
                options=dict(
                    key_store_type=dict(
                        type="str",
                        choices=[
                            "CLIENT_CERTIFICATE_PEM",
                            "CLIENT_PRIVATE_KEY_PEM",
                            "CA_CERTIFICATE_PEM",
                            "JAVA_KEY_STORE",
                            "JAVA_TRUST_STORE",
                            "PKCS12",
                            "SSO",
                        ],
                    ),
                    key_store_content=dict(
                        type="dict",
                        no_log=False,
                        options=dict(
                            value_type=dict(
                                type="str", required=True, choices=["SECRETID"]
                            ),
                            secret_id=dict(type="str"),
                        ),
                    ),
                    key_store_password=dict(
                        type="dict",
                        no_log=False,
                        options=dict(
                            value_type=dict(
                                type="str", required=True, choices=["SECRETID"]
                            ),
                            secret_id=dict(type="str"),
                        ),
                    ),
                ),
            ),
            private_endpoint_id=dict(type="str"),
            database_tools_connection_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

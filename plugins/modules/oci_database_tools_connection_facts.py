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
module: oci_database_tools_connection_facts
short_description: Fetches details about one or multiple DatabaseToolsConnection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DatabaseToolsConnection resources in Oracle Cloud Infrastructure
    - Returns a list of DatabaseToolsConnections.
    - If I(database_tools_connection_id) is specified, the details of a single DatabaseToolsConnection will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    database_tools_connection_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a DatabaseToolsConnection.
            - Required to get a specific database_tools_connection.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple database_tools_connections.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    type:
        description:
            - A filter to return only resources their endpointServiceId matches the given endpointServiceId.
        type: list
        elements: str
        choices:
            - "ORACLE_DATABASE"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List database_tools_connections
  oci_database_tools_connection_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific database_tools_connection
  oci_database_tools_connection_facts:
    database_tools_connection_id: "ocid1.databasetoolsconnection.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
database_tools_connections:
    description:
        - List of DatabaseToolsConnection resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DatabaseToolsConnection.
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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the containing Compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the DatabaseToolsConnection.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time the DatabaseToolsConnection was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the DatabaseToolsConnection was updated. An RFC3339 formatted datetime string
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
                - The DatabaseToolsConnection type.
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
                    sample: AUTONOMOUSDATABASE
                identifier:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the related resource.
                    returned: on success
                    type: str
                    sample: identifier_example
        connection_string:
            description:
                - Connect descriptor or Easy Connect Naming method to connect to the database.
            returned: on success
            type: str
            sample: connection_string_example
        user_name:
            description:
                - Database user name.
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
                - Advanced connection properties key-value pair (e.g., oracle.net.ssl_server_dn_match).
            returned: on success
            type: dict
            sample: {}
        key_stores:
            description:
                - Oracle wallet or Java Keystores containing trusted certificates for authenticating the server's public certificate and
                  the client private key and associated certificates required for client authentication.
            returned: on success
            type: complex
            contains:
                key_store_type:
                    description:
                        - The key store type.
                    returned: on success
                    type: str
                    sample: JAVA_KEY_STORE
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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DatabaseToolsPrivateEndpoint used to access the
                  database in the Customer VCN.
            returned: on success
            type: str
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
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
            "entity_type": "AUTONOMOUSDATABASE",
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
            "key_store_type": "JAVA_KEY_STORE",
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_tools import DatabaseToolsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseToolsConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "database_tools_connection_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_tools_connection,
            database_tools_connection_id=self.module.params.get(
                "database_tools_connection_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_database_tools_connections,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DatabaseToolsConnectionFactsHelperCustom = get_custom_class(
    "DatabaseToolsConnectionFactsHelperCustom"
)


class ResourceFactsHelper(
    DatabaseToolsConnectionFactsHelperCustom, DatabaseToolsConnectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            database_tools_connection_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            type=dict(type="list", elements="str", choices=["ORACLE_DATABASE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database_tools_connection",
        service_client_class=DatabaseToolsClient,
        namespace="database_tools",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(database_tools_connections=result)


if __name__ == "__main__":
    main()

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
module: oci_database_management_external_db_system_connector_facts
short_description: Fetches details about one or multiple ExternalDbSystemConnector resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalDbSystemConnector resources in Oracle Cloud Infrastructure
    - Lists the external connectors in the specified external DB system.
    - If I(external_db_system_connector_id) is specified, the details of a single ExternalDbSystemConnector will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_db_system_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            - Required to get a specific external_db_system_connector.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    external_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
        type: str
    display_name:
        description:
            - A filter to only return the resources that match the entire display name.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending.
              The `DISPLAYNAME` sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific external_db_system_connector
  oci_database_management_external_db_system_connector_facts:
    # required
    external_db_system_connector_id: "ocid1.externaldbsystemconnector.oc1..xxxxxxEXAMPLExxxxxx"

- name: List external_db_system_connectors
  oci_database_management_external_db_system_connector_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
external_db_system_connectors:
    description:
        - List of ExternalDbSystemConnector resources
    returned: on success
    type: complex
    contains:
        connection_status:
            description:
                - The status of connectivity to the external DB system component.
                - Returned for get operation
            returned: on success
            type: str
            sample: connection_status_example
        connection_failure_message:
            description:
                - The error message indicating the reason for connection failure or `null` if
                  the connection was successful.
                - Returned for get operation
            returned: on success
            type: str
            sample: connection_failure_message_example
        time_connection_status_last_updated:
            description:
                - The date and time the connectionStatus of the external DB system connector was last updated.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        connection_info:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                component_type:
                    description:
                        - The component type.
                    returned: on success
                    type: str
                    sample: DATABASE
                connection_string:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        hosts:
                            description:
                                - The list of host names of the ASM instances.
                            returned: on success
                            type: list
                            sample: []
                        port:
                            description:
                                - The port used to connect to the ASM instance.
                            returned: on success
                            type: int
                            sample: 56
                        service:
                            description:
                                - The service name of the ASM instance.
                            returned: on success
                            type: str
                            sample: service_example
                        protocol:
                            description:
                                - The protocol used to connect to the ASM instance.
                            returned: on success
                            type: str
                            sample: TCP
                        host_name:
                            description:
                                - The host name of the database or the SCAN name in case of a RAC database.
                            returned: on success
                            type: str
                            sample: host_name_example
                connection_credentials:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        user_name:
                            description:
                                - The user name used to connect to the ASM instance.
                            returned: on success
                            type: str
                            sample: user_name_example
                        password_secret_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the user password.
                            returned: on success
                            type: str
                            sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                        role:
                            description:
                                - The role of the user connecting to the ASM instance.
                            returned: on success
                            type: str
                            sample: SYSASM
                        credential_type:
                            description:
                                - The type of credential used to connect to the ASM instance.
                            returned: on success
                            type: str
                            sample: NAME_REFERENCE
                        credential_name:
                            description:
                                - "The name of the credential information that used to connect to the DB system resource.
                                  The name should be in \\"x.y\\" format, where the length of \\"x\\" has a maximum of 64 characters,
                                  and length of \\"y\\" has a maximum of 199 characters. The name strings can contain letters,
                                  numbers and the underscore character only. Other characters are not valid, except for
                                  the \\".\\" character that separates the \\"x\\" and \\"y\\" portions of the name.
                                  *IMPORTANT* - The name must be unique within the OCI region the credential is being created in.
                                  If you specify a name that duplicates the name of another credential within the same OCI region,
                                  you may overwrite or corrupt the credential that is already using the name."
                                - "For example: inventorydb.abc112233445566778899"
                            returned: on success
                            type: str
                            sample: credential_name_example
                        ssl_secret_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret containing the SSL keystore
                                  and truststore details.
                            returned: on success
                            type: str
                            sample: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system connector.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the external connector. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        connector_type:
            description:
                - The type of connector.
            returned: on success
            type: str
            sample: MACS
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system that the connector is a part of.
            returned: on success
            type: str
            sample: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management agent
                  used for the external DB system connector.
            returned: on success
            type: str
            sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the external DB system connector.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the external DB system connector was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external DB system connector was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "connection_status": "connection_status_example",
        "connection_failure_message": "connection_failure_message_example",
        "time_connection_status_last_updated": "2013-10-20T19:20:30+01:00",
        "connection_info": {
            "component_type": "DATABASE",
            "connection_string": {
                "hosts": [],
                "port": 56,
                "service": "service_example",
                "protocol": "TCP",
                "host_name": "host_name_example"
            },
            "connection_credentials": {
                "user_name": "user_name_example",
                "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx",
                "role": "SYSASM",
                "credential_type": "NAME_REFERENCE",
                "credential_name": "credential_name_example",
                "ssl_secret_id": "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
            }
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "connector_type": "MACS",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_system_id": "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDbSystemConnectorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "external_db_system_connector_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system_connector,
            external_db_system_connector_id=self.module.params.get(
                "external_db_system_connector_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "external_db_system_id",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_external_db_system_connectors, **optional_kwargs
        )


ExternalDbSystemConnectorFactsHelperCustom = get_custom_class(
    "ExternalDbSystemConnectorFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalDbSystemConnectorFactsHelperCustom, ExternalDbSystemConnectorFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_db_system_connector_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            external_db_system_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_db_system_connector",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(external_db_system_connectors=result)


if __name__ == "__main__":
    main()

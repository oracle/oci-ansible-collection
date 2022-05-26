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
module: oci_database_external_database_connector_facts
short_description: Fetches details about one or multiple ExternalDatabaseConnector resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalDatabaseConnector resources in Oracle Cloud Infrastructure
    - Gets a list of the external database connectors in the specified compartment.
    - If I(external_database_connector_id) is specified, the details of a single ExternalDatabaseConnector will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_database_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              external database connector resource (`ExternalDatabaseConnectorId`).
            - Required to get a specific external_database_connector.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple external_database_connectors.
        type: str
    external_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external database whose connectors will be listed.
            - Required to list multiple external_database_connectors.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
              Default order for TIMECREATED is descending.
              Default order for DISPLAYNAME is ascending.
              The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "DISPLAYNAME"
            - "TIMECREATED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the specified lifecycle state.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "UPDATING"
            - "TERMINATING"
            - "TERMINATED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific external_database_connector
  oci_database_external_database_connector_facts:
    # required
    external_database_connector_id: "ocid1.externaldatabaseconnector.oc1..xxxxxxEXAMPLExxxxxx"

- name: List external_database_connectors
  oci_database_external_database_connector_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_database_id: "ocid1.externaldatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: DISPLAYNAME
    sort_order: ASC
    lifecycle_state: PROVISIONING
    display_name: display_name_example

"""

RETURN = """
external_database_connectors:
    description:
        - List of ExternalDatabaseConnector resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - The user-friendly name for the
                  L(external database connector,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
                  The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                  L(external database connector,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the external database connector resource.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the external connector was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        connector_type:
            description:
                - The type of connector used by the external database resource.
            returned: on success
            type: str
            sample: MACS
        external_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external database resource.
            returned: on success
            type: str
            sample: "ocid1.externaldatabase.oc1..xxxxxxEXAMPLExxxxxx"
        connection_status:
            description:
                - The status of connectivity to the external database.
            returned: on success
            type: str
            sample: connection_status_example
        time_connection_status_last_updated:
            description:
                - The date and time the connectionStatus of this external connector was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        connection_string:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - The host name of the database.
                    returned: on success
                    type: str
                    sample: hostname_example
                port:
                    description:
                        - The port used to connect to the database.
                    returned: on success
                    type: int
                    sample: 56
                service:
                    description:
                        - The name of the service alias used to connect to the database.
                    returned: on success
                    type: str
                    sample: service_example
                protocol:
                    description:
                        - The protocol used to connect to the database.
                    returned: on success
                    type: str
                    sample: TCP
        connection_credentials:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                credential_type:
                    description:
                        - The type of credential used to connect to the database.
                    returned: on success
                    type: str
                    sample: NAME_REFERENCE
                credential_name:
                    description:
                        - "The name of the credential information that used to connect to the database. The name should be in \\"x.y\\" format, where
                          the length of \\"x\\" has a maximum of 64 characters, and length of \\"y\\" has a maximum of 199 characters.
                          The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for
                          the \\".\\" character that separates the \\"x\\" and \\"y\\" portions of the name.
                          *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name
                          that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already
                          using the name."
                        - "For example: inventorydb.abc112233445566778899"
                    returned: on success
                    type: str
                    sample: credential_name_example
                username:
                    description:
                        - The username that will be used to connect to the database.
                    returned: on success
                    type: str
                    sample: username_example
                password:
                    description:
                        - The password that will be used to connect to the database.
                    returned: on success
                    type: str
                    sample: example-password
                role:
                    description:
                        - The role of the user that will be connecting to the database.
                    returned: on success
                    type: str
                    sample: SYSDBA
                ssl_secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                          L(secret,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
                    returned: on success
                    type: str
                    sample: "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
        connector_agent_id:
            description:
                - The ID of the agent used for the
                  L(external database connector,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
            returned: on success
            type: str
            sample: "ocid1.connectoragent.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "connector_type": "MACS",
        "external_database_id": "ocid1.externaldatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_status": "connection_status_example",
        "time_connection_status_last_updated": "2013-10-20T19:20:30+01:00",
        "connection_string": {
            "hostname": "hostname_example",
            "port": 56,
            "service": "service_example",
            "protocol": "TCP"
        },
        "connection_credentials": {
            "credential_type": "NAME_REFERENCE",
            "credential_name": "credential_name_example",
            "username": "username_example",
            "password": "example-password",
            "role": "SYSDBA",
            "ssl_secret_id": "ocid1.sslsecret.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "connector_agent_id": "ocid1.connectoragent.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDatabaseConnectorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "external_database_connector_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "external_database_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_database_connector,
            external_database_connector_id=self.module.params.get(
                "external_database_connector_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_external_database_connectors,
            compartment_id=self.module.params.get("compartment_id"),
            external_database_id=self.module.params.get("external_database_id"),
            **optional_kwargs
        )


ExternalDatabaseConnectorFactsHelperCustom = get_custom_class(
    "ExternalDatabaseConnectorFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalDatabaseConnectorFactsHelperCustom, ExternalDatabaseConnectorFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_database_connector_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            external_database_id=dict(type="str"),
            sort_by=dict(type="str", choices=["DISPLAYNAME", "TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "UPDATING",
                    "TERMINATING",
                    "TERMINATED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_database_connector",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(external_database_connectors=result)


if __name__ == "__main__":
    main()

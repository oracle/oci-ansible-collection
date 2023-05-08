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
module: oci_database_management_external_exadata_storage_connector_facts
short_description: Fetches details about one or multiple ExternalExadataStorageConnector resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalExadataStorageConnector resources in Oracle Cloud Infrastructure
    - Lists the connectors for the specific Exadata infrastructures.
    - If I(external_exadata_storage_connector_id) is specified, the details of a single ExternalExadataStorageConnector will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_exadata_storage_connector_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connector to the Exadata storage server.
            - Required to get a specific external_exadata_storage_connector.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple external_exadata_storage_connectors.
        type: str
    external_exadata_infrastructure_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            - Required to list multiple external_exadata_storage_connectors.
        type: str
    display_name:
        description:
            - The optional single value query filter parameter on the entity display name.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for 'TIMECREATED' is descending and the default sort order for 'NAME' is ascending.
              The 'NAME' sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
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
- name: Get a specific external_exadata_storage_connector
  oci_database_management_external_exadata_storage_connector_facts:
    # required
    external_exadata_storage_connector_id: "ocid1.externalexadatastorageconnector.oc1..xxxxxxEXAMPLExxxxxx"

- name: List external_exadata_storage_connectors
  oci_database_management_external_exadata_storage_connector_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_exadata_infrastructure_id: "ocid1.externalexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
external_exadata_storage_connectors:
    description:
        - List of ExternalExadataStorageConnector resources
    returned: on success
    type: complex
    contains:
        exadata_infrastructure_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of Exadata infrastructure system.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - "The name of the resource. English letters, numbers, \\"-\\", \\"_\\" and \\".\\" only."
            returned: on success
            type: str
            sample: display_name_example
        version:
            description:
                - The version of the resource.
            returned: on success
            type: str
            sample: version_example
        internal_id:
            description:
                - The internal ID.
            returned: on success
            type: str
            sample: "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The status of the entity.
            returned: on success
            type: str
            sample: status_example
        lifecycle_state:
            description:
                - The current lifecycle state of the database resource.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The timestamp of the creation.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The timestamp of the last update.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - The details of the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        additional_details:
            description:
                - "The additional details of the resource defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
        resource_type:
            description:
                - The type of resource.
            returned: on success
            type: str
            sample: INFRASTRUCTURE_SUMMARY
        connection_uri:
            description:
                - "The unique connection string of the connection. For example, \\"https://slcm21celadm02.us.oracle.com:443/MS/RESTService/\\"."
            returned: on success
            type: str
            sample: connection_uri_example
        storage_server_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata storage server.
            returned: on success
            type: str
            sample: "ocid1.storageserver.oc1..xxxxxxEXAMPLExxxxxx"
        agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the agent for the Exadata storage server.
            returned: on success
            type: str
            sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "exadata_infrastructure_id": "ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "version": "version_example",
        "internal_id": "ocid1.internal.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "status_example",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "additional_details": {},
        "resource_type": "INFRASTRUCTURE_SUMMARY",
        "connection_uri": "connection_uri_example",
        "storage_server_id": "ocid1.storageserver.oc1..xxxxxxEXAMPLExxxxxx",
        "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
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


class ExternalExadataStorageConnectorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "external_exadata_storage_connector_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "external_exadata_infrastructure_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_exadata_storage_connector,
            external_exadata_storage_connector_id=self.module.params.get(
                "external_exadata_storage_connector_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_external_exadata_storage_connectors,
            compartment_id=self.module.params.get("compartment_id"),
            external_exadata_infrastructure_id=self.module.params.get(
                "external_exadata_infrastructure_id"
            ),
            **optional_kwargs
        )


ExternalExadataStorageConnectorFactsHelperCustom = get_custom_class(
    "ExternalExadataStorageConnectorFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalExadataStorageConnectorFactsHelperCustom,
    ExternalExadataStorageConnectorFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_exadata_storage_connector_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            external_exadata_infrastructure_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_exadata_storage_connector",
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

    module.exit_json(external_exadata_storage_connectors=result)


if __name__ == "__main__":
    main()

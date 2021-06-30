#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_opsi_database_insights_facts
short_description: Fetches details about one or multiple DatabaseInsights resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DatabaseInsights resources in Oracle Cloud Infrastructure
    - Gets a list of database insights based on the query parameters specified. Either compartmentId or id query parameter must be specified.
    - If I(database_insight_id) is specified, the details of a single DatabaseInsights will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    database_insight_id:
        description:
            - Unique database insight identifier
            - Required to get a specific database_insights.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    enterprise_manager_bridge_id:
        description:
            - Unique Enterprise Manager bridge identifier
        type: str
    status:
        description:
            - Resource Status
        type: list
        choices:
            - "DISABLED"
            - "ENABLED"
            - "TERMINATED"
    lifecycle_state:
        description:
            - Lifecycle states
        type: list
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    database_type:
        description:
            - Filter by one or more database type.
              Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.
        type: list
        choices:
            - "ADW-S"
            - "ATP-S"
            - "ADW-D"
            - "ATP-D"
            - "EXTERNAL-PDB"
            - "EXTERNAL-NONCDB"
    database_id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated DBaaS entity.
        type: list
    fields:
        description:
            - Specifies the fields to return in a database summary response. By default all fields are returned if omitted.
        type: list
        choices:
            - "compartmentId"
            - "databaseName"
            - "databaseDisplayName"
            - "databaseType"
            - "databaseVersion"
            - "databaseHostNames"
            - "freeformTags"
            - "definedTags"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Database insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.
        type: str
        choices:
            - "databaseName"
            - "databaseDisplayName"
            - "databaseType"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List database_insights
  oci_opsi_database_insights_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific database_insights
  oci_opsi_database_insights_facts:
    database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
database_insights:
    description:
        - List of DatabaseInsights resources
    returned: on success
    type: complex
    contains:
        entity_source:
            description:
                - Source of the database entity.
            returned: on success
            type: string
            sample: AUTONOMOUS_DATABASE
        id:
            description:
                - Database insight identifier
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment identifier of the database
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - Indicates the status of a database insight in Operations Insights
            returned: on success
            type: string
            sample: ENABLED
        database_type:
            description:
                - Operations Insights internal representation of the database type.
            returned: on success
            type: string
            sample: database_type_example
        database_version:
            description:
                - The version of the database.
            returned: on success
            type: string
            sample: database_version_example
        processor_count:
            description:
                - Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.
            returned: on success
            type: int
            sample: 56
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
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The time the the database insight was first enabled. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the database insight was updated. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the database.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        enterprise_manager_identifier:
            description:
                - Enterprise Manager Unique Identifier
            returned: on success
            type: string
            sample: enterprise_manager_identifier_example
        enterprise_manager_entity_name:
            description:
                - Enterprise Manager Entity Name
            returned: on success
            type: string
            sample: enterprise_manager_entity_name_example
        enterprise_manager_entity_type:
            description:
                - Enterprise Manager Entity Type
            returned: on success
            type: string
            sample: enterprise_manager_entity_type_example
        enterprise_manager_entity_identifier:
            description:
                - Enterprise Manager Entity Unique Identifier
            returned: on success
            type: string
            sample: enterprise_manager_entity_identifier_example
        enterprise_manager_entity_display_name:
            description:
                - Enterprise Manager Entity Display Name
            returned: on success
            type: string
            sample: enterprise_manager_entity_display_name_example
        enterprise_manager_bridge_id:
            description:
                - OPSI Enterprise Manager Bridge OCID
            returned: on success
            type: string
            sample: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"
        management_agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Management Agent
            returned: on success
            type: string
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of External Database Connector
            returned: on success
            type: string
            sample: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
        connection_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                host_name:
                    description:
                        - Name of the listener host that will be used to create the connect string to the database.
                    returned: on success
                    type: string
                    sample: host_name_example
                protocol:
                    description:
                        - Protocol used for connection requests.
                    returned: on success
                    type: string
                    sample: TCP
                port:
                    description:
                        - Listener port number used for connection requests.
                    returned: on success
                    type: int
                    sample: 56
                service_name:
                    description:
                        - Service name used for connection requests.
                    returned: on success
                    type: string
                    sample: service_name_example
        connection_credential_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                credential_source_name:
                    description:
                        - Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.
                    returned: on success
                    type: string
                    sample: credential_source_name_example
                credential_type:
                    description:
                        - Credential type.
                    returned: on success
                    type: string
                    sample: CREDENTIALS_BY_SOURCE
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: string
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        database_name:
            description:
                - Name of database
            returned: on success
            type: string
            sample: database_name_example
        database_display_name:
            description:
                - Display name of database
            returned: on success
            type: string
            sample: database_display_name_example
        database_resource_type:
            description:
                - OCI database resource type
            returned: on success
            type: string
            sample: externalpluggabledatabase
        db_additional_details:
            description:
                - Additional details of a database in JSON format. For autonomous databases, this is the AutonomousDatabase object serialized as a JSON string
                  as defined in https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/. For EM, pass in null or an empty
                  string. Note that this string needs to be escaped when specified in the curl command.
            returned: on success
            type: dict
            sample: {}
        database_host_names:
            description:
                - The hostnames for the database.
            returned: on success
            type: list
            sample: []
    sample: [{
        "entity_source": "AUTONOMOUS_DATABASE",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "ENABLED",
        "database_type": "database_type_example",
        "database_version": "database_version_example",
        "processor_count": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "enterprise_manager_identifier": "enterprise_manager_identifier_example",
        "enterprise_manager_entity_name": "enterprise_manager_entity_name_example",
        "enterprise_manager_entity_type": "enterprise_manager_entity_type_example",
        "enterprise_manager_entity_identifier": "enterprise_manager_entity_identifier_example",
        "enterprise_manager_entity_display_name": "enterprise_manager_entity_display_name_example",
        "enterprise_manager_bridge_id": "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx",
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "connector_id": "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_details": {
            "host_name": "host_name_example",
            "protocol": "TCP",
            "port": 56,
            "service_name": "service_name_example"
        },
        "connection_credential_details": {
            "credential_source_name": "credential_source_name_example",
            "credential_type": "CREDENTIALS_BY_SOURCE"
        },
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "database_name": "database_name_example",
        "database_display_name": "database_display_name_example",
        "database_resource_type": "externalpluggabledatabase",
        "db_additional_details": {},
        "database_host_names": []
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseInsightsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "database_insight_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_insight,
            database_insight_id=self.module.params.get("database_insight_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "enterprise_manager_bridge_id",
            "status",
            "lifecycle_state",
            "database_type",
            "database_id",
            "fields",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_database_insights, **optional_kwargs
        )


DatabaseInsightsFactsHelperCustom = get_custom_class(
    "DatabaseInsightsFactsHelperCustom"
)


class ResourceFactsHelper(
    DatabaseInsightsFactsHelperCustom, DatabaseInsightsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            database_insight_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            enterprise_manager_bridge_id=dict(type="str"),
            status=dict(type="list", choices=["DISABLED", "ENABLED", "TERMINATED"]),
            lifecycle_state=dict(
                type="list",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            database_type=dict(
                type="list",
                choices=[
                    "ADW-S",
                    "ATP-S",
                    "ADW-D",
                    "ATP-D",
                    "EXTERNAL-PDB",
                    "EXTERNAL-NONCDB",
                ],
            ),
            database_id=dict(type="list"),
            fields=dict(
                type="list",
                choices=[
                    "compartmentId",
                    "databaseName",
                    "databaseDisplayName",
                    "databaseType",
                    "databaseVersion",
                    "databaseHostNames",
                    "freeformTags",
                    "definedTags",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=["databaseName", "databaseDisplayName", "databaseType"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database_insights",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(database_insights=result)


if __name__ == "__main__":
    main()

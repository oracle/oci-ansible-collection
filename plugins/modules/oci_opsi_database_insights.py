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
module: oci_opsi_database_insights
short_description: Manage a DatabaseInsights resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DatabaseInsights resource in Oracle Cloud Infrastructure
    - For I(state=present), create a Database Insight resource for a database in Operations Insights. The database will be enabled in Operations Insights.
      Database metric collection and analysis will be started.
    - "This resource has the following action operations in the M(oracle.oci.oci_opsi_database_insights_actions) module:
      change_autonomous_database_insight_advanced_features, change, change_pe_comanaged, disable_autonomous_database_insight_advanced_features, disable,
      enable_autonomous_database_insight_advanced_features, enable, ingest_addm_reports, ingest_database_configuration, ingest_sql_bucket,
      ingest_sql_plan_lines, ingest_sql_stats, ingest_sql_text."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    enterprise_manager_identifier:
        description:
            - Enterprise Manager Unique Identifier
            - Required when entity_source is 'EM_MANAGED_EXTERNAL_DATABASE'
        type: str
    enterprise_manager_bridge_id:
        description:
            - OPSI Enterprise Manager Bridge OCID
            - Required when entity_source is 'EM_MANAGED_EXTERNAL_DATABASE'
        type: str
    enterprise_manager_entity_identifier:
        description:
            - Enterprise Manager Entity Unique Identifier
            - Required when entity_source is 'EM_MANAGED_EXTERNAL_DATABASE'
        type: str
    exadata_insight_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata insight.
            - Applicable when entity_source is 'EM_MANAGED_EXTERNAL_DATABASE'
        type: str
    compartment_id:
        description:
            - Compartment Identifier of database
            - Required for create using I(state=present).
            - Required when entity_source is one of ['EM_MANAGED_EXTERNAL_DATABASE', 'PE_COMANAGED_DATABASE']
        type: str
    database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.
            - Required when entity_source is 'PE_COMANAGED_DATABASE'
        type: str
    database_resource_type:
        description:
            - OCI database resource type
            - Required when entity_source is 'PE_COMANAGED_DATABASE'
        type: str
    opsi_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the OPSI private endpoint
            - Applicable when entity_source is 'PE_COMANAGED_DATABASE'
        type: str
    dbm_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Database Management private endpoint
            - Applicable when entity_source is 'PE_COMANAGED_DATABASE'
        type: str
    service_name:
        description:
            - Database service name used for connection requests.
            - Required when entity_source is 'PE_COMANAGED_DATABASE'
        type: str
    credential_details:
        description:
            - ""
            - Required when entity_source is 'PE_COMANAGED_DATABASE'
        type: dict
        suboptions:
            credential_source_name:
                description:
                    - Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.
                type: str
                required: true
            credential_type:
                description:
                    - Credential type.
                type: str
                choices:
                    - "CREDENTIALS_BY_SOURCE"
                    - "CREDENTIALS_BY_VAULT"
                required: true
            user_name:
                description:
                    - database user name.
                    - Applicable when credential_type is 'CREDENTIALS_BY_VAULT'
                type: str
            password_secret_id:
                description:
                    - The secret L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) mapping to the database credentials.
                    - Applicable when credential_type is 'CREDENTIALS_BY_VAULT'
                type: str
            role:
                description:
                    - database user role.
                    - Applicable when credential_type is 'CREDENTIALS_BY_VAULT'
                type: str
                choices:
                    - "NORMAL"
    deployment_type:
        description:
            - Database Deployment Type
            - Required when entity_source is 'PE_COMANAGED_DATABASE'
        type: str
        choices:
            - "VIRTUAL_MACHINE"
            - "BARE_METAL"
            - "EXACS"
    system_tags:
        description:
            - "System tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            - Applicable when entity_source is 'PE_COMANAGED_DATABASE'
        type: dict
    entity_source:
        description:
            - Source of the database entity.
            - Required for create using I(state=present), update using I(state=present) with database_insight_id present.
        type: str
        choices:
            - "EM_MANAGED_EXTERNAL_DATABASE"
            - "PE_COMANAGED_DATABASE"
            - "MACS_MANAGED_EXTERNAL_DATABASE"
            - "AUTONOMOUS_DATABASE"
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
    database_insight_id:
        description:
            - Unique database insight identifier
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DatabaseInsights.
            - Use I(state=present) to create or update a DatabaseInsights.
            - Use I(state=absent) to delete a DatabaseInsights.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create database_insights with entity_source = EM_MANAGED_EXTERNAL_DATABASE
  oci_opsi_database_insights:
    # required
    enterprise_manager_identifier: enterprise_manager_identifier_example
    enterprise_manager_bridge_id: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"
    enterprise_manager_entity_identifier: enterprise_manager_entity_identifier_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    entity_source: EM_MANAGED_EXTERNAL_DATABASE

    # optional
    exadata_insight_id: "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create database_insights with entity_source = PE_COMANAGED_DATABASE
  oci_opsi_database_insights:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    database_resource_type: database_resource_type_example
    service_name: service_name_example
    credential_details:
      # required
      credential_source_name: credential_source_name_example
      credential_type: CREDENTIALS_BY_SOURCE
    deployment_type: VIRTUAL_MACHINE
    entity_source: PE_COMANAGED_DATABASE

    # optional
    opsi_private_endpoint_id: "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    dbm_private_endpoint_id: "ocid1.dbmprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    system_tags: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create database_insights with entity_source = MACS_MANAGED_EXTERNAL_DATABASE
  oci_opsi_database_insights:
    # required
    entity_source: MACS_MANAGED_EXTERNAL_DATABASE

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create database_insights with entity_source = AUTONOMOUS_DATABASE
  oci_opsi_database_insights:
    # required
    entity_source: AUTONOMOUS_DATABASE

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update database_insights with entity_source = EM_MANAGED_EXTERNAL_DATABASE
  oci_opsi_database_insights:
    # required
    entity_source: EM_MANAGED_EXTERNAL_DATABASE

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update database_insights with entity_source = PE_COMANAGED_DATABASE
  oci_opsi_database_insights:
    # required
    entity_source: PE_COMANAGED_DATABASE

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update database_insights with entity_source = MACS_MANAGED_EXTERNAL_DATABASE
  oci_opsi_database_insights:
    # required
    entity_source: MACS_MANAGED_EXTERNAL_DATABASE

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update database_insights with entity_source = AUTONOMOUS_DATABASE
  oci_opsi_database_insights:
    # required
    entity_source: AUTONOMOUS_DATABASE

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete database_insights
  oci_opsi_database_insights:
    # required
    database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
database_insights:
    description:
        - Details of the DatabaseInsights resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        is_advanced_features_enabled:
            description:
                - Flag is to identify if advanced features for autonomous database is enabled or not
            returned: on success
            type: bool
            sample: true
        enterprise_manager_identifier:
            description:
                - Enterprise Manager Unique Identifier
            returned: on success
            type: str
            sample: enterprise_manager_identifier_example
        enterprise_manager_entity_name:
            description:
                - Enterprise Manager Entity Name
            returned: on success
            type: str
            sample: enterprise_manager_entity_name_example
        enterprise_manager_entity_type:
            description:
                - Enterprise Manager Entity Type
            returned: on success
            type: str
            sample: enterprise_manager_entity_type_example
        enterprise_manager_entity_identifier:
            description:
                - Enterprise Manager Entity Unique Identifier
            returned: on success
            type: str
            sample: enterprise_manager_entity_identifier_example
        enterprise_manager_entity_display_name:
            description:
                - Enterprise Manager Entity Display Name
            returned: on success
            type: str
            sample: enterprise_manager_entity_display_name_example
        enterprise_manager_bridge_id:
            description:
                - OPSI Enterprise Manager Bridge OCID
            returned: on success
            type: str
            sample: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"
        exadata_insight_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata insight.
            returned: on success
            type: str
            sample: "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx"
        management_agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Management Agent
            returned: on success
            type: str
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of External Database Connector
            returned: on success
            type: str
            sample: "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx"
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
                    type: str
                    sample: credential_source_name_example
                credential_type:
                    description:
                        - Credential type.
                    returned: on success
                    type: str
                    sample: CREDENTIALS_BY_SOURCE
                user_name:
                    description:
                        - database user name.
                    returned: on success
                    type: str
                    sample: user_name_example
                password_secret_id:
                    description:
                        - The secret L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) mapping to the database credentials.
                    returned: on success
                    type: str
                    sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                role:
                    description:
                        - database user role.
                    returned: on success
                    type: str
                    sample: NORMAL
        db_additional_details:
            description:
                - Additional details of a database in JSON format. For autonomous databases, this is the AutonomousDatabase object serialized as a JSON string
                  as defined in https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/. For EM, pass in null or an empty
                  string. Note that this string needs to be escaped when specified in the curl command.
            returned: on success
            type: dict
            sample: {}
        entity_source:
            description:
                - Source of the database entity.
            returned: on success
            type: str
            sample: AUTONOMOUS_DATABASE
        id:
            description:
                - Database insight identifier
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment identifier of the database
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - Indicates the status of a database insight in Operations Insights
            returned: on success
            type: str
            sample: DISABLED
        database_type:
            description:
                - Operations Insights internal representation of the database type.
            returned: on success
            type: str
            sample: database_type_example
        database_version:
            description:
                - The version of the database.
            returned: on success
            type: str
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
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the database insight was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the database.
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
        database_connection_status_details:
            description:
                - A message describing the status of the database connection of this resource. For example, it can be used to provide actionable information
                  about the permission and content validity of the database connection.
            returned: on success
            type: str
            sample: database_connection_status_details_example
        opsi_private_endpoint_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the OPSI private endpoint
            returned: on success
            type: str
            sample: "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
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
                    type: str
                    sample: host_name_example
                protocol:
                    description:
                        - Protocol used for connection requests.
                    returned: on success
                    type: str
                    sample: TCP
                port:
                    description:
                        - Listener port number used for connection requests.
                    returned: on success
                    type: int
                    sample: 56
                service_name:
                    description:
                        - Database service name used for connection requests.
                    returned: on success
                    type: str
                    sample: service_name_example
                hosts:
                    description:
                        - List of hosts and port for private endpoint accessed database resource.
                    returned: on success
                    type: complex
                    contains:
                        host_ip:
                            description:
                                - Host IP used for connection requests for Cloud DB resource.
                            returned: on success
                            type: str
                            sample: host_ip_example
                        port:
                            description:
                                - Listener port number used for connection requests for rivate endpoint accessed db resource.
                            returned: on success
                            type: int
                            sample: 56
        credential_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                credential_source_name:
                    description:
                        - Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.
                    returned: on success
                    type: str
                    sample: credential_source_name_example
                credential_type:
                    description:
                        - Credential type.
                    returned: on success
                    type: str
                    sample: CREDENTIALS_BY_SOURCE
                user_name:
                    description:
                        - database user name.
                    returned: on success
                    type: str
                    sample: user_name_example
                password_secret_id:
                    description:
                        - The secret L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) mapping to the database credentials.
                    returned: on success
                    type: str
                    sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
                role:
                    description:
                        - database user role.
                    returned: on success
                    type: str
                    sample: NORMAL
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: str
            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        database_name:
            description:
                - Name of database
            returned: on success
            type: str
            sample: database_name_example
        database_display_name:
            description:
                - Display name of database
            returned: on success
            type: str
            sample: database_display_name_example
        database_resource_type:
            description:
                - OCI database resource type
            returned: on success
            type: str
            sample: database_resource_type_example
        parent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VM Cluster or DB System ID, depending on which
                  configuration the resource belongs to.
            returned: on success
            type: str
            sample: "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx"
        root_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata Infrastructure.
            returned: on success
            type: str
            sample: "ocid1.root.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "is_advanced_features_enabled": true,
        "enterprise_manager_identifier": "enterprise_manager_identifier_example",
        "enterprise_manager_entity_name": "enterprise_manager_entity_name_example",
        "enterprise_manager_entity_type": "enterprise_manager_entity_type_example",
        "enterprise_manager_entity_identifier": "enterprise_manager_entity_identifier_example",
        "enterprise_manager_entity_display_name": "enterprise_manager_entity_display_name_example",
        "enterprise_manager_bridge_id": "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx",
        "exadata_insight_id": "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx",
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "connector_id": "ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_credential_details": {
            "credential_source_name": "credential_source_name_example",
            "credential_type": "CREDENTIALS_BY_SOURCE",
            "user_name": "user_name_example",
            "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "role": "NORMAL"
        },
        "db_additional_details": {},
        "entity_source": "AUTONOMOUS_DATABASE",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "DISABLED",
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
        "database_connection_status_details": "database_connection_status_details_example",
        "opsi_private_endpoint_id": "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_details": {
            "host_name": "host_name_example",
            "protocol": "TCP",
            "port": 56,
            "service_name": "service_name_example",
            "hosts": [{
                "host_ip": "host_ip_example",
                "port": 56
            }]
        },
        "credential_details": {
            "credential_source_name": "credential_source_name_example",
            "credential_type": "CREDENTIALS_BY_SOURCE",
            "user_name": "user_name_example",
            "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "role": "NORMAL"
        },
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "database_name": "database_name_example",
        "database_display_name": "database_display_name_example",
        "database_resource_type": "database_resource_type_example",
        "parent_id": "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx",
        "root_id": "ocid1.root.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import CreateDatabaseInsightDetails
    from oci.opsi.models import UpdateDatabaseInsightDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseInsightsHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DatabaseInsightsHelperGen, self).get_possible_entity_types() + [
            "opsidatabaseinsight",
            "opsidatabaseinsights",
            "opsiopsidatabaseinsight",
            "opsiopsidatabaseinsights",
            "opsidatabaseinsightresource",
            "opsidatabaseinsightsresource",
            "databaseinsights",
            "databaseinsight",
            "databaseinsightsresource",
            "databaseinsightresource",
            "opsi",
        ]

    def get_module_resource_id_param(self):
        return "database_insight_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_insight_id")

    def get_get_fn(self):
        return self.client.get_database_insight

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_insight, database_insight_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_insight,
            database_insight_id=self.module.params.get("database_insight_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "enterprise_manager_bridge_id",
            "exadata_insight_id",
            "opsi_private_endpoint_id",
        ]

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
            self.client.list_database_insights, **kwargs
        )

    def get_create_model_class(self):
        return CreateDatabaseInsightDetails

    def get_exclude_attributes(self):
        return ["deployment_type", "service_name", "dbm_private_endpoint_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(create_database_insight_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDatabaseInsightDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
                update_database_insight_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_database_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_insight_id=self.module.params.get("database_insight_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseInsightsHelperCustom = get_custom_class("DatabaseInsightsHelperCustom")


class ResourceHelper(DatabaseInsightsHelperCustom, DatabaseInsightsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            enterprise_manager_identifier=dict(type="str"),
            enterprise_manager_bridge_id=dict(type="str"),
            enterprise_manager_entity_identifier=dict(type="str"),
            exadata_insight_id=dict(type="str"),
            compartment_id=dict(type="str"),
            database_id=dict(type="str"),
            database_resource_type=dict(type="str"),
            opsi_private_endpoint_id=dict(type="str"),
            dbm_private_endpoint_id=dict(type="str"),
            service_name=dict(type="str"),
            credential_details=dict(
                type="dict",
                options=dict(
                    credential_source_name=dict(type="str", required=True),
                    credential_type=dict(
                        type="str",
                        required=True,
                        choices=["CREDENTIALS_BY_SOURCE", "CREDENTIALS_BY_VAULT"],
                    ),
                    user_name=dict(type="str"),
                    password_secret_id=dict(type="str"),
                    role=dict(type="str", choices=["NORMAL"]),
                ),
            ),
            deployment_type=dict(
                type="str", choices=["VIRTUAL_MACHINE", "BARE_METAL", "EXACS"]
            ),
            system_tags=dict(type="dict"),
            entity_source=dict(
                type="str",
                choices=[
                    "EM_MANAGED_EXTERNAL_DATABASE",
                    "PE_COMANAGED_DATABASE",
                    "MACS_MANAGED_EXTERNAL_DATABASE",
                    "AUTONOMOUS_DATABASE",
                ],
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            database_insight_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_insights",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

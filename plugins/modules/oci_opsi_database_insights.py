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
module: oci_opsi_database_insights
short_description: Manage a DatabaseInsights resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DatabaseInsights resource in Oracle Cloud Infrastructure
    - For I(state=present), create a Database Insight resource for a database in Operations Insights. The database will be enabled in Operations Insights.
      Database metric collection and analysis will be started.
    - "This resource has the following action operations in the M(oci_database_insights_actions) module: change, disable, enable, ingest_database_configuration,
      ingest_sql_bucket, ingest_sql_plan_lines, ingest_sql_text."
version_added: "2.9"
author: Oracle (@oracle)
options:
    entity_source:
        description:
            - Source of the database entity.
            - Required for create using I(state=present), update using I(state=present) with database_insight_id present.
        type: str
        choices:
            - "EM_MANAGED_EXTERNAL_DATABASE"
            - "MACS_MANAGED_EXTERNAL_DATABASE"
            - "AUTONOMOUS_DATABASE"
    compartment_id:
        description:
            - Compartment Identifier of database
            - Required for create using I(state=present).
            - Required when entity_source is 'EM_MANAGED_EXTERNAL_DATABASE'
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
    enterprise_manager_identifier:
        description:
            - Enterprise Manager Unique Identifier
            - Required for create using I(state=present).
            - Required when entity_source is 'EM_MANAGED_EXTERNAL_DATABASE'
        type: str
    enterprise_manager_bridge_id:
        description:
            - OPSI Enterprise Manager Bridge OCID
            - Required for create using I(state=present).
            - Required when entity_source is 'EM_MANAGED_EXTERNAL_DATABASE'
        type: str
    enterprise_manager_entity_identifier:
        description:
            - Enterprise Manager Entity Unique Identifier
            - Required for create using I(state=present).
            - Required when entity_source is 'EM_MANAGED_EXTERNAL_DATABASE'
        type: str
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
- name: Create database_insights
  oci_opsi_database_insights:
    entity_source: AUTONOMOUS_DATABASE
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    enterprise_manager_identifier: enterprise_manager_identifier_example
    enterprise_manager_bridge_id: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"
    enterprise_manager_entity_identifier: enterprise_manager_entity_identifier_example

- name: Update database_insights
  oci_opsi_database_insights:
    entity_source: AUTONOMOUS_DATABASE
    freeform_tags: {'Department': 'Finance'}
    database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete database_insights
  oci_opsi_database_insights:
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
    sample: {
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
        "db_additional_details": {}
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import CreateDatabaseInsightDetails
    from oci.opsi.models import UpdateDatabaseInsightDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseInsightsHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "database_insight_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_insight_id")

    def get_get_fn(self):
        return self.client.get_database_insight

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_insight,
            database_insight_id=self.module.params.get("database_insight_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "enterprise_manager_bridge_id"]

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
            entity_source=dict(
                type="str",
                choices=[
                    "EM_MANAGED_EXTERNAL_DATABASE",
                    "MACS_MANAGED_EXTERNAL_DATABASE",
                    "AUTONOMOUS_DATABASE",
                ],
            ),
            compartment_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            enterprise_manager_identifier=dict(type="str"),
            enterprise_manager_bridge_id=dict(type="str"),
            enterprise_manager_entity_identifier=dict(type="str"),
            database_insight_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

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

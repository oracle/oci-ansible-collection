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
module: oci_log_analytics_entity_facts
short_description: Fetches details about one or multiple LogAnalyticsEntity resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LogAnalyticsEntity resources in Oracle Cloud Infrastructure
    - Return a list of log analytics entities.
    - If I(log_analytics_entity_id) is specified, the details of a single LogAnalyticsEntity will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    log_analytics_entity_id:
        description:
            - The log analytics entity OCID.
            - Required to get a specific log_analytics_entity.
        type: str
        aliases: ["id"]
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple log_analytics_entities.
        type: str
    name:
        description:
            - A filter to return only log analytics entities whose name matches the entire name given. The match
              is case-insensitive.
        type: str
    name_contains:
        description:
            - A filter to return only log analytics entities whose name contains the name given. The match
              is case-insensitive.
        type: str
    entity_type_name:
        description:
            - A filter to return only log analytics entities whose entityTypeName matches the entire log analytics entity type name of
              one of the entityTypeNames given in the list. The match is case-insensitive.
        type: list
        elements: str
    cloud_resource_id:
        description:
            - A filter to return only log analytics entities whose cloudResourceId matches the cloudResourceId given.
        type: str
    lifecycle_state:
        description:
            - A filter to return only those log analytics entities with the specified lifecycle state. The state
              value is case-insensitive.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    lifecycle_details_contains:
        description:
            - A filter to return only log analytics entities whose lifecycleDetails contains the specified string.
        type: str
    is_management_agent_id_null:
        description:
            - A filter to return only those log analytics entities whose managementAgentId is null or is not null.
        type: str
        choices:
            - "true"
            - "false"
    hostname:
        description:
            - A filter to return only log analytics entities whose hostname matches the entire hostname given.
        type: str
    hostname_contains:
        description:
            - A filter to return only log analytics entities whose hostname contains the substring given.
              The match is case-insensitive.
        type: str
    source_id:
        description:
            - A filter to return only log analytics entities whose sourceId matches the sourceId given.
        type: str
    creation_source_type:
        description:
            - A filter to return only those log analytics entities with the specified auto-creation source.
        type: list
        elements: str
        choices:
            - "EM_BRIDGE"
            - "SERVICE_CONNECTOR_HUB"
            - "DISCOVERY"
            - "NONE"
    creation_source_details:
        description:
            - A filter to return only log analytics entities whose auto-creation source details contains the specified string.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort entities by. Only one sort order may be provided. Default order for timeCreated and timeUpdated
              is descending. Default order for entity name is ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific log_analytics_entity
  oci_log_analytics_entity_facts:
    # required
    log_analytics_entity_id: "ocid1.loganalyticsentity.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_name: namespace_name_example

- name: List log_analytics_entities
  oci_log_analytics_entity_facts:
    # required
    namespace_name: namespace_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    name_contains: name_contains_example
    entity_type_name: [ "entity_type_name_example" ]
    cloud_resource_id: "ocid1.cloudresource.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    lifecycle_details_contains: lifecycle_details_contains_example
    is_management_agent_id_null: true
    hostname: hostname_example
    hostname_contains: hostname_contains_example
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    creation_source_type: [ "EM_BRIDGE" ]
    creation_source_details: creation_source_details_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
log_analytics_entities:
    description:
        - List of LogAnalyticsEntity resources
    returned: on success
    type: complex
    contains:
        management_agent_display_name:
            description:
                - Management agent (management-agents resource kind) display name
                - Returned for get operation
            returned: on success
            type: str
            sample: management_agent_display_name_example
        management_agent_compartment_id:
            description:
                - Management agent (management-agents resource kind) compartment OCID
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.managementagentcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        properties:
            description:
                - The name/value pairs for parameter values to be used in file patterns specified in log sources.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        hostname:
            description:
                - The hostname where the entity represented here is actually present. This would be the output one would get if
                  they run `echo $HOSTNAME` on Linux or an equivalent OS command. This may be different from
                  management agents host since logs may be collected remotely.
                - Returned for get operation
            returned: on success
            type: str
            sample: hostname_example
        id:
            description:
                - The log analytics entity OCID. This ID is a reference used by log analytics features and it represents
                  a resource that is provisioned and managed by the customer on their premises or on the cloud.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Log analytics entity name.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        entity_type_name:
            description:
                - Log analytics entity type name.
            returned: on success
            type: str
            sample: entity_type_name_example
        entity_type_internal_name:
            description:
                - Internal name for the log analytics entity type.
            returned: on success
            type: str
            sample: entity_type_internal_name_example
        lifecycle_state:
            description:
                - The current state of the log analytics entity.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - lifecycleDetails has additional information regarding substeps such as management agent plugin deployment.
            returned: on success
            type: str
            sample: lifecycle_details_example
        management_agent_id:
            description:
                - The OCID of the Management Agent.
            returned: on success
            type: str
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        cloud_resource_id:
            description:
                - The OCID of the Cloud resource which this entity is a representation of. This may be blank when the entity
                  represents a non-cloud resource that the customer may have on their premises.
            returned: on success
            type: str
            sample: "ocid1.cloudresource.oc1..xxxxxxEXAMPLExxxxxx"
        timezone_region:
            description:
                - The timezone region of the log analytics entity.
            returned: on success
            type: str
            sample: Asia/Kolkata
        time_created:
            description:
                - The date and time the resource was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the resource was last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        are_logs_collected:
            description:
                - The Boolean flag to indicate if logs are collected for an entity for log analytics usage.
            returned: on success
            type: bool
            sample: true
        source_id:
            description:
                - This indicates the type of source. It is primarily for Enterprise Manager Repository ID.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        creation_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Source that auto-created the entity.
                    returned: on success
                    type: str
                    sample: EM_BRIDGE
                details:
                    description:
                        - This will provide additional details for source of auto-creation. For example, if entity is auto-created
                          by enterprise manager bridge, this field provides additional detail on enterprise manager that contributed
                          to the entity auto-creation.
                    returned: on success
                    type: str
                    sample: details_example
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
    sample: [{
        "management_agent_display_name": "management_agent_display_name_example",
        "management_agent_compartment_id": "ocid1.managementagentcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "properties": {},
        "hostname": "hostname_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "entity_type_name": "entity_type_name_example",
        "entity_type_internal_name": "entity_type_internal_name_example",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "cloud_resource_id": "ocid1.cloudresource.oc1..xxxxxxEXAMPLExxxxxx",
        "timezone_region": "Asia/Kolkata",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "are_logs_collected": true,
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "creation_source": {
            "type": "EM_BRIDGE",
            "details": "details_example"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsEntityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "log_analytics_entity_id",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_entity,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_entity_id=self.module.params.get("log_analytics_entity_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "name_contains",
            "entity_type_name",
            "cloud_resource_id",
            "lifecycle_state",
            "lifecycle_details_contains",
            "is_management_agent_id_null",
            "hostname",
            "hostname_contains",
            "source_id",
            "creation_source_type",
            "creation_source_details",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_log_analytics_entities,
            namespace_name=self.module.params.get("namespace_name"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LogAnalyticsEntityFactsHelperCustom = get_custom_class(
    "LogAnalyticsEntityFactsHelperCustom"
)


class ResourceFactsHelper(
    LogAnalyticsEntityFactsHelperCustom, LogAnalyticsEntityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            log_analytics_entity_id=dict(aliases=["id"], type="str"),
            namespace_name=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            name_contains=dict(type="str"),
            entity_type_name=dict(type="list", elements="str"),
            cloud_resource_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            lifecycle_details_contains=dict(type="str"),
            is_management_agent_id_null=dict(type="str", choices=["true", "false"]),
            hostname=dict(type="str"),
            hostname_contains=dict(type="str"),
            source_id=dict(type="str"),
            creation_source_type=dict(
                type="list",
                elements="str",
                choices=["EM_BRIDGE", "SERVICE_CONNECTOR_HUB", "DISCOVERY", "NONE"],
            ),
            creation_source_details=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "timeUpdated", "name"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log_analytics_entity",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(log_analytics_entities=result)


if __name__ == "__main__":
    main()

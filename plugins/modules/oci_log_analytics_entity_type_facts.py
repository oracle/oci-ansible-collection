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
module: oci_log_analytics_entity_type_facts
short_description: Fetches details about one or multiple LogAnalyticsEntityType resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LogAnalyticsEntityType resources in Oracle Cloud Infrastructure
    - Return a list of log analytics entity types.
    - If I(entity_type_name) is specified, the details of a single LogAnalyticsEntityType will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    entity_type_name:
        description:
            - Log analytics entity type name.
            - Required to get a specific log_analytics_entity_type.
        type: str
    name:
        description:
            - A filter to return only log analytics entity types whose name matches the entire name given. The match is
              case-insensitive.
        type: str
    name_contains:
        description:
            - A filter to return only log analytics entity types whose name or internalName contains name given. The match
              is case-insensitive.
        type: str
    cloud_type:
        description:
            - A filter to return CLOUD or NON_CLOUD entity types.
        type: str
        choices:
            - "CLOUD"
            - "NON_CLOUD"
            - "ALL"
    lifecycle_state:
        description:
            - A filter to return only those log analytics entities with the specified lifecycle state. The state
              value is case-insensitive.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated and timeUpdated
              is descending. Default order for name is ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific log_analytics_entity_type
  oci_log_analytics_entity_type_facts:
    # required
    namespace_name: namespace_name_example
    entity_type_name: entity_type_name_example

- name: List log_analytics_entity_types
  oci_log_analytics_entity_type_facts:
    # required
    namespace_name: namespace_name_example

    # optional
    name: name_example
    name_contains: name_contains_example
    cloud_type: CLOUD
    lifecycle_state: ACTIVE
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
log_analytics_entity_types:
    description:
        - List of LogAnalyticsEntityType resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Log analytics entity type name.
            returned: on success
            type: str
            sample: name_example
        internal_name:
            description:
                - Internal name for the log analytics entity type.
            returned: on success
            type: str
            sample: internal_name_example
        compartment_id:
            description:
                - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        category:
            description:
                - Log analytics entity type category. Category will be used for grouping and filtering.
            returned: on success
            type: str
            sample: category_example
        cloud_type:
            description:
                - Log analytics entity type group. That can be CLOUD (OCI) or NON_CLOUD otherwise.
            returned: on success
            type: str
            sample: CLOUD
        properties:
            description:
                - The parameters used in file patterns specified in log sources for this log analytics entity type.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Log analytics entity type property name.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - Description for the log analytics entity type property.
                    returned: on success
                    type: str
                    sample: description_example
        lifecycle_state:
            description:
                - The current lifecycle state of the log analytics entity.
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - Time the log analytics entity type was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time the log analytics entity type was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        management_agent_eligibility_status:
            description:
                - This field indicates whether logs for entities of this type can be collected using a management agent.
            returned: on success
            type: str
            sample: ELIGIBLE
    sample: [{
        "name": "name_example",
        "internal_name": "internal_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "category": "category_example",
        "cloud_type": "CLOUD",
        "properties": [{
            "name": "name_example",
            "description": "description_example"
        }],
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "management_agent_eligibility_status": "ELIGIBLE"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsEntityTypeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "entity_type_name",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_entity_type,
            namespace_name=self.module.params.get("namespace_name"),
            entity_type_name=self.module.params.get("entity_type_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "name_contains",
            "cloud_type",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_log_analytics_entity_types,
            namespace_name=self.module.params.get("namespace_name"),
            **optional_kwargs
        )


LogAnalyticsEntityTypeFactsHelperCustom = get_custom_class(
    "LogAnalyticsEntityTypeFactsHelperCustom"
)


class ResourceFactsHelper(
    LogAnalyticsEntityTypeFactsHelperCustom, LogAnalyticsEntityTypeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            entity_type_name=dict(type="str"),
            name=dict(type="str"),
            name_contains=dict(type="str"),
            cloud_type=dict(type="str", choices=["CLOUD", "NON_CLOUD", "ALL"]),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "timeUpdated", "name"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log_analytics_entity_type",
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

    module.exit_json(log_analytics_entity_types=result)


if __name__ == "__main__":
    main()

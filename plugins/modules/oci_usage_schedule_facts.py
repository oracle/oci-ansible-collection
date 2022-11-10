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
module: oci_usage_schedule_facts
short_description: Fetches details about one or multiple Schedule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Schedule resources in Oracle Cloud Infrastructure
    - Returns the saved schedule list.
    - If I(schedule_id) is specified, the details of a single Schedule will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    schedule_id:
        description:
            - The schedule unique OCID.
            - Required to get a specific schedule.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment ID in which to list resources.
            - Required to list multiple schedules.
        type: str
    sort_by:
        description:
            - The field to sort by. If not specified, the default is timeCreated.
        type: str
        choices:
            - "name"
            - "timeCreated"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    name:
        description:
            - Query parameter for filtering by name
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific schedule
  oci_usage_schedule_facts:
    # required
    schedule_id: "ocid1.schedule.oc1..xxxxxxEXAMPLExxxxxx"

- name: List schedules
  oci_usage_schedule_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: name
    sort_order: ASC
    name: name_example

"""

RETURN = """
schedules:
    description:
        - List of Schedule resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The tenancy of the customer
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        result_location:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                location_type:
                    description:
                        - Defines the type of location where the usage/cost CSVs will be stored
                    returned: on success
                    type: str
                    sample: OBJECT_STORAGE
                region:
                    description:
                        - The destination Object Store Region specified by customer
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                namespace:
                    description:
                        - The namespace needed to determine object storage bucket.
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket_name:
                    description:
                        - The bucket name where usage/cost CSVs will be uploaded
                    returned: on success
                    type: str
                    sample: bucket_name_example
        query_properties:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                group_by:
                    description:
                        - "Aggregate the result by. For example: [ \\"tagNamespace\\", \\"tagKey\\", \\"tagValue\\", \\"service\\", \\"skuName\\",
                          \\"skuPartNumber\\", \\"unit\\", \\"compartmentName\\", \\"compartmentPath\\", \\"compartmentId\\", \\"platform\\", \\"region\\",
                          \\"logicalAd\\", \\"resourceId\\", \\"tenantId\\", \\"tenantName\\" ]"
                    returned: on success
                    type: list
                    sample: []
                group_by_tag:
                    description:
                        - "GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: [ {
                          \\"namespace\\": \\"oracle\\", \\"key\\": \\"createdBy\\" ]"
                    returned: on success
                    type: complex
                    contains:
                        namespace:
                            description:
                                - The tag namespace.
                            returned: on success
                            type: str
                            sample: namespace_example
                        key:
                            description:
                                - The tag key.
                            returned: on success
                            type: str
                            sample: key_example
                        value:
                            description:
                                - The tag value.
                            returned: on success
                            type: str
                            sample: value_example
                filter:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        operator:
                            description:
                                - "The filter operator. Example: 'AND', 'OR', 'NOT'."
                            returned: on success
                            type: str
                            sample: AND
                        dimensions:
                            description:
                                - The dimensions to filter on.
                            returned: on success
                            type: complex
                            contains:
                                key:
                                    description:
                                        - The dimension key.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                value:
                                    description:
                                        - The dimension value.
                                    returned: on success
                                    type: str
                                    sample: value_example
                        tags:
                            description:
                                - The tags to filter on.
                            returned: on success
                            type: complex
                            contains:
                                namespace:
                                    description:
                                        - The tag namespace.
                                    returned: on success
                                    type: str
                                    sample: namespace_example
                                key:
                                    description:
                                        - The tag key.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                value:
                                    description:
                                        - The tag value.
                                    returned: on success
                                    type: str
                                    sample: value_example
                        filters:
                            description:
                                - The nested filter object.
                            returned: on success
                            type: complex
                            contains:
                                operator:
                                    description:
                                        - "The filter operator. Example: 'AND', 'OR', 'NOT'."
                                    returned: on success
                                    type: str
                                    sample: AND
                                dimensions:
                                    description:
                                        - The dimensions to filter on.
                                    returned: on success
                                    type: list
                                    sample: []
                                tags:
                                    description:
                                        - The tags to filter on.
                                    returned: on success
                                    type: list
                                    sample: []
                                filters:
                                    description:
                                        - The nested filter object.
                                    returned: on success
                                    type: list
                                    sample: []
                compartment_depth:
                    description:
                        - The depth level of the compartment.
                    returned: on success
                    type: float
                    sample: 10
                granularity:
                    description:
                        - "The usage granularity. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation.
                          Allowed values are:
                            DAILY
                            MONTHLY"
                    returned: on success
                    type: str
                    sample: DAILY
                query_type:
                    description:
                        - "The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data.
                          Allowed values are:
                            USAGE
                            COST
                            USAGE_AND_COST"
                    returned: on success
                    type: str
                    sample: USAGE
                is_aggregate_by_time:
                    description:
                        - Specifies whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.
                    returned: on success
                    type: bool
                    sample: true
                date_range:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        dynamic_date_range_type:
                            description:
                                - ""
                            returned: on success
                            type: str
                            sample: LAST_7_DAYS
                        date_range_type:
                            description:
                                - Defines whether the schedule date range is STATIC or DYNAMIC
                            returned: on success
                            type: str
                            sample: STATIC
                        time_usage_started:
                            description:
                                - The usage start time.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_usage_ended:
                            description:
                                - The usage end time.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The date and time of when the schedule was created
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        id:
            description:
                - The OCID representing unique shedule
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The unique name of the schedule created by the user
            returned: on success
            type: str
            sample: name_example
        schedule_recurrences:
            description:
                - "In x-obmcs-recurring-time format shown here: https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10
                  Describes the frequency of when the schedule will be run"
            returned: on success
            type: str
            sample: schedule_recurrences_example
        time_scheduled:
            description:
                - The date and time of the first time job execution
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  See L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\":
                  \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        lifecycle_state:
            description:
                - The lifecycle state of the schedule
            returned: on success
            type: str
            sample: ACTIVE
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "result_location": {
            "location_type": "OBJECT_STORAGE",
            "region": "us-phoenix-1",
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example"
        },
        "query_properties": {
            "group_by": [],
            "group_by_tag": [{
                "namespace": "namespace_example",
                "key": "key_example",
                "value": "value_example"
            }],
            "filter": {
                "operator": "AND",
                "dimensions": [{
                    "key": "key_example",
                    "value": "value_example"
                }],
                "tags": [{
                    "namespace": "namespace_example",
                    "key": "key_example",
                    "value": "value_example"
                }],
                "filters": [{
                    "operator": "AND",
                    "dimensions": [],
                    "tags": [],
                    "filters": []
                }]
            },
            "compartment_depth": 10,
            "granularity": "DAILY",
            "query_type": "USAGE",
            "is_aggregate_by_time": true,
            "date_range": {
                "dynamic_date_range_type": "LAST_7_DAYS",
                "date_range_type": "STATIC",
                "time_usage_started": "2013-10-20T19:20:30+01:00",
                "time_usage_ended": "2013-10-20T19:20:30+01:00"
            }
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "schedule_recurrences": "schedule_recurrences_example",
        "time_scheduled": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "lifecycle_state": "ACTIVE"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.usage_api import UsageapiClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScheduleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "schedule_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_schedule, schedule_id=self.module.params.get("schedule_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_schedules,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ScheduleFactsHelperCustom = get_custom_class("ScheduleFactsHelperCustom")


class ResourceFactsHelper(ScheduleFactsHelperCustom, ScheduleFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            schedule_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["name", "timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="schedule",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(schedules=result)


if __name__ == "__main__":
    main()

#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_usage_schedule
short_description: Manage a Schedule resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Schedule resource in Oracle Cloud Infrastructure
    - For I(state=present), returns the created schedule.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - The unique name of the user-created schedule.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The customer tenancy.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    saved_report_id:
        description:
            - The saved report id which can also be used to generate query.
        type: str
    schedule_recurrences:
        description:
            - "Specifies the frequency according to when the schedule will be run,
              in the x-obmcs-recurring-time format described in L(RFC 5545 section 3.3.10,https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10).
              Supported values are : ONE_TIME, DAILY, WEEKLY and MONTHLY."
            - Required for create using I(state=present).
        type: str
    time_scheduled:
        description:
            - The date and time of the first time job execution.
            - Required for create using I(state=present).
        type: str
    query_properties:
        description:
            - ""
        type: dict
        suboptions:
            group_by:
                description:
                    - "Aggregate the result by. For example: [ \\"tagNamespace\\", \\"tagKey\\", \\"tagValue\\", \\"service\\", \\"skuName\\",
                      \\"skuPartNumber\\", \\"unit\\", \\"compartmentName\\", \\"compartmentPath\\", \\"compartmentId\\", \\"platform\\", \\"region\\",
                      \\"logicalAd\\", \\"resourceId\\", \\"tenantId\\", \\"tenantName\\" ]"
                type: list
                elements: str
            group_by_tag:
                description:
                    - "GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: [ {
                      \\"namespace\\": \\"oracle\\", \\"key\\": \\"createdBy\\" ]"
                type: list
                elements: dict
                suboptions:
                    namespace:
                        description:
                            - The tag namespace.
                        type: str
                    key:
                        description:
                            - The tag key.
                        type: str
                    value:
                        description:
                            - The tag value.
                        type: str
            filter:
                description:
                    - ""
                type: dict
                suboptions:
                    operator:
                        description:
                            - "The filter operator. Example: 'AND', 'OR', 'NOT'."
                        type: str
                        choices:
                            - "AND"
                            - "NOT"
                            - "OR"
                    dimensions:
                        description:
                            - The dimensions to filter on.
                        type: list
                        elements: dict
                        suboptions:
                            key:
                                description:
                                    - The dimension key.
                                type: str
                                required: true
                            value:
                                description:
                                    - The dimension value.
                                type: str
                                required: true
                    tags:
                        description:
                            - The tags to filter on.
                        type: list
                        elements: dict
                        suboptions:
                            namespace:
                                description:
                                    - The tag namespace.
                                type: str
                            key:
                                description:
                                    - The tag key.
                                type: str
                            value:
                                description:
                                    - The tag value.
                                type: str
                    filters:
                        description:
                            - The nested filter object.
                        type: list
                        elements: dict
                        suboptions:
                            operator:
                                description:
                                    - "The filter operator. Example: 'AND', 'OR', 'NOT'."
                                type: str
                                choices:
                                    - "AND"
                                    - "NOT"
                                    - "OR"
                            dimensions:
                                description:
                                    - The dimensions to filter on.
                                type: list
                                elements: dict
                            tags:
                                description:
                                    - The tags to filter on.
                                type: list
                                elements: dict
                            filters:
                                description:
                                    - The nested filter object.
                                type: list
                                elements: dict
            compartment_depth:
                description:
                    - The depth level of the compartment.
                type: float
            granularity:
                description:
                    - "The usage granularity. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation.
                      Allowed values are:
                        DAILY
                        MONTHLY"
                type: str
                choices:
                    - "DAILY"
                    - "MONTHLY"
                required: true
            query_type:
                description:
                    - "The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data.
                      Allowed values are:
                        USAGE
                        COST
                        USAGE_AND_COST"
                type: str
                choices:
                    - "USAGE"
                    - "COST"
                    - "USAGE_AND_COST"
            is_aggregate_by_time:
                description:
                    - Specifies whether aggregated by time. If isAggregateByTime is true, all usage or cost over the query time period will be added up.
                type: bool
            date_range:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    time_usage_started:
                        description:
                            - The usage start time.
                            - Required when date_range_type is 'STATIC'
                        type: str
                    time_usage_ended:
                        description:
                            - The usage end time.
                            - Required when date_range_type is 'STATIC'
                        type: str
                    date_range_type:
                        description:
                            - Defines whether the schedule date range is STATIC or DYNAMIC.
                        type: str
                        choices:
                            - "STATIC"
                            - "DYNAMIC"
                        required: true
                    dynamic_date_range_type:
                        description:
                            - ""
                            - Required when date_range_type is 'DYNAMIC'
                        type: str
                        choices:
                            - "LAST_7_DAYS"
                            - "LAST_10_DAYS"
                            - "LAST_CALENDAR_WEEK"
                            - "LAST_CALENDAR_MONTH"
                            - "LAST_2_CALENDAR_MONTHS"
                            - "LAST_3_CALENDAR_MONTHS"
                            - "LAST_6_CALENDAR_MONTHS"
                            - "LAST_30_DAYS"
                            - "MONTH_TO_DATE"
                            - "LAST_YEAR"
                            - "YEAR_TODATE"
                            - "ALL"
    description:
        description:
            - The description of the schedule.
            - This parameter is updatable.
        type: str
    output_file_format:
        description:
            - Specifies supported output file format.
            - This parameter is updatable.
        type: str
        choices:
            - "CSV"
            - "PDF"
    result_location:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            location_type:
                description:
                    - Defines the type of location where the usage or cost CSVs will be stored.
                type: str
                choices:
                    - "OBJECT_STORAGE"
                required: true
            region:
                description:
                    - The destination Object Store Region specified by the customer.
                type: str
                required: true
            namespace:
                description:
                    - The namespace needed to determine the object storage bucket.
                type: str
                required: true
            bucket_name:
                description:
                    - The bucket name where usage or cost CSVs will be uploaded.
                type: str
                required: true
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              See L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    schedule_id:
        description:
            - The schedule unique OCID.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Schedule.
            - Use I(state=present) to create or update a Schedule.
            - Use I(state=absent) to delete a Schedule.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create schedule
  oci_usage_schedule:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    schedule_recurrences: schedule_recurrences_example
    time_scheduled: time_scheduled_example
    result_location:
      # required
      location_type: OBJECT_STORAGE
      region: us-phoenix-1
      namespace: namespace_example
      bucket_name: bucket_name_example

    # optional
    saved_report_id: "ocid1.savedreport.oc1..xxxxxxEXAMPLExxxxxx"
    query_properties:
      # required
      granularity: DAILY
      date_range:
        # required
        time_usage_started: time_usage_started_example
        time_usage_ended: time_usage_ended_example
        date_range_type: STATIC

        # optional
      group_by: [ "group_by_example" ]
      group_by_tag:
      - # optional
        namespace: namespace_example
        key: key_example
        value: value_example
      filter:
        # optional
        operator: AND
        dimensions:
        - # required
          key: key_example
          value: value_example
        tags:
        - # optional
          namespace: namespace_example
          key: key_example
          value: value_example
        filters:
        - # optional
          operator: AND
          dimensions: [ "dimensions_example" ]
          tags: [ "tags_example" ]
          filters: [ "filters_example" ]
      compartment_depth: 3.4
      query_type: USAGE
      is_aggregate_by_time: true
    description: description_example
    output_file_format: CSV
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update schedule
  oci_usage_schedule:
    # required
    schedule_id: "ocid1.schedule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    output_file_format: CSV
    result_location:
      # required
      location_type: OBJECT_STORAGE
      region: us-phoenix-1
      namespace: namespace_example
      bucket_name: bucket_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update schedule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_usage_schedule:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    output_file_format: CSV
    result_location:
      # required
      location_type: OBJECT_STORAGE
      region: us-phoenix-1
      namespace: namespace_example
      bucket_name: bucket_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete schedule
  oci_usage_schedule:
    # required
    schedule_id: "ocid1.schedule.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete schedule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_usage_schedule:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
schedule:
    description:
        - Details of the Schedule resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID representing a unique shedule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The unique name of the schedule created by the user.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - The customer tenancy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        result_location:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                location_type:
                    description:
                        - Defines the type of location where the usage or cost CSVs will be stored.
                    returned: on success
                    type: str
                    sample: OBJECT_STORAGE
                region:
                    description:
                        - The destination Object Store Region specified by the customer.
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                namespace:
                    description:
                        - The namespace needed to determine the object storage bucket.
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket_name:
                    description:
                        - The bucket name where usage or cost CSVs will be uploaded.
                    returned: on success
                    type: str
                    sample: bucket_name_example
        description:
            description:
                - The description of the schedule.
            returned: on success
            type: str
            sample: description_example
        time_next_run:
            description:
                - The date and time of the next job execution.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        output_file_format:
            description:
                - Specifies supported output file format.
            returned: on success
            type: str
            sample: CSV
        saved_report_id:
            description:
                - The saved report id which can also be used to generate query.
            returned: on success
            type: str
            sample: "ocid1.savedreport.oc1..xxxxxxEXAMPLExxxxxx"
        schedule_recurrences:
            description:
                - "Specifies the frequency according to when the schedule will be run,
                  in the x-obmcs-recurring-time format described in L(RFC 5545 section 3.3.10,https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10).
                  Supported values are : ONE_TIME, DAILY, WEEKLY and MONTHLY."
            returned: on success
            type: str
            sample: schedule_recurrences_example
        time_scheduled:
            description:
                - The date and time of the first time job execution.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        query_properties:
            description:
                - ""
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
                        - Specifies whether aggregated by time. If isAggregateByTime is true, all usage or cost over the query time period will be added up.
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
                                - Defines whether the schedule date range is STATIC or DYNAMIC.
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
                - The date and time the schedule was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The schedule lifecycle state.
            returned: on success
            type: str
            sample: ACTIVE
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "result_location": {
            "location_type": "OBJECT_STORAGE",
            "region": "us-phoenix-1",
            "namespace": "namespace_example",
            "bucket_name": "bucket_name_example"
        },
        "description": "description_example",
        "time_next_run": "2013-10-20T19:20:30+01:00",
        "output_file_format": "CSV",
        "saved_report_id": "ocid1.savedreport.oc1..xxxxxxEXAMPLExxxxxx",
        "schedule_recurrences": "schedule_recurrences_example",
        "time_scheduled": "2013-10-20T19:20:30+01:00",
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
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.usage_api import UsageapiClient
    from oci.usage_api.models import CreateScheduleDetails
    from oci.usage_api.models import UpdateScheduleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScheduleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ScheduleHelperGen, self).get_possible_entity_types() + [
            "schedule",
            "schedules",
            "usageApischedule",
            "usageApischedules",
            "scheduleresource",
            "schedulesresource",
            "usageapi",
        ]

    def get_module_resource_id_param(self):
        return "schedule_id"

    def get_module_resource_id(self):
        return self.module.params.get("schedule_id")

    def get_get_fn(self):
        return self.client.get_schedule

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_schedule, schedule_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_schedule, schedule_id=self.module.params.get("schedule_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(self.client.list_schedules, **kwargs)

    def get_create_model_class(self):
        return CreateScheduleDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(create_schedule_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateScheduleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_schedule_details=update_details,
                schedule_id=self.module.params.get("schedule_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(schedule_id=self.module.params.get("schedule_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ScheduleHelperCustom = get_custom_class("ScheduleHelperCustom")


class ResourceHelper(ScheduleHelperCustom, ScheduleHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            saved_report_id=dict(type="str"),
            schedule_recurrences=dict(type="str"),
            time_scheduled=dict(type="str"),
            query_properties=dict(
                type="dict",
                options=dict(
                    group_by=dict(type="list", elements="str"),
                    group_by_tag=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            namespace=dict(type="str"),
                            key=dict(type="str", no_log=True),
                            value=dict(type="str"),
                        ),
                    ),
                    filter=dict(
                        type="dict",
                        options=dict(
                            operator=dict(type="str", choices=["AND", "NOT", "OR"]),
                            dimensions=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    key=dict(type="str", required=True, no_log=True),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                            tags=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    namespace=dict(type="str"),
                                    key=dict(type="str", no_log=True),
                                    value=dict(type="str"),
                                ),
                            ),
                            filters=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    operator=dict(
                                        type="str", choices=["AND", "NOT", "OR"]
                                    ),
                                    dimensions=dict(type="list", elements="dict"),
                                    tags=dict(type="list", elements="dict"),
                                    filters=dict(type="list", elements="dict"),
                                ),
                            ),
                        ),
                    ),
                    compartment_depth=dict(type="float"),
                    granularity=dict(
                        type="str", required=True, choices=["DAILY", "MONTHLY"]
                    ),
                    query_type=dict(
                        type="str", choices=["USAGE", "COST", "USAGE_AND_COST"]
                    ),
                    is_aggregate_by_time=dict(type="bool"),
                    date_range=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            time_usage_started=dict(type="str"),
                            time_usage_ended=dict(type="str"),
                            date_range_type=dict(
                                type="str", required=True, choices=["STATIC", "DYNAMIC"]
                            ),
                            dynamic_date_range_type=dict(
                                type="str",
                                choices=[
                                    "LAST_7_DAYS",
                                    "LAST_10_DAYS",
                                    "LAST_CALENDAR_WEEK",
                                    "LAST_CALENDAR_MONTH",
                                    "LAST_2_CALENDAR_MONTHS",
                                    "LAST_3_CALENDAR_MONTHS",
                                    "LAST_6_CALENDAR_MONTHS",
                                    "LAST_30_DAYS",
                                    "MONTH_TO_DATE",
                                    "LAST_YEAR",
                                    "YEAR_TODATE",
                                    "ALL",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            description=dict(type="str"),
            output_file_format=dict(type="str", choices=["CSV", "PDF"]),
            result_location=dict(
                type="dict",
                options=dict(
                    location_type=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE"]
                    ),
                    region=dict(type="str", required=True),
                    namespace=dict(type="str", required=True),
                    bucket_name=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            schedule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="schedule",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

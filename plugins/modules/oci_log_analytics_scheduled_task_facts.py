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
module: oci_log_analytics_scheduled_task_facts
short_description: Fetches details about one or multiple ScheduledTask resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ScheduledTask resources in Oracle Cloud Infrastructure
    - Lists scheduled tasks.
    - If I(scheduled_task_id) is specified, the details of a single ScheduledTask will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    scheduled_task_id:
        description:
            - Unique scheduledTask id returned from task create.
              If invalid will lead to a 404 not found.
            - Required to get a specific scheduled_task.
        type: str
        aliases: ["id"]
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    task_type:
        description:
            - Required parameter to specify schedule task type.
            - Required to list multiple scheduled_tasks.
        type: str
        choices:
            - "SAVED_SEARCH"
            - "ACCELERATION"
            - "PURGE"
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple scheduled_tasks.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "displayName"
    saved_search_id:
        description:
            - A filter to return only scheduled tasks whose stream action savedSearchId matches the given
              ManagementSavedSearch id [OCID] exactly.
        type: str
    display_name_contains:
        description:
            - A filter to return only resources whose display name contains the substring.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific scheduled_task
  oci_log_analytics_scheduled_task_facts:
    # required
    scheduled_task_id: "ocid1.scheduledtask.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_name: namespace_name_example

- name: List scheduled_tasks
  oci_log_analytics_scheduled_task_facts:
    # required
    namespace_name: namespace_name_example
    task_type: SAVED_SEARCH
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated
    saved_search_id: "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx"
    display_name_contains: display_name_contains_example

"""

RETURN = """
scheduled_tasks:
    description:
        - List of ScheduledTask resources
    returned: on success
    type: complex
    contains:
        kind:
            description:
                - Discriminator.
                - Returned for get operation
            returned: on success
            type: str
            sample: ACCELERATION
        schedules:
            description:
                - Schedules.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                expression:
                    description:
                        - Value in cron format.
                    returned: on success
                    type: str
                    sample: expression_example
                time_zone:
                    description:
                        - Time zone, by default UTC.
                    returned: on success
                    type: str
                    sample: time_zone_example
                type:
                    description:
                        - Schedule type discriminator.
                    returned: on success
                    type: str
                    sample: FIXED_FREQUENCY
                misfire_policy:
                    description:
                        - Schedule misfire retry policy.
                    returned: on success
                    type: str
                    sample: RETRY_ONCE
                time_of_first_execution:
                    description:
                        - The date and time the scheduled task should execute first time after create or update;
                          thereafter the task will execute as specified in the schedule.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                recurring_interval:
                    description:
                        - Recurring interval in ISO 8601 extended format as described in
                          https://en.wikipedia.org/wiki/ISO_8601#Durations.
                          The largest supported unit is D, e.g. P14D (not P2W).
                          The value must be at least 5 minutes (PT5M) and at most 3 weeks (P21D or PT30240M).
                    returned: on success
                    type: str
                    sample: recurring_interval_example
                repeat_count:
                    description:
                        - Number of times (0-based) to execute until auto-stop.
                          Default value -1 will execute indefinitely.
                          Value 0 will execute once.
                    returned: on success
                    type: int
                    sample: 56
        action:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                query_string:
                    description:
                        - Purge query string.
                    returned: on success
                    type: str
                    sample: query_string_example
                data_type:
                    description:
                        - the type of the log data to be purged
                    returned: on success
                    type: str
                    sample: LOG
                purge_duration:
                    description:
                        - The duration of data to be retained, which is used to
                          calculate the timeDataEnded when the task fires.
                          The value should be negative.
                          Purge duration in ISO 8601 extended format as described in
                          https://en.wikipedia.org/wiki/ISO_8601#Durations.
                          The largest supported unit is D, e.g. -P365D (not -P1Y) or -P14D (not -P2W).
                    returned: on success
                    type: str
                    sample: purge_duration_example
                purge_compartment_id:
                    description:
                        - the compartment OCID under which the data will be purged
                    returned: on success
                    type: str
                    sample: "ocid1.purgecompartment.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id_in_subtree:
                    description:
                        - if true, purge child compartments data
                    returned: on success
                    type: bool
                    sample: true
                type:
                    description:
                        - Action type discriminator.
                    returned: on success
                    type: str
                    sample: STREAM
                saved_search_id:
                    description:
                        - The ManagementSavedSearch id [OCID] utilized in the action.
                    returned: on success
                    type: str
                    sample: "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx"
                metric_extraction:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        compartment_id:
                            description:
                                - The compartment OCID (/iaas/Content/General/Concepts/identifiers.htm) of the extracted metric.
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        namespace:
                            description:
                                - The namespace of the extracted metric.
                                  A valid value starts with an alphabetical character and includes only
                                  alphanumeric characters and underscores (_).
                            returned: on success
                            type: str
                            sample: namespace_example
                        metric_name:
                            description:
                                - The metric name of the extracted metric.
                                  A valid value starts with an alphabetical character and includes only
                                  alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
                            returned: on success
                            type: str
                            sample: metric_name_example
                        resource_group:
                            description:
                                - The resourceGroup of the extracted metric.
                                  A valid value starts with an alphabetical character and includes only
                                  alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
                            returned: on success
                            type: str
                            sample: resource_group_example
                saved_search_duration:
                    description:
                        - The duration of data to be searched for SAVED_SEARCH tasks,
                          used when the task fires to calculate the query time range.
                        - Duration in ISO 8601 extended format as described in
                          https://en.wikipedia.org/wiki/ISO_8601#Durations.
                          The value should be positive.
                          The largest supported unit (as opposed to value) is D, e.g.  P14D (not P2W).
                        - "There are restrictions on the maximum duration value relative to the task schedule
                          value as specified in the following table.
                             Schedule Interval Range          | Maximum Duration
                          ----------------------------------- | -----------------
                            5 Minutes     to 30 Minutes       |   1 hour  \\"PT60M\\"
                           31 Minutes     to  1 Hour          |  12 hours \\"PT720M\\"
                           1 Hour+1Minute to  1 Day           |   1 day   \\"P1D\\"
                           1 Day+1Minute  to  1 Week-1Minute  |   7 days  \\"P7D\\"
                           1 Week         to  2 Weeks         |  14 days  \\"P14D\\"
                           greater than 2 Weeks               |  30 days  \\"P30D\\""
                        - "If not specified, the duration will be based on the schedule. For example,
                          if the schedule is every 5 minutes then the savedSearchDuration will be \\"PT5M\\";
                          if the schedule is every 3 weeks then the savedSearchDuration will be \\"P21D\\"."
                    returned: on success
                    type: str
                    sample: saved_search_duration_example
        num_occurrences:
            description:
                - Number of execution occurrences.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        time_of_next_execution:
            description:
                - The date and time the scheduled task will execute next,
                  in the format defined by RFC3339.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the data plane resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        task_type:
            description:
                - Task type.
            returned: on success
            type: str
            sample: SAVED_SEARCH
        compartment_id:
            description:
                - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the scheduled task was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the scheduled task was last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the scheduled task.
            returned: on success
            type: str
            sample: ACTIVE
        task_status:
            description:
                - Status of the scheduled task.
            returned: on success
            type: str
            sample: READY
        pause_reason:
            description:
                - reason for taskStatus PAUSED.
            returned: on success
            type: str
            sample: METRIC_EXTRACTION_NOT_VALID
        work_request_id:
            description:
                - most recent Work Request Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the asynchronous
                  request.
            returned: on success
            type: str
            sample: "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - "A user-friendly name that is changeable and that does not have to be unique.
                  Format: a leading alphanumeric, followed by zero or more
                  alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
                  No trailing spaces allowed."
            returned: on success
            type: str
            sample: display_name_example
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
        last_execution_status:
            description:
                - The most recent task execution status.
            returned: on success
            type: str
            sample: FAILED
        time_last_executed:
            description:
                - The date and time the scheduled task last executed, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "kind": "ACCELERATION",
        "schedules": [{
            "expression": "expression_example",
            "time_zone": "time_zone_example",
            "type": "FIXED_FREQUENCY",
            "misfire_policy": "RETRY_ONCE",
            "time_of_first_execution": "2013-10-20T19:20:30+01:00",
            "recurring_interval": "recurring_interval_example",
            "repeat_count": 56
        }],
        "action": {
            "query_string": "query_string_example",
            "data_type": "LOG",
            "purge_duration": "purge_duration_example",
            "purge_compartment_id": "ocid1.purgecompartment.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id_in_subtree": true,
            "type": "STREAM",
            "saved_search_id": "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx",
            "metric_extraction": {
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "namespace": "namespace_example",
                "metric_name": "metric_name_example",
                "resource_group": "resource_group_example"
            },
            "saved_search_duration": "saved_search_duration_example"
        },
        "num_occurrences": 56,
        "time_of_next_execution": "2013-10-20T19:20:30+01:00",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "task_type": "SAVED_SEARCH",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "task_status": "READY",
        "pause_reason": "METRIC_EXTRACTION_NOT_VALID",
        "work_request_id": "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "last_execution_status": "FAILED",
        "time_last_executed": "2013-10-20T19:20:30+01:00"
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


class ScheduledTaskFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "scheduled_task_id",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "task_type",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_scheduled_task,
            namespace_name=self.module.params.get("namespace_name"),
            scheduled_task_id=self.module.params.get("scheduled_task_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
            "saved_search_id",
            "display_name_contains",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_scheduled_tasks,
            namespace_name=self.module.params.get("namespace_name"),
            task_type=self.module.params.get("task_type"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ScheduledTaskFactsHelperCustom = get_custom_class("ScheduledTaskFactsHelperCustom")


class ResourceFactsHelper(ScheduledTaskFactsHelperCustom, ScheduledTaskFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            scheduled_task_id=dict(aliases=["id"], type="str"),
            namespace_name=dict(type="str", required=True),
            task_type=dict(
                type="str", choices=["SAVED_SEARCH", "ACCELERATION", "PURGE"]
            ),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["timeCreated", "timeUpdated", "displayName"]
            ),
            saved_search_id=dict(type="str"),
            display_name_contains=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="scheduled_task",
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

    module.exit_json(scheduled_tasks=result)


if __name__ == "__main__":
    main()

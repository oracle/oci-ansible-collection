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
module: oci_log_analytics_scheduled_task_actions
short_description: Perform actions on a ScheduledTask resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ScheduledTask resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), move the scheduled task into a different compartment within the same tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    scheduled_task_id:
        description:
            - Unique scheduledTask id returned from task create.
              If invalid will lead to a 404 not found.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    action:
        description:
            - The action to perform on the ScheduledTask.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on scheduled_task
  oci_log_analytics_scheduled_task_actions:
    # required
    namespace_name: namespace_name_example
    scheduled_task_id: "ocid1.scheduledtask.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
scheduled_task:
    description:
        - Details of the ScheduledTask resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        kind:
            description:
                - Discriminator.
            returned: on success
            type: str
            sample: ACCELERATION
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the data plane resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - "A user-friendly name that is changeable and that does not have to be unique.
                  Format: a leading alphanumeric, followed by zero or more
                  alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
                  No trailing spaces allowed."
            returned: on success
            type: str
            sample: display_name_example
        task_type:
            description:
                - Task type.
            returned: on success
            type: str
            sample: SAVED_SEARCH
        schedules:
            description:
                - Schedules.
            returned: on success
            type: complex
            contains:
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
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Action type discriminator.
                    returned: on success
                    type: str
                    sample: STREAM
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
        num_occurrences:
            description:
                - Number of execution occurrences.
            returned: on success
            type: int
            sample: 56
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
        time_of_next_execution:
            description:
                - The date and time the scheduled task will execute next,
                  in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the scheduled task.
            returned: on success
            type: str
            sample: ACTIVE
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
    sample: {
        "kind": "ACCELERATION",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "task_type": "SAVED_SEARCH",
        "schedules": [{
            "type": "FIXED_FREQUENCY",
            "misfire_policy": "RETRY_ONCE",
            "time_of_first_execution": "2013-10-20T19:20:30+01:00",
            "expression": "expression_example",
            "time_zone": "time_zone_example",
            "recurring_interval": "recurring_interval_example",
            "repeat_count": 56
        }],
        "action": {
            "type": "STREAM",
            "query_string": "query_string_example",
            "data_type": "LOG",
            "purge_duration": "purge_duration_example",
            "purge_compartment_id": "ocid1.purgecompartment.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id_in_subtree": true,
            "saved_search_id": "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx",
            "metric_extraction": {
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "namespace": "namespace_example",
                "metric_name": "metric_name_example",
                "resource_group": "resource_group_example"
            },
            "saved_search_duration": "saved_search_duration_example"
        },
        "task_status": "READY",
        "pause_reason": "METRIC_EXTRACTION_NOT_VALID",
        "work_request_id": "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx",
        "num_occurrences": 56,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_of_next_execution": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "last_execution_status": "FAILED",
        "time_last_executed": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import ChangeScheduledTaskCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScheduledTaskActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "scheduled_task_id"

    def get_module_resource_id(self):
        return self.module.params.get("scheduled_task_id")

    def get_get_fn(self):
        return self.client.get_scheduled_task

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_scheduled_task,
            namespace_name=self.module.params.get("namespace_name"),
            scheduled_task_id=self.module.params.get("scheduled_task_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeScheduledTaskCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_scheduled_task_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                scheduled_task_id=self.module.params.get("scheduled_task_id"),
                change_scheduled_task_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ScheduledTaskActionsHelperCustom = get_custom_class("ScheduledTaskActionsHelperCustom")


class ResourceHelper(ScheduledTaskActionsHelperCustom, ScheduledTaskActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            scheduled_task_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="scheduled_task",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

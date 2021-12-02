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
module: oci_log_analytics_scheduled_task
short_description: Manage a ScheduledTask resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ScheduledTask resource in Oracle Cloud Infrastructure
    - For I(state=present), schedule a task as specified and return task info.
    - "This resource has the following action operations in the M(oracle.oci.oci_log_analytics_scheduled_task_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    kind:
        description:
            - Discriminator.
            - Required for create using I(state=present), update using I(state=present) with scheduled_task_id present.
        type: str
        choices:
            - "STANDARD"
            - "ACCELERATION"
    compartment_id:
        description:
            - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - "A user-friendly name that is changeable and that does not have to be unique.
              Format: a leading alphanumeric, followed by zero or more
              alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
              No trailing spaces allowed."
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
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
    task_type:
        description:
            - Task type.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required when kind is 'STANDARD'
        type: str
        choices:
            - "SAVED_SEARCH"
            - "ACCELERATION"
            - "PURGE"
            - "ACCELERATION_MAINTENANCE"
    schedules:
        description:
            - Schedules, typically a single schedule.
              Note there may only be a single schedule for SAVED_SEARCH and PURGE scheduled tasks.
            - This parameter is updatable.
            - Required when kind is 'STANDARD'
        type: list
        elements: dict
        suboptions:
            type:
                description:
                    - Schedule type discriminator.
                type: str
                choices:
                    - "CRON"
                    - "FIXED_FREQUENCY"
                required: true
            misfire_policy:
                description:
                    - Schedule misfire retry policy.
                type: str
                choices:
                    - "RETRY_ONCE"
                    - "RETRY_INDEFINITELY"
                    - "SKIP"
            time_of_first_execution:
                description:
                    - The date and time the scheduled task should execute first time after create or update;
                      thereafter the task will execute as specified in the schedule.
                type: str
            expression:
                description:
                    - Value in cron format.
                    - Required when type is 'CRON'
                type: str
            time_zone:
                description:
                    - Time zone, by default UTC.
                    - Required when type is 'CRON'
                type: str
            recurring_interval:
                description:
                    - Recurring interval in ISO 8601 extended format as described in
                      https://en.wikipedia.org/wiki/ISO_8601#Durations.
                      The largest supported unit is D, e.g. P14D (not P2W).
                      The value must be at least 5 minutes (PT5M) and at most 3 weeks (P21D or PT30240M).
                    - Required when type is 'FIXED_FREQUENCY'
                type: str
            repeat_count:
                description:
                    - Number of times (0-based) to execute until auto-stop.
                      Default value -1 will execute indefinitely.
                      Value 0 will execute once.
                    - Applicable when type is 'FIXED_FREQUENCY'
                type: int
    action:
        description:
            - ""
            - This parameter is updatable.
            - Required when kind is 'STANDARD'
        type: dict
        suboptions:
            type:
                description:
                    - Action type discriminator.
                type: str
                choices:
                    - "PURGE"
                    - "STREAM"
                required: true
            query_string:
                description:
                    - Purge query string.
                    - Required when type is 'PURGE'
                type: str
            data_type:
                description:
                    - the type of the log data to be purged
                    - Required when type is 'PURGE'
                type: str
                choices:
                    - "LOG"
                    - "LOOKUP"
            purge_duration:
                description:
                    - The duration of data to be retained, which is used to
                      calculate the timeDataEnded when the task fires.
                      The value should be negative.
                      Purge duration in ISO 8601 extended format as described in
                      https://en.wikipedia.org/wiki/ISO_8601#Durations.
                      The largest supported unit is D, e.g. -P365D (not -P1Y) or -P14D (not -P2W).
                    - Required when type is 'PURGE'
                type: str
            purge_compartment_id:
                description:
                    - the compartment OCID under which the data will be purged
                    - Required when type is 'PURGE'
                type: str
            compartment_id_in_subtree:
                description:
                    - if true, purge child compartments data
                    - Applicable when type is 'PURGE'
                type: bool
            saved_search_id:
                description:
                    - The ManagementSavedSearch id [OCID] utilized in the action.
                    - Applicable when type is 'STREAM'
                type: str
            metric_extraction:
                description:
                    - ""
                    - Applicable when type is 'STREAM'
                type: dict
                suboptions:
                    compartment_id:
                        description:
                            - The compartment OCID (/iaas/Content/General/Concepts/identifiers.htm) of the extracted metric.
                            - Required when type is 'STREAM'
                        type: str
                        required: true
                    namespace:
                        description:
                            - The namespace of the extracted metric.
                              A valid value starts with an alphabetical character and includes only
                              alphanumeric characters and underscores (_).
                            - Required when type is 'STREAM'
                        type: str
                        required: true
                    metric_name:
                        description:
                            - The metric name of the extracted metric.
                              A valid value starts with an alphabetical character and includes only
                              alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
                            - Required when type is 'STREAM'
                        type: str
                        required: true
                    resource_group:
                        description:
                            - The resourceGroup of the extracted metric.
                              A valid value starts with an alphabetical character and includes only
                              alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($).
                            - Applicable when type is 'STREAM'
                        type: str
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
                    - Applicable when type is 'STREAM'
                type: str
    saved_search_id:
        description:
            - The ManagementSavedSearch id [OCID] to be accelerated.
            - Required when kind is 'ACCELERATION'
        type: str
    scheduled_task_id:
        description:
            - Unique scheduledTask id returned from task create.
              If invalid will lead to a 404 not found.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ScheduledTask.
            - Use I(state=present) to create or update a ScheduledTask.
            - Use I(state=absent) to delete a ScheduledTask.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create scheduled_task with kind = STANDARD
  oci_log_analytics_scheduled_task:
    # required
    kind: STANDARD
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    task_type: SAVED_SEARCH

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    schedules:
    - # required
      type: CRON
      expression: expression_example
      time_zone: time_zone_example

      # optional
      misfire_policy: RETRY_ONCE
      time_of_first_execution: 2013-10-20T19:20:30+01:00
    action:
      # required
      type: PURGE
      query_string: query_string_example
      data_type: LOG
      purge_duration: purge_duration_example
      purge_compartment_id: "ocid1.purgecompartment.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      compartment_id_in_subtree: true

- name: Create scheduled_task with kind = ACCELERATION
  oci_log_analytics_scheduled_task:
    # required
    kind: ACCELERATION
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    saved_search_id: "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update scheduled_task with kind = STANDARD
  oci_log_analytics_scheduled_task:
    # required
    kind: STANDARD

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    schedules:
    - # required
      type: CRON
      expression: expression_example
      time_zone: time_zone_example

      # optional
      misfire_policy: RETRY_ONCE
      time_of_first_execution: 2013-10-20T19:20:30+01:00
    action:
      # required
      type: PURGE
      query_string: query_string_example
      data_type: LOG
      purge_duration: purge_duration_example
      purge_compartment_id: "ocid1.purgecompartment.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      compartment_id_in_subtree: true

- name: Update scheduled_task with kind = ACCELERATION
  oci_log_analytics_scheduled_task:
    # required
    kind: ACCELERATION

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update scheduled_task using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with kind = STANDARD
  oci_log_analytics_scheduled_task:
    # required
    kind: STANDARD
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    task_type: SAVED_SEARCH

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    schedules:
    - # required
      type: CRON
      expression: expression_example
      time_zone: time_zone_example

      # optional
      misfire_policy: RETRY_ONCE
      time_of_first_execution: 2013-10-20T19:20:30+01:00
    action:
      # required
      type: PURGE
      query_string: query_string_example
      data_type: LOG
      purge_duration: purge_duration_example
      purge_compartment_id: "ocid1.purgecompartment.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      compartment_id_in_subtree: true

- name: Update scheduled_task using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with kind = ACCELERATION
  oci_log_analytics_scheduled_task:
    # required
    kind: ACCELERATION
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete scheduled_task
  oci_log_analytics_scheduled_task:
    # required
    namespace_name: namespace_name_example
    scheduled_task_id: "ocid1.scheduledtask.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete scheduled_task using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_log_analytics_scheduled_task:
    # required
    namespace_name: namespace_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    task_type: SAVED_SEARCH
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import CreateScheduledTaskDetails
    from oci.log_analytics.models import UpdateScheduledTaskDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScheduledTaskHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "namespace_name",
            "task_type",
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "saved_search_id"]

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
            self.client.list_scheduled_tasks, **kwargs
        )

    def get_create_model_class(self):
        return CreateScheduledTaskDetails

    def get_exclude_attributes(self):
        return ["saved_search_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_scheduled_task,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                create_scheduled_task_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateScheduledTaskDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_scheduled_task,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                scheduled_task_id=self.module.params.get("scheduled_task_id"),
                update_scheduled_task_details=update_details,
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
            call_fn=self.client.delete_scheduled_task,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                scheduled_task_id=self.module.params.get("scheduled_task_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ScheduledTaskHelperCustom = get_custom_class("ScheduledTaskHelperCustom")


class ResourceHelper(ScheduledTaskHelperCustom, ScheduledTaskHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            kind=dict(type="str", choices=["STANDARD", "ACCELERATION"]),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            task_type=dict(
                type="str",
                choices=[
                    "SAVED_SEARCH",
                    "ACCELERATION",
                    "PURGE",
                    "ACCELERATION_MAINTENANCE",
                ],
            ),
            schedules=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(
                        type="str", required=True, choices=["CRON", "FIXED_FREQUENCY"]
                    ),
                    misfire_policy=dict(
                        type="str", choices=["RETRY_ONCE", "RETRY_INDEFINITELY", "SKIP"]
                    ),
                    time_of_first_execution=dict(type="str"),
                    expression=dict(type="str"),
                    time_zone=dict(type="str"),
                    recurring_interval=dict(type="str"),
                    repeat_count=dict(type="int"),
                ),
            ),
            action=dict(
                type="dict",
                options=dict(
                    type=dict(type="str", required=True, choices=["PURGE", "STREAM"]),
                    query_string=dict(type="str"),
                    data_type=dict(type="str", choices=["LOG", "LOOKUP"]),
                    purge_duration=dict(type="str"),
                    purge_compartment_id=dict(type="str"),
                    compartment_id_in_subtree=dict(type="bool"),
                    saved_search_id=dict(type="str"),
                    metric_extraction=dict(
                        type="dict",
                        options=dict(
                            compartment_id=dict(type="str", required=True),
                            namespace=dict(type="str", required=True),
                            metric_name=dict(type="str", required=True),
                            resource_group=dict(type="str"),
                        ),
                    ),
                    saved_search_duration=dict(type="str"),
                ),
            ),
            saved_search_id=dict(type="str"),
            scheduled_task_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

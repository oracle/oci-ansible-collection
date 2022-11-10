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
module: oci_monitoring_alarm_history_collection_facts
short_description: Fetches details about a AlarmHistoryCollection resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AlarmHistoryCollection resource in Oracle Cloud Infrastructure
    - Get the history of the specified alarm.
      For important limits information, see L(Limits on
      Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits).
    - This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
      Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
      or transactions, per second (TPS) for a given tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    alarm_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of an alarm.
        type: str
        aliases: ["id"]
        required: true
    alarm_historytype:
        description:
            - The type of history entries to retrieve. State history (STATE_HISTORY) or state transition history (STATE_TRANSITION_HISTORY).
              If not specified, entries of both types are retrieved.
            - "Example: `STATE_HISTORY`"
        type: str
        choices:
            - "STATE_HISTORY"
            - "STATE_TRANSITION_HISTORY"
    timestamp_greater_than_or_equal_to:
        description:
            - A filter to return only alarm history entries with timestamps occurring on or after the specified date and time. Format defined by RFC3339.
            - "Example: `2019-01-01T01:00:00.789Z`"
        type: str
    timestamp_less_than:
        description:
            - A filter to return only alarm history entries with timestamps occurring before the specified date and time. Format defined by RFC3339.
            - "Example: `2019-01-02T01:00:00.789Z`"
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific alarm_history_collection
  oci_monitoring_alarm_history_collection_facts:
    # required
    alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    alarm_historytype: STATE_HISTORY
    timestamp_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    timestamp_less_than: 2013-10-20T19:20:30+01:00

"""

RETURN = """
alarm_history_collection:
    description:
        - AlarmHistoryCollection resource
    returned: on success
    type: complex
    contains:
        alarm_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm for which to retrieve history.
            returned: on success
            type: str
            sample: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"
        is_enabled:
            description:
                - Whether the alarm is enabled.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        entries:
            description:
                - The set of history entries retrieved for the alarm.
            returned: on success
            type: complex
            contains:
                summary:
                    description:
                        - Description for this alarm history entry.
                        - "Example 1 - alarm state history entry: `The alarm state is FIRING`"
                        - "Example 2 - alarm state transition history entry: `State transitioned from OK to Firing`"
                    returned: on success
                    type: str
                    sample: summary_example
                timestamp:
                    description:
                        - Timestamp for this alarm history entry. Format defined by RFC3339.
                        - "Example: `2019-02-01T01:02:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                timestamp_triggered:
                    description:
                        - "Timestamp for the transition of the alarm state. For example, the time when the alarm transitioned from OK to Firing.
                          Available for state transition entries only. Note: A three-minute lag for this value accounts for any late-arriving metrics."
                        - "Example: `2019-02-01T0:59:00.789Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "alarm_id": "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx",
        "is_enabled": true,
        "entries": [{
            "summary": "summary_example",
            "timestamp": "2013-10-20T19:20:30+01:00",
            "timestamp_triggered": "2013-10-20T19:20:30+01:00"
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.monitoring import MonitoringClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AlarmHistoryCollectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "alarm_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "alarm_historytype",
            "timestamp_greater_than_or_equal_to",
            "timestamp_less_than",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_alarm_history,
            alarm_id=self.module.params.get("alarm_id"),
            **optional_kwargs
        )


AlarmHistoryCollectionFactsHelperCustom = get_custom_class(
    "AlarmHistoryCollectionFactsHelperCustom"
)


class ResourceFactsHelper(
    AlarmHistoryCollectionFactsHelperCustom, AlarmHistoryCollectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            alarm_id=dict(aliases=["id"], type="str", required=True),
            alarm_historytype=dict(
                type="str", choices=["STATE_HISTORY", "STATE_TRANSITION_HISTORY"]
            ),
            timestamp_greater_than_or_equal_to=dict(type="str"),
            timestamp_less_than=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="alarm_history_collection",
        service_client_class=MonitoringClient,
        namespace="monitoring",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(alarm_history_collection=result)


if __name__ == "__main__":
    main()

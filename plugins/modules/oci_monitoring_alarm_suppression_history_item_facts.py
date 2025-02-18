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
module: oci_monitoring_alarm_suppression_history_item_facts
short_description: Fetches details about one or multiple AlarmSuppressionHistoryItem resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AlarmSuppressionHistoryItem resources in Oracle Cloud Infrastructure
    - Returns history of suppressions for the specified alarm, including both dimension-specific and and alarm-wide suppressions.
    - For important limits information, see
      L(Limits on Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).
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
        required: true
    dimensions:
        description:
            - "A filter to suppress only alarm state entries that include the set of specified dimension key-value pairs.
              If you specify {\\"availabilityDomain\\": \\"phx-ad-1\\"}
              and the alarm state entry corresponds to the set {\\"availabilityDomain\\": \\"phx-ad-1\\" and \\"resourceId\\":
              \\"ocid1.instance.region1.phx.exampleuniqueID\\"},
              then this alarm will be included for suppression."
            - "Example: `{\\"resourceId\\": \\"ocid1.instance.region1.phx.exampleuniqueID\\"}`"
        type: dict
    time_suppress_from_greater_than_or_equal_to:
        description:
            - "A filter to return only entries with \\"timeSuppressFrom\\" time occurring on or after the specified time."
            - The value cannot be a future time.
              Format defined by RFC3339.
            - "Example: `2023-02-01T01:02:29.600Z`"
        type: str
    time_suppress_from_less_than:
        description:
            - "A filter to return only entries with \\"timeSuppressFrom\\" time occurring before the specified time."
            - The value cannot be a future time.
              Format defined by RFC3339.
            - "Example: `2023-02-01T01:02:29.600Z`"
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List alarm_suppression_history_items
  oci_monitoring_alarm_suppression_history_item_facts:
    # required
    alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    dimensions: null
    time_suppress_from_greater_than_or_equal_to: time_suppress_from_greater_than_or_equal_to_example
    time_suppress_from_less_than: time_suppress_from_less_than_example

"""

RETURN = """
alarm_suppression_history_items:
    description:
        - List of AlarmSuppressionHistoryItem resources
    returned: on success
    type: complex
    contains:
        suppression_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm suppression.
            returned: on success
            type: str
            sample: "ocid1.suppression.oc1..xxxxxxEXAMPLExxxxxx"
        alarm_suppression_target:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                target_type:
                    description:
                        - The type of the alarm suppression target.
                    returned: on success
                    type: str
                    sample: ALARM
                alarm_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm that is the target of the alarm
                          suppression.
                    returned: on success
                    type: str
                    sample: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"
        level:
            description:
                - The level of this alarm suppression.
                  `ALARM` indicates a suppression of the entire alarm, regardless of dimension.
                  `DIMENSION` indicates a suppression configured for specified dimensions.
            returned: on success
            type: str
            sample: ALARM
        display_name:
            description:
                - A user-friendly name for the alarm suppression. It does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Human-readable reason for this alarm suppression.
                  It does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - Oracle recommends including tracking information for the event or associated work,
                  such as a ticket number.
                - "Example: `Planned outage due to change IT-1234.`"
            returned: on success
            type: str
            sample: description_example
        dimensions:
            description:
                - Configured dimension filter for suppressing alarm state entries that include the set of specified dimension key-value pairs.
                - "Example: `{\\"resourceId\\": \\"ocid1.instance.region1.phx.exampleuniqueID\\"}`"
            returned: on success
            type: dict
            sample: {}
        time_effective_from:
            description:
                - The start date and time for the suppression actually starts, inclusive. Format defined by RFC3339.
                - "Example: `2023-02-01T01:02:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_effective_until:
            description:
                - The end date and time for the suppression actually ends, inclusive. Format defined by RFC3339.
                - "Example: `2023-02-01T02:02:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "suppression_id": "ocid1.suppression.oc1..xxxxxxEXAMPLExxxxxx",
        "alarm_suppression_target": {
            "target_type": "ALARM",
            "alarm_id": "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "level": "ALARM",
        "display_name": "display_name_example",
        "description": "description_example",
        "dimensions": {},
        "time_effective_from": "2013-10-20T19:20:30+01:00",
        "time_effective_until": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.monitoring import MonitoringClient
    from oci.monitoring.models import SummarizeAlarmSuppressionHistoryDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AlarmSuppressionHistoryItemFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "alarm_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_alarm_suppression_history,
            alarm_id=self.module.params.get("alarm_id"),
            summarize_alarm_suppression_history_details=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, SummarizeAlarmSuppressionHistoryDetails
            ),
            **optional_kwargs
        )


AlarmSuppressionHistoryItemFactsHelperCustom = get_custom_class(
    "AlarmSuppressionHistoryItemFactsHelperCustom"
)


class ResourceFactsHelper(
    AlarmSuppressionHistoryItemFactsHelperCustom,
    AlarmSuppressionHistoryItemFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            alarm_id=dict(type="str", required=True),
            dimensions=dict(type="dict"),
            time_suppress_from_greater_than_or_equal_to=dict(type="str"),
            time_suppress_from_less_than=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="alarm_suppression_history_item",
        service_client_class=MonitoringClient,
        namespace="monitoring",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(alarm_suppression_history_items=result)


if __name__ == "__main__":
    main()

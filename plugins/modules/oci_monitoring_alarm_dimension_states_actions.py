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
module: oci_monitoring_alarm_dimension_states_actions
short_description: Perform actions on an AlarmDimensionStates resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AlarmDimensionStates resource in Oracle Cloud Infrastructure
    - For I(action=retrieve_dimension_states), lists the current alarm status of each metric stream, where status is derived from the metric stream's last
      associated transition.
      Optionally filter by status value and one or more dimension key-value pairs.
      For more information, see
      L(Listing Metric Stream Status in an Alarm,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/list-alarm-status-metric-stream.htm).
      For important limits information, see
      L(Limits on Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).
      This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
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
    dimension_filters:
        description:
            - "A filter to return only alarm state entries that match the exact set of specified dimension key-value pairs.
              If you specify `\\"availabilityDomain\\": \\"phx-ad-1\\"` but the alarm state entry corresponds to the set `\\"availabilityDomain\\": \\"phx-
              ad-1\\"`
              and `\\"resourceId\\": \\"ocid1.instance.region1.phx.exampleuniqueID\\"`, then no results are returned."
        type: dict
    status:
        description:
            - "A filter to return only alarm state entries that match the status value.
              Example: `FIRING`"
        type: str
    action:
        description:
            - The action to perform on the AlarmDimensionStates.
        type: str
        required: true
        choices:
            - "retrieve_dimension_states"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action retrieve_dimension_states on alarm_dimension_states
  oci_monitoring_alarm_dimension_states_actions:
    # required
    alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"
    action: retrieve_dimension_states

    # optional
    dimension_filters: null
    status: status_example

"""

RETURN = """
alarm_dimension_states_collection:
    description:
        - Details of the AlarmDimensionStates resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        dimensions:
            description:
                - Indicator of the metric stream associated with the alarm state entry. Includes one or more dimension key-value pairs.
            returned: on success
            type: dict
            sample: {}
        status:
            description:
                - Transition state (status value) associated with the alarm state entry.
                - "Example: `FIRING`"
            returned: on success
            type: str
            sample: FIRING
        timestamp:
            description:
                - Transition time associated with the alarm state entry. Format defined by RFC3339.
                - "Example: `2022-02-01T01:02:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "dimensions": {},
        "status": "FIRING",
        "timestamp": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.monitoring import MonitoringClient
    from oci.monitoring.models import RetrieveDimensionStatesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AlarmDimensionStatesActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        retrieve_dimension_states
    """

    @staticmethod
    def get_module_resource_id_param():
        return "alarm_id"

    def get_module_resource_id(self):
        return self.module.params.get("alarm_id")

    def retrieve_dimension_states(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RetrieveDimensionStatesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.retrieve_dimension_states,
            call_fn_args=(),
            call_fn_kwargs=dict(
                alarm_id=self.module.params.get("alarm_id"),
                retrieve_dimension_states_details=action_details,
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


AlarmDimensionStatesActionsHelperCustom = get_custom_class(
    "AlarmDimensionStatesActionsHelperCustom"
)


class ResourceHelper(
    AlarmDimensionStatesActionsHelperCustom, AlarmDimensionStatesActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            alarm_id=dict(aliases=["id"], type="str", required=True),
            dimension_filters=dict(type="dict"),
            status=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["retrieve_dimension_states"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="alarm_dimension_states",
        service_client_class=MonitoringClient,
        namespace="monitoring",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

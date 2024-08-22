#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_monitoring_alarm_status_facts
short_description: Fetches details about one or multiple AlarmStatus resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AlarmStatus resources in Oracle Cloud Infrastructure
    - List the status of each alarm in the specified compartment.
      Status is collective, across all metric streams in the alarm.
      To list alarm status for each metric stream, use L(RetrieveDimensionStates,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/monitoring/latest/AlarmDimensionStatesCollection/RetrieveDimensionStates).
      Optionally filter by resource or status value.
      For more information, see
      L(Listing Alarm Statuses,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/list-alarm-status.htm).
      For important limits information, see
      L(Limits on Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).
    - This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
      Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
      or transactions, per second (TPS) for a given tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the
              resources monitored by the metric that you are searching for. Use tenancyId to search in
              the root compartment.
            - "Example: `ocid1.compartment.oc1..exampleuniqueID`"
        type: str
        required: true
    compartment_id_in_subtree:
        description:
            - When true, returns resources from all compartments and subcompartments. The parameter can
              only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment).
              A true value requires the user to have tenancy-level permissions. If this requirement is not met,
              then the call is rejected. When false, returns resources from only the compartment specified in
              compartmentId. Default is false.
        type: bool
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
              Use this filter to list an alarm by name. Alternatively, when you know the alarm OCID, use the GetAlarm operation.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to use when sorting returned alarm definitions. Only one sorting level is provided.
            - "Example: `severity`"
        type: str
        choices:
            - "displayName"
            - "severity"
    sort_order:
        description:
            - The sort order to use when sorting returned alarm definitions. Ascending (ASC) or descending (DESC).
            - "Example: `ASC`"
        type: str
        choices:
            - "ASC"
            - "DESC"
    resource_id:
        description:
            - A filter to return only the resource with the specified L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
              The resource must be monitored by the metric that you are searching for.
            - "Example: `ocid1.instance.oc1.phx.exampleuniqueID`"
        type: str
    service_name:
        description:
            - "A filter to return only resources that match the given service name exactly.
              Use this filter to list all alarms containing metric streams that match the *exact* service-name dimension."
            - "Example: `logging-analytics`"
        type: str
    entity_id:
        description:
            - A filter to return only resources that match the given entity L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)
              exactly.
              The resource (entity) must be monitored by the metric that you are searching for.
            - "Example: `ocid1.instance.oc1.phx.exampleuniqueID`"
        type: str
    status:
        description:
            - "A filter to return only metric streams that match the specified status.
              For example, the value \\"FIRING\\" returns only firing metric streams."
            - "Example: `FIRING`"
        type: str
        choices:
            - "FIRING"
            - "OK"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List alarm_statuses
  oci_monitoring_alarm_status_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id_in_subtree: true
    display_name: display_name_example
    sort_by: displayName
    sort_order: ASC
    resource_id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    service_name: service_name_example
    entity_id: "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx"
    status: FIRING

"""

RETURN = """
alarm_statuses:
    description:
        - List of AlarmStatus resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The configured name of the alarm.
                - "Example: `High CPU Utilization`"
            returned: on success
            type: str
            sample: display_name_example
        severity:
            description:
                - "The perceived type of response required when the alarm is in the \\"FIRING\\" state."
                - "Example: `CRITICAL`"
            returned: on success
            type: str
            sample: CRITICAL
        rule_name:
            description:
                - Identifier of the alarm's base values for alarm evaluation, for use when the alarm contains overrides.
                  Default value is `BASE`. For information about alarm overrides, see L(AlarmOverride,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/monitoring/latest/datatypes/AlarmOverride).
            returned: on success
            type: str
            sample: rule_name_example
        timestamp_triggered:
            description:
                - "Timestamp for the transition of the alarm state. For example, the time when the alarm transitioned from OK to Firing.
                  Note: A three-minute lag for this value accounts for any late-arriving metrics."
                - "Example: `2023-02-01T01:02:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        alarm_summary:
            description:
                - Customizable alarm summary (`alarmSummary` L(alarm message parameter,https://docs.cloud.oracle.com/iaas/Content/Monitoring/alarm-message-
                  format.htm)).
                  Optionally include L(dynamic variables,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-dynamic-variables.htm).
                  The alarm summary appears within the body of the alarm message and in responses to
                  L(ListAlarmStatus,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/monitoring/latest/AlarmStatusSummary/ListAlarmsStatus)
                  L(GetAlarmHistory,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/monitoring/latest/AlarmHistoryCollection/GetAlarmHistory) and
                  L(RetrieveDimensionStates,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/monitoring/latest/AlarmDimensionStatesCollection/RetrieveDimensionStates).
            returned: on success
            type: str
            sample: alarm_summary_example
        status:
            description:
                - "The status of this alarm.
                  Status is collective, across all metric streams in the alarm.
                  To list alarm status for each metric stream, use L(RetrieveDimensionStates,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/monitoring/latest/AlarmDimensionStatesCollection/RetrieveDimensionStates).
                  Example: `FIRING`"
            returned: on success
            type: str
            sample: FIRING
        suppression:
            description:
                - The configuration details for suppressing an alarm.
            returned: on success
            type: complex
            contains:
                description:
                    description:
                        - Human-readable reason for suppressing alarm notifications.
                          It does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                        - Oracle recommends including tracking information for the event or associated work,
                          such as a ticket number.
                        - "Example: `Planned outage due to change IT-1234.`"
                    returned: on success
                    type: str
                    sample: description_example
                time_suppress_from:
                    description:
                        - The start date and time for the suppression to take place, inclusive. Format defined by RFC3339.
                        - "Example: `2023-02-01T01:02:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_suppress_until:
                    description:
                        - The end date and time for the suppression to take place, inclusive. Format defined by RFC3339.
                        - "Example: `2023-02-01T02:02:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "severity": "CRITICAL",
        "rule_name": "rule_name_example",
        "timestamp_triggered": "2013-10-20T19:20:30+01:00",
        "alarm_summary": "alarm_summary_example",
        "status": "FIRING",
        "suppression": {
            "description": "description_example",
            "time_suppress_from": "2013-10-20T19:20:30+01:00",
            "time_suppress_until": "2013-10-20T19:20:30+01:00"
        }
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

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AlarmStatusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "display_name",
            "sort_by",
            "sort_order",
            "resource_id",
            "service_name",
            "entity_id",
            "status",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_alarms_status,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AlarmStatusFactsHelperCustom = get_custom_class("AlarmStatusFactsHelperCustom")


class ResourceFactsHelper(AlarmStatusFactsHelperCustom, AlarmStatusFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            compartment_id_in_subtree=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["displayName", "severity"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            resource_id=dict(type="str"),
            service_name=dict(type="str"),
            entity_id=dict(type="str"),
            status=dict(type="str", choices=["FIRING", "OK"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="alarm_status",
        service_client_class=MonitoringClient,
        namespace="monitoring",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(alarm_statuses=result)


if __name__ == "__main__":
    main()

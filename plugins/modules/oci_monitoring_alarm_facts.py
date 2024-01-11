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
module: oci_monitoring_alarm_facts
short_description: Fetches details about one or multiple Alarm resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Alarm resources in Oracle Cloud Infrastructure
    - Lists the alarms for the specified compartment.
      For more information, see
      L(Listing Alarms,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/list-alarm.htm).
      For important limits information, see
      L(Limits on Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).
    - This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
      Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
      or transactions, per second (TPS) for a given tenancy.
    - If I(alarm_id) is specified, the details of a single Alarm will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    alarm_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of an alarm.
            - Required to get a specific alarm.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the
              resources monitored by the metric that you are searching for. Use tenancyId to search in
              the root compartment.
            - "Example: `ocid1.compartment.oc1..exampleuniqueID`"
            - Required to list multiple alarms.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
              Use this filter to list an alarm by name. Alternatively, when you know the alarm OCID, use the GetAlarm operation.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only alarms that match the given lifecycle state exactly. When not specified, only alarms in the ACTIVE lifecycle state are
              listed.
        type: str
        choices:
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
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
    compartment_id_in_subtree:
        description:
            - When true, returns resources from all compartments and subcompartments. The parameter can
              only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment).
              A true value requires the user to have tenancy-level permissions. If this requirement is not met,
              then the call is rejected. When false, returns resources from only the compartment specified in
              compartmentId. Default is false.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific alarm
  oci_monitoring_alarm_facts:
    # required
    alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"

- name: List alarms
  oci_monitoring_alarm_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: ACTIVE
    sort_by: displayName
    sort_order: ASC
    compartment_id_in_subtree: true

"""

RETURN = """
alarms:
    description:
        - List of Alarm resources
    returned: on success
    type: complex
    contains:
        metric_compartment_id_in_subtree:
            description:
                - When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can
                  only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment).
                  A true value requires the user to have tenancy-level permissions. If this requirement is not met,
                  then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified
                  in metricCompartmentId. Default is false.
                - "Example: `true`"
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        resource_group:
            description:
                - Resource group to match for metric data retrieved by the alarm. A resource group is a custom string that you can match when retrieving custom
                  metrics. Only one resource group can be applied per metric.
                  A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_),
                  hyphens (-), and dollar signs ($).
                - "Example: `frontend-fleet`"
                - Returned for get operation
            returned: on success
            type: str
            sample: resource_group_example
        resolution:
            description:
                - "The time between calculated aggregation windows for the alarm. Supported value: `1m`"
                - Returned for get operation
            returned: on success
            type: str
            sample: resolution_example
        pending_duration:
            description:
                - "The period of time that the condition defined in the alarm must persist before the alarm state
                  changes from \\"OK\\" to \\"FIRING\\". For example, a value of 5 minutes means that the
                  alarm must persist in breaching the condition for five minutes before the alarm updates its
                  state to \\"FIRING\\"."
                - "The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H`
                  for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M."
                - "Under the default value of PT1M, the first evaluation that breaches the alarm updates the
                  state to \\"FIRING\\"."
                - "The alarm updates its status to \\"OK\\" when the breaching condition has been clear for
                  the most recent minute."
                - "Example: `PT5M`"
                - Returned for get operation
            returned: on success
            type: str
            sample: pending_duration_example
        body:
            description:
                - The human-readable content of the delivered alarm notification. Oracle recommends providing guidance
                  to operators for resolving the alarm condition. Consider adding links to standard runbook
                  practices.
                - "Example: `High CPU usage alert. Follow runbook instructions for resolution.`"
                - Returned for get operation
            returned: on success
            type: str
            sample: body_example
        is_notifications_per_metric_dimension_enabled:
            description:
                - When set to `true`, splits alarm notifications per metric stream.
                  When set to `false`, groups alarm notifications across metric streams.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        message_format:
            description:
                - "The format to use for alarm notifications. The formats are:
                  * `RAW` - Raw JSON blob. Default value. When the `destinations` attribute specifies `Streaming`, all alarm notifications use this format.
                  * `PRETTY_JSON`: JSON with new lines and indents. Available when the `destinations` attribute specifies `Notifications` only.
                  * `ONS_OPTIMIZED`: Simplified, user-friendly layout. Available when the `destinations` attribute specifies `Notifications` only. Applies to
                  Email subscription types only."
                - Returned for get operation
            returned: on success
            type: str
            sample: RAW
        repeat_notification_duration:
            description:
                - "The frequency for re-submitting alarm notifications, if the alarm keeps firing without
                  interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours.
                  Minimum: PT1M. Maximum: P30D."
                - "Default value: null (notifications are not re-submitted)."
                - "Example: `PT2H`"
                - Returned for get operation
            returned: on success
            type: str
            sample: repeat_notification_duration_example
        time_created:
            description:
                - The date and time the alarm was created. Format defined by RFC3339.
                - "Example: `2019-02-01T01:02:29.600Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the alarm was last updated. Format defined by RFC3339.
                - "Example: `2019-02-03T01:02:29.600Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the alarm. It does not have to be unique, and it's changeable.
                - This value determines the title of each alarm notification.
                - "Example: `High CPU Utilization`"
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the alarm.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        metric_compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the metric
                  being evaluated by the alarm.
            returned: on success
            type: str
            sample: "ocid1.metriccompartment.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - The source service or application emitting the metric that is evaluated by the alarm.
                - "Example: `oci_computeagent`"
            returned: on success
            type: str
            sample: namespace_example
        query:
            description:
                - "The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
                  the Monitoring service interprets results for each returned time series as Boolean values,
                  where zero represents false and a non-zero value represents true. A true value means that the trigger
                  rule condition has been met. The query must specify a metric, statistic, interval, and trigger
                  rule (threshold or absence). Supported values for interval depend on the specified time range. More
                  interval values are supported for smaller time ranges. You can optionally
                  specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`.
                  For information about writing MQL expressions, see
                  L(Editing the MQL Expression for a Query,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).
                  For details about MQL, see
                  L(Monitoring Query Language (MQL) Reference,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm).
                  For available dimensions, review the metric definition for the supported service. See
                  L(Supported Services,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices)."
                - "Example of threshold alarm:"
                -   -----
                - "   CpuUtilization[1m]{availabilityDomain=\\"cumS:PHX-AD-1\\"}.groupBy(availabilityDomain).percentile(0.9) > 85"
                -   -----
                - "Example of absence alarm:"
                -   -----
                - "   CpuUtilization[1m]{availabilityDomain=\\"cumS:PHX-AD-1\\"}.absent()"
                -   -----
            returned: on success
            type: str
            sample: query_example
        severity:
            description:
                - "The perceived type of response required when the alarm is in the \\"FIRING\\" state."
                - "Example: `CRITICAL`"
            returned: on success
            type: str
            sample: CRITICAL
        destinations:
            description:
                - "A list of destinations for alarm notifications.
                  Each destination is represented by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)
                  of a related resource, such as a L(topic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/notification/latest/NotificationTopic).
                  Supported destination services: Notifications
                  , Streaming.
                  Limit: One destination per supported destination service."
            returned: on success
            type: list
            sample: []
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
                        - "Example: `2019-02-01T01:02:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_suppress_until:
                    description:
                        - The end date and time for the suppression to take place, inclusive. Format defined by RFC3339.
                        - "Example: `2019-02-01T02:02:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        is_enabled:
            description:
                - Whether the alarm is enabled.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        lifecycle_state:
            description:
                - The current lifecycle state of the alarm.
                - "Example: `DELETED`"
            returned: on success
            type: str
            sample: ACTIVE
    sample: [{
        "metric_compartment_id_in_subtree": true,
        "resource_group": "resource_group_example",
        "resolution": "resolution_example",
        "pending_duration": "pending_duration_example",
        "body": "body_example",
        "is_notifications_per_metric_dimension_enabled": true,
        "message_format": "RAW",
        "repeat_notification_duration": "repeat_notification_duration_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "metric_compartment_id": "ocid1.metriccompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "namespace": "namespace_example",
        "query": "query_example",
        "severity": "CRITICAL",
        "destinations": [],
        "suppression": {
            "description": "description_example",
            "time_suppress_from": "2013-10-20T19:20:30+01:00",
            "time_suppress_until": "2013-10-20T19:20:30+01:00"
        },
        "is_enabled": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
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
    from oci.monitoring import MonitoringClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AlarmFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "alarm_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_alarm, alarm_id=self.module.params.get("alarm_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "compartment_id_in_subtree",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_alarms,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AlarmFactsHelperCustom = get_custom_class("AlarmFactsHelperCustom")


class ResourceFactsHelper(AlarmFactsHelperCustom, AlarmFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            alarm_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETING", "DELETED"]),
            sort_by=dict(type="str", choices=["displayName", "severity"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            compartment_id_in_subtree=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="alarm",
        service_client_class=MonitoringClient,
        namespace="monitoring",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(alarms=result)


if __name__ == "__main__":
    main()

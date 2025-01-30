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
module: oci_monitoring_alarm_suppression_facts
short_description: Fetches details about one or multiple AlarmSuppression resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AlarmSuppression resources in Oracle Cloud Infrastructure
    - Lists alarm suppressions for the specified alarm.
      Only dimension-level suppressions are listed. Alarm-level suppressions are not listed.
    - For important limits information, see
      L(Limits on Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).
    - This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
      Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
      or transactions, per second (TPS) for a given tenancy.
    - If I(alarm_suppression_id) is specified, the details of a single AlarmSuppression will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    alarm_suppression_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm suppression.
            - Required to get a specific alarm_suppression.
        type: str
        aliases: ["id"]
    alarm_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm that is the target of the alarm suppression.
            - Required to list multiple alarm_suppressions.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
              Use this filter to list a alarm suppression by name.
              Alternatively, when you know the alarm suppression OCID, use the GetAlarmSuppression operation.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly. When not specified, only resources in the ACTIVE lifecycle state
              are listed.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    sort_by:
        description:
            - The field to use when sorting returned alarm suppressions. Only one sorting level is provided.
            - "Example: `timeCreated`"
        type: str
        choices:
            - "displayName"
            - "timeCreated"
            - "timeSuppressFrom"
    sort_order:
        description:
            - The sort order to use when sorting returned alarm suppressions. Ascending (ASC) or descending (DESC).
            - "Example: `ASC`"
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific alarm_suppression
  oci_monitoring_alarm_suppression_facts:
    # required
    alarm_suppression_id: "ocid1.alarmsuppression.oc1..xxxxxxEXAMPLExxxxxx"

- name: List alarm_suppressions
  oci_monitoring_alarm_suppression_facts:
    # required
    alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: ACTIVE
    sort_by: displayName
    sort_order: ASC

"""

RETURN = """
alarm_suppressions:
    description:
        - List of AlarmSuppression resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm suppression.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the alarm suppression.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        time_suppress_from:
            description:
                - The start date and time for the suppression to take place, inclusive. Format defined by RFC3339.
                - "Example: `2018-02-01T01:02:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_suppress_until:
            description:
                - The end date and time for the suppression to take place, inclusive. Format defined by RFC3339.
                - "Example: `2018-02-01T02:02:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the alarm suppression.
                - "Example: `DELETED`"
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - The date and time the alarm suppression was created. Format defined by RFC3339.
                - "Example: `2018-02-01T01:02:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the alarm suppression was last updated (deleted). Format defined by RFC3339.
                - "Example: `2018-02-03T01:02:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "alarm_suppression_target": {
            "target_type": "ALARM",
            "alarm_id": "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "display_name": "display_name_example",
        "description": "description_example",
        "dimensions": {},
        "time_suppress_from": "2013-10-20T19:20:30+01:00",
        "time_suppress_until": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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


class AlarmSuppressionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "alarm_suppression_id",
        ]

    def get_required_params_for_list(self):
        return [
            "alarm_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_alarm_suppression,
            alarm_suppression_id=self.module.params.get("alarm_suppression_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_alarm_suppressions,
            alarm_id=self.module.params.get("alarm_id"),
            **optional_kwargs
        )


AlarmSuppressionFactsHelperCustom = get_custom_class(
    "AlarmSuppressionFactsHelperCustom"
)


class ResourceFactsHelper(
    AlarmSuppressionFactsHelperCustom, AlarmSuppressionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            alarm_suppression_id=dict(aliases=["id"], type="str"),
            alarm_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            sort_by=dict(
                type="str", choices=["displayName", "timeCreated", "timeSuppressFrom"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="alarm_suppression",
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

    module.exit_json(alarm_suppressions=result)


if __name__ == "__main__":
    main()

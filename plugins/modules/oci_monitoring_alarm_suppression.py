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
module: oci_monitoring_alarm_suppression
short_description: Manage an AlarmSuppression resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete an AlarmSuppression resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a dimension-specific suppression for an alarm.
    - For important limits information, see
      L(Limits on Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits).
    - This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
      Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
      or transactions, per second (TPS) for a given tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    alarm_suppression_target:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            target_type:
                description:
                    - The type of the alarm suppression target.
                type: str
                choices:
                    - "ALARM"
                required: true
            alarm_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm that is the target of the alarm
                      suppression.
                type: str
                required: true
    display_name:
        description:
            - A user-friendly name for the alarm suppression. It does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Human-readable reason for this alarm suppression.
              It does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Oracle recommends including tracking information for the event or associated work,
              such as a ticket number.
            - "Example: `Planned outage due to change IT-1234.`"
        type: str
    dimensions:
        description:
            - "A filter to suppress only alarm state entries that include the set of specified dimension key-value pairs.
              If you specify {\\"availabilityDomain\\": \\"phx-ad-1\\"}
              and the alarm state entry corresponds to the set {\\"availabilityDomain\\": \\"phx-ad-1\\" and \\"resourceId\\":
              \\"ocid1.instance.region1.phx.exampleuniqueID\\"},
              then this alarm will be included for suppression."
            - "The value cannot be an empty object.
              Only a single value is allowed per key. No grouping of multiple values is allowed under the same key.
              Maximum characters (after serialization): 4000. This maximum satisfies typical use cases.
              The response for an exceeded maximum is `HTTP 400` with an \\"dimensions values are too long\\" message."
            - Required for create using I(state=present).
        type: dict
    time_suppress_from:
        description:
            - The start date and time for the suppression to take place, inclusive. Format defined by RFC3339.
            - "Example: `2023-02-01T01:02:29.600Z`"
            - Required for create using I(state=present).
        type: str
    time_suppress_until:
        description:
            - The end date and time for the suppression to take place, inclusive. Format defined by RFC3339.
            - "Example: `2023-02-01T02:02:29.600Z`"
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    alarm_suppression_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm suppression.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    alarm_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the alarm that is the target of the alarm suppression.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the AlarmSuppression.
            - Use I(state=present) to create an AlarmSuppression.
            - Use I(state=absent) to delete an AlarmSuppression.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create alarm_suppression
  oci_monitoring_alarm_suppression:
    # required
    alarm_suppression_target:
      # required
      target_type: ALARM
      alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    dimensions: null
    time_suppress_from: time_suppress_from_example
    time_suppress_until: time_suppress_until_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete alarm_suppression
  oci_monitoring_alarm_suppression:
    # required
    alarm_suppression_id: "ocid1.alarmsuppression.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete alarm_suppression using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_monitoring_alarm_suppression:
    # required
    display_name: display_name_example
    alarm_id: "ocid1.alarm.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
alarm_suppression:
    description:
        - Details of the AlarmSuppression resource acted upon by the current operation
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
    sample: {
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
    from oci.monitoring import MonitoringClient
    from oci.monitoring.models import CreateAlarmSuppressionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AlarmSuppressionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AlarmSuppressionHelperGen, self).get_possible_entity_types() + [
            "alarmsuppression",
            "alarmsuppressions",
            "monitoringalarmsuppression",
            "monitoringalarmsuppressions",
            "alarmsuppressionresource",
            "alarmsuppressionsresource",
            "monitoring",
        ]

    def get_module_resource_id_param(self):
        return "alarm_suppression_id"

    def get_module_resource_id(self):
        return self.module.params.get("alarm_suppression_id")

    def get_get_fn(self):
        return self.client.get_alarm_suppression

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_alarm_suppression, alarm_suppression_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_alarm_suppression,
            alarm_suppression_id=self.module.params.get("alarm_suppression_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "alarm_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_alarm_suppressions, **kwargs
        )

    def get_create_model_class(self):
        return CreateAlarmSuppressionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_alarm_suppression,
            call_fn_args=(),
            call_fn_kwargs=dict(create_alarm_suppression_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_alarm_suppression,
            call_fn_args=(),
            call_fn_kwargs=dict(
                alarm_suppression_id=self.module.params.get("alarm_suppression_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AlarmSuppressionHelperCustom = get_custom_class("AlarmSuppressionHelperCustom")


class ResourceHelper(AlarmSuppressionHelperCustom, AlarmSuppressionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            alarm_suppression_target=dict(
                type="dict",
                options=dict(
                    target_type=dict(type="str", required=True, choices=["ALARM"]),
                    alarm_id=dict(type="str", required=True),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            dimensions=dict(type="dict"),
            time_suppress_from=dict(type="str"),
            time_suppress_until=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            alarm_suppression_id=dict(aliases=["id"], type="str"),
            alarm_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="alarm_suppression",
        service_client_class=MonitoringClient,
        namespace="monitoring",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

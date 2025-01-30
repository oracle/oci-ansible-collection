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
module: oci_compute_cloud_at_customer_ccc_upgrade_schedule_actions
short_description: Perform actions on a CccUpgradeSchedule resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a CccUpgradeSchedule resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Compute Cloud@Customer upgrade schedule from one compartment to another using the
      specified L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ccc_upgrade_schedule_id:
        description:
            - Compute Cloud@Customer upgrade schedule
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the CccUpgradeSchedule.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on ccc_upgrade_schedule
  oci_compute_cloud_at_customer_ccc_upgrade_schedule_actions:
    # required
    ccc_upgrade_schedule_id: "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
ccc_upgrade_schedule:
    description:
        - Details of the CccUpgradeSchedule resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Upgrade schedule L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
                  This cannot be changed once created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Compute Cloud@Customer upgrade schedule display name.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - An optional description of the Compute Cloud@Customer upgrade schedule.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - Compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the
                  Compute Cloud@Customer upgrade schedule.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the upgrade schedule was created, using an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the upgrade schedule was updated, using an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Lifecycle state of the resource.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, the message can be used to provide actionable information for a resource in
                  a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        events:
            description:
                - List of preferred times for Compute Cloud@Customer infrastructures associated with this
                  schedule to be upgraded.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Generated name associated with the event.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - A description of the Compute Cloud@Customer upgrade schedule time block.
                    returned: on success
                    type: str
                    sample: description_example
                time_start:
                    description:
                        - The date and time when the Compute Cloud@Customer upgrade schedule event starts,
                          inclusive. An RFC3339 formatted UTC datetime string. For an event with recurrences,
                          this is the date that a recurrence can start being applied.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                schedule_event_duration:
                    description:
                        - The duration of this block of time. The duration must be specified and be of the
                          ISO-8601 format for durations.
                    returned: on success
                    type: str
                    sample: schedule_event_duration_example
                schedule_event_recurrences:
                    description:
                        - Frequency of recurrence of schedule block. When this field is not included, the event
                          is assumed to be a one time occurrence. The frequency field is strictly parsed and must
                          conform to RFC-5545 formatting for recurrences.
                    returned: on success
                    type: str
                    sample: schedule_event_recurrences_example
        infrastructure_ids:
            description:
                - List of Compute Cloud@Customer infrastructure
                  L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that are using this upgrade
                  schedule.
            returned: on success
            type: list
            sample: []
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
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "events": [{
            "name": "name_example",
            "description": "description_example",
            "time_start": "2013-10-20T19:20:30+01:00",
            "schedule_event_duration": "schedule_event_duration_example",
            "schedule_event_recurrences": "schedule_event_recurrences_example"
        }],
        "infrastructure_ids": [],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.compute_cloud_at_customer import ComputeCloudAtCustomerClient
    from oci.compute_cloud_at_customer.models import (
        ChangeCccUpgradeScheduleCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CccUpgradeScheduleActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "ccc_upgrade_schedule_id"

    def get_module_resource_id(self):
        return self.module.params.get("ccc_upgrade_schedule_id")

    def get_get_fn(self):
        return self.client.get_ccc_upgrade_schedule

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ccc_upgrade_schedule,
            ccc_upgrade_schedule_id=self.module.params.get("ccc_upgrade_schedule_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCccUpgradeScheduleCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_ccc_upgrade_schedule_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ccc_upgrade_schedule_id=self.module.params.get(
                    "ccc_upgrade_schedule_id"
                ),
                change_ccc_upgrade_schedule_compartment_details=action_details,
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


CccUpgradeScheduleActionsHelperCustom = get_custom_class(
    "CccUpgradeScheduleActionsHelperCustom"
)


class ResourceHelper(
    CccUpgradeScheduleActionsHelperCustom, CccUpgradeScheduleActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            ccc_upgrade_schedule_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ccc_upgrade_schedule",
        service_client_class=ComputeCloudAtCustomerClient,
        namespace="compute_cloud_at_customer",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

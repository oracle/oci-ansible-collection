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
module: oci_compute_cloud_at_customer_ccc_upgrade_schedule
short_description: Manage a CccUpgradeSchedule resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CccUpgradeSchedule resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Compute Cloud@Customer upgrade schedule.
    - "This resource has the following action operations in the M(oracle.oci.oci_compute_cloud_at_customer_ccc_upgrade_schedule_actions) module:
      change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the
              Compute Cloud@Customer Upgrade Schedule.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - Compute Cloud@Customer upgrade schedule display name.
              Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - An optional description of the Compute Cloud@Customer upgrade schedule.
              Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    events:
        description:
            - List of preferred times for Compute Cloud@Customer infrastructure to be upgraded.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            description:
                description:
                    - A description of the Compute Cloud@Customer upgrade schedule time block.
                    - This parameter is updatable.
                type: str
                required: true
            time_start:
                description:
                    - The date and time when the Compute Cloud@Customer upgrade schedule event starts,
                      inclusive. An RFC3339 formatted UTC datetime string. For an event with recurrences,
                      this is the date that a recurrence can start being applied.
                    - This parameter is updatable.
                type: str
                required: true
            schedule_event_duration:
                description:
                    - The duration of this block of time. The duration must be specified and be of the
                      ISO-8601 format for durations.
                    - This parameter is updatable.
                type: str
                required: true
            schedule_event_recurrences:
                description:
                    - Frequency of recurrence of schedule block. When this field is not included, the event
                      is assumed to be a one time occurrence. The frequency field is strictly parsed and must
                      conform to RFC-5545 formatting for recurrences.
                    - This parameter is updatable.
                type: str
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
    ccc_upgrade_schedule_id:
        description:
            - Compute Cloud@Customer upgrade schedule
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the CccUpgradeSchedule.
            - Use I(state=present) to create or update a CccUpgradeSchedule.
            - Use I(state=absent) to delete a CccUpgradeSchedule.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create ccc_upgrade_schedule
  oci_compute_cloud_at_customer_ccc_upgrade_schedule:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    events:
    - # required
      description: description_example
      time_start: time_start_example
      schedule_event_duration: schedule_event_duration_example

      # optional
      schedule_event_recurrences: schedule_event_recurrences_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update ccc_upgrade_schedule
  oci_compute_cloud_at_customer_ccc_upgrade_schedule:
    # required
    ccc_upgrade_schedule_id: "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    events:
    - # required
      description: description_example
      time_start: time_start_example
      schedule_event_duration: schedule_event_duration_example

      # optional
      schedule_event_recurrences: schedule_event_recurrences_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update ccc_upgrade_schedule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_cloud_at_customer_ccc_upgrade_schedule:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    events:
    - # required
      description: description_example
      time_start: time_start_example
      schedule_event_duration: schedule_event_duration_example

      # optional
      schedule_event_recurrences: schedule_event_recurrences_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete ccc_upgrade_schedule
  oci_compute_cloud_at_customer_ccc_upgrade_schedule:
    # required
    ccc_upgrade_schedule_id: "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete ccc_upgrade_schedule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_cloud_at_customer_ccc_upgrade_schedule:
    # required
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.compute_cloud_at_customer import ComputeCloudAtCustomerClient
    from oci.compute_cloud_at_customer.models import CreateCccUpgradeScheduleDetails
    from oci.compute_cloud_at_customer.models import UpdateCccUpgradeScheduleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CccUpgradeScheduleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(CccUpgradeScheduleHelperGen, self).get_possible_entity_types() + [
            "cccupgradeschedule",
            "cccupgradeschedules",
            "computeCloudAtCustomercccupgradeschedule",
            "computeCloudAtCustomercccupgradeschedules",
            "cccupgradescheduleresource",
            "cccupgradeschedulesresource",
            "computecloudatcustomer",
        ]

    def get_module_resource_id_param(self):
        return "ccc_upgrade_schedule_id"

    def get_module_resource_id(self):
        return self.module.params.get("ccc_upgrade_schedule_id")

    def get_get_fn(self):
        return self.client.get_ccc_upgrade_schedule

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_ccc_upgrade_schedule,
            ccc_upgrade_schedule_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ccc_upgrade_schedule,
            ccc_upgrade_schedule_id=self.module.params.get("ccc_upgrade_schedule_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "ccc_upgrade_schedule_id",
            "compartment_id",
            "display_name",
        ]

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
            self.client.list_ccc_upgrade_schedules, **kwargs
        )

    def get_create_model_class(self):
        return CreateCccUpgradeScheduleDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_ccc_upgrade_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(create_ccc_upgrade_schedule_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCccUpgradeScheduleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ccc_upgrade_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ccc_upgrade_schedule_id=self.module.params.get(
                    "ccc_upgrade_schedule_id"
                ),
                update_ccc_upgrade_schedule_details=update_details,
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
            call_fn=self.client.delete_ccc_upgrade_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ccc_upgrade_schedule_id=self.module.params.get(
                    "ccc_upgrade_schedule_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


CccUpgradeScheduleHelperCustom = get_custom_class("CccUpgradeScheduleHelperCustom")


class ResourceHelper(CccUpgradeScheduleHelperCustom, CccUpgradeScheduleHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            events=dict(
                type="list",
                elements="dict",
                options=dict(
                    description=dict(type="str", required=True),
                    time_start=dict(type="str", required=True),
                    schedule_event_duration=dict(type="str", required=True),
                    schedule_event_recurrences=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            ccc_upgrade_schedule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

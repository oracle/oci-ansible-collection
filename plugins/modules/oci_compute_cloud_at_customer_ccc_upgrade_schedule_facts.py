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
module: oci_compute_cloud_at_customer_ccc_upgrade_schedule_facts
short_description: Fetches details about one or multiple CccUpgradeSchedule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CccUpgradeSchedule resources in Oracle Cloud Infrastructure
    - Returns a list of Compute Cloud@Customer upgrade schedules.
    - If I(ccc_upgrade_schedule_id) is specified, the details of a single CccUpgradeSchedule will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ccc_upgrade_schedule_id:
        description:
            - Compute Cloud@Customer upgrade schedule
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            - Required to get a specific ccc_upgrade_schedule.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to
              list resources.
        type: str
    compartment_id_in_subtree:
        description:
            - Default is false.
              When set to true, the hierarchy of compartments is traversed and all compartments and
              sub-compartments in the tenancy are returned. Depends on the 'accessLevel' setting.
        type: bool
    access_level:
        description:
            - Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED.
              Setting this to ACCESSIBLE returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment). When set to RESTRICTED permissions are checked and no
              partial results are displayed.
        type: str
        choices:
            - "RESTRICTED"
            - "ACCESSIBLE"
    lifecycle_state:
        description:
            - A filter to return resources only when their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "NEEDS_ATTENTION"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - A filter to return only resources whose display name contains the substring.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific ccc_upgrade_schedule
  oci_compute_cloud_at_customer_ccc_upgrade_schedule_facts:
    # required
    ccc_upgrade_schedule_id: "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx"

- name: List ccc_upgrade_schedules
  oci_compute_cloud_at_customer_ccc_upgrade_schedule_facts:

    # optional
    ccc_upgrade_schedule_id: "ocid1.cccupgradeschedule.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id_in_subtree: true
    access_level: RESTRICTED
    lifecycle_state: ACTIVE
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
ccc_upgrade_schedules:
    description:
        - List of CccUpgradeSchedule resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - An optional description of the Compute Cloud@Customer upgrade schedule.
                  Avoid entering confidential information.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        time_updated:
            description:
                - The time the upgrade schedule was updated, using an RFC3339 formatted datetime string.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, the message can be used to provide actionable information for a resource in
                  a Failed state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        events:
            description:
                - List of preferred times for Compute Cloud@Customer infrastructures associated with this
                  schedule to be upgraded.
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: list
            sample: []
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
        lifecycle_state:
            description:
                - Lifecycle state of the resource.
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
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "description": "description_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "events": [{
            "name": "name_example",
            "description": "description_example",
            "time_start": "2013-10-20T19:20:30+01:00",
            "schedule_event_duration": "schedule_event_duration_example",
            "schedule_event_recurrences": "schedule_event_recurrences_example"
        }],
        "infrastructure_ids": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.compute_cloud_at_customer import ComputeCloudAtCustomerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CccUpgradeScheduleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "ccc_upgrade_schedule_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ccc_upgrade_schedule,
            ccc_upgrade_schedule_id=self.module.params.get("ccc_upgrade_schedule_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "ccc_upgrade_schedule_id",
            "compartment_id",
            "compartment_id_in_subtree",
            "access_level",
            "lifecycle_state",
            "display_name",
            "display_name_contains",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_ccc_upgrade_schedules, **optional_kwargs
        )


CccUpgradeScheduleFactsHelperCustom = get_custom_class(
    "CccUpgradeScheduleFactsHelperCustom"
)


class ResourceFactsHelper(
    CccUpgradeScheduleFactsHelperCustom, CccUpgradeScheduleFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            ccc_upgrade_schedule_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "NEEDS_ATTENTION", "DELETED", "FAILED"]
            ),
            display_name=dict(aliases=["name"], type="str"),
            display_name_contains=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ccc_upgrade_schedule",
        service_client_class=ComputeCloudAtCustomerClient,
        namespace="compute_cloud_at_customer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(ccc_upgrade_schedules=result)


if __name__ == "__main__":
    main()

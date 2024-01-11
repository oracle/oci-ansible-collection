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
module: oci_fusion_apps_scheduled_activity_facts
short_description: Fetches details about one or multiple ScheduledActivity resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ScheduledActivity resources in Oracle Cloud Infrastructure
    - Returns a list of ScheduledActivities.
    - If I(scheduled_activity_id) is specified, the details of a single ScheduledActivity will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    scheduled_activity_id:
        description:
            - Unique ScheduledActivity identifier.
            - Required to get a specific scheduled_activity.
        type: str
        aliases: ["id"]
    fusion_environment_id:
        description:
            - unique FusionEnvironment identifier
        type: str
        required: true
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    time_scheduled_start_greater_than_or_equal_to:
        description:
            - A filter that returns all resources that are scheduled after this date
        type: str
    time_expected_finish_less_than_or_equal_to:
        description:
            - A filter that returns all resources that end before this date
        type: str
    run_cycle:
        description:
            - A filter that returns all resources that match the specified run cycle.
        type: str
        choices:
            - "QUARTERLY"
            - "MONTHLY"
            - "ONEOFF"
            - "VERTEX"
    lifecycle_state:
        description:
            - A filter that returns all resources that match the specified status
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "FAILED"
            - "SUCCEEDED"
            - "CANCELED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "TIME_CREATED"
            - "DISPLAY_NAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific scheduled_activity
  oci_fusion_apps_scheduled_activity_facts:
    # required
    scheduled_activity_id: "ocid1.scheduledactivity.oc1..xxxxxxEXAMPLExxxxxx"
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List scheduled_activities
  oci_fusion_apps_scheduled_activity_facts:
    # required
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    time_scheduled_start_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_expected_finish_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    run_cycle: QUARTERLY
    lifecycle_state: ACCEPTED
    sort_order: ASC
    sort_by: TIME_CREATED

"""

RETURN = """
scheduled_activities:
    description:
        - List of ScheduledActivity resources
    returned: on success
    type: complex
    contains:
        time_created:
            description:
                - The time the scheduled activity record was created. An RFC3339 formatted datetime string.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - scheduled activity display name, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        run_cycle:
            description:
                - run cadence.
            returned: on success
            type: str
            sample: QUARTERLY
        fusion_environment_id:
            description:
                - FAaaS Environment Identifier.
            returned: on success
            type: str
            sample: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the scheduledActivity.
            returned: on success
            type: str
            sample: ACCEPTED
        actions:
            description:
                - List of actions
            returned: on success
            type: complex
            contains:
                mode:
                    description:
                        - A string that describeds whether the change is applied hot or cold
                    returned: on success
                    type: str
                    sample: HOT
                category:
                    description:
                        - patch artifact category
                    returned: on success
                    type: str
                    sample: MONTHLY
                version:
                    description:
                        - name of the repo
                    returned: on success
                    type: str
                    sample: version_example
                qualifier:
                    description:
                        - month qualifier
                    returned: on success
                    type: str
                    sample: qualifier_example
                reference_key:
                    description:
                        - Unique identifier of the object that represents the action
                    returned: on success
                    type: str
                    sample: reference_key_example
                action_type:
                    description:
                        - Type of action
                    returned: on success
                    type: str
                    sample: QUARTERLY_UPGRADE
                state:
                    description:
                        - A string that describes whether the change is applied hot or cold
                    returned: on success
                    type: str
                    sample: ACCEPTED
                description:
                    description:
                        - A string that describes the details of the action. It does not have to be unique, and you can change it. Avoid entering confidential
                          information.
                    returned: on success
                    type: str
                    sample: description_example
                artifact:
                    description:
                        - patch bundle name
                    returned: on success
                    type: str
                    sample: artifact_example
        time_scheduled_start:
            description:
                - Current time the scheduled activity is scheduled to start. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_expected_finish:
            description:
                - Current time the scheduled activity is scheduled to end. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - The time the scheduled activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        delay_in_hours:
            description:
                - Cumulative delay hours
            returned: on success
            type: int
            sample: 56
        service_availability:
            description:
                - Service availability / impact during scheduled activity execution up down
            returned: on success
            type: str
            sample: AVAILABLE
        time_accepted:
            description:
                - The time the scheduled activity record was created. An RFC3339 formatted datetime string.
                - Returned for list operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the scheduled activity record was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: NONE
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
                - Returned for list operation
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                - Returned for list operation
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "time_created": "2013-10-20T19:20:30+01:00",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "run_cycle": "QUARTERLY",
        "fusion_environment_id": "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACCEPTED",
        "actions": [{
            "mode": "HOT",
            "category": "MONTHLY",
            "version": "version_example",
            "qualifier": "qualifier_example",
            "reference_key": "reference_key_example",
            "action_type": "QUARTERLY_UPGRADE",
            "state": "ACCEPTED",
            "description": "description_example",
            "artifact": "artifact_example"
        }],
        "time_scheduled_start": "2013-10-20T19:20:30+01:00",
        "time_expected_finish": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "delay_in_hours": 56,
        "service_availability": "AVAILABLE",
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "NONE",
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
    from oci.fusion_apps import FusionApplicationsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScheduledActivityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "fusion_environment_id",
            "scheduled_activity_id",
        ]

    def get_required_params_for_list(self):
        return [
            "fusion_environment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_scheduled_activity,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            scheduled_activity_id=self.module.params.get("scheduled_activity_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "time_scheduled_start_greater_than_or_equal_to",
            "time_expected_finish_less_than_or_equal_to",
            "run_cycle",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_scheduled_activities,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            **optional_kwargs
        )


ScheduledActivityFactsHelperCustom = get_custom_class(
    "ScheduledActivityFactsHelperCustom"
)


class ResourceFactsHelper(
    ScheduledActivityFactsHelperCustom, ScheduledActivityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            scheduled_activity_id=dict(aliases=["id"], type="str"),
            fusion_environment_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            time_scheduled_start_greater_than_or_equal_to=dict(type="str"),
            time_expected_finish_less_than_or_equal_to=dict(type="str"),
            run_cycle=dict(
                type="str", choices=["QUARTERLY", "MONTHLY", "ONEOFF", "VERTEX"]
            ),
            lifecycle_state=dict(
                type="str",
                choices=["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIME_CREATED", "DISPLAY_NAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="scheduled_activity",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(scheduled_activities=result)


if __name__ == "__main__":
    main()

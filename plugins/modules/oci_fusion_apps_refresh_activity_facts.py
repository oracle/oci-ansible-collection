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
module: oci_fusion_apps_refresh_activity_facts
short_description: Fetches details about one or multiple RefreshActivity resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RefreshActivity resources in Oracle Cloud Infrastructure
    - Returns a list of RefreshActivities.
    - If I(refresh_activity_id) is specified, the details of a single RefreshActivity will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    refresh_activity_id:
        description:
            - The unique identifier (OCID) of the Refresh activity.
            - Required to get a specific refresh_activity.
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
    lifecycle_state:
        description:
            - A filter that returns all resources that match the specified status
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "NEEDS_ATTENTION"
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
- name: Get a specific refresh_activity
  oci_fusion_apps_refresh_activity_facts:
    # required
    refresh_activity_id: "ocid1.refreshactivity.oc1..xxxxxxEXAMPLExxxxxx"
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List refresh_activities
  oci_fusion_apps_refresh_activity_facts:
    # required
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    time_scheduled_start_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_expected_finish_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    lifecycle_state: ACCEPTED
    sort_order: ASC
    sort_by: TIME_CREATED

"""

RETURN = """
refresh_activities:
    description:
        - List of RefreshActivity resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier (OCID) of the refresh activity. Can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A friendly name for the refresh activity. Can be changed later.
            returned: on success
            type: str
            sample: display_name_example
        source_fusion_environment_id:
            description:
                - The OCID of the Fusion environment that is the source environment for the refresh.
            returned: on success
            type: str
            sample: "ocid1.sourcefusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        time_of_restoration_point:
            description:
                - The date and time of the most recent source environment backup used for the environment refresh.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the refreshActivity.
            returned: on success
            type: str
            sample: ACCEPTED
        time_scheduled_start:
            description:
                - The time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_expected_finish:
            description:
                - The time the refresh activity is scheduled to end. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - The time the refresh activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        service_availability:
            description:
                - Service availability / impact during refresh activity execution up down
            returned: on success
            type: str
            sample: AVAILABLE
        time_accepted:
            description:
                - The time the refresh activity record was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the refresh activity record was updated. An RFC3339 formatted datetime string.
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
        refresh_issue_details_list:
            description:
                - Details of refresh investigation information, each item represents a different issue.
            returned: on success
            type: complex
            contains:
                refresh_issues:
                    description:
                        - Detail reasons of refresh failure or validation failure that needs to be shown to customer.
                    returned: on success
                    type: str
                    sample: refresh_issues_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "source_fusion_environment_id": "ocid1.sourcefusionenvironment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_of_restoration_point": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACCEPTED",
        "time_scheduled_start": "2013-10-20T19:20:30+01:00",
        "time_expected_finish": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "service_availability": "AVAILABLE",
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "NONE",
        "refresh_issue_details_list": [{
            "refresh_issues": "refresh_issues_example"
        }]
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


class RefreshActivityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "fusion_environment_id",
            "refresh_activity_id",
        ]

    def get_required_params_for_list(self):
        return [
            "fusion_environment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_refresh_activity,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            refresh_activity_id=self.module.params.get("refresh_activity_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "time_scheduled_start_greater_than_or_equal_to",
            "time_expected_finish_less_than_or_equal_to",
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
            self.client.list_refresh_activities,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            **optional_kwargs
        )


RefreshActivityFactsHelperCustom = get_custom_class("RefreshActivityFactsHelperCustom")


class ResourceFactsHelper(
    RefreshActivityFactsHelperCustom, RefreshActivityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            refresh_activity_id=dict(aliases=["id"], type="str"),
            fusion_environment_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            time_scheduled_start_greater_than_or_equal_to=dict(type="str"),
            time_expected_finish_less_than_or_equal_to=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "NEEDS_ATTENTION",
                    "FAILED",
                    "SUCCEEDED",
                    "CANCELED",
                ],
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
        resource_type="refresh_activity",
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

    module.exit_json(refresh_activities=result)


if __name__ == "__main__":
    main()

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
module: oci_usage_scheduled_run_facts
short_description: Fetches details about one or multiple ScheduledRun resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ScheduledRun resources in Oracle Cloud Infrastructure
    - Returns schedule history list.
    - If I(scheduled_run_id) is specified, the details of a single ScheduledRun will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    scheduled_run_id:
        description:
            - The scheduledRun unique OCID.
            - Required to get a specific scheduled_run.
        type: str
        aliases: ["id"]
    schedule_id:
        description:
            - The unique ID of a schedule.
            - Required to list multiple scheduled_runs.
        type: str
    sort_by:
        description:
            - The field to sort by. If not specified, the default is timeCreated.
        type: str
        choices:
            - "timeCreated"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific scheduled_run
  oci_usage_scheduled_run_facts:
    # required
    scheduled_run_id: "ocid1.scheduledrun.oc1..xxxxxxEXAMPLExxxxxx"

- name: List scheduled_runs
  oci_usage_scheduled_run_facts:
    # required
    schedule_id: "ocid1.schedule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
scheduled_runs:
    description:
        - List of ScheduledRun resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The ocid representing unique shedule run
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        schedule_id:
            description:
                - The ocid representing unique shedule
            returned: on success
            type: str
            sample: "ocid1.schedule.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time when schedule started executing
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - The time when schedule finished executing
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Specifies if the schedule job was run successfully or not.
            returned: on success
            type: str
            sample: FAILED
        lifecycle_details:
            description:
                - Additional details about scheduled run failure
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "schedule_id": "ocid1.schedule.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "FAILED",
        "lifecycle_details": "lifecycle_details_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.usage_api import UsageapiClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScheduledRunFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "scheduled_run_id",
        ]

    def get_required_params_for_list(self):
        return [
            "schedule_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_scheduled_run,
            scheduled_run_id=self.module.params.get("scheduled_run_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_scheduled_runs,
            schedule_id=self.module.params.get("schedule_id"),
            **optional_kwargs
        )


ScheduledRunFactsHelperCustom = get_custom_class("ScheduledRunFactsHelperCustom")


class ResourceFactsHelper(ScheduledRunFactsHelperCustom, ScheduledRunFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            scheduled_run_id=dict(aliases=["id"], type="str"),
            schedule_id=dict(type="str"),
            sort_by=dict(type="str", choices=["timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="scheduled_run",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(scheduled_runs=result)


if __name__ == "__main__":
    main()

#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_os_management_upcoming_scheduled_job_facts
short_description: Fetches details about one or multiple UpcomingScheduledJob resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple UpcomingScheduledJob resources in Oracle Cloud Infrastructure
    - Returns a list of all of the Scheduled Jobs whose next execution time is at or before the specified time.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
        required: true
    time_end:
        description:
            - The cut-off time before which to list all upcoming schedules, in ISO 8601 format
            - "Example: 2017-07-14T02:40:00.000Z"
        type: str
        required: true
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    tag_name:
        description:
            - The name of the tag.
        type: str
    tag_value:
        description:
            - The value for the tag.
        type: str
    lifecycle_state:
        description:
            - The current lifecycle state for the object.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    os_family:
        description:
            - The OS family for which to list resources.
        type: str
        choices:
            - "LINUX"
            - "WINDOWS"
            - "ALL"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List upcoming_scheduled_jobs
  oci_os_management_upcoming_scheduled_job_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    time_end: 2013-10-20T19:20:30+01:00

"""

RETURN = """
upcoming_scheduled_jobs:
    description:
        - List of UpcomingScheduledJob resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID for the Scheduled Job
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - Scheduled Job name
            returned: on success
            type: string
            sample: display_name_example
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        schedule_type:
            description:
                - the type of scheduling this Scheduled Job follows
            returned: on success
            type: string
            sample: ONETIME
        time_next_execution:
            description:
                - the time/date of the next scheduled execution of this Scheduled Job
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_last_execution:
            description:
                - the time/date of the last execution of this Scheduled Job
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        managed_instances:
            description:
                - the list of managed instances this scheduled job operates on (mutually exclusive with managedInstanceGroups)
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: string
                    sample: display_name_example
        managed_instance_groups:
            description:
                - the list of managed instance groups this scheduled job operates on (mutually exclusive with managedInstances)
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: string
                    sample: display_name_example
        operation_type:
            description:
                - the type of operation this Scheduled Job performs
            returned: on success
            type: string
            sample: INSTALL
        lifecycle_state:
            description:
                - The current state of the Scheduled Job.
            returned: on success
            type: string
            sample: CREATING
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
        os_family:
            description:
                - The Operating System type of the managed instance.
            returned: on success
            type: string
            sample: LINUX
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "schedule_type": "ONETIME",
        "time_next_execution": "2013-10-20T19:20:30+01:00",
        "time_last_execution": "2013-10-20T19:20:30+01:00",
        "managed_instances": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "managed_instance_groups": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "operation_type": "INSTALL",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "os_family": "LINUX"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UpcomingScheduledJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "time_end",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
            "tag_name",
            "tag_value",
            "lifecycle_state",
            "os_family",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_upcoming_scheduled_jobs,
            compartment_id=self.module.params.get("compartment_id"),
            time_end=self.module.params.get("time_end"),
            **optional_kwargs
        )


UpcomingScheduledJobFactsHelperCustom = get_custom_class(
    "UpcomingScheduledJobFactsHelperCustom"
)


class ResourceFactsHelper(
    UpcomingScheduledJobFactsHelperCustom, UpcomingScheduledJobFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            time_end=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            tag_name=dict(type="str"),
            tag_value=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            os_family=dict(type="str", choices=["LINUX", "WINDOWS", "ALL"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="upcoming_scheduled_job",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(upcoming_scheduled_jobs=result)


if __name__ == "__main__":
    main()

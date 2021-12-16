#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_os_management_scheduled_job_facts
short_description: Fetches details about one or multiple ScheduledJob resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ScheduledJob resources in Oracle Cloud Infrastructure
    - Returns a list of all of the currently active Scheduled Jobs in the system
    - If I(scheduled_job_id) is specified, the details of a single ScheduledJob will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    scheduled_job_id:
        description:
            - The ID of the scheduled job.
            - Required to get a specific scheduled_job.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple scheduled_jobs.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    managed_instance_id:
        description:
            - The ID of the managed instance for which to list resources.
        type: str
    managed_instance_group_id:
        description:
            - The ID of the managed instace group for which to list resources.
        type: str
    operation_type:
        description:
            - The operation type for which to list resources
        type: str
        choices:
            - "INSTALL"
            - "UPDATE"
            - "REMOVE"
            - "UPDATEALL"
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
    is_restricted:
        description:
            - If true, will only filter out restricted Autonomous Linux Scheduled Job
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific scheduled_job
  oci_os_management_scheduled_job_facts:
    # required
    scheduled_job_id: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"

- name: List scheduled_jobs
  oci_os_management_scheduled_job_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    operation_type: INSTALL
    sort_order: ASC
    sort_by: TIMECREATED
    lifecycle_state: CREATING
    os_family: LINUX
    is_restricted: true

"""

RETURN = """
scheduled_jobs:
    description:
        - List of ScheduledJob resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID for the Scheduled Job
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Scheduled Job name
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Details describing the Scheduled Job.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        schedule_type:
            description:
                - the type of scheduling this Scheduled Job follows
            returned: on success
            type: str
            sample: ONETIME
        time_next_execution:
            description:
                - the time of the next execution of this Scheduled Job
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_execution:
            description:
                - the time of the last execution of this Scheduled Job
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        interval_type:
            description:
                - the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)
                - Returned for get operation
            returned: on success
            type: str
            sample: HOUR
        interval_value:
            description:
                - the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)
                - Returned for get operation
            returned: on success
            type: str
            sample: interval_value_example
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
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: str
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
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: str
                    sample: display_name_example
        operation_type:
            description:
                - the type of operation this Scheduled Job performs
            returned: on success
            type: str
            sample: INSTALL
        update_type:
            description:
                - Type of the update (only if operation type is UPDATEALL)
                - Returned for get operation
            returned: on success
            type: str
            sample: SECURITY
        package_names:
            description:
                - the names of the updates (only if operation type is INSTALL/UPDATE/REMOVE)
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - package identifier
                    returned: on success
                    type: str
                    sample: name_example
        work_requests:
            description:
                - list of Work Requests associated with this Scheduled Job
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: str
                    sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the Scheduled Job.
            returned: on success
            type: str
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
        update_names:
            description:
                - The unique names of the Windows Updates (only if operation type is INSTALL).
                  This is only applicable when the osFamily is for Windows managed instances.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        os_family:
            description:
                - The Operating System type of the managed instance.
            returned: on success
            type: str
            sample: LINUX
        is_restricted:
            description:
                - true, if the schedule job has its update capabilities restricted. (Used to track Autonomous Scheduled Job)
            returned: on success
            type: bool
            sample: true
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "schedule_type": "ONETIME",
        "time_next_execution": "2013-10-20T19:20:30+01:00",
        "time_last_execution": "2013-10-20T19:20:30+01:00",
        "interval_type": "HOUR",
        "interval_value": "interval_value_example",
        "managed_instances": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "managed_instance_groups": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "operation_type": "INSTALL",
        "update_type": "SECURITY",
        "package_names": [{
            "name": "name_example"
        }],
        "work_requests": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "update_names": [],
        "os_family": "LINUX",
        "is_restricted": true
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


class ScheduledJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "scheduled_job_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_scheduled_job,
            scheduled_job_id=self.module.params.get("scheduled_job_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "managed_instance_id",
            "managed_instance_group_id",
            "operation_type",
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "os_family",
            "is_restricted",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_scheduled_jobs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ScheduledJobFactsHelperCustom = get_custom_class("ScheduledJobFactsHelperCustom")


class ResourceFactsHelper(ScheduledJobFactsHelperCustom, ScheduledJobFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            scheduled_job_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            managed_instance_id=dict(type="str"),
            managed_instance_group_id=dict(type="str"),
            operation_type=dict(
                type="str", choices=["INSTALL", "UPDATE", "REMOVE", "UPDATEALL"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
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
            is_restricted=dict(type="bool"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="scheduled_job",
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

    module.exit_json(scheduled_jobs=result)


if __name__ == "__main__":
    main()

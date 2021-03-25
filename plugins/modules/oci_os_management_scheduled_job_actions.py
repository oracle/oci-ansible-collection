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
module: oci_os_management_scheduled_job_actions
short_description: Perform actions on a ScheduledJob resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ScheduledJob resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a resource into a different compartment. When provided, If-Match
      is checked against ETag values of the resource.
    - For I(action=run_scheduled_job_now), this will trigger an already created Scheduled Job to being executing
      immediately instead of waiting for its next regularly scheduled time.
    - For I(action=skip_next_scheduled_job_execution), this will force an already created Scheduled Job to skip its
      next regularly scheduled execution
version_added: "2.9"
author: Oracle (@oracle)
options:
    scheduled_job_id:
        description:
            - The ID of the scheduled job.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              compartment into which the resource should be moved.
            - Applicable only for I(action=change_compartment).
        type: str
    action:
        description:
            - The action to perform on the ScheduledJob.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "run_scheduled_job_now"
            - "skip_next_scheduled_job_execution"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on scheduled_job
  oci_os_management_scheduled_job_actions:
    scheduled_job_id: ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx
    action: change_compartment

- name: Perform action run_scheduled_job_now on scheduled_job
  oci_os_management_scheduled_job_actions:
    scheduled_job_id: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
    action: run_scheduled_job_now

- name: Perform action skip_next_scheduled_job_execution on scheduled_job
  oci_os_management_scheduled_job_actions:
    scheduled_job_id: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
    action: skip_next_scheduled_job_execution

"""

RETURN = """
scheduled_job:
    description:
        - Details of the ScheduledJob resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID for the Scheduled Job
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Scheduled Job name
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Details describing the Scheduled Job.
            returned: on success
            type: string
            sample: description_example
        schedule_type:
            description:
                - the type of scheduling this Scheduled Job follows
            returned: on success
            type: string
            sample: ONETIME
        time_next_execution:
            description:
                - the time of the next execution of this Scheduled Job
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_last_execution:
            description:
                - the time of the last execution of this Scheduled Job
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        interval_type:
            description:
                - the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)
            returned: on success
            type: string
            sample: HOUR
        interval_value:
            description:
                - the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)
            returned: on success
            type: string
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
                    type: string
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
        update_type:
            description:
                - Type of the update (only if operation type is UPDATEALL)
            returned: on success
            type: string
            sample: SECURITY
        package_names:
            description:
                - the names of the updates (only if operation type is INSTALL/UPDATE/REMOVE)
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - package identifier
                    returned: on success
                    type: string
                    sample: name_example
        work_requests:
            description:
                - list of Work Requests associated with this Scheduled Job
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: string
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: string
                    sample: display_name_example
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
        update_names:
            description:
                - The unique names of the Windows Updates (only if operation type is INSTALL).
                  This is only applicable when the osFamily is for Windows managed instances.
            returned: on success
            type: list
            sample: []
        os_family:
            description:
                - The Operating System type of the managed instance.
            returned: on success
            type: string
            sample: LINUX
    sample: {
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
        "os_family": "LINUX"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import OsManagementClient
    from oci.os_management.models import ChangeScheduledJobCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScheduledJobActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        run_scheduled_job_now
        skip_next_scheduled_job_execution
    """

    @staticmethod
    def get_module_resource_id_param():
        return "scheduled_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("scheduled_job_id")

    def get_get_fn(self):
        return self.client.get_scheduled_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_scheduled_job,
            scheduled_job_id=self.module.params.get("scheduled_job_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeScheduledJobCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_scheduled_job_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                scheduled_job_id=self.module.params.get("scheduled_job_id"),
                change_scheduled_job_compartment_details=action_details,
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

    def run_scheduled_job_now(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.run_scheduled_job_now,
            call_fn_args=(),
            call_fn_kwargs=dict(
                scheduled_job_id=self.module.params.get("scheduled_job_id"),
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

    def skip_next_scheduled_job_execution(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.skip_next_scheduled_job_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                scheduled_job_id=self.module.params.get("scheduled_job_id"),
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


ScheduledJobActionsHelperCustom = get_custom_class("ScheduledJobActionsHelperCustom")


class ResourceHelper(ScheduledJobActionsHelperCustom, ScheduledJobActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            scheduled_job_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "run_scheduled_job_now",
                    "skip_next_scheduled_job_execution",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="scheduled_job",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

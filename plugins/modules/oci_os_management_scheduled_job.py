#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_os_management_scheduled_job
short_description: Manage a ScheduledJob resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ScheduledJob resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Scheduled Job to perform a specific package operation on
      a set of managed instances or managed instance groups.  Can be created
      as a one-time execution in the future, or as a recurring execution
      that repeats on a defined interval.
    - "This resource has the following action operations in the M(oci_scheduled_job_actions) module: run_scheduled_job_now, skip_next_scheduled_job_execution."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - OCID for the Compartment
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - Scheduled Job name
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Details describing the Scheduled Job.
        type: str
    schedule_type:
        description:
            - the type of scheduling this Scheduled Job follows
            - Required for create using I(state=present).
        type: str
        choices:
            - "ONETIME"
            - "RECURRING"
    time_next_execution:
        description:
            - the desired time for the next execution of this Scheduled Job
            - Required for create using I(state=present).
        type: str
    interval_type:
        description:
            - the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)
        type: str
        choices:
            - "HOUR"
            - "DAY"
            - "WEEK"
            - "MONTH"
    interval_value:
        description:
            - the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)
        type: str
    managed_instances:
        description:
            - The list of managed instances this scheduled job operates on
              (mutually exclusive with managedInstanceGroups). Either this or the
              managedInstanceGroups must be supplied.
        type: list
        suboptions:
            id:
                description:
                    - unique identifier that is immutable on creation
                type: str
                required: true
            display_name:
                description:
                    - User friendly name
                type: str
                aliases: ["name"]
                required: true
    managed_instance_groups:
        description:
            - The list of managed instance groups this scheduled job operates on
              (mutually exclusive with managedInstances). Either this or
              managedInstances must be supplied.
        type: list
        suboptions:
            id:
                description:
                    - unique identifier that is immutable on creation
                type: str
                required: true
            display_name:
                description:
                    - User friendly name
                type: str
                aliases: ["name"]
                required: true
    operation_type:
        description:
            - the type of operation this Scheduled Job performs
            - Required for create using I(state=present).
        type: str
        choices:
            - "INSTALL"
            - "UPDATE"
            - "REMOVE"
            - "UPDATEALL"
    update_type:
        description:
            - Type of the update (only if operation type is UPDATEALL)
        type: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "ALL"
    package_names:
        description:
            - the id of the package (only if operation type is INSTALL/UPDATE/REMOVE)
        type: list
        suboptions:
            name:
                description:
                    - package identifier
                type: str
                required: true
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
        type: dict
    update_names:
        description:
            - The unique names of the Windows Updates (only if operation type is INSTALL).
              This is only applicable when the osFamily is for Windows managed instances.
        type: list
    os_family:
        description:
            - The Operating System type of the managed instance(s) on which this scheduled job will operate.
              If not specified, this defaults to Linux.
        type: str
        choices:
            - "LINUX"
            - "WINDOWS"
            - "ALL"
    scheduled_job_id:
        description:
            - The ID of the scheduled job.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ScheduledJob.
            - Use I(state=present) to create or update a ScheduledJob.
            - Use I(state=absent) to delete a ScheduledJob.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create scheduled_job
  oci_os_management_scheduled_job:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: display_name_example
    schedule_type: ONETIME
    time_next_execution: 2013-10-20T19:20:30+01:00
    operation_type: INSTALL

- name: Update scheduled_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_scheduled_job:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: display_name_example
    description: description_example
    schedule_type: ONETIME
    time_next_execution: 2013-10-20T19:20:30+01:00
    interval_type: HOUR
    interval_value: interval_value_example
    operation_type: INSTALL
    update_type: SECURITY
    package_names:
    - name: name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update scheduled_job
  oci_os_management_scheduled_job:
    display_name: display_name_example
    description: description_example
    scheduled_job_id: ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete scheduled_job
  oci_os_management_scheduled_job:
    scheduled_job_id: ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete scheduled_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_scheduled_job:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: display_name_example
    state: absent

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
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import OsManagementClient
    from oci.os_management.models import CreateScheduledJobDetails
    from oci.os_management.models import UpdateScheduledJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScheduledJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name", "os_family"]
            if self._use_name_as_identifier()
            else ["display_name", "operation_type", "os_family"]
        )

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
            self.client.list_scheduled_jobs, **kwargs
        )

    def get_create_model_class(self):
        return CreateScheduledJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_scheduled_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_scheduled_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateScheduledJobDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_scheduled_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                scheduled_job_id=self.module.params.get("scheduled_job_id"),
                update_scheduled_job_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_scheduled_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                scheduled_job_id=self.module.params.get("scheduled_job_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


ScheduledJobHelperCustom = get_custom_class("ScheduledJobHelperCustom")


class ResourceHelper(ScheduledJobHelperCustom, ScheduledJobHelperGen):
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
            schedule_type=dict(type="str", choices=["ONETIME", "RECURRING"]),
            time_next_execution=dict(type="str"),
            interval_type=dict(type="str", choices=["HOUR", "DAY", "WEEK", "MONTH"]),
            interval_value=dict(type="str"),
            managed_instances=dict(
                type="list",
                elements="dict",
                options=dict(
                    id=dict(type="str", required=True),
                    display_name=dict(aliases=["name"], type="str", required=True),
                ),
            ),
            managed_instance_groups=dict(
                type="list",
                elements="dict",
                options=dict(
                    id=dict(type="str", required=True),
                    display_name=dict(aliases=["name"], type="str", required=True),
                ),
            ),
            operation_type=dict(
                type="str", choices=["INSTALL", "UPDATE", "REMOVE", "UPDATEALL"]
            ),
            update_type=dict(
                type="str", choices=["SECURITY", "BUGFIX", "ENHANCEMENT", "ALL"]
            ),
            package_names=dict(
                type="list",
                elements="dict",
                options=dict(name=dict(type="str", required=True)),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            update_names=dict(type="list"),
            os_family=dict(type="str", choices=["LINUX", "WINDOWS", "ALL"]),
            scheduled_job_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

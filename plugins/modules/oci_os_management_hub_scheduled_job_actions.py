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
module: oci_os_management_hub_scheduled_job_actions
short_description: Perform actions on a ScheduledJob resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ScheduledJob resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a scheduled job to another compartment.
    - For I(action=run_scheduled_job_now), triggers an already created recurring scheduled job to run immediately instead of waiting for its next regularly
      scheduled time. This operation only applies to recurring jobs, not one-time scheduled jobs.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the scheduled job to.
            - Required for I(action=change_compartment).
        type: str
    scheduled_job_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the scheduled job.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the ScheduledJob.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "run_scheduled_job_now"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on scheduled_job
  oci_os_management_hub_scheduled_job_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    scheduled_job_id: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action run_scheduled_job_now on scheduled_job
  oci_os_management_hub_scheduled_job_actions:
    # required
    scheduled_job_id: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
    action: run_scheduled_job_now

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
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the scheduled job.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friendly name for the scheduled job.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the scheduled job.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - User-specified description for the scheduled job.
            returned: on success
            type: str
            sample: description_example
        schedule_type:
            description:
                - The type of scheduling frequency for the job.
            returned: on success
            type: str
            sample: ONETIME
        locations:
            description:
                - The list of locations this scheduled job should operate on for a job targeting on compartments. (Empty list means apply to all locations).
                  This can only be set when managedCompartmentIds is not empty.
            returned: on success
            type: list
            sample: []
        time_next_execution:
            description:
                - The time of the next execution of this scheduled job (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_execution:
            description:
                - The time of the last execution of this scheduled job (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        recurring_rule:
            description:
                - The frequency schedule for a recurring scheduled job.
            returned: on success
            type: str
            sample: recurring_rule_example
        managed_instance_ids:
            description:
                - The managed instance L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job operates on.
                  A scheduled job can only operate on one type of target, therefore this parameter is mutually exclusive with
                  managedInstanceGroupIds, managedCompartmentIds, and lifecycleStageIds.
            returned: on success
            type: list
            sample: []
        managed_instance_group_ids:
            description:
                - The managed instance group L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job
                  operates on. A scheduled job can only operate on one type of target, therefore this parameter is mutually exclusive with managedInstanceIds,
                  managedCompartmentIds, and lifecycleStageIds.
            returned: on success
            type: list
            sample: []
        managed_compartment_ids:
            description:
                - The compartment L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job operates on. A
                  scheduled job can only operate on one type of target, therefore this parameter is mutually exclusive with managedInstanceIds,
                  managedInstanceGroupIds, and lifecycleStageIds.
            returned: on success
            type: list
            sample: []
        lifecycle_stage_ids:
            description:
                - The lifecycle stage L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that this scheduled job operates on.
                  A scheduled job can only operate on one type of target, therefore this parameter is mutually exclusive with
                  managedInstanceIds, managedInstanceGroupIds, and managedCompartmentIds.
            returned: on success
            type: list
            sample: []
        is_subcompartment_included:
            description:
                - Indicates whether to apply the scheduled job to all compartments in the tenancy when managedCompartmentIds specifies the tenancy
                  L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) (root compartment).
            returned: on success
            type: bool
            sample: true
        operations:
            description:
                - "The list of operations this scheduled job needs to perform.
                  A scheduled job supports only one operation type, unless it is one of the following:
                  * UPDATE_PACKAGES
                  * UPDATE_ALL
                  * UPDATE_SECURITY
                  * UPDATE_BUGFIX
                  * UPDATE_ENHANCEMENT
                  * UPDATE_OTHER
                  * UPDATE_KSPLICE_USERSPACE
                  * UPDATE_KSPLICE_KERNEL"
            returned: on success
            type: complex
            contains:
                operation_type:
                    description:
                        - The type of operation this scheduled job performs.
                    returned: on success
                    type: str
                    sample: INSTALL_PACKAGES
                package_names:
                    description:
                        - The names of the target packages. This parameter only applies when the scheduled job is for installing, updating, or removing
                          packages.
                    returned: on success
                    type: list
                    sample: []
                windows_update_names:
                    description:
                        - "Unique identifier for the Windows update. This parameter only applies if the scheduled job is for installing Windows updates.
                          Note that this is not an OCID, but is a unique identifier assigned by Microsoft.
                          For example: '6981d463-cd91-4a26-b7c4-ea4ded9183ed'."
                    returned: on success
                    type: list
                    sample: []
                manage_module_streams_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        enable:
                            description:
                                - The set of module streams to enable.
                            returned: on success
                            type: complex
                            contains:
                                module_name:
                                    description:
                                        - The name of a module.
                                    returned: on success
                                    type: str
                                    sample: module_name_example
                                stream_name:
                                    description:
                                        - The name of a stream of the specified module.
                                    returned: on success
                                    type: str
                                    sample: stream_name_example
                                software_source_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                          contains the module stream.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                        disable:
                            description:
                                - The set of module streams to disable.
                            returned: on success
                            type: complex
                            contains:
                                module_name:
                                    description:
                                        - The name of a module.
                                    returned: on success
                                    type: str
                                    sample: module_name_example
                                stream_name:
                                    description:
                                        - The name of a stream of the specified module.
                                    returned: on success
                                    type: str
                                    sample: stream_name_example
                                software_source_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                          contains the module stream.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                        install:
                            description:
                                - The set of module stream profiles to install.
                            returned: on success
                            type: complex
                            contains:
                                module_name:
                                    description:
                                        - The name of a module.
                                    returned: on success
                                    type: str
                                    sample: module_name_example
                                stream_name:
                                    description:
                                        - The name of a stream of the specified module.
                                    returned: on success
                                    type: str
                                    sample: stream_name_example
                                profile_name:
                                    description:
                                        - The name of a profile of the specified module stream.
                                    returned: on success
                                    type: str
                                    sample: profile_name_example
                                software_source_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                          contains the module stream.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                        remove:
                            description:
                                - The set of module stream profiles to remove.
                            returned: on success
                            type: complex
                            contains:
                                module_name:
                                    description:
                                        - The name of a module.
                                    returned: on success
                                    type: str
                                    sample: module_name_example
                                stream_name:
                                    description:
                                        - The name of a stream of the specified module.
                                    returned: on success
                                    type: str
                                    sample: stream_name_example
                                profile_name:
                                    description:
                                        - The name of a profile of the specified module stream.
                                    returned: on success
                                    type: str
                                    sample: profile_name_example
                                software_source_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that
                                          contains the module stream.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                switch_module_streams_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        module_name:
                            description:
                                - The name of a module.
                            returned: on success
                            type: str
                            sample: module_name_example
                        stream_name:
                            description:
                                - The name of a stream of the specified module.
                            returned: on success
                            type: str
                            sample: stream_name_example
                        software_source_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that contains
                                  the module stream.
                            returned: on success
                            type: str
                            sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                software_source_ids:
                    description:
                        - The software source L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
                          This parameter only applies when the scheduled job is for attaching or detaching software sources.
                    returned: on success
                    type: list
                    sample: []
        work_request_ids:
            description:
                - The list of work request L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) associated with this scheduled
                  job.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The time this scheduled job was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time this scheduled job was updated (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the scheduled job.
            returned: on success
            type: str
            sample: CREATING
        is_managed_by_autonomous_linux:
            description:
                - Indicates whether this scheduled job is managed by the Autonomous Linux service.
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
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
        is_restricted:
            description:
                - Indicates if the schedule job has restricted update and deletion capabilities. For restricted scheduled jobs,
                  you can update only the timeNextExecution, recurringRule, and tags.
            returned: on success
            type: bool
            sample: true
        retry_intervals:
            description:
                - The amount of time in minutes to wait until retrying the scheduled job. If set, the service will automatically retry
                  a failed scheduled job after the interval. For example, you could set the interval to [2,5,10]. If the initial
                  execution of the job fails, the service waits 2 minutes and then retries. If that fails, the service waits 5 minutes
                  and then retries. If that fails, the service waits 10 minutes and then retries.
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "schedule_type": "ONETIME",
        "locations": [],
        "time_next_execution": "2013-10-20T19:20:30+01:00",
        "time_last_execution": "2013-10-20T19:20:30+01:00",
        "recurring_rule": "recurring_rule_example",
        "managed_instance_ids": [],
        "managed_instance_group_ids": [],
        "managed_compartment_ids": [],
        "lifecycle_stage_ids": [],
        "is_subcompartment_included": true,
        "operations": [{
            "operation_type": "INSTALL_PACKAGES",
            "package_names": [],
            "windows_update_names": [],
            "manage_module_streams_details": {
                "enable": [{
                    "module_name": "module_name_example",
                    "stream_name": "stream_name_example",
                    "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                }],
                "disable": [{
                    "module_name": "module_name_example",
                    "stream_name": "stream_name_example",
                    "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                }],
                "install": [{
                    "module_name": "module_name_example",
                    "stream_name": "stream_name_example",
                    "profile_name": "profile_name_example",
                    "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                }],
                "remove": [{
                    "module_name": "module_name_example",
                    "stream_name": "stream_name_example",
                    "profile_name": "profile_name_example",
                    "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
                }]
            },
            "switch_module_streams_details": {
                "module_name": "module_name_example",
                "stream_name": "stream_name_example",
                "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "software_source_ids": []
        }],
        "work_request_ids": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "is_managed_by_autonomous_linux": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "is_restricted": true,
        "retry_intervals": []
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
    from oci.os_management_hub import ScheduledJobClient
    from oci.os_management_hub.models import ChangeScheduledJobCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubScheduledJobActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        run_scheduled_job_now
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


OsManagementHubScheduledJobActionsHelperCustom = get_custom_class(
    "OsManagementHubScheduledJobActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubScheduledJobActionsHelperCustom,
    OsManagementHubScheduledJobActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            scheduled_job_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "run_scheduled_job_now"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="scheduled_job",
        service_client_class=ScheduledJobClient,
        namespace="os_management_hub",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

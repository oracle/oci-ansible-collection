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
module: oci_os_management_hub_scheduled_job_facts
short_description: Fetches details about one or multiple ScheduledJob resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ScheduledJob resources in Oracle Cloud Infrastructure
    - Lists scheduled jobs that match the specified compartment or scheduled job
      L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - If I(scheduled_job_id) is specified, the details of a single ScheduledJob will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    scheduled_job_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the scheduled job.
            - Required to get a specific scheduled_job.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    display_name:
        description:
            - A filter to return resources that match the given user-friendly name.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    lifecycle_state:
        description:
            - A filter to return only scheduled jobs currently in the given state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    managed_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance. This filter returns resources
              associated with this managed instance.
        type: str
    managed_instance_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group. This filter returns
              resources associated with this group.
        type: str
    managed_compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed compartment. This filter returns resources
              associated with this compartment.
        type: str
    lifecycle_stage_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the lifecycle stage. This resource returns resources
              associated with this lifecycle stage.
        type: str
    operation_type:
        description:
            - A filter to return only scheduled jobs with the given operation type.
        type: str
        choices:
            - "INSTALL_PACKAGES"
            - "UPDATE_PACKAGES"
            - "REMOVE_PACKAGES"
            - "UPDATE_ALL"
            - "UPDATE_SECURITY"
            - "UPDATE_BUGFIX"
            - "UPDATE_ENHANCEMENT"
            - "UPDATE_OTHER"
            - "UPDATE_KSPLICE_USERSPACE"
            - "UPDATE_KSPLICE_KERNEL"
            - "MANAGE_MODULE_STREAMS"
            - "SWITCH_MODULE_STREAM"
            - "ATTACH_SOFTWARE_SOURCES"
            - "DETACH_SOFTWARE_SOURCES"
            - "SYNC_MANAGEMENT_STATION_MIRROR"
            - "PROMOTE_LIFECYCLE"
            - "INSTALL_WINDOWS_UPDATES"
            - "INSTALL_ALL_WINDOWS_UPDATES"
            - "INSTALL_SECURITY_WINDOWS_UPDATES"
            - "INSTALL_BUGFIX_WINDOWS_UPDATES"
            - "INSTALL_ENHANCEMENT_WINDOWS_UPDATES"
            - "INSTALL_OTHER_WINDOWS_UPDATES"
    schedule_type:
        description:
            - A filter to return only scheduled jobs of the given scheduling type (one-time or recurring).
        type: str
        choices:
            - "ONETIME"
            - "RECURRING"
    time_start:
        description:
            - A filter to return only resources with a date on or after the given value, in ISO 8601 format.
            - "Example: 2017-07-14T02:40:00.000Z"
        type: str
    time_end:
        description:
            - A filter to return only resources with a date on or before the given value, in ISO 8601 format.
            - "Example: 2017-07-14T02:40:00.000Z"
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
    is_restricted:
        description:
            - A filter to return only restricted scheduled jobs.
        type: bool
    compartment_id_in_subtree:
        description:
            - Indicates whether to include subcompartments in the returned results. Default is false.
        type: bool
    location:
        description:
            - A filter to return only resources whose location matches the given value.
        type: list
        elements: str
        choices:
            - "ON_PREMISE"
            - "OCI_COMPUTE"
            - "AZURE"
            - "EC2"
            - "GCP"
    location_not_equal_to:
        description:
            - A filter to return only resources whose location does not match the given value.
        type: list
        elements: str
        choices:
            - "ON_PREMISE"
            - "OCI_COMPUTE"
            - "AZURE"
            - "EC2"
            - "GCP"
    is_managed_by_autonomous_linux:
        description:
            - Indicates whether to list only resources managed by the Autonomous Linux service.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific scheduled_job
  oci_os_management_hub_scheduled_job_facts:
    # required
    scheduled_job_id: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"

- name: List scheduled_jobs
  oci_os_management_hub_scheduled_job_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    lifecycle_state: CREATING
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    managed_compartment_id: "ocid1.managedcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_stage_id: "ocid1.lifecyclestage.oc1..xxxxxxEXAMPLExxxxxx"
    operation_type: INSTALL_PACKAGES
    schedule_type: ONETIME
    time_start: 2013-10-20T19:20:30+01:00
    time_end: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: timeCreated
    is_restricted: true
    compartment_id_in_subtree: true
    location: [ "ON_PREMISE" ]
    location_not_equal_to: [ "ON_PREMISE" ]
    is_managed_by_autonomous_linux: true

"""

RETURN = """
scheduled_jobs:
    description:
        - List of ScheduledJob resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - User-specified description for the scheduled job.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        recurring_rule:
            description:
                - The frequency schedule for a recurring scheduled job.
                - Returned for get operation
            returned: on success
            type: str
            sample: recurring_rule_example
        is_subcompartment_included:
            description:
                - Indicates whether to apply the scheduled job to all compartments in the tenancy when managedCompartmentIds specifies the tenancy
                  L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) (root compartment).
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        work_request_ids:
            description:
                - The list of work request L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) associated with this scheduled
                  job.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
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
    sample: [{
        "description": "description_example",
        "recurring_rule": "recurring_rule_example",
        "is_subcompartment_included": true,
        "work_request_ids": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "schedule_type": "ONETIME",
        "locations": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_next_execution": "2013-10-20T19:20:30+01:00",
        "time_last_execution": "2013-10-20T19:20:30+01:00",
        "managed_instance_ids": [],
        "managed_instance_group_ids": [],
        "managed_compartment_ids": [],
        "lifecycle_stage_ids": [],
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
        "lifecycle_state": "CREATING",
        "is_managed_by_autonomous_linux": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "is_restricted": true,
        "retry_intervals": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import ScheduledJobClient

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
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_scheduled_job,
            scheduled_job_id=self.module.params.get("scheduled_job_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "display_name_contains",
            "lifecycle_state",
            "managed_instance_id",
            "managed_instance_group_id",
            "managed_compartment_id",
            "lifecycle_stage_id",
            "operation_type",
            "schedule_type",
            "time_start",
            "time_end",
            "sort_order",
            "sort_by",
            "is_restricted",
            "compartment_id_in_subtree",
            "location",
            "location_not_equal_to",
            "is_managed_by_autonomous_linux",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_scheduled_jobs, **optional_kwargs
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
            display_name_contains=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            managed_instance_id=dict(type="str"),
            managed_instance_group_id=dict(type="str"),
            managed_compartment_id=dict(type="str"),
            lifecycle_stage_id=dict(type="str"),
            operation_type=dict(
                type="str",
                choices=[
                    "INSTALL_PACKAGES",
                    "UPDATE_PACKAGES",
                    "REMOVE_PACKAGES",
                    "UPDATE_ALL",
                    "UPDATE_SECURITY",
                    "UPDATE_BUGFIX",
                    "UPDATE_ENHANCEMENT",
                    "UPDATE_OTHER",
                    "UPDATE_KSPLICE_USERSPACE",
                    "UPDATE_KSPLICE_KERNEL",
                    "MANAGE_MODULE_STREAMS",
                    "SWITCH_MODULE_STREAM",
                    "ATTACH_SOFTWARE_SOURCES",
                    "DETACH_SOFTWARE_SOURCES",
                    "SYNC_MANAGEMENT_STATION_MIRROR",
                    "PROMOTE_LIFECYCLE",
                    "INSTALL_WINDOWS_UPDATES",
                    "INSTALL_ALL_WINDOWS_UPDATES",
                    "INSTALL_SECURITY_WINDOWS_UPDATES",
                    "INSTALL_BUGFIX_WINDOWS_UPDATES",
                    "INSTALL_ENHANCEMENT_WINDOWS_UPDATES",
                    "INSTALL_OTHER_WINDOWS_UPDATES",
                ],
            ),
            schedule_type=dict(type="str", choices=["ONETIME", "RECURRING"]),
            time_start=dict(type="str"),
            time_end=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            is_restricted=dict(type="bool"),
            compartment_id_in_subtree=dict(type="bool"),
            location=dict(
                type="list",
                elements="str",
                choices=["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"],
            ),
            location_not_equal_to=dict(
                type="list",
                elements="str",
                choices=["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"],
            ),
            is_managed_by_autonomous_linux=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="scheduled_job",
        service_client_class=ScheduledJobClient,
        namespace="os_management_hub",
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

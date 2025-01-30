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
module: oci_os_management_hub_managed_instance_facts
short_description: Fetches details about one or multiple ManagedInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagedInstance resources in Oracle Cloud Infrastructure
    - Lists managed instances that match the specified compartment or managed instance OCID. Filter the list against a variety of criteria including but not
      limited to its name, status, architecture, and OS version.
    - If I(managed_instance_id) is specified, the details of a single ManagedInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    display_name:
        description:
            - A filter to return resources that match the given display names.
        type: list
        elements: str
        aliases: ["name"]
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    managed_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
            - Required to get a specific managed_instance.
        type: str
        aliases: ["id"]
    status:
        description:
            - A filter to return only managed instances whose status matches the status provided.
        type: list
        elements: str
        choices:
            - "NORMAL"
            - "UNREACHABLE"
            - "ERROR"
            - "WARNING"
            - "REGISTRATION_ERROR"
            - "DELETING"
            - "ONBOARDING"
    arch_type:
        description:
            - A filter to return only instances whose architecture type matches the given architecture.
        type: list
        elements: str
        choices:
            - "X86_64"
            - "AARCH64"
            - "I686"
            - "NOARCH"
            - "SRC"
    os_family:
        description:
            - A filter to return only resources that match the given operating system family.
        type: list
        elements: str
        choices:
            - "ORACLE_LINUX_9"
            - "ORACLE_LINUX_8"
            - "ORACLE_LINUX_7"
            - "ORACLE_LINUX_6"
            - "WINDOWS_SERVER_2016"
            - "WINDOWS_SERVER_2019"
            - "WINDOWS_SERVER_2022"
            - "ALL"
    is_management_station:
        description:
            - A filter to return only managed instances that are acting as management stations.
        type: bool
    group:
        description:
            - A filter to return only managed instances that are attached to the specified group.
        type: str
    group_not_equal_to:
        description:
            - A filter to return only managed instances that are NOT attached to the specified group.
        type: str
    lifecycle_stage:
        description:
            - A filter to return only managed instances that are associated with the specified lifecycle environment.
        type: str
    lifecycle_stage_not_equal_to:
        description:
            - A filter to return only managed instances that are NOT associated with the specified lifecycle environment.
        type: str
    is_attached_to_group_or_lifecycle_stage:
        description:
            - A filter to return only managed instances that are attached to the specified group or lifecycle environment.
        type: bool
    software_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source. This filter returns resources
              associated with this software source.
        type: str
    advisory_name:
        description:
            - The assigned erratum name. It's unique and not changeable.
            - "Example: `ELSA-2020-5804`"
        type: list
        elements: str
    lifecycle_environment:
        description:
            - A filter to return only managed instances in a specific lifecycle environment.
        type: str
    lifecycle_environment_not_equal_to:
        description:
            - A filter to return only managed instances that aren't in a specific lifecycle environment.
        type: str
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
    profile:
        description:
            - A multi filter to return only managed instances that match the given profile ids.
        type: list
        elements: str
    profile_not_equal_to:
        description:
            - A multi filter to return only managed instances that don't contain the given profile
              L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    is_profile_attached:
        description:
            - A filter to return only managed instances with a registration profile attached.
        type: bool
    is_managed_by_autonomous_linux:
        description:
            - Indicates whether to list only resources managed by the Autonomous Linux service.
        type: bool
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
- name: Get a specific managed_instance
  oci_os_management_hub_managed_instance_facts:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List managed_instances
  oci_os_management_hub_managed_instance_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: [ "display_name_example" ]
    display_name_contains: display_name_contains_example
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    status: [ "NORMAL" ]
    arch_type: [ "X86_64" ]
    os_family: [ "ORACLE_LINUX_9" ]
    is_management_station: true
    group: group_example
    group_not_equal_to: group_not_equal_to_example
    lifecycle_stage: lifecycle_stage_example
    lifecycle_stage_not_equal_to: lifecycle_stage_not_equal_to_example
    is_attached_to_group_or_lifecycle_stage: true
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    advisory_name: [ "advisory_name_example" ]
    lifecycle_environment: lifecycle_environment_example
    lifecycle_environment_not_equal_to: lifecycle_environment_not_equal_to_example
    location: [ "ON_PREMISE" ]
    location_not_equal_to: [ "ON_PREMISE" ]
    profile: [ "profile_example" ]
    profile_not_equal_to: [ "profile_not_equal_to_example" ]
    is_profile_attached: true
    is_managed_by_autonomous_linux: true
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
managed_instances:
    description:
        - List of ManagedInstance resources
    returned: on success
    type: complex
    contains:
        time_last_checkin:
            description:
                - Time that the instance last checked in with the service (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_boot:
            description:
                - Time that the instance last booted (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        os_name:
            description:
                - Operating system name.
                - Returned for get operation
            returned: on success
            type: str
            sample: os_name_example
        os_version:
            description:
                - Operating system version.
                - Returned for get operation
            returned: on success
            type: str
            sample: os_version_example
        os_kernel_version:
            description:
                - Operating system kernel version.
                - Returned for get operation
            returned: on success
            type: str
            sample: os_kernel_version_example
        ksplice_effective_kernel_version:
            description:
                - The ksplice effective kernel version.
                - Returned for get operation
            returned: on success
            type: str
            sample: ksplice_effective_kernel_version_example
        profile:
            description:
                - The profile that was used to register this instance with the service.
                - Returned for get operation
            returned: on success
            type: str
            sample: profile_example
        primary_management_station_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station for the instance to use as
                  primary management station.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.primarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx"
        secondary_management_station_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station for the instance to use as
                  secondary managment station.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.secondarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx"
        software_sources:
            description:
                - The list of software sources currently attached to the managed instance.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Software source name.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Software source description.
                    returned: on success
                    type: str
                    sample: description_example
                software_source_type:
                    description:
                        - Type of the software source.
                    returned: on success
                    type: str
                    sample: VENDOR
                is_mandatory_for_autonomous_linux:
                    description:
                        - Indicates whether this is a required software source for Autonomous Linux instances. If true, the user can't unselect it.
                    returned: on success
                    type: bool
                    sample: true
        installed_packages:
            description:
                - Number of packages installed on the instance.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        installed_windows_updates:
            description:
                - Number of Windows updates installed on the instance.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        security_updates_available:
            description:
                - Number of security type updates available for installation.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        bug_updates_available:
            description:
                - Number of bug fix type updates available for installation.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        enhancement_updates_available:
            description:
                - Number of enhancement type updates available for installation.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        other_updates_available:
            description:
                - Number of non-classified (other) updates available for installation.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        scheduled_job_count:
            description:
                - Number of scheduled jobs associated with this instance.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        work_request_count:
            description:
                - Number of work requests associated with this instance.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The date and time the instance was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the instance was last updated (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friendly name for the managed instance.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User-specified description for the managed instance.
            returned: on success
            type: str
            sample: description_example
        tenancy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy that the managed instance resides in.
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the managed instance.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        location:
            description:
                - The location of the managed instance.
            returned: on success
            type: str
            sample: ON_PREMISE
        architecture:
            description:
                - The CPU architecture type of the managed instance.
            returned: on success
            type: str
            sample: X86_64
        os_family:
            description:
                - The operating system type of the managed instance.
            returned: on success
            type: str
            sample: ORACLE_LINUX_9
        status:
            description:
                - Current status of the managed instance.
            returned: on success
            type: str
            sample: NORMAL
        managed_instance_group:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User-friendly name.
                    returned: on success
                    type: str
                    sample: display_name_example
        lifecycle_environment:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User-friendly name.
                    returned: on success
                    type: str
                    sample: display_name_example
        lifecycle_stage:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is immutable on creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - User-friendly name.
                    returned: on success
                    type: str
                    sample: display_name_example
        is_reboot_required:
            description:
                - Indicates whether a reboot is required to complete installation of updates.
            returned: on success
            type: bool
            sample: true
        updates_available:
            description:
                - Number of updates available for installation.
            returned: on success
            type: int
            sample: 56
        is_management_station:
            description:
                - Indicates whether this managed instance is acting as an on-premises management station.
            returned: on success
            type: bool
            sample: true
        notification_topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Oracle Notifications service (ONS) topic. ONS
                  is the channel used to send notifications to the customer.
            returned: on success
            type: str
            sample: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
        autonomous_settings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_data_collection_authorized:
                    description:
                        - Indicates whether Autonomous Linux will collect crash files. This setting can be changed by the user.
                    returned: on success
                    type: bool
                    sample: true
                scheduled_job_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the restricted scheduled job associated
                          with this instance. This value cannot be deleted by the user.
                    returned: on success
                    type: str
                    sample: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        is_managed_by_autonomous_linux:
            description:
                - Indicates whether the Autonomous Linux service manages the instance.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "time_last_checkin": "2013-10-20T19:20:30+01:00",
        "time_last_boot": "2013-10-20T19:20:30+01:00",
        "os_name": "os_name_example",
        "os_version": "os_version_example",
        "os_kernel_version": "os_kernel_version_example",
        "ksplice_effective_kernel_version": "ksplice_effective_kernel_version_example",
        "profile": "profile_example",
        "primary_management_station_id": "ocid1.primarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx",
        "secondary_management_station_id": "ocid1.secondarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx",
        "software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
        "installed_packages": 56,
        "installed_windows_updates": 56,
        "security_updates_available": 56,
        "bug_updates_available": 56,
        "enhancement_updates_available": 56,
        "other_updates_available": 56,
        "scheduled_job_count": 56,
        "work_request_count": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "location": "ON_PREMISE",
        "architecture": "X86_64",
        "os_family": "ORACLE_LINUX_9",
        "status": "NORMAL",
        "managed_instance_group": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        },
        "lifecycle_environment": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        },
        "lifecycle_stage": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        },
        "is_reboot_required": true,
        "updates_available": 56,
        "is_management_station": true,
        "notification_topic_id": "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_settings": {
            "is_data_collection_authorized": true,
            "scheduled_job_id": "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_managed_by_autonomous_linux": true
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import ManagedInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubManagedInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "managed_instance_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "display_name_contains",
            "managed_instance_id",
            "status",
            "arch_type",
            "os_family",
            "is_management_station",
            "group",
            "group_not_equal_to",
            "lifecycle_stage",
            "lifecycle_stage_not_equal_to",
            "is_attached_to_group_or_lifecycle_stage",
            "software_source_id",
            "advisory_name",
            "lifecycle_environment",
            "lifecycle_environment_not_equal_to",
            "location",
            "location_not_equal_to",
            "profile",
            "profile_not_equal_to",
            "is_profile_attached",
            "is_managed_by_autonomous_linux",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_managed_instances, **optional_kwargs
        )


OsManagementHubManagedInstanceFactsHelperCustom = get_custom_class(
    "OsManagementHubManagedInstanceFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubManagedInstanceFactsHelperCustom,
    OsManagementHubManagedInstanceFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="list", elements="str"),
            display_name_contains=dict(type="str"),
            managed_instance_id=dict(aliases=["id"], type="str"),
            status=dict(
                type="list",
                elements="str",
                choices=[
                    "NORMAL",
                    "UNREACHABLE",
                    "ERROR",
                    "WARNING",
                    "REGISTRATION_ERROR",
                    "DELETING",
                    "ONBOARDING",
                ],
            ),
            arch_type=dict(
                type="list",
                elements="str",
                choices=["X86_64", "AARCH64", "I686", "NOARCH", "SRC"],
            ),
            os_family=dict(
                type="list",
                elements="str",
                choices=[
                    "ORACLE_LINUX_9",
                    "ORACLE_LINUX_8",
                    "ORACLE_LINUX_7",
                    "ORACLE_LINUX_6",
                    "WINDOWS_SERVER_2016",
                    "WINDOWS_SERVER_2019",
                    "WINDOWS_SERVER_2022",
                    "ALL",
                ],
            ),
            is_management_station=dict(type="bool"),
            group=dict(type="str"),
            group_not_equal_to=dict(type="str"),
            lifecycle_stage=dict(type="str"),
            lifecycle_stage_not_equal_to=dict(type="str"),
            is_attached_to_group_or_lifecycle_stage=dict(type="bool"),
            software_source_id=dict(type="str"),
            advisory_name=dict(type="list", elements="str"),
            lifecycle_environment=dict(type="str"),
            lifecycle_environment_not_equal_to=dict(type="str"),
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
            profile=dict(type="list", elements="str"),
            profile_not_equal_to=dict(type="list", elements="str"),
            is_profile_attached=dict(type="bool"),
            is_managed_by_autonomous_linux=dict(type="bool"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_instance",
        service_client_class=ManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_instances=result)


if __name__ == "__main__":
    main()

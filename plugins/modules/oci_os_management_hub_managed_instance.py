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
module: oci_os_management_hub_managed_instance
short_description: Manage a ManagedInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a ManagedInstance resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oracle.oci.oci_os_management_hub_managed_instance_actions) module: attach_profile,
      attach_software_sources, detach_profile, detach_software_sources, disable_module_stream, enable_module_stream,
      install_all_windows_updates_on_managed_instances_in_compartment, install_module_stream_profile, install_packages, install_windows_updates,
      manage_module_streams, refresh_software, remove_module_stream_profile, remove_packages, switch_module_stream,
      update_all_packages_on_managed_instances_in_compartment, update_packages."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    description:
        description:
            - User-specified description of the managed instance. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    primary_management_station_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station for the instance to use as
              primary management station.
            - This parameter is updatable.
        type: str
    secondary_management_station_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station for the instance to use as
              secondary management station.
            - This parameter is updatable.
        type: str
    notification_topic_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Oracle Notifications service (ONS) topic. ONS is
              the channel used to send notifications to the customer.
            - This parameter is updatable.
        type: str
    autonomous_settings:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_data_collection_authorized:
                description:
                    - Indicates whether Autonomous Linux will collect crash files.
                    - This parameter is updatable.
                type: bool
    managed_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
        type: str
        aliases: ["id"]
        required: true
    state:
        description:
            - The state of the ManagedInstance.
            - Use I(state=present) to update an existing a ManagedInstance.
            - Use I(state=absent) to delete a ManagedInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update managed_instance
  oci_os_management_hub_managed_instance:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    primary_management_station_id: "ocid1.primarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx"
    secondary_management_station_id: "ocid1.secondarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx"
    notification_topic_id: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_settings:
      # optional
      is_data_collection_authorized: true

- name: Delete managed_instance
  oci_os_management_hub_managed_instance:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
managed_instance:
    description:
        - Details of the ManagedInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        time_last_checkin:
            description:
                - Time that the instance last checked in with the service (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_boot:
            description:
                - Time that the instance last booted (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        os_name:
            description:
                - Operating system name.
            returned: on success
            type: str
            sample: os_name_example
        os_version:
            description:
                - Operating system version.
            returned: on success
            type: str
            sample: os_version_example
        os_kernel_version:
            description:
                - Operating system kernel version.
            returned: on success
            type: str
            sample: os_kernel_version_example
        ksplice_effective_kernel_version:
            description:
                - The ksplice effective kernel version.
            returned: on success
            type: str
            sample: ksplice_effective_kernel_version_example
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
        profile:
            description:
                - The profile that was used to register this instance with the service.
            returned: on success
            type: str
            sample: profile_example
        is_management_station:
            description:
                - Indicates whether this managed instance is acting as an on-premises management station.
            returned: on success
            type: bool
            sample: true
        primary_management_station_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station for the instance to use as
                  primary management station.
            returned: on success
            type: str
            sample: "ocid1.primarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx"
        secondary_management_station_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station for the instance to use as
                  secondary managment station.
            returned: on success
            type: str
            sample: "ocid1.secondarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx"
        software_sources:
            description:
                - The list of software sources currently attached to the managed instance.
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
        installed_packages:
            description:
                - Number of packages installed on the instance.
            returned: on success
            type: int
            sample: 56
        installed_windows_updates:
            description:
                - Number of Windows updates installed on the instance.
            returned: on success
            type: int
            sample: 56
        updates_available:
            description:
                - Number of updates available for installation.
            returned: on success
            type: int
            sample: 56
        security_updates_available:
            description:
                - Number of security type updates available for installation.
            returned: on success
            type: int
            sample: 56
        bug_updates_available:
            description:
                - Number of bug fix type updates available for installation.
            returned: on success
            type: int
            sample: 56
        enhancement_updates_available:
            description:
                - Number of enhancement type updates available for installation.
            returned: on success
            type: int
            sample: 56
        other_updates_available:
            description:
                - Number of non-classified (other) updates available for installation.
            returned: on success
            type: int
            sample: 56
        scheduled_job_count:
            description:
                - Number of scheduled jobs associated with this instance.
            returned: on success
            type: int
            sample: 56
        work_request_count:
            description:
                - Number of work requests associated with this instance.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The date and time the instance was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the instance was last updated (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "location": "ON_PREMISE",
        "time_last_checkin": "2013-10-20T19:20:30+01:00",
        "time_last_boot": "2013-10-20T19:20:30+01:00",
        "os_name": "os_name_example",
        "os_version": "os_version_example",
        "os_kernel_version": "os_kernel_version_example",
        "ksplice_effective_kernel_version": "ksplice_effective_kernel_version_example",
        "architecture": "X86_64",
        "os_family": "ORACLE_LINUX_9",
        "status": "NORMAL",
        "profile": "profile_example",
        "is_management_station": true,
        "primary_management_station_id": "ocid1.primarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx",
        "secondary_management_station_id": "ocid1.secondarymanagementstation.oc1..xxxxxxEXAMPLExxxxxx",
        "software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
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
        "installed_packages": 56,
        "installed_windows_updates": 56,
        "updates_available": 56,
        "security_updates_available": 56,
        "bug_updates_available": 56,
        "enhancement_updates_available": 56,
        "other_updates_available": 56,
        "scheduled_job_count": 56,
        "work_request_count": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "notification_topic_id": "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_settings": {
            "is_data_collection_authorized": true,
            "scheduled_job_id": "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_managed_by_autonomous_linux": true
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import WorkRequestClient
    from oci.os_management_hub import ManagedInstanceClient
    from oci.os_management_hub.models import UpdateManagedInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(ManagedInstanceHelperGen, self).get_possible_entity_types() + [
            "managedinstance",
            "managedinstances",
            "osManagementHubmanagedinstance",
            "osManagementHubmanagedinstances",
            "managedinstanceresource",
            "managedinstancesresource",
            "osmanagementhub",
        ]

    def get_module_resource_id_param(self):
        return "managed_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_instance_id")

    def get_get_fn(self):
        return self.client.get_managed_instance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance, managed_instance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["managed_instance_id"]

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
            self.client.list_managed_instances, **kwargs
        )

    def get_update_model_class(self):
        return UpdateManagedInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                update_managed_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ManagedInstanceHelperCustom = get_custom_class("ManagedInstanceHelperCustom")


class ResourceHelper(ManagedInstanceHelperCustom, ManagedInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            description=dict(type="str"),
            primary_management_station_id=dict(type="str"),
            secondary_management_station_id=dict(type="str"),
            notification_topic_id=dict(type="str"),
            autonomous_settings=dict(
                type="dict",
                options=dict(is_data_collection_authorized=dict(type="bool")),
            ),
            managed_instance_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_instance",
        service_client_class=ManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

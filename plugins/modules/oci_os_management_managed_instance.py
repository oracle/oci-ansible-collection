#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_os_management_managed_instance
short_description: Manage a ManagedInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a ManagedInstance resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oracle.oci.oci_os_management_managed_instance_actions) module: attach_child_software_source,
      attach_parent_software_source, detach_child_software_source, detach_parent_software_source, disable_module_stream, enable_module_stream,
      install_all_package_updates, install_all_windows_updates, install_module_stream_profile, install_package, install_package_update, install_windows_update,
      manage_module_streams, remove_module_stream_profile, remove_package, switch_module_stream."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - OCID for the managed instance
        type: str
        aliases: ["id"]
        required: true
    notification_topic_id:
        description:
            - OCID of the ONS topic used to send notification to users
            - This parameter is updatable.
        type: str
    is_data_collection_authorized:
        description:
            - True if user allow data collection for this instance
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the ManagedInstance.
            - Use I(state=present) to update an existing a ManagedInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update managed_instance
  oci_os_management_managed_instance:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    notification_topic_id: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
    is_data_collection_authorized: true

"""

RETURN = """
managed_instance:
    description:
        - Details of the ManagedInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Managed Instance identifier
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - OCID for the managed instance
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Information specified by the user about the managed instance
            returned: on success
            type: str
            sample: description_example
        last_checkin:
            description:
                - Time at which the instance last checked in
            returned: on success
            type: str
            sample: last_checkin_example
        last_boot:
            description:
                - Time at which the instance last booted
            returned: on success
            type: str
            sample: last_boot_example
        updates_available:
            description:
                - Number of updates available to be installed
            returned: on success
            type: int
            sample: 56
        os_name:
            description:
                - Operating System Name
            returned: on success
            type: str
            sample: os_name_example
        os_version:
            description:
                - Operating System Version
            returned: on success
            type: str
            sample: os_version_example
        os_kernel_version:
            description:
                - Operating System Kernel Version
            returned: on success
            type: str
            sample: os_kernel_version_example
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - status of the managed instance.
            returned: on success
            type: str
            sample: NORMAL
        parent_software_source:
            description:
                - the parent (base) Software Source attached to the Managed Instance
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - software source name
                    returned: on success
                    type: str
                    sample: name_example
                id:
                    description:
                        - software source identifier
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        child_software_sources:
            description:
                - list of child Software Sources attached to the Managed Instance
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - software source name
                    returned: on success
                    type: str
                    sample: name_example
                id:
                    description:
                        - software source identifier
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_groups:
            description:
                - The ids of the managed instance groups of which this instance is a
                  member.
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
        os_family:
            description:
                - The Operating System type of the managed instance.
            returned: on success
            type: str
            sample: LINUX
        is_reboot_required:
            description:
                - Indicates whether a reboot is required to complete installation of updates.
            returned: on success
            type: bool
            sample: true
        notification_topic_id:
            description:
                - OCID of the ONS topic used to send notification to users
            returned: on success
            type: str
            sample: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
        ksplice_effective_kernel_version:
            description:
                - The ksplice effective kernel version
            returned: on success
            type: str
            sample: ksplice_effective_kernel_version_example
        is_data_collection_authorized:
            description:
                - True if user allow data collection for this instance
            returned: on success
            type: bool
            sample: true
        autonomous:
            description:
                - if present, indicates the Managed Instance is an autonomous instance. Holds all the Autonomous specific information
            returned: on success
            type: complex
            contains:
                is_auto_update_enabled:
                    description:
                        - True if daily updates are enabled
                    returned: on success
                    type: bool
                    sample: true
        security_updates_available:
            description:
                - Number of security type updates available to be installed
            returned: on success
            type: int
            sample: 56
        bug_updates_available:
            description:
                - Number of bug fix type updates available to be installed
            returned: on success
            type: int
            sample: 56
        enhancement_updates_available:
            description:
                - Number of enhancement type updates available to be installed
            returned: on success
            type: int
            sample: 56
        other_updates_available:
            description:
                - Number of non-classified updates available to be installed
            returned: on success
            type: int
            sample: 56
        scheduled_job_count:
            description:
                - Number of scheduled jobs associated with this instance
            returned: on success
            type: int
            sample: 56
        work_request_count:
            description:
                - Number of work requests associated with this instance
            returned: on success
            type: int
            sample: 56
    sample: {
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "last_checkin": "last_checkin_example",
        "last_boot": "last_boot_example",
        "updates_available": 56,
        "os_name": "os_name_example",
        "os_version": "os_version_example",
        "os_kernel_version": "os_kernel_version_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "NORMAL",
        "parent_software_source": {
            "name": "name_example",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "child_software_sources": [{
            "name": "name_example",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "managed_instance_groups": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "os_family": "LINUX",
        "is_reboot_required": true,
        "notification_topic_id": "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx",
        "ksplice_effective_kernel_version": "ksplice_effective_kernel_version_example",
        "is_data_collection_authorized": true,
        "autonomous": {
            "is_auto_update_enabled": true
        },
        "security_updates_available": 56,
        "bug_updates_available": 56,
        "enhancement_updates_available": 56,
        "other_updates_available": 56,
        "scheduled_job_count": 56,
        "work_request_count": 56
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
    from oci.os_management.models import UpdateManagedInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(ManagedInstanceHelperGen, self).get_possible_entity_types() + [
            "managedinstance",
            "managedinstances",
            "osManagementmanagedinstance",
            "osManagementmanagedinstances",
            "managedinstanceresource",
            "managedinstancesresource",
            "osmanagement",
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
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

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


ManagedInstanceHelperCustom = get_custom_class("ManagedInstanceHelperCustom")


class ResourceHelper(ManagedInstanceHelperCustom, ManagedInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            managed_instance_id=dict(aliases=["id"], type="str", required=True),
            notification_topic_id=dict(type="str"),
            is_data_collection_authorized=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_instance",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

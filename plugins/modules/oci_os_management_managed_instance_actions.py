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
module: oci_os_management_managed_instance_actions
short_description: Perform actions on a ManagedInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagedInstance resource in Oracle Cloud Infrastructure
    - For I(action=attach_child_software_source), adds a child software source to a managed instance. After the software
      source has been added, then packages from that software source can be
      installed on the managed instance.
    - For I(action=attach_parent_software_source), adds a parent software source to a managed instance. After the software
      source has been added, then packages from that software source can be
      installed on the managed instance. Software sources that have this
      software source as a parent will be able to be added to this managed instance.
    - For I(action=detach_child_software_source), removes a child software source from a managed instance. Packages will no longer be able to be
      installed from these software sources.
    - For I(action=detach_parent_software_source), removes a software source from a managed instance. All child software sources will also be removed
      from the managed instance. Packages will no longer be able to be installed from these software sources.
    - For I(action=install_all_package_updates), install all of the available package updates for the managed instance.
    - For I(action=install_all_windows_updates), install all of the available Windows updates for the managed instance.
    - For I(action=install_package), installs a package on a managed instance.
    - For I(action=install_package_update), updates a package on a managed instance.
    - For I(action=install_windows_update), installs a Windows update on a managed instance.
    - For I(action=remove_package), removes an installed package from a managed instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - OCID for the managed instance
        type: str
        aliases: ["id"]
        required: true
    software_source_id:
        description:
            - OCID for the Software Source
            - Required for I(action=attach_child_software_source), I(action=attach_parent_software_source), I(action=detach_child_software_source),
              I(action=detach_parent_software_source).
        type: str
    update_type:
        description:
            - The type of updates to be applied
            - Applicable only for I(action=install_all_package_updates)I(action=install_all_windows_updates).
        type: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "OTHER"
            - "KSPLICE"
            - "ALL"
    software_package_name:
        description:
            - Package name
            - Required for I(action=install_package), I(action=install_package_update), I(action=remove_package).
        type: str
    windows_update_name:
        description:
            - "Unique identifier for the Windows update. NOTE - This is not an OCID,
              but is a unique identifier assigned by Microsoft.
              Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`"
            - Required for I(action=install_windows_update).
        type: str
    action:
        description:
            - The action to perform on the ManagedInstance.
        type: str
        required: true
        choices:
            - "attach_child_software_source"
            - "attach_parent_software_source"
            - "detach_child_software_source"
            - "detach_parent_software_source"
            - "install_all_package_updates"
            - "install_all_windows_updates"
            - "install_package"
            - "install_package_update"
            - "install_windows_update"
            - "remove_package"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action attach_child_software_source on managed_instance
  oci_os_management_managed_instance_actions:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_child_software_source

- name: Perform action attach_parent_software_source on managed_instance
  oci_os_management_managed_instance_actions:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_parent_software_source

- name: Perform action detach_child_software_source on managed_instance
  oci_os_management_managed_instance_actions:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_child_software_source

- name: Perform action detach_parent_software_source on managed_instance
  oci_os_management_managed_instance_actions:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_parent_software_source

- name: Perform action install_all_package_updates on managed_instance
  oci_os_management_managed_instance_actions:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_all_package_updates

- name: Perform action install_all_windows_updates on managed_instance
  oci_os_management_managed_instance_actions:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_all_windows_updates

- name: Perform action install_package on managed_instance
  oci_os_management_managed_instance_actions:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    software_package_name: software_package_name_example
    action: install_package

- name: Perform action install_package_update on managed_instance
  oci_os_management_managed_instance_actions:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    software_package_name: software_package_name_example
    action: install_package_update

- name: Perform action install_windows_update on managed_instance
  oci_os_management_managed_instance_actions:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    windows_update_name: 6981d463-cd91-4a26-b7c4-ea4ded9183ed
    action: install_windows_update

- name: Perform action remove_package on managed_instance
  oci_os_management_managed_instance_actions:
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    software_package_name: software_package_name_example
    action: remove_package

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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import OsManagementClient
    from oci.os_management.models import (
        AttachChildSoftwareSourceToManagedInstanceDetails,
    )
    from oci.os_management.models import (
        AttachParentSoftwareSourceToManagedInstanceDetails,
    )
    from oci.os_management.models import (
        DetachChildSoftwareSourceFromManagedInstanceDetails,
    )
    from oci.os_management.models import (
        DetachParentSoftwareSourceFromManagedInstanceDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_child_software_source
        attach_parent_software_source
        detach_child_software_source
        detach_parent_software_source
        install_all_package_updates
        install_all_windows_updates
        install_package
        install_package_update
        install_windows_update
        remove_package
    """

    @staticmethod
    def get_module_resource_id_param():
        return "managed_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_instance_id")

    def get_get_fn(self):
        return self.client.get_managed_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
        )

    def attach_child_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachChildSoftwareSourceToManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_child_software_source_to_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                attach_child_software_source_to_managed_instance_details=action_details,
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

    def attach_parent_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachParentSoftwareSourceToManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_parent_software_source_to_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                attach_parent_software_source_to_managed_instance_details=action_details,
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

    def detach_child_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachChildSoftwareSourceFromManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_child_software_source_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                detach_child_software_source_from_managed_instance_details=action_details,
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

    def detach_parent_software_source(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachParentSoftwareSourceFromManagedInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_parent_software_source_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                detach_parent_software_source_from_managed_instance_details=action_details,
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

    def install_all_package_updates(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_all_package_updates_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                update_type=self.module.params.get("update_type"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_all_windows_updates(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_all_windows_updates_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                update_type=self.module.params.get("update_type"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_package(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_package_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                software_package_name=self.module.params.get("software_package_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_package_update(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_package_update_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                software_package_name=self.module.params.get("software_package_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_windows_update(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_windows_update_on_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                windows_update_name=self.module.params.get("windows_update_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_package(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_package_from_managed_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_id=self.module.params.get("managed_instance_id"),
                software_package_name=self.module.params.get("software_package_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ManagedInstanceActionsHelperCustom = get_custom_class(
    "ManagedInstanceActionsHelperCustom"
)


class ResourceHelper(
    ManagedInstanceActionsHelperCustom, ManagedInstanceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            managed_instance_id=dict(aliases=["id"], type="str", required=True),
            software_source_id=dict(type="str"),
            update_type=dict(
                type="str",
                choices=[
                    "SECURITY",
                    "BUGFIX",
                    "ENHANCEMENT",
                    "OTHER",
                    "KSPLICE",
                    "ALL",
                ],
            ),
            software_package_name=dict(type="str"),
            windows_update_name=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "attach_child_software_source",
                    "attach_parent_software_source",
                    "detach_child_software_source",
                    "detach_parent_software_source",
                    "install_all_package_updates",
                    "install_all_windows_updates",
                    "install_package",
                    "install_package_update",
                    "install_windows_update",
                    "remove_package",
                ],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

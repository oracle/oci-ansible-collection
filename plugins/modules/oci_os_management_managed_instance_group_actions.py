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
module: oci_os_management_managed_instance_group_actions
short_description: Perform actions on a ManagedInstanceGroup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagedInstanceGroup resource in Oracle Cloud Infrastructure
    - For I(action=attach_managed_instance), adds a Managed Instance to a Managed Instance Group. After the Managed
      Instance has been added, then operations can be performed on the Managed
      Instance Group which will then apply to all Managed Instances in the
      group.
    - For I(action=change_compartment), moves a resource into a different compartment. When provided, If-Match
      is checked against ETag values of the resource.
    - For I(action=detach_managed_instance), removes a Managed Instance from a Managed Instance Group.
    - For I(action=install_all_updates), install all of the available updates for the Managed Instance Group.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              compartment into which the resource should be moved.
            - Applicable only for I(action=change_compartment).
        type: str
    managed_instance_id:
        description:
            - OCID for the managed instance
            - Required for I(action=attach_managed_instance), I(action=detach_managed_instance).
        type: str
    managed_instance_group_id:
        description:
            - OCID for the managed instance group
        type: str
        aliases: ["id"]
        required: true
    update_type:
        description:
            - The type of updates to be applied
            - Applicable only for I(action=install_all_updates).
        type: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "OTHER"
            - "KSPLICE"
            - "ALL"
    action:
        description:
            - The action to perform on the ManagedInstanceGroup.
        type: str
        required: true
        choices:
            - "attach_managed_instance"
            - "change_compartment"
            - "detach_managed_instance"
            - "install_all_updates"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action attach_managed_instance on managed_instance_group
  oci_os_management_managed_instance_group_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_managed_instance

- name: Perform action change_compartment on managed_instance_group
  oci_os_management_managed_instance_group_actions:
    # required
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action detach_managed_instance on managed_instance_group
  oci_os_management_managed_instance_group_actions:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_managed_instance

- name: Perform action install_all_updates on managed_instance_group
  oci_os_management_managed_instance_group_actions:
    # required
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_all_updates

    # optional
    update_type: SECURITY

"""

RETURN = """
managed_instance_group:
    description:
        - Details of the ManagedInstanceGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Managed Instance Group identifier
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - OCID for the managed instance group
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Information specified by the user about the managed instance group
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instances:
            description:
                - list of Managed Instances in the group
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
                - The current state of the Software Source.
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
        os_family:
            description:
                - The Operating System type of the managed instance.
            returned: on success
            type: str
            sample: LINUX
    sample: {
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_instances": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "os_family": "LINUX"
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
    from oci.os_management import OsManagementClient
    from oci.os_management.models import ChangeManagedInstanceGroupCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceGroupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_managed_instance
        change_compartment
        detach_managed_instance
        install_all_updates
    """

    @staticmethod
    def get_module_resource_id_param():
        return "managed_instance_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_instance_group_id")

    def get_get_fn(self):
        return self.client.get_managed_instance_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance_group,
            managed_instance_group_id=self.module.params.get(
                "managed_instance_group_id"
            ),
        )

    def attach_managed_instance(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_managed_instance_to_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                managed_instance_id=self.module.params.get("managed_instance_id"),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeManagedInstanceGroupCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_managed_instance_group_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                change_managed_instance_group_compartment_details=action_details,
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

    def detach_managed_instance(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_managed_instance_from_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                managed_instance_id=self.module.params.get("managed_instance_id"),
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

    def install_all_updates(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_all_updates_on_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
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


ManagedInstanceGroupActionsHelperCustom = get_custom_class(
    "ManagedInstanceGroupActionsHelperCustom"
)


class ResourceHelper(
    ManagedInstanceGroupActionsHelperCustom, ManagedInstanceGroupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            managed_instance_id=dict(type="str"),
            managed_instance_group_id=dict(aliases=["id"], type="str", required=True),
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
            action=dict(
                type="str",
                required=True,
                choices=[
                    "attach_managed_instance",
                    "change_compartment",
                    "detach_managed_instance",
                    "install_all_updates",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_instance_group",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

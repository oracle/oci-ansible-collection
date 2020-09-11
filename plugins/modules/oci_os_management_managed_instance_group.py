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
module: oci_os_management_managed_instance_group
short_description: Manage a ManagedInstanceGroup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ManagedInstanceGroup resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Managed Instance Group on the management system.
      This will not contain any managed instances after it is first created,
      and they must be added later.
    - "This resource has the following action operations in the M(oci_managed_instance_group_actions) module: attach_managed_instance, detach_managed_instance."
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Managed Instance Group identifier
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Information specified by the user about the managed instance group
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - OCID for the Compartment
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    os_family:
        description:
            - The Operating System type of the managed instance(s) on which this scheduled job will operate.
              If not specified, this defaults to Linux.
        type: str
        choices:
            - "LINUX"
            - "WINDOWS"
            - "ALL"
    managed_instance_group_id:
        description:
            - OCID for the managed instance group
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ManagedInstanceGroup.
            - Use I(state=present) to create or update a ManagedInstanceGroup.
            - Use I(state=absent) to delete a ManagedInstanceGroup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create managed_instance_group
  oci_os_management_managed_instance_group:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update managed_instance_group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_managed_instance_group:
    display_name: display_name_example
    description: description_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update managed_instance_group
  oci_os_management_managed_instance_group:
    display_name: display_name_example
    description: description_example
    managed_instance_group_id: ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete managed_instance_group
  oci_os_management_managed_instance_group:
    managed_instance_group_id: ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete managed_instance_group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_managed_instance_group:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

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
            type: string
            sample: display_name_example
        id:
            description:
                - OCID for the managed instance group
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        description:
            description:
                - Information specified by the user about the managed instance group
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
                - The current state of the Software Source.
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
        os_family:
            description:
                - The Operating System type of the managed instance.
            returned: on success
            type: string
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
    from oci.os_management.models import CreateManagedInstanceGroupDetails
    from oci.os_management.models import UpdateManagedInstanceGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceGroupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "os_family"]

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
            self.client.list_managed_instance_groups, **kwargs
        )

    def get_create_model_class(self):
        return CreateManagedInstanceGroupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(create_managed_instance_group_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateManagedInstanceGroupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                update_managed_instance_group_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


ManagedInstanceGroupHelperCustom = get_custom_class("ManagedInstanceGroupHelperCustom")


class ResourceHelper(ManagedInstanceGroupHelperCustom, ManagedInstanceGroupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            compartment_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            os_family=dict(type="str", choices=["LINUX", "WINDOWS", "ALL"]),
            managed_instance_group_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_instance_group",
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

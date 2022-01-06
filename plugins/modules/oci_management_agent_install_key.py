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
module: oci_management_agent_install_key
short_description: Manage a ManagementAgentInstallKey resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ManagementAgentInstallKey resource in Oracle Cloud Infrastructure
    - For I(state=present), user creates a new install key as part of this API.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Management Agent install Key Name
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    allowed_key_install_count:
        description:
            - Total number of install for this keys
        type: int
    time_expires:
        description:
            - date after which key would expire after creation
        type: str
    compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    management_agent_install_key_id:
        description:
            - Unique Management Agent Install Key identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    is_key_active:
        description:
            - if set to true the install key state would be set to Active and if false to Inactive
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the ManagementAgentInstallKey.
            - Use I(state=present) to create or update a ManagementAgentInstallKey.
            - Use I(state=absent) to delete a ManagementAgentInstallKey.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create management_agent_install_key
  oci_management_agent_install_key:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    allowed_key_install_count: 56
    time_expires: time_expires_example

- name: Update management_agent_install_key
  oci_management_agent_install_key:
    # required
    management_agent_install_key_id: "ocid1.managementagentinstallkey.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    is_key_active: true

- name: Update management_agent_install_key using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_management_agent_install_key:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_key_active: true

- name: Delete management_agent_install_key
  oci_management_agent_install_key:
    # required
    management_agent_install_key_id: "ocid1.managementagentinstallkey.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete management_agent_install_key using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_management_agent_install_key:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
management_agent_install_key:
    description:
        - Details of the ManagementAgentInstallKey resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Agent install Key identifier
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Management Agent Install Key Name
            returned: on success
            type: str
            sample: display_name_example
        key:
            description:
                - Management Agent Install Key
            returned: on success
            type: str
            sample: key_example
        created_by_principal_id:
            description:
                - Principal id of user who created the Agent Install key
            returned: on success
            type: str
            sample: "ocid1.createdbyprincipal.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        allowed_key_install_count:
            description:
                - Total number of install for this keys
            returned: on success
            type: int
            sample: 56
        current_key_install_count:
            description:
                - Total number of install for this keys
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - Status of Key
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_expires:
            description:
                - date after which key would expire after creation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The time when Management Agent install Key was created. An RFC3339 formatted date time string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when Management Agent install Key was updated. An RFC3339 formatted date time string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "key": "key_example",
        "created_by_principal_id": "ocid1.createdbyprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "allowed_key_install_count": 56,
        "current_key_install_count": 56,
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_expires": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.management_agent import ManagementAgentClient
    from oci.management_agent.models import CreateManagementAgentInstallKeyDetails
    from oci.management_agent.models import UpdateManagementAgentInstallKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementAgentInstallKeyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "management_agent_install_key_id"

    def get_module_resource_id(self):
        return self.module.params.get("management_agent_install_key_id")

    def get_get_fn(self):
        return self.client.get_management_agent_install_key

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_agent_install_key,
            management_agent_install_key_id=self.module.params.get(
                "management_agent_install_key_id"
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
        optional_list_method_params = ["display_name"]

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
            self.client.list_management_agent_install_keys, **kwargs
        )

    def get_create_model_class(self):
        return CreateManagementAgentInstallKeyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_management_agent_install_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_management_agent_install_key_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateManagementAgentInstallKeyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_management_agent_install_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_agent_install_key_id=self.module.params.get(
                    "management_agent_install_key_id"
                ),
                update_management_agent_install_key_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_management_agent_install_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_agent_install_key_id=self.module.params.get(
                    "management_agent_install_key_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ManagementAgentInstallKeyHelperCustom = get_custom_class(
    "ManagementAgentInstallKeyHelperCustom"
)


class ResourceHelper(
    ManagementAgentInstallKeyHelperCustom, ManagementAgentInstallKeyHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            allowed_key_install_count=dict(type="int"),
            time_expires=dict(type="str"),
            compartment_id=dict(type="str"),
            management_agent_install_key_id=dict(aliases=["id"], type="str"),
            is_key_active=dict(type="bool", no_log=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="management_agent_install_key",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
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

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
module: oci_management_agent
short_description: Manage a ManagementAgent resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a ManagementAgent resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oci_management_agent_actions) module: deploy_plugins."
version_added: "2.9"
author: Oracle (@oracle)
options:
    management_agent_id:
        description:
            - Unique Management Agent identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    is_agent_auto_upgradable:
        description:
            - true if the agent can be upgraded automatically; false if it must be upgraded manually. true is currently unsupported.
            - This parameter is updatable.
        type: bool
    display_name:
        description:
            - New displayName of Agent.
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
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
    compartment_id:
        description:
            - The ID of the compartment from which the Management Agents to be listed.
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the ManagementAgent.
            - Use I(state=present) to update an existing a ManagementAgent.
            - Use I(state=absent) to delete a ManagementAgent.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update management_agent using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_management_agent:
    is_agent_auto_upgradable: true
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update management_agent
  oci_management_agent:
    management_agent_id: ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx
    is_agent_auto_upgradable: true

- name: Delete management_agent
  oci_management_agent:
    management_agent_id: ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete management_agent using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_management_agent:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
management_agent:
    description:
        - Details of the ManagementAgent resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - agent identifier
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        install_key_id:
            description:
                - agent install key identifier
            returned: on success
            type: string
            sample: ocid1.installkey.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - Management Agent Name
            returned: on success
            type: string
            sample: display_name_example
        platform_type:
            description:
                - Platform Type
            returned: on success
            type: string
            sample: LINUX
        platform_name:
            description:
                - Platform Name
            returned: on success
            type: string
            sample: platform_name_example
        platform_version:
            description:
                - Platform Version
            returned: on success
            type: string
            sample: platform_version_example
        version:
            description:
                - Management Agent Version
            returned: on success
            type: string
            sample: version_example
        host:
            description:
                - Management Agent host machine name
            returned: on success
            type: string
            sample: host_example
        install_path:
            description:
                - Path where Management Agent is installed
            returned: on success
            type: string
            sample: install_path_example
        plugin_list:
            description:
                - list of managementAgentPlugins associated with the agent
            returned: on success
            type: complex
            contains:
                plugin_id:
                    description:
                        - Plugin Id
                    returned: on success
                    type: string
                    sample: ocid1.plugin.oc1..xxxxxxEXAMPLExxxxxx
                plugin_name:
                    description:
                        - Management Agent Plugin Name
                    returned: on success
                    type: string
                    sample: plugin_name_example
                plugin_display_name:
                    description:
                        - Management Agent Plugin Identifier, can be renamed
                    returned: on success
                    type: string
                    sample: plugin_display_name_example
                plugin_version:
                    description:
                        - Plugin Version
                    returned: on success
                    type: string
                    sample: plugin_version_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        is_agent_auto_upgradable:
            description:
                - true if the agent can be upgraded automatically; false if it must be upgraded manually. true is currently unsupported.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time the Management Agent was created. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the Management Agent was updated. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_last_heartbeat:
            description:
                - The time the Management Agent has last recorded its health status in telemetry. This value will be null if the agent has not recorded its
                  health status in last 7 days. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        availability_status:
            description:
                - The current availability status of managementAgent
            returned: on success
            type: string
            sample: ACTIVE
        lifecycle_state:
            description:
                - The current state of managementAgent
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: lifecycle_details_example
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "install_key_id": "ocid1.installkey.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "platform_type": "LINUX",
        "platform_name": "platform_name_example",
        "platform_version": "platform_version_example",
        "version": "version_example",
        "host": "host_example",
        "install_path": "install_path_example",
        "plugin_list": [{
            "plugin_id": "ocid1.plugin.oc1..xxxxxxEXAMPLExxxxxx",
            "plugin_name": "plugin_name_example",
            "plugin_display_name": "plugin_display_name_example",
            "plugin_version": "plugin_version_example"
        }],
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_agent_auto_upgradable": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_last_heartbeat": "2013-10-20T19:20:30+01:00",
        "availability_status": "ACTIVE",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.management_agent.models import UpdateManagementAgentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementAgentHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "management_agent_id"

    def get_module_resource_id(self):
        return self.module.params.get("management_agent_id")

    def get_get_fn(self):
        return self.client.get_management_agent

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_agent,
            management_agent_id=self.module.params.get("management_agent_id"),
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
            self.client.list_management_agents, **kwargs
        )

    def get_update_model_class(self):
        return UpdateManagementAgentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_management_agent,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_agent_id=self.module.params.get("management_agent_id"),
                update_management_agent_details=update_details,
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
            call_fn=self.client.delete_management_agent,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_agent_id=self.module.params.get("management_agent_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ManagementAgentHelperCustom = get_custom_class("ManagementAgentHelperCustom")


class ResourceHelper(ManagementAgentHelperCustom, ManagementAgentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            management_agent_id=dict(aliases=["id"], type="str"),
            is_agent_auto_upgradable=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="management_agent",
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

    module.exit_json(**result)


if __name__ == "__main__":
    main()

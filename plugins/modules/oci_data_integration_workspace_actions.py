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
module: oci_data_integration_workspace_actions
short_description: Perform actions on a Workspace resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Workspace resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a workspace to a specified compartment.
    - For I(action=start), starts a workspace.
    - For I(action=stop), stops a workspace.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to move the the workspace to.
            - Required for I(action=change_compartment).
        type: str
    workspace_id:
        description:
            - The workspace ID.
        type: str
        aliases: ["id"]
        required: true
    quiesce_timeout:
        description:
            - Used to set the timeout for Data Integration to gracefully close down any running jobs before stopping the workspace.
            - Applicable only for I(action=stop).
        type: int
    is_force_operation:
        description:
            - Used to force close down the workspace.
            - Applicable only for I(action=stop).
        type: bool
    action:
        description:
            - The action to perform on the Workspace.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on workspace
  oci_data_integration_workspace_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    workspace_id: "ocid1.workspace.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action start on workspace
  oci_data_integration_workspace_actions:
    # required
    workspace_id: "ocid1.workspace.oc1..xxxxxxEXAMPLExxxxxx"
    action: start

- name: Perform action stop on workspace
  oci_data_integration_workspace_actions:
    # required
    workspace_id: "ocid1.workspace.oc1..xxxxxxEXAMPLExxxxxx"
    action: stop

    # optional
    quiesce_timeout: 0
    is_force_operation: true

"""

RETURN = """
workspace:
    description:
        - Details of the Workspace resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        vcn_id:
            description:
                - The OCID of the VCN the subnet is in.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The OCID of the subnet for customer connected databases.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        dns_server_ip:
            description:
                - The IP of the custom DNS.
            returned: on success
            type: str
            sample: dns_server_ip_example
        dns_server_zone:
            description:
                - The DNS zone of the custom DNS to use to resolve names.
            returned: on success
            type: str
            sample: dns_server_zone_example
        is_private_network_enabled:
            description:
                - Specifies whether the private network connection is enabled or disabled.
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        description:
            description:
                - A detailed description for the workspace.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment containing the workspace.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the workspace was created, in the timestamp format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the workspace was updated, in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - "Lifecycle states for workspaces in Data Integration Service
                  CREATING - The resource is being created and may not be usable until the entire metadata is defined
                  UPDATING - The resource is being updated and may not be usable until all changes are commited
                  DELETING - The resource is being deleted and might require deep cleanup of children.
                  ACTIVE   - The resource is valid and available for access
                  INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for
                           administrative reasons
                  DELETED  - The resource has been deleted and isn't available
                  FAILED   - The resource is in a failed state due to validation or other errors
                  STARTING - The resource is being started and may not be usable until becomes ACTIVE again
                  STOPPING - The resource is in the process of Stopping and may not be usable until it Stops or fails
                  STOPPED  - The resource is in Stopped state due to stop operation."
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed
                  state.
            returned: on success
            type: str
            sample: state_message_example
        id:
            description:
                - A system-generated and immutable identifier assigned to the workspace upon creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint_id:
            description:
                - OCID of the private endpoint associated with the container/workspace.
            returned: on success
            type: str
            sample: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint_name:
            description:
                - Name of the private endpoint associated with the container/workspace.
            returned: on success
            type: str
            sample: endpoint_name_example
        registry_id:
            description:
                - DCMS Registry ID associated with the container/workspace.
            returned: on success
            type: str
            sample: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "dns_server_ip": "dns_server_ip_example",
        "dns_server_zone": "dns_server_zone_example",
        "is_private_network_enabled": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "description": "description_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint_id": "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint_name": "endpoint_name_example",
        "registry_id": "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.data_integration import DataIntegrationClient
    from oci.data_integration.models import ChangeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WorkspaceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "workspace_id"

    def get_module_resource_id(self):
        return self.module.params.get("workspace_id")

    def get_get_fn(self):
        return self.client.get_workspace

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_workspace,
            workspace_id=self.module.params.get("workspace_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                workspace_id=self.module.params.get("workspace_id"),
                change_compartment_details=action_details,
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

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_workspace,
            call_fn_args=(),
            call_fn_kwargs=dict(workspace_id=self.module.params.get("workspace_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_workspace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                workspace_id=self.module.params.get("workspace_id"),
                quiesce_timeout=self.module.params.get("quiesce_timeout"),
                is_force_operation=self.module.params.get("is_force_operation"),
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


WorkspaceActionsHelperCustom = get_custom_class("WorkspaceActionsHelperCustom")


class ResourceHelper(WorkspaceActionsHelperCustom, WorkspaceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            workspace_id=dict(aliases=["id"], type="str", required=True),
            quiesce_timeout=dict(type="int"),
            is_force_operation=dict(type="bool"),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "start", "stop"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="workspace",
        service_client_class=DataIntegrationClient,
        namespace="data_integration",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

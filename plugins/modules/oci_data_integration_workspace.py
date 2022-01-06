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
module: oci_data_integration_workspace
short_description: Manage a Workspace resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Workspace resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Data Integration workspace ready for performing data integration tasks.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_integration_workspace_actions) module: change_compartment, start, stop."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vcn_id:
        description:
            - The OCID of the VCN the subnet is in.
        type: str
    subnet_id:
        description:
            - The OCID of the subnet for customer connected databases.
        type: str
    dns_server_ip:
        description:
            - The IP of the custom DNS.
        type: str
    dns_server_zone:
        description:
            - The DNS zone of the custom DNS to use to resolve names.
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    description:
        description:
            - A user defined description for the workspace.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - The OCID of the compartment containing the workspace.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    is_private_network_enabled:
        description:
            - Specifies whether the private network connection is enabled or disabled.
        type: bool
    workspace_id:
        description:
            - The workspace ID.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    quiesce_timeout:
        description:
            - Used to set the timeout for Data Integration to gracefully close down any running jobs before stopping the workspace.
        type: int
    is_force_operation:
        description:
            - Used to force close down the workspace.
        type: bool
    state:
        description:
            - The state of the Workspace.
            - Use I(state=present) to create or update a Workspace.
            - Use I(state=absent) to delete a Workspace.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create workspace
  oci_data_integration_workspace:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    dns_server_ip: dns_server_ip_example
    dns_server_zone: dns_server_zone_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    is_private_network_enabled: true

- name: Update workspace
  oci_data_integration_workspace:
    # required
    workspace_id: "ocid1.workspace.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    display_name: display_name_example

- name: Update workspace using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_integration_workspace:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example

- name: Delete workspace
  oci_data_integration_workspace:
    # required
    workspace_id: "ocid1.workspace.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    quiesce_timeout: 0
    is_force_operation: true

- name: Delete workspace using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_integration_workspace:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.data_integration import DataIntegrationClient
    from oci.data_integration.models import CreateWorkspaceDetails
    from oci.data_integration.models import UpdateWorkspaceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WorkspaceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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
            self.client.list_workspaces, **kwargs
        )

    def get_create_model_class(self):
        return CreateWorkspaceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_workspace,
            call_fn_args=(),
            call_fn_kwargs=dict(create_workspace_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateWorkspaceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_workspace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                workspace_id=self.module.params.get("workspace_id"),
                update_workspace_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_workspace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                workspace_id=self.module.params.get("workspace_id"),
                quiesce_timeout=self.module.params.get("quiesce_timeout"),
                is_force_operation=self.module.params.get("is_force_operation"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


WorkspaceHelperCustom = get_custom_class("WorkspaceHelperCustom")


class ResourceHelper(WorkspaceHelperCustom, WorkspaceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            vcn_id=dict(type="str"),
            subnet_id=dict(type="str"),
            dns_server_ip=dict(type="str"),
            dns_server_zone=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            is_private_network_enabled=dict(type="bool"),
            workspace_id=dict(aliases=["id"], type="str"),
            quiesce_timeout=dict(type="int"),
            is_force_operation=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="workspace",
        service_client_class=DataIntegrationClient,
        namespace="data_integration",
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

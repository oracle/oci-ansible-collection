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
module: oci_data_integration_workspace_facts
short_description: Fetches details about one or multiple Workspace resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Workspace resources in Oracle Cloud Infrastructure
    - Retrieves a list of Data Integration workspaces.
    - If I(workspace_id) is specified, the details of a single Workspace will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    workspace_id:
        description:
            - The workspace ID.
            - Required to get a specific workspace.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment containing the resources you want to list.
            - Required to list multiple workspaces.
        type: str
    name:
        description:
            - Used to filter by the name of the object.
        type: str
    lifecycle_state:
        description:
            - The lifecycle state of a resource. When specified, the operation only returns resources that match the given lifecycle state. When not specified,
              all lifecycle states are processed as a match.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "STARTING"
            - "STOPPING"
            - "STOPPED"
    sort_order:
        description:
            - Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other
              fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is
              by relevance score in descending order).
        type: str
        choices:
            - "TIME_CREATED"
            - "DISPLAY_NAME"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List workspaces
  oci_data_integration_workspace_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific workspace
  oci_data_integration_workspace_facts:
    workspace_id: "ocid1.workspace.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
workspaces:
    description:
        - List of Workspace resources
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
            sample: "2019-08-25T21:10:29.410+0000"
        time_updated:
            description:
                - The date and time the workspace was updated, in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2019-08-25T21:10:29.410+0000"
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
    sample: [{
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
        "time_created": "2019-08-25T21:10:29.410+0000",
        "time_updated": "2019-08-25T21:10:29.410+0000",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_integration import DataIntegrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WorkspaceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "workspace_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_workspace,
            workspace_id=self.module.params.get("workspace_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_workspaces,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


WorkspaceFactsHelperCustom = get_custom_class("WorkspaceFactsHelperCustom")


class ResourceFactsHelper(WorkspaceFactsHelperCustom, WorkspaceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            workspace_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "STARTING",
                    "STOPPING",
                    "STOPPED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIME_CREATED", "DISPLAY_NAME"]),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="workspace",
        service_client_class=DataIntegrationClient,
        namespace="data_integration",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(workspaces=result)


if __name__ == "__main__":
    main()

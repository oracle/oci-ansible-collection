#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_service_mesh_virtual_service_route_table_actions
short_description: Perform actions on a VirtualServiceRouteTable resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a VirtualServiceRouteTable resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a VirtualServiceRouteTable resource from one compartment identifier to another. When provided, If-Match is checked
      against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    virtual_service_route_table_id:
        description:
            - Unique VirtualServiceRouteTable identifier.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    action:
        description:
            - The action to perform on the VirtualServiceRouteTable.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on virtual_service_route_table
  oci_service_mesh_virtual_service_route_table_actions:
    # required
    virtual_service_route_table_id: "ocid1.virtualserviceroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
virtual_service_route_table:
    description:
        - Details of the VirtualServiceRouteTable resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        virtual_service_id:
            description:
                - The OCID of the virtual service in which this virtual service route table is created.
            returned: on success
            type: str
            sample: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation.
                  Avoid entering confidential information.
                - "Example: `My unique resource name`"
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Description of the resource. It can be changed after creation.
                  Avoid entering confidential information.
                - "Example: `This is my new resource`"
            returned: on success
            type: str
            sample: description_example
        priority:
            description:
                - The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.
            returned: on success
            type: int
            sample: 56
        route_rules:
            description:
                - The route rules for the virtual service.
            returned: on success
            type: complex
            contains:
                path:
                    description:
                        - Route to match
                    returned: on success
                    type: str
                    sample: path_example
                path_type:
                    description:
                        - Match type for the route
                    returned: on success
                    type: str
                    sample: PREFIX
                is_grpc:
                    description:
                        - If true, the rule will check that the content-type header has a application/grpc
                          or one of the various application/grpc+ values.
                    returned: on success
                    type: bool
                    sample: true
                type:
                    description:
                        - Type of protocol.
                    returned: on success
                    type: str
                    sample: HTTP
                destinations:
                    description:
                        - The destination of the request.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of the traffic target.
                            returned: on success
                            type: str
                            sample: VIRTUAL_DEPLOYMENT
                        virtual_deployment_id:
                            description:
                                - The OCID of the virtual deployment where the request will be routed.
                            returned: on success
                            type: str
                            sample: "ocid1.virtualdeployment.oc1..xxxxxxEXAMPLExxxxxx"
                        port:
                            description:
                                - Port on virtual deployment to target.
                                  If port is missing, the rule will target all ports on the virtual deployment.
                            returned: on success
                            type: int
                            sample: 56
                        weight:
                            description:
                                - Weight of traffic target.
                            returned: on success
                            type: int
                            sample: 56
        time_created:
            description:
                - The time when this resource was created in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when this resource was updated in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed
                  state.
            returned: on success
            type: str
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
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "virtual_service_id": "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "priority": 56,
        "route_rules": [{
            "path": "path_example",
            "path_type": "PREFIX",
            "is_grpc": true,
            "type": "HTTP",
            "destinations": [{
                "type": "VIRTUAL_DEPLOYMENT",
                "virtual_deployment_id": "ocid1.virtualdeployment.oc1..xxxxxxEXAMPLExxxxxx",
                "port": 56,
                "weight": 56
            }]
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.service_mesh import ServiceMeshClient
    from oci.service_mesh.models import ChangeVirtualServiceRouteTableCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VirtualServiceRouteTableActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "virtual_service_route_table_id"

    def get_module_resource_id(self):
        return self.module.params.get("virtual_service_route_table_id")

    def get_get_fn(self):
        return self.client.get_virtual_service_route_table

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_virtual_service_route_table,
            virtual_service_route_table_id=self.module.params.get(
                "virtual_service_route_table_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVirtualServiceRouteTableCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_virtual_service_route_table_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_service_route_table_id=self.module.params.get(
                    "virtual_service_route_table_id"
                ),
                change_virtual_service_route_table_compartment_details=action_details,
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


VirtualServiceRouteTableActionsHelperCustom = get_custom_class(
    "VirtualServiceRouteTableActionsHelperCustom"
)


class ResourceHelper(
    VirtualServiceRouteTableActionsHelperCustom,
    VirtualServiceRouteTableActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            virtual_service_route_table_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="virtual_service_route_table",
        service_client_class=ServiceMeshClient,
        namespace="service_mesh",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

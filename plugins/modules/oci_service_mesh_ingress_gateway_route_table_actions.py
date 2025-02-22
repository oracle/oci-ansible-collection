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
module: oci_service_mesh_ingress_gateway_route_table_actions
short_description: Perform actions on an IngressGatewayRouteTable resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an IngressGatewayRouteTable resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a IngressGatewayRouteTable resource from one compartment identifier to another. When provided, If-Match is checked
      against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ingress_gateway_route_table_id:
        description:
            - Unique IngressGatewayRouteTable identifier.
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
            - The action to perform on the IngressGatewayRouteTable.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on ingress_gateway_route_table
  oci_service_mesh_ingress_gateway_route_table_actions:
    # required
    ingress_gateway_route_table_id: "ocid1.ingressgatewayroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
ingress_gateway_route_table:
    description:
        - Details of the IngressGatewayRouteTable resource acted upon by the current operation
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
        ingress_gateway_id:
            description:
                - The OCID of the ingress gateway.
            returned: on success
            type: str
            sample: "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A user-friendly name. The name must be unique within the same ingress gateway and cannot be changed after creation.
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
                - The priority of the route table. A lower value means a higher priority. The routes are declared based on the priority.
            returned: on success
            type: int
            sample: 56
        route_rules:
            description:
                - The route rules for the ingress gateway.
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
                is_host_rewrite_enabled:
                    description:
                        - If true, the hostname will be rewritten to the target virtual deployment's DNS hostname.
                    returned: on success
                    type: bool
                    sample: true
                is_path_rewrite_enabled:
                    description:
                        - If true, the matched path prefix will be rewritten to '/' before being directed to the target virtual deployment.
                    returned: on success
                    type: bool
                    sample: true
                request_timeout_in_ms:
                    description:
                        - The maximum duration in milliseconds for the upstream service to respond to a request.
                          If provided, the timeout value overrides the default timeout of 15 seconds for the HTTP based route rules, and disabled (no timeout)
                          when 'isGrpc' is true.
                          The value 0 (zero) indicates that the timeout is disabled.
                          For streaming responses from the upstream service, consider either keeping the timeout disabled or set a sufficiently high value.
                    returned: on success
                    type: int
                    sample: 56
                type:
                    description:
                        - Type of protocol.
                    returned: on success
                    type: str
                    sample: HTTP
                ingress_gateway_host:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the ingress gateway host that this route should apply to.
                            returned: on success
                            type: str
                            sample: name_example
                        port:
                            description:
                                - The port of the ingress gateway host listener. Leave empty to match all ports for the host.
                            returned: on success
                            type: int
                            sample: 56
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
                        virtual_service_id:
                            description:
                                - The OCID of the virtual service where the request will be routed.
                            returned: on success
                            type: str
                            sample: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
                        port:
                            description:
                                - The port on the virtual service to target.
                                  Mandatory if the virtual deployments are listening on multiple ports.
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
        "ingress_gateway_id": "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "priority": 56,
        "route_rules": [{
            "path": "path_example",
            "path_type": "PREFIX",
            "is_grpc": true,
            "is_host_rewrite_enabled": true,
            "is_path_rewrite_enabled": true,
            "request_timeout_in_ms": 56,
            "type": "HTTP",
            "ingress_gateway_host": {
                "name": "name_example",
                "port": 56
            },
            "destinations": [{
                "type": "VIRTUAL_DEPLOYMENT",
                "virtual_service_id": "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx",
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
    from oci.service_mesh.models import ChangeIngressGatewayRouteTableCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IngressGatewayRouteTableActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "ingress_gateway_route_table_id"

    def get_module_resource_id(self):
        return self.module.params.get("ingress_gateway_route_table_id")

    def get_get_fn(self):
        return self.client.get_ingress_gateway_route_table

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ingress_gateway_route_table,
            ingress_gateway_route_table_id=self.module.params.get(
                "ingress_gateway_route_table_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeIngressGatewayRouteTableCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_ingress_gateway_route_table_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingress_gateway_route_table_id=self.module.params.get(
                    "ingress_gateway_route_table_id"
                ),
                change_ingress_gateway_route_table_compartment_details=action_details,
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


IngressGatewayRouteTableActionsHelperCustom = get_custom_class(
    "IngressGatewayRouteTableActionsHelperCustom"
)


class ResourceHelper(
    IngressGatewayRouteTableActionsHelperCustom,
    IngressGatewayRouteTableActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            ingress_gateway_route_table_id=dict(
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
        resource_type="ingress_gateway_route_table",
        service_client_class=ServiceMeshClient,
        namespace="service_mesh",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

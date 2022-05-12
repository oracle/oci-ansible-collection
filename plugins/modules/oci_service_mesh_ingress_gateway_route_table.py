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
module: oci_service_mesh_ingress_gateway_route_table
short_description: Manage an IngressGatewayRouteTable resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an IngressGatewayRouteTable resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new IngressGatewayRouteTable.
    - "This resource has the following action operations in the M(oracle.oci.oci_service_mesh_ingress_gateway_route_table_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ingress_gateway_id:
        description:
            - The OCID of the service mesh in which this access policy is created.
            - Required for create using I(state=present).
        type: str
    name:
        description:
            - A user-friendly name. The name must be unique within the same ingress gateway and cannot be changed after creation.
              Avoid entering confidential information.
            - "Example: `My unique resource name`"
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - Description of the resource. It can be changed after creation.
              Avoid entering confidential information.
            - "Example: `This is my new resource`"
            - This parameter is updatable.
        type: str
    priority:
        description:
            - The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.
            - This parameter is updatable.
        type: int
    route_rules:
        description:
            - The route rules for the ingress gateway.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            path:
                description:
                    - Route to match
                    - Applicable when type is 'HTTP'
                type: str
            path_type:
                description:
                    - Match type for the route
                    - Applicable when type is 'HTTP'
                type: str
                choices:
                    - "PREFIX"
            is_grpc:
                description:
                    - If true, the rule will check that the content-type header has a application/grpc
                      or one of the various application/grpc+ values.
                    - Applicable when type is 'HTTP'
                type: bool
            is_host_rewrite_enabled:
                description:
                    - If true, the hostname will be rewritten to the target virtual deployment's DNS hostname.
                    - Applicable when type is 'HTTP'
                type: bool
            is_path_rewrite_enabled:
                description:
                    - If true, the matched path prefix will be rewritten to '/' before being directed to the target virtual deployment.
                    - Applicable when type is 'HTTP'
                type: bool
            type:
                description:
                    - Type of protocol.
                type: str
                choices:
                    - "HTTP"
                    - "TLS_PASSTHROUGH"
                    - "TCP"
                required: true
            ingress_gateway_host:
                description:
                    - ""
                type: dict
                suboptions:
                    name:
                        description:
                            - Name of the ingress gateway host that this route should apply to.
                            - Required when type is 'HTTP'
                        type: str
                        required: true
                    port:
                        description:
                            - The port of the ingress gateway host listener. Leave empty to match all ports for the host.
                            - Applicable when type is 'HTTP'
                        type: int
            destinations:
                description:
                    - The destination of the request.
                type: list
                elements: dict
                required: true
                suboptions:
                    type:
                        description:
                            - Type of the traffic target.
                            - Required when type is 'HTTP'
                        type: str
                        choices:
                            - "VIRTUAL_DEPLOYMENT"
                            - "VIRTUAL_SERVICE"
                        required: true
                    virtual_service_id:
                        description:
                            - The OCID of the virtual service where the request will be routed.
                            - Required when type is 'HTTP'
                        type: str
                        required: true
                    port:
                        description:
                            - The port on the virtual service to target.
                              Mandatory if the virtual deployments are listening on multiple ports.
                            - Applicable when type is 'HTTP'
                        type: int
                    weight:
                        description:
                            - Weight of traffic target.
                            - Applicable when type is 'HTTP'
                        type: int
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
    ingress_gateway_route_table_id:
        description:
            - Unique IngressGatewayRouteTable identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the IngressGatewayRouteTable.
            - Use I(state=present) to create or update an IngressGatewayRouteTable.
            - Use I(state=absent) to delete an IngressGatewayRouteTable.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create ingress_gateway_route_table
  oci_service_mesh_ingress_gateway_route_table:
    # required
    ingress_gateway_id: "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    route_rules:
    - # required
      type: HTTP
      destinations:
      - # required
        type: VIRTUAL_DEPLOYMENT
        virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        port: 56
        weight: 56

      # optional
      path: path_example
      path_type: PREFIX
      is_grpc: true
      is_host_rewrite_enabled: true
      is_path_rewrite_enabled: true
      ingress_gateway_host:
        # required
        name: name_example

        # optional
        port: 56

    # optional
    description: description_example
    priority: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update ingress_gateway_route_table
  oci_service_mesh_ingress_gateway_route_table:
    # required
    ingress_gateway_route_table_id: "ocid1.ingressgatewayroutetable.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    priority: 56
    route_rules:
    - # required
      type: HTTP
      destinations:
      - # required
        type: VIRTUAL_DEPLOYMENT
        virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        port: 56
        weight: 56

      # optional
      path: path_example
      path_type: PREFIX
      is_grpc: true
      is_host_rewrite_enabled: true
      is_path_rewrite_enabled: true
      ingress_gateway_host:
        # required
        name: name_example

        # optional
        port: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update ingress_gateway_route_table using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_service_mesh_ingress_gateway_route_table:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    priority: 56
    route_rules:
    - # required
      type: HTTP
      destinations:
      - # required
        type: VIRTUAL_DEPLOYMENT
        virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        port: 56
        weight: 56

      # optional
      path: path_example
      path_type: PREFIX
      is_grpc: true
      is_host_rewrite_enabled: true
      is_path_rewrite_enabled: true
      ingress_gateway_host:
        # required
        name: name_example

        # optional
        port: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete ingress_gateway_route_table
  oci_service_mesh_ingress_gateway_route_table:
    # required
    ingress_gateway_route_table_id: "ocid1.ingressgatewayroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete ingress_gateway_route_table using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_service_mesh_ingress_gateway_route_table:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
    from oci.service_mesh import ServiceMeshClient
    from oci.service_mesh.models import CreateIngressGatewayRouteTableDetails
    from oci.service_mesh.models import UpdateIngressGatewayRouteTableDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IngressGatewayRouteTableHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            IngressGatewayRouteTableHelperGen, self
        ).get_possible_entity_types() + [
            "ingressgatewayroutetable",
            "ingressgatewayroutetables",
            "serviceMeshingressgatewayroutetable",
            "serviceMeshingressgatewayroutetables",
            "ingressgatewayroutetableresource",
            "ingressgatewayroutetablesresource",
            "servicemesh",
        ]

    def get_module_resource_id_param(self):
        return "ingress_gateway_route_table_id"

    def get_module_resource_id(self):
        return self.module.params.get("ingress_gateway_route_table_id")

    def get_get_fn(self):
        return self.client.get_ingress_gateway_route_table

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_ingress_gateway_route_table,
            ingress_gateway_route_table_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ingress_gateway_route_table,
            ingress_gateway_route_table_id=self.module.params.get(
                "ingress_gateway_route_table_id"
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
        optional_list_method_params = ["name", "ingress_gateway_id"]

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
            self.client.list_ingress_gateway_route_tables, **kwargs
        )

    def get_create_model_class(self):
        return CreateIngressGatewayRouteTableDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_ingress_gateway_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_ingress_gateway_route_table_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateIngressGatewayRouteTableDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ingress_gateway_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingress_gateway_route_table_id=self.module.params.get(
                    "ingress_gateway_route_table_id"
                ),
                update_ingress_gateway_route_table_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_ingress_gateway_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ingress_gateway_route_table_id=self.module.params.get(
                    "ingress_gateway_route_table_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


IngressGatewayRouteTableHelperCustom = get_custom_class(
    "IngressGatewayRouteTableHelperCustom"
)


class ResourceHelper(
    IngressGatewayRouteTableHelperCustom, IngressGatewayRouteTableHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            ingress_gateway_id=dict(type="str"),
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            priority=dict(type="int"),
            route_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    path=dict(type="str"),
                    path_type=dict(type="str", choices=["PREFIX"]),
                    is_grpc=dict(type="bool"),
                    is_host_rewrite_enabled=dict(type="bool"),
                    is_path_rewrite_enabled=dict(type="bool"),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["HTTP", "TLS_PASSTHROUGH", "TCP"],
                    ),
                    ingress_gateway_host=dict(
                        type="dict",
                        options=dict(
                            name=dict(type="str", required=True), port=dict(type="int")
                        ),
                    ),
                    destinations=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=["VIRTUAL_DEPLOYMENT", "VIRTUAL_SERVICE"],
                            ),
                            virtual_service_id=dict(type="str", required=True),
                            port=dict(type="int"),
                            weight=dict(type="int"),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            ingress_gateway_route_table_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ingress_gateway_route_table",
        service_client_class=ServiceMeshClient,
        namespace="service_mesh",
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

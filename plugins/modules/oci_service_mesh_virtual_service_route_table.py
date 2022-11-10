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
module: oci_service_mesh_virtual_service_route_table
short_description: Manage a VirtualServiceRouteTable resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VirtualServiceRouteTable resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new VirtualServiceRouteTable.
    - "This resource has the following action operations in the M(oracle.oci.oci_service_mesh_virtual_service_route_table_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    virtual_service_id:
        description:
            - The OCID of the service mesh in which this access policy is created.
            - Required for create using I(state=present).
        type: str
    name:
        description:
            - A user-friendly name. The name must be unique within the same virtual service and cannot be changed after creation.
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
            - The route rules for the virtual service.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            type:
                description:
                    - Type of protocol.
                type: str
                choices:
                    - "TCP"
                    - "TLS_PASSTHROUGH"
                    - "HTTP"
                required: true
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
                            - Required when type is 'TCP'
                        type: str
                        choices:
                            - "VIRTUAL_DEPLOYMENT"
                            - "VIRTUAL_SERVICE"
                        required: true
                    virtual_deployment_id:
                        description:
                            - The OCID of the virtual deployment where the request will be routed.
                            - Required when type is 'TCP'
                        type: str
                        required: true
                    port:
                        description:
                            - Port on virtual deployment to target.
                              If port is missing, the rule will target all ports on the virtual deployment.
                            - Applicable when type is 'TCP'
                        type: int
                    weight:
                        description:
                            - Weight of traffic target.
                            - Required when type is 'TCP'
                        type: int
                        required: true
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
    virtual_service_route_table_id:
        description:
            - Unique VirtualServiceRouteTable identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the VirtualServiceRouteTable.
            - Use I(state=present) to create or update a VirtualServiceRouteTable.
            - Use I(state=absent) to delete a VirtualServiceRouteTable.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create virtual_service_route_table
  oci_service_mesh_virtual_service_route_table:
    # required
    virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    route_rules:
    - # required
      type: TCP
      destinations:
      - # required
        type: VIRTUAL_DEPLOYMENT
        virtual_deployment_id: "ocid1.virtualdeployment.oc1..xxxxxxEXAMPLExxxxxx"
        weight: 56

        # optional
        port: 56

    # optional
    description: description_example
    priority: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update virtual_service_route_table
  oci_service_mesh_virtual_service_route_table:
    # required
    virtual_service_route_table_id: "ocid1.virtualserviceroutetable.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    priority: 56
    route_rules:
    - # required
      type: TCP
      destinations:
      - # required
        type: VIRTUAL_DEPLOYMENT
        virtual_deployment_id: "ocid1.virtualdeployment.oc1..xxxxxxEXAMPLExxxxxx"
        weight: 56

        # optional
        port: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update virtual_service_route_table using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_service_mesh_virtual_service_route_table:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    priority: 56
    route_rules:
    - # required
      type: TCP
      destinations:
      - # required
        type: VIRTUAL_DEPLOYMENT
        virtual_deployment_id: "ocid1.virtualdeployment.oc1..xxxxxxEXAMPLExxxxxx"
        weight: 56

        # optional
        port: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete virtual_service_route_table
  oci_service_mesh_virtual_service_route_table:
    # required
    virtual_service_route_table_id: "ocid1.virtualserviceroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete virtual_service_route_table using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_service_mesh_virtual_service_route_table:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.service_mesh import ServiceMeshClient
    from oci.service_mesh.models import CreateVirtualServiceRouteTableDetails
    from oci.service_mesh.models import UpdateVirtualServiceRouteTableDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VirtualServiceRouteTableHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            VirtualServiceRouteTableHelperGen, self
        ).get_possible_entity_types() + [
            "virtualserviceroutetable",
            "virtualserviceroutetables",
            "serviceMeshvirtualserviceroutetable",
            "serviceMeshvirtualserviceroutetables",
            "virtualserviceroutetableresource",
            "virtualserviceroutetablesresource",
            "servicemesh",
        ]

    def get_module_resource_id_param(self):
        return "virtual_service_route_table_id"

    def get_module_resource_id(self):
        return self.module.params.get("virtual_service_route_table_id")

    def get_get_fn(self):
        return self.client.get_virtual_service_route_table

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_virtual_service_route_table,
            virtual_service_route_table_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_virtual_service_route_table,
            virtual_service_route_table_id=self.module.params.get(
                "virtual_service_route_table_id"
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
        optional_list_method_params = ["name", "virtual_service_id"]

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
            self.client.list_virtual_service_route_tables, **kwargs
        )

    def get_create_model_class(self):
        return CreateVirtualServiceRouteTableDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_virtual_service_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_virtual_service_route_table_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateVirtualServiceRouteTableDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_virtual_service_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_service_route_table_id=self.module.params.get(
                    "virtual_service_route_table_id"
                ),
                update_virtual_service_route_table_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_virtual_service_route_table,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_service_route_table_id=self.module.params.get(
                    "virtual_service_route_table_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


VirtualServiceRouteTableHelperCustom = get_custom_class(
    "VirtualServiceRouteTableHelperCustom"
)


class ResourceHelper(
    VirtualServiceRouteTableHelperCustom, VirtualServiceRouteTableHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            virtual_service_id=dict(type="str"),
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            priority=dict(type="int"),
            route_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(
                        type="str",
                        required=True,
                        choices=["TCP", "TLS_PASSTHROUGH", "HTTP"],
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
                            virtual_deployment_id=dict(type="str", required=True),
                            port=dict(type="int"),
                            weight=dict(type="int", required=True),
                        ),
                    ),
                    path=dict(type="str"),
                    path_type=dict(type="str", choices=["PREFIX"]),
                    is_grpc=dict(type="bool"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            virtual_service_route_table_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

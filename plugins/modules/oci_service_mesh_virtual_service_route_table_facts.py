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
module: oci_service_mesh_virtual_service_route_table_facts
short_description: Fetches details about one or multiple VirtualServiceRouteTable resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VirtualServiceRouteTable resources in Oracle Cloud Infrastructure
    - Returns a list of VirtualServiceRouteTable objects.
    - If I(virtual_service_route_table_id) is specified, the details of a single VirtualServiceRouteTable will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    virtual_service_route_table_id:
        description:
            - Unique VirtualServiceRouteTable identifier.
            - Required to get a specific virtual_service_route_table.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple virtual_service_route_tables.
        type: str
    name:
        description:
            - A filter to return only resources that match the entire name given.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for 'timeCreated' is descending. Default order for 'name' is ascending.
        type: str
        choices:
            - "id"
            - "timeCreated"
            - "name"
    virtual_service_id:
        description:
            - Unique VirtualService identifier.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the life cycle state given.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific virtual_service_route_table
  oci_service_mesh_virtual_service_route_table_facts:
    # required
    virtual_service_route_table_id: "ocid1.virtualserviceroutetable.oc1..xxxxxxEXAMPLExxxxxx"

- name: List virtual_service_route_tables
  oci_service_mesh_virtual_service_route_table_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    sort_by: id
    virtual_service_id: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: lifecycle_state_example

"""

RETURN = """
virtual_service_route_tables:
    description:
        - List of VirtualServiceRouteTable resources
    returned: on success
    type: complex
    contains:
        route_rules:
            description:
                - The route rules for the virtual service.
                - Returned for get operation
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
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        priority:
            description:
                - The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.
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
    sample: [{
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "virtual_service_id": "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "priority": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.service_mesh import ServiceMeshClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VirtualServiceRouteTableFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "virtual_service_route_table_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_virtual_service_route_table,
            virtual_service_route_table_id=self.module.params.get(
                "virtual_service_route_table_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "sort_by",
            "virtual_service_id",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_virtual_service_route_tables,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VirtualServiceRouteTableFactsHelperCustom = get_custom_class(
    "VirtualServiceRouteTableFactsHelperCustom"
)


class ResourceFactsHelper(
    VirtualServiceRouteTableFactsHelperCustom, VirtualServiceRouteTableFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            virtual_service_route_table_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["id", "timeCreated", "name"]),
            virtual_service_id=dict(type="str"),
            lifecycle_state=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="virtual_service_route_table",
        service_client_class=ServiceMeshClient,
        namespace="service_mesh",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(virtual_service_route_tables=result)


if __name__ == "__main__":
    main()

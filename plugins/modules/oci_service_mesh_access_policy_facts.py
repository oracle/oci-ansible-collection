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
module: oci_service_mesh_access_policy_facts
short_description: Fetches details about one or multiple AccessPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AccessPolicy resources in Oracle Cloud Infrastructure
    - Returns a list of AccessPolicy objects.
    - If I(access_policy_id) is specified, the details of a single AccessPolicy will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    access_policy_id:
        description:
            - Unique AccessPolicy identifier.
            - Required to get a specific access_policy.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple access_policies.
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
    mesh_id:
        description:
            - Unique Mesh identifier.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the life cycle state given.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific access_policy
  oci_service_mesh_access_policy_facts:
    # required
    access_policy_id: "ocid1.accesspolicy.oc1..xxxxxxEXAMPLExxxxxx"

- name: List access_policies
  oci_service_mesh_access_policy_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    sort_by: id
    mesh_id: "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING

"""

RETURN = """
access_policies:
    description:
        - List of AccessPolicy resources
    returned: on success
    type: complex
    contains:
        rules:
            description:
                - List of applicable rules.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                action:
                    description:
                        - Action for the traffic between the source and the destination.
                    returned: on success
                    type: str
                    sample: ALLOW
                source:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        hostnames:
                            description:
                                - "The hostnames of the external service. Only applicable for HTTP and HTTPS protocols.
                                  Wildcard hostnames are supported in the prefix form.
                                  Examples of valid hostnames are \\"www.example.com\\", \\"*.example.com\\", \\"*.com\\", \\"*\\".
                                  Hostname \\"*\\" can be used to allow all hosts."
                            returned: on success
                            type: list
                            sample: []
                        ip_addresses:
                            description:
                                - "The ipAddresses of the external service in CIDR notation. Only applicable for TCP protocol.
                                  All requests matching the given CIDR notation will pass through.
                                  In case a wildcard CIDR \\"0.0.0.0/0\\" is provided, the same port cannot be used for a virtual service communication."
                            returned: on success
                            type: list
                            sample: []
                        ports:
                            description:
                                - Ports exposed by an external service. If left empty all ports will be allowed.
                            returned: on success
                            type: list
                            sample: []
                        protocol:
                            description:
                                - Protocol of the external service
                            returned: on success
                            type: str
                            sample: HTTP
                        ingress_gateway_id:
                            description:
                                - The OCID of the ingress gateway resource.
                            returned: on success
                            type: str
                            sample: "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx"
                        type:
                            description:
                                - Traffic type of the target.
                            returned: on success
                            type: str
                            sample: ALL_VIRTUAL_SERVICES
                        virtual_service_id:
                            description:
                                - The OCID of the virtual service resource.
                            returned: on success
                            type: str
                            sample: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
                destination:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        hostnames:
                            description:
                                - "The hostnames of the external service. Only applicable for HTTP and HTTPS protocols.
                                  Wildcard hostnames are supported in the prefix form.
                                  Examples of valid hostnames are \\"www.example.com\\", \\"*.example.com\\", \\"*.com\\", \\"*\\".
                                  Hostname \\"*\\" can be used to allow all hosts."
                            returned: on success
                            type: list
                            sample: []
                        ip_addresses:
                            description:
                                - "The ipAddresses of the external service in CIDR notation. Only applicable for TCP protocol.
                                  All requests matching the given CIDR notation will pass through.
                                  In case a wildcard CIDR \\"0.0.0.0/0\\" is provided, the same port cannot be used for a virtual service communication."
                            returned: on success
                            type: list
                            sample: []
                        ports:
                            description:
                                - Ports exposed by an external service. If left empty all ports will be allowed.
                            returned: on success
                            type: list
                            sample: []
                        protocol:
                            description:
                                - Protocol of the external service
                            returned: on success
                            type: str
                            sample: HTTP
                        ingress_gateway_id:
                            description:
                                - The OCID of the ingress gateway resource.
                            returned: on success
                            type: str
                            sample: "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx"
                        type:
                            description:
                                - Traffic type of the target.
                            returned: on success
                            type: str
                            sample: ALL_VIRTUAL_SERVICES
                        virtual_service_id:
                            description:
                                - The OCID of the virtual service resource.
                            returned: on success
                            type: str
                            sample: "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
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
        mesh_id:
            description:
                - The OCID of the service mesh in which this access policy is created.
            returned: on success
            type: str
            sample: "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx"
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
        "rules": [{
            "action": "ALLOW",
            "source": {
                "hostnames": [],
                "ip_addresses": [],
                "ports": [],
                "protocol": "HTTP",
                "ingress_gateway_id": "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx",
                "type": "ALL_VIRTUAL_SERVICES",
                "virtual_service_id": "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "destination": {
                "hostnames": [],
                "ip_addresses": [],
                "ports": [],
                "protocol": "HTTP",
                "ingress_gateway_id": "ocid1.ingressgateway.oc1..xxxxxxEXAMPLExxxxxx",
                "type": "ALL_VIRTUAL_SERVICES",
                "virtual_service_id": "ocid1.virtualservice.oc1..xxxxxxEXAMPLExxxxxx"
            }
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "mesh_id": "ocid1.mesh.oc1..xxxxxxEXAMPLExxxxxx",
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


class AccessPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "access_policy_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_policy,
            access_policy_id=self.module.params.get("access_policy_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "sort_by",
            "mesh_id",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_access_policies,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AccessPolicyFactsHelperCustom = get_custom_class("AccessPolicyFactsHelperCustom")


class ResourceFactsHelper(AccessPolicyFactsHelperCustom, AccessPolicyFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            access_policy_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["id", "timeCreated", "name"]),
            mesh_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="access_policy",
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

    module.exit_json(access_policies=result)


if __name__ == "__main__":
    main()

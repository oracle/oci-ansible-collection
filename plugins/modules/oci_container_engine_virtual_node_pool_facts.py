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
module: oci_container_engine_virtual_node_pool_facts
short_description: Fetches details about one or multiple VirtualNodePool resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VirtualNodePool resources in Oracle Cloud Infrastructure
    - List all the virtual node pools in a compartment, and optionally filter by cluster.
    - If I(virtual_node_pool_id) is specified, the details of a single VirtualNodePool will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    virtual_node_pool_id:
        description:
            - The OCID of the virtual node pool.
            - Required to get a specific virtual_node_pool.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple virtual_node_pools.
        type: str
    cluster_id:
        description:
            - The OCID of the cluster.
        type: str
    name:
        description:
            - The name to filter on.
        type: str
    sort_order:
        description:
            - The optional order in which to sort the results.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The optional field to sort the results by.
        type: str
        choices:
            - "ID"
            - "NAME"
            - "TIME_CREATED"
    lifecycle_state:
        description:
            - A virtual node pool lifecycle state to filter on. Can have multiple parameters of this name.
        type: list
        elements: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "NEEDS_ATTENTION"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific virtual_node_pool
  oci_container_engine_virtual_node_pool_facts:
    # required
    virtual_node_pool_id: "ocid1.virtualnodepool.oc1..xxxxxxEXAMPLExxxxxx"

- name: List virtual_node_pools
  oci_container_engine_virtual_node_pool_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    sort_order: ASC
    sort_by: ID
    lifecycle_state: [ "CREATING" ]

"""

RETURN = """
virtual_node_pools:
    description:
        - List of VirtualNodePool resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the virtual node pool.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment of the virtual node pool.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        cluster_id:
            description:
                - The cluster the virtual node pool is associated with. A virtual node pool can only be associated with one cluster.
            returned: on success
            type: str
            sample: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Display name of the virtual node pool. This is a non-unique value.
            returned: on success
            type: str
            sample: display_name_example
        kubernetes_version:
            description:
                - The version of Kubernetes running on the nodes in the node pool.
            returned: on success
            type: str
            sample: kubernetes_version_example
        initial_virtual_node_labels:
            description:
                - Initial labels that will be added to the Kubernetes Virtual Node object when it registers. This is the same as virtualNodePool resources.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - The key of the pair.
                    returned: on success
                    type: str
                    sample: key_example
                value:
                    description:
                        - The value of the pair.
                    returned: on success
                    type: str
                    sample: value_example
        taints:
            description:
                - A taint is a collection of <key, value, effect>. These taints will be applied to the Virtual Nodes of this Virtual Node Pool for Kubernetes
                  scheduling.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - The key of the pair.
                    returned: on success
                    type: str
                    sample: key_example
                value:
                    description:
                        - The value of the pair.
                    returned: on success
                    type: str
                    sample: value_example
                effect:
                    description:
                        - The effect of the pair.
                    returned: on success
                    type: str
                    sample: effect_example
        size:
            description:
                - The number of Virtual Nodes that should be in the Virtual Node Pool. The placement configurations determine where these virtual nodes are
                  placed.
            returned: on success
            type: int
            sample: 56
        placement_configurations:
            description:
                - The list of placement configurations which determines where Virtual Nodes will be provisioned across as it relates to the subnet and
                  availability domains. The size attribute determines how many we evenly spread across these placement configurations
            returned: on success
            type: complex
            contains:
                availability_domain:
                    description:
                        - "The availability domain in which to place virtual nodes.
                          Example: `Uocm:PHX-AD-1`"
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                fault_domain:
                    description:
                        - The fault domain of this virtual node.
                    returned: on success
                    type: list
                    sample: []
                subnet_id:
                    description:
                        - The OCID of the subnet in which to place virtual nodes.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids:
            description:
                - List of network security group id's applied to the Virtual Node VNIC.
            returned: on success
            type: list
            sample: []
        pod_configuration:
            description:
                - The pod configuration for pods run on virtual nodes of this virtual node pool.
            returned: on success
            type: complex
            contains:
                subnet_id:
                    description:
                        - The regional subnet where pods' VNIC will be placed.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                nsg_ids:
                    description:
                        - List of network security group IDs applied to the Pod VNIC.
                    returned: on success
                    type: list
                    sample: []
                shape:
                    description:
                        - Shape of the pods.
                    returned: on success
                    type: str
                    sample: shape_example
        lifecycle_state:
            description:
                - The state of the Virtual Node Pool.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the state of the Virtual Node Pool.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time the virtual node pool was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the virtual node pool was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
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
        virtual_node_tags:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                freeform_tags:
                    description:
                        - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                          For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                          Example: `{\\"Department\\": \\"Finance\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                          For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                          Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "cluster_id": "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "kubernetes_version": "kubernetes_version_example",
        "initial_virtual_node_labels": [{
            "key": "key_example",
            "value": "value_example"
        }],
        "taints": [{
            "key": "key_example",
            "value": "value_example",
            "effect": "effect_example"
        }],
        "size": 56,
        "placement_configurations": [{
            "availability_domain": "Uocm:PHX-AD-1",
            "fault_domain": [],
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "nsg_ids": [],
        "pod_configuration": {
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "nsg_ids": [],
            "shape": "shape_example"
        },
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "virtual_node_tags": {
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.container_engine import ContainerEngineClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VirtualNodePoolFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "virtual_node_pool_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_virtual_node_pool,
            virtual_node_pool_id=self.module.params.get("virtual_node_pool_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "cluster_id",
            "name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_virtual_node_pools,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VirtualNodePoolFactsHelperCustom = get_custom_class("VirtualNodePoolFactsHelperCustom")


class ResourceFactsHelper(
    VirtualNodePoolFactsHelperCustom, VirtualNodePoolFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            virtual_node_pool_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            cluster_id=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["ID", "NAME", "TIME_CREATED"]),
            lifecycle_state=dict(
                type="list",
                elements="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "NEEDS_ATTENTION",
                ],
            ),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="virtual_node_pool",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(virtual_node_pools=result)


if __name__ == "__main__":
    main()

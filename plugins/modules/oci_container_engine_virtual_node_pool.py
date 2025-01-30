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
module: oci_container_engine_virtual_node_pool
short_description: Manage a VirtualNodePool resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VirtualNodePool resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new virtual node pool.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment of the virtual node pool.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    cluster_id:
        description:
            - The cluster the virtual node pool is associated with. A virtual node pool can only be associated with one cluster.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - Display name of the virtual node pool. This is a non-unique value.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    initial_virtual_node_labels:
        description:
            - Initial labels that will be added to the Kubernetes Virtual Node object when it registers.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            key:
                description:
                    - The key of the pair.
                type: str
            value:
                description:
                    - The value of the pair.
                type: str
    taints:
        description:
            - A taint is a collection of <key, value, effect>. These taints will be applied to the Virtual Nodes of this Virtual Node Pool for Kubernetes
              scheduling.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            key:
                description:
                    - The key of the pair.
                type: str
            value:
                description:
                    - The value of the pair.
                type: str
            effect:
                description:
                    - The effect of the pair.
                type: str
    size:
        description:
            - The number of Virtual Nodes that should be in the Virtual Node Pool. The placement configurations determine where these virtual nodes are placed.
            - This parameter is updatable.
        type: int
    placement_configurations:
        description:
            - The list of placement configurations which determines where Virtual Nodes will be provisioned across as it relates to the subnet and availability
              domains. The size attribute determines how many we evenly spread across these placement configurations
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            availability_domain:
                description:
                    - "The availability domain in which to place virtual nodes.
                      Example: `Uocm:PHX-AD-1`"
                type: str
            fault_domain:
                description:
                    - The fault domain of this virtual node.
                type: list
                elements: str
            subnet_id:
                description:
                    - The OCID of the subnet in which to place virtual nodes.
                type: str
    nsg_ids:
        description:
            - List of network security group id's applied to the Virtual Node VNIC.
            - This parameter is updatable.
        type: list
        elements: str
    pod_configuration:
        description:
            - The pod configuration for pods run on virtual nodes of this virtual node pool.
            - This parameter is updatable.
        type: dict
        suboptions:
            subnet_id:
                description:
                    - The regional subnet where pods' VNIC will be placed.
                type: str
                required: true
            nsg_ids:
                description:
                    - List of network security group IDs applied to the Pod VNIC.
                type: list
                elements: str
            shape:
                description:
                    - Shape of the pods.
                type: str
                required: true
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    virtual_node_tags:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            freeform_tags:
                description:
                    - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                      Example: `{\\"Department\\": \\"Finance\\"}`"
                type: dict
            defined_tags:
                description:
                    - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                      Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                type: dict
    virtual_node_pool_id:
        description:
            - The OCID of the virtual node pool.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    override_eviction_grace_duration_vnp:
        description:
            - "Duration after which Sk8s will give up eviction of the pods on the node.
              PT0M will indicate you want to delete the virtual node without cordon and drain. Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M"
        type: str
    is_force_deletion_after_override_grace_duration_vnp:
        description:
            - If the underlying compute instance should be deleted if you cannot evict all the pods in grace period
        type: bool
    state:
        description:
            - The state of the VirtualNodePool.
            - Use I(state=present) to create or update a VirtualNodePool.
            - Use I(state=absent) to delete a VirtualNodePool.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create virtual_node_pool
  oci_container_engine_virtual_node_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    placement_configurations:
    - # optional
      availability_domain: Uocm:PHX-AD-1
      fault_domain: [ "fault_domain_example" ]
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    initial_virtual_node_labels:
    - # optional
      key: key_example
      value: value_example
    taints:
    - # optional
      key: key_example
      value: value_example
      effect: effect_example
    size: 56
    nsg_ids: [ "nsg_ids_example" ]
    pod_configuration:
      # required
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      shape: shape_example

      # optional
      nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    virtual_node_tags:
      # optional
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update virtual_node_pool
  oci_container_engine_virtual_node_pool:
    # required
    virtual_node_pool_id: "ocid1.virtualnodepool.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    initial_virtual_node_labels:
    - # optional
      key: key_example
      value: value_example
    taints:
    - # optional
      key: key_example
      value: value_example
      effect: effect_example
    size: 56
    placement_configurations:
    - # optional
      availability_domain: Uocm:PHX-AD-1
      fault_domain: [ "fault_domain_example" ]
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    pod_configuration:
      # required
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      shape: shape_example

      # optional
      nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    virtual_node_tags:
      # optional
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update virtual_node_pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_engine_virtual_node_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    initial_virtual_node_labels:
    - # optional
      key: key_example
      value: value_example
    taints:
    - # optional
      key: key_example
      value: value_example
      effect: effect_example
    size: 56
    placement_configurations:
    - # optional
      availability_domain: Uocm:PHX-AD-1
      fault_domain: [ "fault_domain_example" ]
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    pod_configuration:
      # required
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      shape: shape_example

      # optional
      nsg_ids: [ "nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    virtual_node_tags:
      # optional
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete virtual_node_pool
  oci_container_engine_virtual_node_pool:
    # required
    virtual_node_pool_id: "ocid1.virtualnodepool.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    override_eviction_grace_duration_vnp: override_eviction_grace_duration_vnp_example
    is_force_deletion_after_override_grace_duration_vnp: true

- name: Delete virtual_node_pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_engine_virtual_node_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
virtual_node_pool:
    description:
        - Details of the VirtualNodePool resource acted upon by the current operation
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
    sample: {
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
    from oci.container_engine import ContainerEngineClient
    from oci.container_engine.models import CreateVirtualNodePoolDetails
    from oci.container_engine.models import UpdateVirtualNodePoolDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VirtualNodePoolHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(VirtualNodePoolHelperGen, self).get_possible_entity_types() + [
            "virtualnodepool",
            "virtualnodepools",
            "containerEnginevirtualnodepool",
            "containerEnginevirtualnodepools",
            "virtualnodepoolresource",
            "virtualnodepoolsresource",
            "containerengine",
        ]

    def get_module_resource_id_param(self):
        return "virtual_node_pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("virtual_node_pool_id")

    def get_get_fn(self):
        return self.client.get_virtual_node_pool

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_virtual_node_pool, virtual_node_pool_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_virtual_node_pool,
            virtual_node_pool_id=self.module.params.get("virtual_node_pool_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["cluster_id"]

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
            self.client.list_virtual_node_pools, **kwargs
        )

    def get_create_model_class(self):
        return CreateVirtualNodePoolDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_virtual_node_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(create_virtual_node_pool_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateVirtualNodePoolDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_virtual_node_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_node_pool_id=self.module.params.get("virtual_node_pool_id"),
                update_virtual_node_pool_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_virtual_node_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_node_pool_id=self.module.params.get("virtual_node_pool_id"),
                override_eviction_grace_duration_vnp=self.module.params.get(
                    "override_eviction_grace_duration_vnp"
                ),
                is_force_deletion_after_override_grace_duration_vnp=self.module.params.get(
                    "is_force_deletion_after_override_grace_duration_vnp"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


VirtualNodePoolHelperCustom = get_custom_class("VirtualNodePoolHelperCustom")


class ResourceHelper(VirtualNodePoolHelperCustom, VirtualNodePoolHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            cluster_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            initial_virtual_node_labels=dict(
                type="list",
                elements="dict",
                options=dict(key=dict(type="str", no_log=True), value=dict(type="str")),
            ),
            taints=dict(
                type="list",
                elements="dict",
                options=dict(
                    key=dict(type="str", no_log=True),
                    value=dict(type="str"),
                    effect=dict(type="str"),
                ),
            ),
            size=dict(type="int"),
            placement_configurations=dict(
                type="list",
                elements="dict",
                options=dict(
                    availability_domain=dict(type="str"),
                    fault_domain=dict(type="list", elements="str"),
                    subnet_id=dict(type="str"),
                ),
            ),
            nsg_ids=dict(type="list", elements="str"),
            pod_configuration=dict(
                type="dict",
                options=dict(
                    subnet_id=dict(type="str", required=True),
                    nsg_ids=dict(type="list", elements="str"),
                    shape=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            virtual_node_tags=dict(
                type="dict",
                options=dict(
                    freeform_tags=dict(type="dict"), defined_tags=dict(type="dict")
                ),
            ),
            virtual_node_pool_id=dict(aliases=["id"], type="str"),
            override_eviction_grace_duration_vnp=dict(type="str"),
            is_force_deletion_after_override_grace_duration_vnp=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="virtual_node_pool",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
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

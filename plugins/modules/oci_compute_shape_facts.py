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
module: oci_compute_shape_facts
short_description: Fetches details about one or multiple Shape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Shape resources in Oracle Cloud Infrastructure
    - Lists the shapes that can be used to launch an instance within the specified compartment. You can
      filter the list by compatibility with a specific image.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
    image_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of an image.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List shapes
  oci_compute_shape_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    availability_domain: Uocm:PHX-AD-1
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
shapes:
    description:
        - List of Shape resources
    returned: on success
    type: complex
    contains:
        baseline_ocpu_utilizations:
            description:
                - For a subcore burstable VM, the supported baseline OCPU utilization for instances that use this shape.
            returned: on success
            type: list
            sample: []
        min_total_baseline_ocpus_required:
            description:
                - For a subcore burstable VM, the minimum total baseline OCPUs required. The total baseline OCPUs is equal to
                  baselineOcpuUtilization chosen multiplied by the number of OCPUs chosen.
            returned: on success
            type: float
            sample: 10
        shape:
            description:
                - The name of the shape. You can enumerate all available shapes by calling
                  L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Shape/ListShapes).
            returned: on success
            type: str
            sample: shape_example
        processor_description:
            description:
                - A short description of the shape's processor (CPU).
            returned: on success
            type: str
            sample: processor_description_example
        ocpus:
            description:
                - The default number of OCPUs available for this shape.
            returned: on success
            type: float
            sample: 3.4
        memory_in_gbs:
            description:
                - The default amount of memory available for this shape, in gigabytes.
            returned: on success
            type: float
            sample: 3.4
        network_ports:
            description:
                - The number of physical network interface card (NIC) ports available for this shape.
            returned: on success
            type: int
            sample: 56
        networking_bandwidth_in_gbps:
            description:
                - The networking bandwidth available for this shape, in gigabits per second.
            returned: on success
            type: float
            sample: 3.4
        max_vnic_attachments:
            description:
                - The maximum number of VNIC attachments available for this shape.
            returned: on success
            type: int
            sample: 56
        gpus:
            description:
                - The number of GPUs available for this shape.
            returned: on success
            type: int
            sample: 56
        gpu_description:
            description:
                - A short description of the graphics processing unit (GPU) available for this shape.
                - If the shape does not have any GPUs, this field is `null`.
            returned: on success
            type: str
            sample: gpu_description_example
        local_disks:
            description:
                - The number of local disks available for this shape.
            returned: on success
            type: int
            sample: 56
        local_disks_total_size_in_gbs:
            description:
                - The aggregate size of the local disks available for this shape, in gigabytes.
                - If the shape does not have any local disks, this field is `null`.
            returned: on success
            type: float
            sample: 3.4
        local_disk_description:
            description:
                - A short description of the local disks available for this shape.
                - If the shape does not have any local disks, this field is `null`.
            returned: on success
            type: str
            sample: local_disk_description_example
        rdma_ports:
            description:
                - The number of networking ports available for the remote direct memory access (RDMA) network between nodes in
                  a high performance computing (HPC) cluster network. If the shape does not support cluster networks, this
                  value is `0`.
            returned: on success
            type: int
            sample: 56
        rdma_bandwidth_in_gbps:
            description:
                - The networking bandwidth available for the remote direct memory access (RDMA) network for this shape, in
                  gigabits per second.
            returned: on success
            type: int
            sample: 56
        is_live_migration_supported:
            description:
                - Whether live migration is supported for this shape.
            returned: on success
            type: bool
            sample: true
        ocpu_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                min:
                    description:
                        - The minimum number of OCPUs.
                    returned: on success
                    type: float
                    sample: 3.4
                max:
                    description:
                        - The maximum number of OCPUs.
                    returned: on success
                    type: float
                    sample: 3.4
        memory_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                min_in_g_bs:
                    description:
                        - The minimum amount of memory, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
                max_in_g_bs:
                    description:
                        - The maximum amount of memory, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
                default_per_ocpu_in_g_bs:
                    description:
                        - The default amount of memory per OCPU available for this shape, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
                min_per_ocpu_in_gbs:
                    description:
                        - The minimum amount of memory per OCPU available for this shape, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
                max_per_ocpu_in_gbs:
                    description:
                        - The maximum amount of memory per OCPU available for this shape, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
        networking_bandwidth_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                min_in_gbps:
                    description:
                        - The minimum amount of networking bandwidth, in gigabits per second.
                    returned: on success
                    type: float
                    sample: 3.4
                max_in_gbps:
                    description:
                        - The maximum amount of networking bandwidth, in gigabits per second.
                    returned: on success
                    type: float
                    sample: 3.4
                default_per_ocpu_in_gbps:
                    description:
                        - The default amount of networking bandwidth per OCPU, in gigabits per second.
                    returned: on success
                    type: float
                    sample: 3.4
        max_vnic_attachment_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                min:
                    description:
                        - The lowest maximum value of VNIC attachments.
                    returned: on success
                    type: int
                    sample: 56
                max:
                    description:
                        - The highest maximum value of VNIC attachments.
                    returned: on success
                    type: float
                    sample: 3.4
                default_per_ocpu:
                    description:
                        - The default number of VNIC attachments allowed per OCPU.
                    returned: on success
                    type: float
                    sample: 3.4
        platform_config_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The type of platform being configured.
                    returned: on success
                    type: str
                    sample: AMD_MILAN_BM
                secure_boot_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        allowed_values:
                            description:
                                - Boolean values that indicate whether Secure Boot can be enabled or disabled.
                            returned: on success
                            type: list
                            sample: []
                        is_default_enabled:
                            description:
                                - Whether Secure Boot is enabled by default.
                            returned: on success
                            type: bool
                            sample: true
                measured_boot_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        allowed_values:
                            description:
                                - Boolean values that indicate whether the Measured Boot feature can be enabled or disabled.
                            returned: on success
                            type: list
                            sample: []
                        is_default_enabled:
                            description:
                                - Whether the Measured Boot feature is enabled by default.
                            returned: on success
                            type: bool
                            sample: true
                trusted_platform_module_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        allowed_values:
                            description:
                                - Boolean values that indicate whether the Trusted Platform Module can be enabled or disabled.
                            returned: on success
                            type: list
                            sample: []
                        is_default_enabled:
                            description:
                                - Whether the Trusted Platform Module is enabled by default.
                            returned: on success
                            type: bool
                            sample: true
                numa_nodes_per_socket_platform_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        service_allowed_values:
                            description:
                                - The supported values for this platform configuration property.
                            returned: on success
                            type: list
                            sample: []
                        default_value:
                            description:
                                - The default NUMA nodes per socket configuration.
                            returned: on success
                            type: str
                            sample: default_value_example
        is_billed_for_stopped_instance:
            description:
                - Whether billing continues when the instances that use this shape are in the stopped state.
            returned: on success
            type: bool
            sample: true
        billing_type:
            description:
                - How instances that use this shape are charged.
            returned: on success
            type: str
            sample: ALWAYS_FREE
        quota_names:
            description:
                - The list of of compartment quotas for the shape.
            returned: on success
            type: list
            sample: []
        is_subcore:
            description:
                - Whether the shape supports creating subcore or burstable instances. A L(burstable
                  instance,https://docs.cloud.oracle.com/iaas/Content/Compute/References/burstable-instances.htm)
                  is a virtual machine (VM) instance that provides a baseline level of CPU performance with the ability to burst to a higher level to support
                  occasional
                  spikes in usage.
            returned: on success
            type: bool
            sample: true
        is_flexible:
            description:
                - Whether the shape supports creating flexible instances. A L(flexible
                  shape,https://docs.cloud.oracle.com/iaas/Content/Compute/References/computeshapes.htm#flexible)
                  is a shape that lets you customize the number of OCPUs and the amount of memory when launching or resizing your instance.
            returned: on success
            type: bool
            sample: true
        resize_compatible_shapes:
            description:
                - The list of compatible shapes that this shape can be changed to. For more information,
                  see L(Changing the Shape of an Instance,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm).
            returned: on success
            type: list
            sample: []
        recommended_alternatives:
            description:
                - The list of shapes and shape details (if applicable) that Oracle recommends that you use as an alternative to the current shape.
            returned: on success
            type: complex
            contains:
                shape_name:
                    description:
                        - The name of the shape.
                    returned: on success
                    type: str
                    sample: shape_name_example
    sample: [{
        "baseline_ocpu_utilizations": [],
        "min_total_baseline_ocpus_required": 10,
        "shape": "shape_example",
        "processor_description": "processor_description_example",
        "ocpus": 3.4,
        "memory_in_gbs": 3.4,
        "network_ports": 56,
        "networking_bandwidth_in_gbps": 3.4,
        "max_vnic_attachments": 56,
        "gpus": 56,
        "gpu_description": "gpu_description_example",
        "local_disks": 56,
        "local_disks_total_size_in_gbs": 3.4,
        "local_disk_description": "local_disk_description_example",
        "rdma_ports": 56,
        "rdma_bandwidth_in_gbps": 56,
        "is_live_migration_supported": true,
        "ocpu_options": {
            "min": 3.4,
            "max": 3.4
        },
        "memory_options": {
            "min_in_g_bs": 3.4,
            "max_in_g_bs": 3.4,
            "default_per_ocpu_in_g_bs": 3.4,
            "min_per_ocpu_in_gbs": 3.4,
            "max_per_ocpu_in_gbs": 3.4
        },
        "networking_bandwidth_options": {
            "min_in_gbps": 3.4,
            "max_in_gbps": 3.4,
            "default_per_ocpu_in_gbps": 3.4
        },
        "max_vnic_attachment_options": {
            "min": 56,
            "max": 3.4,
            "default_per_ocpu": 3.4
        },
        "platform_config_options": {
            "type": "AMD_MILAN_BM",
            "secure_boot_options": {
                "allowed_values": [],
                "is_default_enabled": true
            },
            "measured_boot_options": {
                "allowed_values": [],
                "is_default_enabled": true
            },
            "trusted_platform_module_options": {
                "allowed_values": [],
                "is_default_enabled": true
            },
            "numa_nodes_per_socket_platform_options": {
                "service_allowed_values": [],
                "default_value": "default_value_example"
            }
        },
        "is_billed_for_stopped_instance": true,
        "billing_type": "ALWAYS_FREE",
        "quota_names": [],
        "is_subcore": true,
        "is_flexible": true,
        "resize_compatible_shapes": [],
        "recommended_alternatives": [{
            "shape_name": "shape_name_example"
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "image_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_shapes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ShapeFactsHelperCustom = get_custom_class("ShapeFactsHelperCustom")


class ResourceFactsHelper(ShapeFactsHelperCustom, ShapeFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type="str"),
            image_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="shape",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(shapes=result)


if __name__ == "__main__":
    main()

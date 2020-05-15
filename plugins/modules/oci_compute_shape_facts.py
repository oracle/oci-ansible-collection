#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
version_added: "2.5"
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
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
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List shapes
  oci_compute_shape_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
shapes:
    description:
        - List of Shape resources
    returned: on success
    type: complex
    contains:
        shape:
            description:
                - The name of the shape. You can enumerate all available shapes by calling
                  L(ListShapes,https://docs.cloud.oracle.com/#/en/iaas/20160918/Shape/ListShapes).
            returned: on success
            type: string
            sample: shape_example
        processor_description:
            description:
                - A short description of the processors available to an instance of this shape.
            returned: on success
            type: string
            sample: processor_description_example
        ocpus:
            description:
                - The default number of OCPUs available to an instance of this shape.
            returned: on success
            type: float
            sample: 3.4
        memory_in_gbs:
            description:
                - The default amount of memory, in gigabytes, available to an instance of this shape.
            returned: on success
            type: float
            sample: 3.4
        networking_bandwidth_in_gbps:
            description:
                - The networking bandwidth, in gigabits per second, available to an instance of this shape.
            returned: on success
            type: float
            sample: 3.4
        max_vnic_attachments:
            description:
                - The maximum number of VNIC attachments available to an instance of this shape.
            returned: on success
            type: int
            sample: 56
        gpus:
            description:
                - The number of GPUs available to an instance of this shape.
            returned: on success
            type: int
            sample: 56
        gpu_description:
            description:
                - A short description of the GPUs available to instances of this shape.
                  This field is `null` if `gpus` is `0`.
            returned: on success
            type: string
            sample: gpu_description_example
        local_disks:
            description:
                - The number of local disks available to the instance.
            returned: on success
            type: int
            sample: 56
        local_disks_total_size_in_gbs:
            description:
                - The size of the local disks, aggregated, in gigabytes.
                  This field is `null` if `localDisks` is equal to `0`.
            returned: on success
            type: float
            sample: 3.4
        local_disk_description:
            description:
                - A short description of the local disks available to instances of this shape.
                  This field is `null` if `localDisks` is equal to `0`.
            returned: on success
            type: string
            sample: local_disk_description_example
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
                        - The default amount of memory, in gigabytes, per OCPU available to an instance
                          of this shape.
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
                        - The default amount of networking bandwidth, in gigabits per second,
                          per OCPU.
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
    sample: [{
        "shape": "shape_example",
        "processor_description": "processor_description_example",
        "ocpus": 3.4,
        "memory_in_gbs": 3.4,
        "networking_bandwidth_in_gbps": 3.4,
        "max_vnic_attachments": 56,
        "gpus": 56,
        "gpu_description": "gpu_description_example",
        "local_disks": 56,
        "local_disks_total_size_in_gbs": 3.4,
        "local_disk_description": "local_disk_description_example",
        "ocpu_options": {
            "min": 3.4,
            "max": 3.4
        },
        "memory_options": {
            "min_in_g_bs": 3.4,
            "max_in_g_bs": 3.4,
            "default_per_ocpu_in_g_bs": 3.4
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
        }
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

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(shapes=result)


if __name__ == "__main__":
    main()

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
module: oci_container_engine_pod_shape_facts
short_description: Fetches details about one or multiple PodShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PodShape resources in Oracle Cloud Infrastructure
    - List all the Pod Shapes in a compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
        required: true
    availability_domain:
        description:
            - The availability domain of the pod shape.
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List pod_shapes
  oci_container_engine_pod_shape_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    availability_domain: Uocm:PHX-AD-1
    name: name_example
    sort_order: ASC
    sort_by: ID

"""

RETURN = """
pod_shapes:
    description:
        - List of PodShape resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the identifying shape.
            returned: on success
            type: str
            sample: name_example
        processor_description:
            description:
                - A short description of the VM's processor (CPU).
            returned: on success
            type: str
            sample: processor_description_example
        ocpu_options:
            description:
                - Options for OCPU shape.
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
                - ShapeMemoryOptions.
            returned: on success
            type: complex
            contains:
                min_in_gbs:
                    description:
                        - The minimum amount of memory, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
                max_in_gbs:
                    description:
                        - The maximum amount of memory, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
                default_per_ocpu_in_gbs:
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
        network_bandwidth_options:
            description:
                - ShapeNetworkBandwidthOptions.
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
    sample: [{
        "name": "name_example",
        "processor_description": "processor_description_example",
        "ocpu_options": [{
            "min": 3.4,
            "max": 3.4
        }],
        "memory_options": [{
            "min_in_gbs": 3.4,
            "max_in_gbs": 3.4,
            "default_per_ocpu_in_gbs": 3.4,
            "min_per_ocpu_in_gbs": 3.4,
            "max_per_ocpu_in_gbs": 3.4
        }],
        "network_bandwidth_options": [{
            "min_in_gbps": 3.4,
            "max_in_gbps": 3.4,
            "default_per_ocpu_in_gbps": 3.4
        }]
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


class PodShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_pod_shapes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


PodShapeFactsHelperCustom = get_custom_class("PodShapeFactsHelperCustom")


class ResourceFactsHelper(PodShapeFactsHelperCustom, PodShapeFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["ID", "NAME", "TIME_CREATED"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="pod_shape",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(pod_shapes=result)


if __name__ == "__main__":
    main()

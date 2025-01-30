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
module: oci_container_instances_container_instance_shape_facts
short_description: Fetches details about one or multiple ContainerInstanceShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ContainerInstanceShape resources in Oracle Cloud Infrastructure
    - Lists the shapes that can be used to create container instances.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
        type: str
        required: true
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List container_instance_shapes
  oci_container_instances_container_instance_shape_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    availability_domain: Uocm:PHX-AD-1

"""

RETURN = """
container_instance_shapes:
    description:
        - List of ContainerInstanceShape resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name identifying the shape.
            returned: on success
            type: str
            sample: name_example
        processor_description:
            description:
                - A short description of the container instance's processor (CPU).
            returned: on success
            type: str
            sample: processor_description_example
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
                min_in_gbs:
                    description:
                        - The minimum amount of memory (GB).
                    returned: on success
                    type: float
                    sample: 3.4
                max_in_gbs:
                    description:
                        - The maximum amount of memory (GB).
                    returned: on success
                    type: float
                    sample: 3.4
                default_per_ocpu_in_gbs:
                    description:
                        - The default amount of memory per OCPU available for this shape (GB).
                    returned: on success
                    type: float
                    sample: 3.4
                min_per_ocpu_in_gbs:
                    description:
                        - The minimum amount of memory per OCPU available for this shape (GB).
                    returned: on success
                    type: float
                    sample: 3.4
                max_per_ocpu_in_gbs:
                    description:
                        - The maximum amount of memory per OCPU available for this shape (GB).
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
    sample: [{
        "name": "name_example",
        "processor_description": "processor_description_example",
        "ocpu_options": {
            "min": 3.4,
            "max": 3.4
        },
        "memory_options": {
            "min_in_gbs": 3.4,
            "max_in_gbs": 3.4,
            "default_per_ocpu_in_gbs": 3.4,
            "min_per_ocpu_in_gbs": 3.4,
            "max_per_ocpu_in_gbs": 3.4
        },
        "networking_bandwidth_options": {
            "min_in_gbps": 3.4,
            "max_in_gbps": 3.4,
            "default_per_ocpu_in_gbps": 3.4
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
    from oci.container_instances import ContainerInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerInstanceShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_container_instance_shapes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ContainerInstanceShapeFactsHelperCustom = get_custom_class(
    "ContainerInstanceShapeFactsHelperCustom"
)


class ResourceFactsHelper(
    ContainerInstanceShapeFactsHelperCustom, ContainerInstanceShapeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type="str"),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="container_instance_shape",
        service_client_class=ContainerInstanceClient,
        namespace="container_instances",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(container_instance_shapes=result)


if __name__ == "__main__":
    main()

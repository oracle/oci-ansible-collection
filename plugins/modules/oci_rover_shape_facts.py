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
module: oci_rover_shape_facts
short_description: Fetches details about one or multiple Shape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Shape resources in Oracle Cloud Infrastructure
    - Returns a list of Shapes.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment in which to list resources.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List shapes
  oci_rover_shape_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
shapes:
    description:
        - List of Shape resources
    returned: on success
    type: complex
    contains:
        gpu_description:
            description:
                - A short description of the graphics processing unit (GPU) available for this shape.
            returned: on success
            type: str
            sample: gpu_description_example
        gpus:
            description:
                - The number of GPUs available for this shape.
            returned: on success
            type: int
            sample: 56
        memory_in_gbs:
            description:
                - The default amount of memory available for this shape, in gigabytes.
            returned: on success
            type: float
            sample: 3.4
        networking_bandwidth_in_gbps:
            description:
                - The networking bandwidth available for this shape, in gigabits per second.
            returned: on success
            type: float
            sample: 3.4
        ocpus:
            description:
                - The default number of OCPUs available for this shape.
            returned: on success
            type: int
            sample: 56
        processor_description:
            description:
                - A short description of the shape's processor (CPU).
            returned: on success
            type: str
            sample: processor_description_example
        shape:
            description:
                - The name of the shape.
            returned: on success
            type: str
            sample: shape_example
        usb_controller_description:
            description:
                - A short description of the USB controller available for this shape.
            returned: on success
            type: str
            sample: usb_controller_description_example
        number_of_usb_controllers:
            description:
                - The number of USB controllers available for this shape.
            returned: on success
            type: int
            sample: 56
        tags:
            description:
                - The tags associated with tagSlug.
            returned: on success
            type: str
            sample: tags_example
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "gpu_description": "gpu_description_example",
        "gpus": 56,
        "memory_in_gbs": 3.4,
        "networking_bandwidth_in_gbps": 3.4,
        "ocpus": 56,
        "processor_description": "processor_description_example",
        "shape": "shape_example",
        "usb_controller_description": "usb_controller_description_example",
        "number_of_usb_controllers": 56,
        "tags": "tags_example",
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
    from oci.rover import ShapeClient

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
            "sort_order",
            "sort_by",
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
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="shape",
        service_client_class=ShapeClient,
        namespace="rover",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(shapes=result)


if __name__ == "__main__":
    main()

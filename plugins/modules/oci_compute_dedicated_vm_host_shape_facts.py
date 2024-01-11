#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_compute_dedicated_vm_host_shape_facts
short_description: Fetches details about one or multiple DedicatedVmHostShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DedicatedVmHostShape resources in Oracle Cloud Infrastructure
    - Lists the shapes that can be used to launch a dedicated virtual machine host within the specified compartment.
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
    instance_shape_name:
        description:
            - The name for the instance's shape.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List dedicated_vm_host_shapes
  oci_compute_dedicated_vm_host_shape_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    availability_domain: Uocm:PHX-AD-1
    instance_shape_name: instance_shape_name_example

"""

RETURN = """
dedicated_vm_host_shapes:
    description:
        - List of DedicatedVmHostShape resources
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The shape's availability domain.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        dedicated_vm_host_shape:
            description:
                - The name of the dedicated VM host shape. You can enumerate all available shapes by calling
                  L(ListDedicatedVmHostShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/dedicatedVmHostShapes).
            returned: on success
            type: str
            sample: dedicated_vm_host_shape_example
    sample: [{
        "availability_domain": "Uocm:PHX-AD-1",
        "dedicated_vm_host_shape": "dedicated_vm_host_shape_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DedicatedVmHostShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "instance_shape_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_dedicated_vm_host_shapes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DedicatedVmHostShapeFactsHelperCustom = get_custom_class(
    "DedicatedVmHostShapeFactsHelperCustom"
)


class ResourceFactsHelper(
    DedicatedVmHostShapeFactsHelperCustom, DedicatedVmHostShapeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type="str"),
            instance_shape_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="dedicated_vm_host_shape",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(dedicated_vm_host_shapes=result)


if __name__ == "__main__":
    main()

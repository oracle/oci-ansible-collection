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
module: oci_ocvp_supported_host_shape_facts
short_description: Fetches details about one or multiple SupportedHostShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SupportedHostShape resources in Oracle Cloud Infrastructure
    - Lists supported compute shapes for ESXi hosts.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    name:
        description:
            - A filter to return only resources that match the given name exactly.
        type: str
    sddc_type:
        description:
            - A filter to return only resources that match the given SDDC type exactly.
        type: str
        choices:
            - "PRODUCTION"
            - "NON_PRODUCTION"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List supported_host_shapes
  oci_ocvp_supported_host_shape_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sddc_type: PRODUCTION

"""

RETURN = """
supported_host_shapes:
    description:
        - List of SupportedHostShape resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the supported compute shape.
            returned: on success
            type: str
            sample: name_example
        supported_operations:
            description:
                - The operations where you can use the shape. The operations can be CREATE_SDDC or CREATE_ESXI_HOST.
            returned: on success
            type: list
            sample: []
        shape_family:
            description:
                - The family of the shape. ESXi hosts of one SDDC must have the same shape family.
            returned: on success
            type: str
            sample: shape_family_example
        default_ocpu_count:
            description:
                - The default OCPU count of the shape.
            returned: on success
            type: float
            sample: 3.4
        supported_ocpu_count:
            description:
                - Support OCPU count of the shape.
            returned: on success
            type: list
            sample: []
        supported_sddc_types:
            description:
                - The supported SDDC types for the shape.
            returned: on success
            type: list
            sample: []
        supported_vmware_software_versions:
            description:
                - The VMware software versions supported by the shape.
            returned: on success
            type: list
            sample: []
        description:
            description:
                - Description of the shape.
            returned: on success
            type: str
            sample: description_example
        is_support_shielded_instances:
            description:
                - Indicates whether the shape supports shielded instances.
            returned: on success
            type: bool
            sample: true
        is_support_monthly_sku:
            description:
                - "Whether the shape supports \\"MONTH\\" SKU."
            returned: on success
            type: bool
            sample: true
    sample: [{
        "name": "name_example",
        "supported_operations": [],
        "shape_family": "shape_family_example",
        "default_ocpu_count": 3.4,
        "supported_ocpu_count": [],
        "supported_sddc_types": [],
        "supported_vmware_software_versions": [],
        "description": "description_example",
        "is_support_shielded_instances": true,
        "is_support_monthly_sku": true
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ocvp import SddcClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SupportedHostShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sddc_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_supported_host_shapes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SupportedHostShapeFactsHelperCustom = get_custom_class(
    "SupportedHostShapeFactsHelperCustom"
)


class ResourceFactsHelper(
    SupportedHostShapeFactsHelperCustom, SupportedHostShapeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            name=dict(type="str"),
            sddc_type=dict(type="str", choices=["PRODUCTION", "NON_PRODUCTION"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="supported_host_shape",
        service_client_class=SddcClient,
        namespace="ocvp",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(supported_host_shapes=result)


if __name__ == "__main__":
    main()

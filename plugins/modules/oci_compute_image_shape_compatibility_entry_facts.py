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
module: oci_compute_image_shape_compatibility_entry_facts
short_description: Fetches details about one or multiple ImageShapeCompatibilityEntry resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ImageShapeCompatibilityEntry resources in Oracle Cloud Infrastructure
    - Lists the shape compatibilities for the image.
    - If I(shape_name) is specified, the details of a single ImageShapeCompatibilityEntry will be returned.
version_added: "2.5"
options:
    image_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the image.
        type: str
        required: true
    shape_name:
        description:
            - Shape name.
            - Required to get a specific image_shape_compatibility_entry.
        type: str
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List image_shape_compatibility_entries
  oci_compute_image_shape_compatibility_entry_facts:
    image_id: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific image_shape_compatibility_entry
  oci_compute_image_shape_compatibility_entry_facts:
    image_id: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
    shape_name: shape_name_example

"""

RETURN = """
image_shape_compatibility_entries:
    description:
        - List of ImageShapeCompatibilityEntry resources
    returned: on success
    type: complex
    contains:
        image_id:
            description:
                - The image OCID.
            returned: on success
            type: string
            sample: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
        shape:
            description:
                - The shape name.
            returned: on success
            type: string
            sample: shape_example
        ocpu_constraints:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                min:
                    description:
                        - The minimum number of OCPUs supported for this image and shape.
                    returned: on success
                    type: int
                    sample: 56
                max:
                    description:
                        - The maximum number of OCPUs supported for this image and shape.
                    returned: on success
                    type: int
                    sample: 56
    sample: [{
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "shape": "shape_example",
        "ocpu_constraints": {
            "min": 56,
            "max": 56
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


class ImageShapeCompatibilityEntryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "image_id",
            "shape_name",
        ]

    def get_required_params_for_list(self):
        return [
            "image_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_image_shape_compatibility_entry,
            image_id=self.module.params.get("image_id"),
            shape_name=self.module.params.get("shape_name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_image_shape_compatibility_entries,
            image_id=self.module.params.get("image_id"),
            **optional_kwargs
        )


ImageShapeCompatibilityEntryFactsHelperCustom = get_custom_class(
    "ImageShapeCompatibilityEntryFactsHelperCustom"
)


class ResourceFactsHelper(
    ImageShapeCompatibilityEntryFactsHelperCustom,
    ImageShapeCompatibilityEntryFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(image_id=dict(type="str", required=True), shape_name=dict(type="str"),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="image_shape_compatibility_entry",
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

    module.exit_json(image_shape_compatibility_entries=result)


if __name__ == "__main__":
    main()

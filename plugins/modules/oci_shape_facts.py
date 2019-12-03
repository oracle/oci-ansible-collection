#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_shape_facts
short_description: Retrieve details about shapes that can be used to launch instances in OCI Compute Service
description:
    - This module retrieves details about shapes that can be used to launch instances within a specified Compartment in
      OCI Compute Service.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment (either the tenancy or another compartment in the tenancy).
        required: true
    availability_domain:
        description: The name of the Availability Domain.
        required: false
    image_id:
        description: The OCID of an image.
        required: false
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get details of all the shapes available to a Tenancy
  oci_shape_facts:
    compartment_id: 'ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx.....uyty4'
- name: Get details of all the shapes of a specific compartment in an Availability Domain
  oci_shape_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'
    availability_domain: "BnQb:PHX-AD-1"
"""

RETURN = """
shapes:
    description: Information about one or more shapes available in the specified compartment
    returned: on success
    type: complex
    contains:
        shape:
            description: The name of the shape
            returned: always
            type: string
            sample: VM.DenseIO1.16
    sample: [{
               "shape": "VM.DenseIO1.16"
             }, {
               "shape": "VM.DenseIO1.8"
             }
            ]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_client import ComputeClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type="str", required=False),
            image_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    compartment_id = module.params["compartment_id"]
    result = dict(changed=False)

    try:
        optional_list_method_params = ["availability_domain", "image_id"]
        optional_kwargs = dict(
            (param, module.params[param])
            for param in optional_list_method_params
            if module.params.get(param) is not None
        )
        shapes = oci_utils.list_all_resources(
            compute_client.list_shapes, compartment_id=compartment_id, **optional_kwargs
        )
        result["shapes"] = to_dict(shapes)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(shapes=result)


if __name__ == "__main__":
    main()

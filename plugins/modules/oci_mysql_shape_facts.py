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
module: oci_mysql_shape_facts
short_description: Fetches details about one or multiple Shape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Shape resources in Oracle Cloud Infrastructure
    - "Gets a list of the shapes you can use to create a new MySQL DB System.
      The shape determines the resources allocated to the DB System:
      CPU cores and memory for VM shapes; CPU cores, memory and
      storage for non-VM (or bare metal) shapes."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    availability_domain:
        description:
            - The name of the Availability Domain.
        type: str
    name:
        description:
            - Name
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List shapes
  oci_mysql_shape_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
shapes:
    description:
        - List of Shape resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the shape used for the DB System.
            returned: on success
            type: string
            sample: name_example
        cpu_core_count:
            description:
                - "The number of CPU Cores the Instance provides. These are \\"OCPU\\"s."
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The amount of RAM the Instance provides. This is an IEC base-2 number.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "name": "name_example",
        "cpu_core_count": 56,
        "memory_size_in_gbs": 56
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import MysqlaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlShapeFactsHelperGen(OCIResourceFactsHelperBase):
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
            self.client.list_shapes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


MysqlShapeFactsHelperCustom = get_custom_class("MysqlShapeFactsHelperCustom")


class ResourceFactsHelper(MysqlShapeFactsHelperCustom, MysqlShapeFactsHelperGen):
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

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="shape",
        service_client_class=MysqlaasClient,
        namespace="mysql",
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

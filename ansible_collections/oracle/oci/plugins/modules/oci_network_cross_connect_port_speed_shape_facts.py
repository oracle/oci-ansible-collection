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
module: oci_network_cross_connect_port_speed_shape_facts
short_description: Fetches details about one or multiple CrossConnectPortSpeedShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CrossConnectPortSpeedShape resources in Oracle Cloud Infrastructure
    - Lists the available port speeds for cross-connects. You need this information
      so you can specify your desired port speed (that is, shape) when you create a
      cross-connect.
version_added: "2.5"
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List cross_connect_port_speed_shapes
  oci_network_cross_connect_port_speed_shape_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
cross_connect_port_speed_shapes:
    description:
        - List of CrossConnectPortSpeedShape resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the port speed shape.
                - "Example: `10 Gbps`"
            returned: on success
            type: string
            sample: 10 Gbps
        port_speed_in_gbps:
            description:
                - The port speed in Gbps.
                - "Example: `10`"
            returned: on success
            type: int
            sample: 10
    sample: [{
        "name": "10 Gbps",
        "port_speed_in_gbps": 10
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CrossConnectPortSpeedShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_crossconnect_port_speed_shapes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


CrossConnectPortSpeedShapeFactsHelperCustom = get_custom_class(
    "CrossConnectPortSpeedShapeFactsHelperCustom"
)


class ResourceFactsHelper(
    CrossConnectPortSpeedShapeFactsHelperCustom,
    CrossConnectPortSpeedShapeFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(compartment_id=dict(type="str", required=True), name=dict(type="str"),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cross_connect_port_speed_shape",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(cross_connect_port_speed_shapes=result)


if __name__ == "__main__":
    main()

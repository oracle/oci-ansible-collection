#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_network_cross_connect_location_facts
short_description: Fetches details about one or multiple CrossConnectLocation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CrossConnectLocation resources in Oracle Cloud Infrastructure
    - Lists the available FastConnect locations for cross-connect installation. You need
      this information so you can specify your desired location when you create a cross-connect.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List cross_connect_locations
  oci_network_cross_connect_location_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
cross_connect_locations:
    description:
        - List of CrossConnectLocation resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - A description of the location.
            returned: on success
            type: str
            sample: description_example
        name:
            description:
                - The name of the location.
                - "Example: `CyrusOne, Chandler, AZ`"
            returned: on success
            type: str
            sample: CyrusOne, Chandler, AZ
    sample: [{
        "description": "description_example",
        "name": "CyrusOne, Chandler, AZ"
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


class CrossConnectLocationFactsHelperGen(OCIResourceFactsHelperBase):
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
            self.client.list_cross_connect_locations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


CrossConnectLocationFactsHelperCustom = get_custom_class(
    "CrossConnectLocationFactsHelperCustom"
)


class ResourceFactsHelper(
    CrossConnectLocationFactsHelperCustom, CrossConnectLocationFactsHelperGen
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
        resource_type="cross_connect_location",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(cross_connect_locations=result)


if __name__ == "__main__":
    main()

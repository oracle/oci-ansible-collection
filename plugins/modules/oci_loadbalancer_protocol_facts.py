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
module: oci_loadbalancer_protocol_facts
short_description: Fetches details about one or multiple LoadBalancerProtocol resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LoadBalancerProtocol resources in Oracle Cloud Infrastructure
    - Lists all supported traffic protocols.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the load balancer protocols to
              list.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List load_balancer_protocols
  oci_loadbalancer_protocol_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
load_balancer_protocols:
    description:
        - List of LoadBalancerProtocol resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of a protocol.
                - "Example: 'HTTP'"
            returned: on success
            type: str
            sample: name_example
    sample: [{
        "name": "name_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LoadBalancerProtocolFactsHelperGen(OCIResourceFactsHelperBase):
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
            self.client.list_protocols,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LoadBalancerProtocolFactsHelperCustom = get_custom_class(
    "LoadBalancerProtocolFactsHelperCustom"
)


class ResourceFactsHelper(
    LoadBalancerProtocolFactsHelperCustom, LoadBalancerProtocolFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="load_balancer_protocol",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(load_balancer_protocols=result)


if __name__ == "__main__":
    main()

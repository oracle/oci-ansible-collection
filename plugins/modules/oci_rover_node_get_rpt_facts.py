#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_rover_node_get_rpt_facts
short_description: Fetches details about a RoverNodeGetRpt resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a RoverNodeGetRpt resource in Oracle Cloud Infrastructure
    - Get the resource principal token for a rover node
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    rover_node_id:
        description:
            - Unique RoverNode identifier
        type: str
        aliases: ["id"]
        required: true
    jwt:
        description:
            - The Java Web Token which is a signature of the request that is signed with the resource's private key
              This is meant solely in the context of getRpt
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific rover_node_get_rpt
  oci_rover_node_get_rpt_facts:
    # required
    rover_node_id: "ocid1.rovernode.oc1..xxxxxxEXAMPLExxxxxx"
    jwt: jwt_example

"""

RETURN = """
rover_node_get_rpt:
    description:
        - RoverNodeGetRpt resource
    returned: on success
    type: complex
    contains:
        resource_principal_token:
            description:
                - The resource principal token blob that contains claims about the resource.
            returned: on success
            type: str
            sample: resource_principal_token_example
        service_principal_session_token:
            description:
                - The service principal session token
            returned: on success
            type: str
            sample: service_principal_session_token_example
    sample: {
        "resource_principal_token": "resource_principal_token_example",
        "service_principal_session_token": "service_principal_session_token_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.rover import RoverNodeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoverNodeGetRptFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "rover_node_id",
            "jwt",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rover_node_get_rpt,
            rover_node_id=self.module.params.get("rover_node_id"),
            jwt=self.module.params.get("jwt"),
        )


RoverNodeGetRptFactsHelperCustom = get_custom_class("RoverNodeGetRptFactsHelperCustom")


class ResourceFactsHelper(
    RoverNodeGetRptFactsHelperCustom, RoverNodeGetRptFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            rover_node_id=dict(aliases=["id"], type="str", required=True),
            jwt=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="rover_node_get_rpt",
        service_client_class=RoverNodeClient,
        namespace="rover",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(rover_node_get_rpt=result)


if __name__ == "__main__":
    main()

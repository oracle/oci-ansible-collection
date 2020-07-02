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
module: oci_network_cross_connect_status_facts
short_description: Fetches details about a CrossConnectStatus resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a CrossConnectStatus resource in Oracle Cloud Infrastructure
    - Gets the status of the specified cross-connect.
version_added: "2.9"
author: Oracle (@oracle)
options:
    cross_connect_id:
        description:
            - The OCID of the cross-connect.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific cross_connect_status
  oci_network_cross_connect_status_facts:
    cross_connect_id: ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
cross_connect_status:
    description:
        - CrossConnectStatus resource
    returned: on success
    type: complex
    contains:
        cross_connect_id:
            description:
                - The OCID of the cross-connect.
            returned: on success
            type: string
            sample: ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx
        interface_state:
            description:
                - Whether Oracle's side of the interface is up or down.
            returned: on success
            type: string
            sample: UP
        light_level_ind_bm:
            description:
                - The light level of the cross-connect (in dBm).
                - "Example: `14.0`"
            returned: on success
            type: float
            sample: 14.0
        light_level_indicator:
            description:
                - Status indicator corresponding to the light level.
                - " * **NO_LIGHT:** No measurable light"
                - " * **LOW_WARN:** There's measurable light but it's too low"
                - " * **HIGH_WARN:** Light level is too high"
                - " * **BAD:** There's measurable light but the signal-to-noise ratio is bad"
                - " * **GOOD:** Good light level"
            returned: on success
            type: string
            sample: NO_LIGHT
    sample: {
        "cross_connect_id": "ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx",
        "interface_state": "UP",
        "light_level_ind_bm": 14.0,
        "light_level_indicator": "NO_LIGHT"
    }
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


class CrossConnectStatusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "cross_connect_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cross_connect_status,
            cross_connect_id=self.module.params.get("cross_connect_id"),
        )


CrossConnectStatusFactsHelperCustom = get_custom_class(
    "CrossConnectStatusFactsHelperCustom"
)


class ResourceFactsHelper(
    CrossConnectStatusFactsHelperCustom, CrossConnectStatusFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(cross_connect_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cross_connect_status",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(cross_connect_status=result)


if __name__ == "__main__":
    main()

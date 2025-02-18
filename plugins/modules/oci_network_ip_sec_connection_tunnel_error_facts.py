#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_network_ip_sec_connection_tunnel_error_facts
short_description: Fetches details about a IpSecConnectionTunnelError resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a IpSecConnectionTunnelError resource in Oracle Cloud Infrastructure
    - Gets the identified error for the specified IPSec tunnel ID.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ipsc_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.
        type: str
        required: true
    tunnel_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific ip_sec_connection_tunnel_error
  oci_network_ip_sec_connection_tunnel_error_facts:
    # required
    ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"
    tunnel_id: "ocid1.tunnel.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
ip_sec_connection_tunnel_error:
    description:
        - IpSecConnectionTunnelError resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique ID generated for each error report.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        error_code:
            description:
                - Unique code describes the error type.
            returned: on success
            type: str
            sample: error_code_example
        error_description:
            description:
                - A detailed description of the error.
            returned: on success
            type: str
            sample: error_description_example
        solution:
            description:
                - Resolution for the error.
            returned: on success
            type: str
            sample: solution_example
        oci_resources_link:
            description:
                - Link to more Oracle resources or relevant documentation.
            returned: on success
            type: str
            sample: oci_resources_link_example
        timestamp:
            description:
                - Timestamp when the error occurred.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "error_code": "error_code_example",
        "error_description": "error_description_example",
        "solution": "solution_example",
        "oci_resources_link": "oci_resources_link_example",
        "timestamp": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IpSecConnectionTunnelErrorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "ipsc_id",
            "tunnel_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ip_sec_connection_tunnel_error,
            ipsc_id=self.module.params.get("ipsc_id"),
            tunnel_id=self.module.params.get("tunnel_id"),
        )


IpSecConnectionTunnelErrorFactsHelperCustom = get_custom_class(
    "IpSecConnectionTunnelErrorFactsHelperCustom"
)


class ResourceFactsHelper(
    IpSecConnectionTunnelErrorFactsHelperCustom,
    IpSecConnectionTunnelErrorFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            ipsc_id=dict(type="str", required=True),
            tunnel_id=dict(aliases=["id"], type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ip_sec_connection_tunnel_error",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(ip_sec_connection_tunnel_error=result)


if __name__ == "__main__":
    main()

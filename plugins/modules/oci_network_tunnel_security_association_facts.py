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
module: oci_network_tunnel_security_association_facts
short_description: Fetches details about one or multiple TunnelSecurityAssociation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TunnelSecurityAssociation resources in Oracle Cloud Infrastructure
    - Lists the tunnel security associations information for the specified IPSec tunnel ID.
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
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List tunnel_security_associations
  oci_network_tunnel_security_association_facts:
    # required
    ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"
    tunnel_id: "ocid1.tunnel.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
tunnel_security_associations:
    description:
        - List of TunnelSecurityAssociation resources
    returned: on success
    type: complex
    contains:
        cpe_subnet:
            description:
                - The IP address and mask of the partner subnet used in policy based VPNs or static routes.
            returned: on success
            type: str
            sample: cpe_subnet_example
        oracle_subnet:
            description:
                - The IP address and mask of the local subnet used in policy based VPNs or static routes.
            returned: on success
            type: str
            sample: oracle_subnet_example
        tunnel_sa_status:
            description:
                - The IPSec tunnel's phase one status.
            returned: on success
            type: str
            sample: INITIATING
        tunnel_sa_error_info:
            description:
                - Current state if the IPSec tunnel status is not `UP`, including phase one and phase two details and a possible reason the tunnel is not `UP`.
            returned: on success
            type: str
            sample: tunnel_sa_error_info_example
        time:
            description:
                - Time in the current state, in seconds.
            returned: on success
            type: str
            sample: time_example
    sample: [{
        "cpe_subnet": "cpe_subnet_example",
        "oracle_subnet": "oracle_subnet_example",
        "tunnel_sa_status": "INITIATING",
        "tunnel_sa_error_info": "tunnel_sa_error_info_example",
        "time": "time_example"
    }]
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


class TunnelSecurityAssociationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "ipsc_id",
            "tunnel_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_ip_sec_connection_tunnel_security_associations,
            ipsc_id=self.module.params.get("ipsc_id"),
            tunnel_id=self.module.params.get("tunnel_id"),
            **optional_kwargs
        )


TunnelSecurityAssociationFactsHelperCustom = get_custom_class(
    "TunnelSecurityAssociationFactsHelperCustom"
)


class ResourceFactsHelper(
    TunnelSecurityAssociationFactsHelperCustom, TunnelSecurityAssociationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            ipsc_id=dict(type="str", required=True),
            tunnel_id=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tunnel_security_association",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(tunnel_security_associations=result)


if __name__ == "__main__":
    main()

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
module: oci_network_cross_connect_mapping_facts
short_description: Fetches details about one or multiple CrossConnectMapping resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CrossConnectMapping resources in Oracle Cloud Infrastructure
    - Lists the Cross Connect mapping Details for the specified
      virtual circuit.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    virtual_circuit_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the virtual circuit.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List cross_connect_mappings
  oci_network_cross_connect_mapping_facts:
    virtual_circuit_id: "ocid1.virtualcircuit.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
cross_connect_mappings:
    description:
        - List of CrossConnectMapping resources
    returned: on success
    type: complex
    contains:
        bgp_md5_auth_key:
            description:
                - The key for BGP MD5 authentication. Only applicable if your system
                  requires MD5 authentication. If empty or not set (null), that
                  means you don't use BGP MD5 authentication.
            returned: on success
            type: str
            sample: bgp_md5_auth_key_example
        cross_connect_or_cross_connect_group_id:
            description:
                - The OCID of the cross-connect or cross-connect group for this mapping.
                  Specified by the owner of the cross-connect or cross-connect group (the
                  customer if the customer is colocated with Oracle, or the provider if the
                  customer is connecting via provider).
            returned: on success
            type: str
            sample: "ocid1.crossconnectorcrossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx"
        customer_bgp_peering_ip:
            description:
                - The BGP IPv4 address for the router on the other end of the BGP session from
                  Oracle. Specified by the owner of that router. If the session goes from Oracle
                  to a customer, this is the BGP IPv4 address of the customer's edge router. If the
                  session goes from Oracle to a provider, this is the BGP IPv4 address of the
                  provider's edge router. Must use a /30 or /31 subnet mask.
                - "There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses."
                - "Example: `10.0.0.18/31`"
            returned: on success
            type: str
            sample: 10.0.0.18/31
        oracle_bgp_peering_ip:
            description:
                - The IPv4 address for Oracle's end of the BGP session. Must use a /30 or /31
                  subnet mask. If the session goes from Oracle to a customer's edge router,
                  the customer specifies this information. If the session goes from Oracle to
                  a provider's edge router, the provider specifies this.
                - "There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses."
                - "Example: `10.0.0.19/31`"
            returned: on success
            type: str
            sample: 10.0.0.19/31
        customer_bgp_peering_ipv6:
            description:
                - The BGP IPv6 address for the router on the other end of the BGP session from
                  Oracle. Specified by the owner of that router. If the session goes from Oracle
                  to a customer, this is the BGP IPv6 address of the customer's edge router. If the
                  session goes from Oracle to a provider, this is the BGP IPv6 address of the
                  provider's edge router. Only subnet masks from /64 up to /127 are allowed.
                - "There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses."
                - "Example: `2001:db8::1/64`"
            returned: on success
            type: str
            sample: 2001:db8::1/64
        oracle_bgp_peering_ipv6:
            description:
                - The IPv6 address for Oracle's end of the BGP session. Only subnet masks from /64 up to /127 are allowed.
                  If the session goes from Oracle to a customer's edge router,
                  the customer specifies this information. If the session goes from Oracle to
                  a provider's edge router, the provider specifies this.
                - "There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv6 addresses."
                - "Example: `2001:db8::2/64`"
            returned: on success
            type: str
            sample: 2001:db8::2/64
        vlan:
            description:
                - The number of the specific VLAN (on the cross-connect or cross-connect group)
                  that is assigned to this virtual circuit. Specified by the owner of the cross-connect
                  or cross-connect group (the customer if the customer is colocated with Oracle, or
                  the provider if the customer is connecting via provider).
                - "Example: `200`"
            returned: on success
            type: int
            sample: 200
        ipv4_bgp_status:
            description:
                - The state of the Ipv4 BGP session.
            returned: on success
            type: str
            sample: UP
        ipv6_bgp_status:
            description:
                - The state of the Ipv6 BGP session.
            returned: on success
            type: str
            sample: UP
    sample: [{
        "bgp_md5_auth_key": "bgp_md5_auth_key_example",
        "cross_connect_or_cross_connect_group_id": "ocid1.crossconnectorcrossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx",
        "customer_bgp_peering_ip": "10.0.0.18/31",
        "oracle_bgp_peering_ip": "10.0.0.19/31",
        "customer_bgp_peering_ipv6": "2001:db8::1/64",
        "oracle_bgp_peering_ipv6": "2001:db8::2/64",
        "vlan": 200,
        "ipv4_bgp_status": "UP",
        "ipv6_bgp_status": "UP"
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


class CrossConnectMappingFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "virtual_circuit_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_cross_connect_mappings,
            virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
            **optional_kwargs
        )


CrossConnectMappingFactsHelperCustom = get_custom_class(
    "CrossConnectMappingFactsHelperCustom"
)


class ResourceFactsHelper(
    CrossConnectMappingFactsHelperCustom, CrossConnectMappingFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(virtual_circuit_id=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cross_connect_mapping",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(cross_connect_mappings=result)


if __name__ == "__main__":
    main()

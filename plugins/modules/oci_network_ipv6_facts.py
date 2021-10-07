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
module: oci_network_ipv6_facts
short_description: Fetches details about one or multiple Ipv6 resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Ipv6 resources in Oracle Cloud Infrastructure
    - "Lists the L(IPv6,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Ipv6/) objects based
      on one of these filters:"
    - " * Subnet OCID.
        * VNIC OCID.
        * Both IPv6 address and subnet OCID: This lets you get an `Ipv6` object based on its private
        IPv6 address (for example, 2001:0db8:0123:1111:abcd:ef01:2345:6789) and not its OCID. For comparison,
        L(GetIpv6,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Ipv6/GetIpv6) requires the OCID."
    - If I(ipv6_id) is specified, the details of a single Ipv6 will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ipv6_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the IPv6.
            - Required to get a specific ipv6.
        type: str
        aliases: ["id"]
    ip_address:
        description:
            - "An IP address. This could be either IPv4 or IPv6, depending on the resource.
              Example: `10.0.3.3`"
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet.
        type: str
    vnic_id:
        description:
            - The OCID of the VNIC.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List ipv6s
  oci_network_ipv6_facts:

- name: Get a specific ipv6
  oci_network_ipv6_facts:
    ipv6_id: "ocid1.ipv6.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
ipv6s:
    description:
        - List of Ipv6 resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the IPv6.
                  This is the same as the VNIC's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid
                  entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the IPv6.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ip_address:
            description:
                - The IPv6 address of the `IPv6` object. The address is within the IPv6 CIDR block of the VNIC's subnet
                  (see the `ipv6CidrBlock` attribute for the L(Subnet,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Subnet/) object.
                - "Example: `2001:0db8:0123:1111:abcd:ef01:2345:6789`"
            returned: on success
            type: str
            sample: 2001:0db8:0123:1111:abcd:ef01:2345:6789
        lifecycle_state:
            description:
                - The IPv6's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet the VNIC is in.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the IPv6 was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        vnic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VNIC the IPv6 is assigned to.
                  The VNIC and IPv6 must be in the same subnet.
            returned: on success
            type: str
            sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "2001:0db8:0123:1111:abcd:ef01:2345:6789",
        "lifecycle_state": "PROVISIONING",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
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


class Ipv6FactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "ipv6_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ipv6, ipv6_id=self.module.params.get("ipv6_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "ip_address",
            "subnet_id",
            "vnic_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_ipv6s, **optional_kwargs
        )


Ipv6FactsHelperCustom = get_custom_class("Ipv6FactsHelperCustom")


class ResourceFactsHelper(Ipv6FactsHelperCustom, Ipv6FactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            ipv6_id=dict(aliases=["id"], type="str"),
            ip_address=dict(type="str"),
            subnet_id=dict(type="str"),
            vnic_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ipv6",
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

    module.exit_json(ipv6s=result)


if __name__ == "__main__":
    main()

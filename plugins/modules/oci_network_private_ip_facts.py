#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_network_private_ip_facts
short_description: Fetches details about one or multiple PrivateIp resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PrivateIp resources in Oracle Cloud Infrastructure
    - "Lists the L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/) objects based
      on one of these filters:"
    - " - Subnet OCID.
        - VNIC OCID.
        - Both private IP address and subnet OCID: This lets
        you get a `privateIP` object based on its private IP
        address (for example, 10.0.3.3) and not its OCID. For comparison,
        L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp)
        requires the OCID."
    - If you're listing all the private IPs associated with a given subnet
      or VNIC, the response includes both primary and secondary private IPs.
    - If you are an Oracle Cloud VMware Solution customer and have VLANs
      in your VCN, you can filter the list by VLAN OCID. See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
    - If I(private_ip_id) is specified, the details of a single PrivateIp will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    private_ip_id:
        description:
            - The OCID of the private IP.
            - Required to get a specific private_ip.
        type: str
        aliases: ["id"]
    ip_address:
        description:
            - "An IP address.
              Example: `10.0.3.3`"
        type: str
    subnet_id:
        description:
            - The OCID of the subnet.
        type: str
    vnic_id:
        description:
            - The OCID of the VNIC.
        type: str
    vlan_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List private_ips
  oci_network_private_ip_facts:

- name: Get a specific private_ip
  oci_network_private_ip_facts:
    private_ip_id: "ocid1.privateip.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
private_ips:
    description:
        - List of PrivateIp resources
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - "The private IP's availability domain. This attribute will be null if this is a *secondary*
                  private IP assigned to a VNIC that is in a *regional* subnet."
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment containing the private IP.
            returned: on success
            type: string
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
            type: string
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
        hostname_label:
            description:
                - The hostname for the private IP. Used for DNS. The value is the hostname
                  portion of the private IP's fully qualified domain name (FQDN)
                  (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                  Must be unique across all VNICs in the subnet and comply with
                  L(RFC 952,https://tools.ietf.org/html/rfc952) and
                  L(RFC 1123,https://tools.ietf.org/html/rfc1123).
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
                - "Example: `bminstance-1`"
            returned: on success
            type: string
            sample: bminstance-1
        id:
            description:
                - The private IP's Oracle ID (OCID).
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ip_address:
            description:
                - The private IP address of the `privateIp` object. The address is within the CIDR
                  of the VNIC's subnet.
                - However, if the `PrivateIp` object is being used with a VLAN as part of
                  the Oracle Cloud VMware Solution, the address is from the range specified by the
                  `cidrBlock` attribute for the VLAN. See L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
                - "Example: `10.0.3.3`"
            returned: on success
            type: string
            sample: 10.0.3.3
        is_primary:
            description:
                - Whether this private IP is the primary one on the VNIC. Primary private IPs
                  are unassigned and deleted automatically when the VNIC is terminated.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        vlan_id:
            description:
                - Applicable only if the `PrivateIp` object is being used with a VLAN as part of
                  the Oracle Cloud VMware Solution. The `vlanId` is the OCID of the VLAN. See
                  L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan).
            returned: on success
            type: string
            sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The OCID of the subnet the VNIC is in.
                - However, if the `PrivateIp` object is being used with a VLAN as part of
                  the Oracle Cloud VMware Solution, the `subnetId` is null.
            returned: on success
            type: string
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the private IP was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vnic_id:
            description:
                - The OCID of the VNIC the private IP is assigned to. The VNIC and private IP
                  must be in the same subnet.
                  However, if the `PrivateIp` object is being used with a VLAN as part of
                  the Oracle Cloud VMware Solution, the `vnicId` is null.
            returned: on success
            type: string
            sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "hostname_label": "bminstance-1",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "10.0.3.3",
        "is_primary": true,
        "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
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


class PrivateIpFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "private_ip_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_ip,
            private_ip_id=self.module.params.get("private_ip_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "ip_address",
            "subnet_id",
            "vnic_id",
            "vlan_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_private_ips, **optional_kwargs
        )


PrivateIpFactsHelperCustom = get_custom_class("PrivateIpFactsHelperCustom")


class ResourceFactsHelper(PrivateIpFactsHelperCustom, PrivateIpFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            private_ip_id=dict(aliases=["id"], type="str"),
            ip_address=dict(type="str"),
            subnet_id=dict(type="str"),
            vnic_id=dict(type="str"),
            vlan_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="private_ip",
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

    module.exit_json(private_ips=result)


if __name__ == "__main__":
    main()

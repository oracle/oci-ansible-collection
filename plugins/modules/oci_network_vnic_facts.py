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
module: oci_network_vnic_facts
short_description: Fetches details about a Vnic resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Vnic resource in Oracle Cloud Infrastructure
    - Gets the information for the specified virtual network interface card (VNIC).
      You can get the VNIC L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) from the
      L(ListVnicAttachments,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/VnicAttachment/ListVnicAttachments)
      operation.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vnic_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VNIC.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific vnic
  oci_network_vnic_facts:
    # required
    vnic_id: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
vnic:
    description:
        - Vnic resource
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The VNIC's availability domain.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the VNIC.
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
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
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
        hostname_label:
            description:
                - The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname
                  portion of the primary private IP's fully qualified domain name (FQDN)
                  (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                  Must be unique across all VNICs in the subnet and comply with
                  L(RFC 952,https://tools.ietf.org/html/rfc952) and
                  L(RFC 1123,https://tools.ietf.org/html/rfc1123).
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
                - "Example: `bminstance-1`"
            returned: on success
            type: str
            sample: hostname_label_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VNIC.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        is_primary:
            description:
                - Whether the VNIC is the primary VNIC (the VNIC that is automatically created
                  and attached during instance launch).
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current state of the VNIC.
            returned: on success
            type: str
            sample: PROVISIONING
        mac_address:
            description:
                - The MAC address of the VNIC.
                - If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution,
                  the MAC address is learned. If the VNIC belongs to a subnet, the
                  MAC address is a static, Oracle-provided value.
                - "Example: `00:00:00:00:00:01`"
            returned: on success
            type: str
            sample: mac_address_example
        nsg_ids:
            description:
                - A list of the OCIDs of the network security groups that the VNIC belongs to.
                - If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
                  belonging to a subnet), the value of the `nsgIds` attribute is ignored. Instead, the
                  VNIC belongs to the NSGs that are associated with the VLAN itself. See L(Vlan,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/latest/Vlan).
                - For more information about NSGs, see
                  L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
            returned: on success
            type: list
            sample: []
        vlan_id:
            description:
                - If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
                  belonging to a subnet), the `vlanId` is the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN
                  the VNIC is in. See
                  L(Vlan,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vlan). If the VNIC is instead in a subnet, `subnetId` has a value.
            returned: on success
            type: str
            sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
        private_ip:
            description:
                - The private IP address of the primary `privateIp` object on the VNIC.
                  The address is within the CIDR of the VNIC's subnet.
                - "Example: `10.0.3.3`"
            returned: on success
            type: str
            sample: private_ip_example
        public_ip:
            description:
                - The public IP address of the VNIC, if one is assigned.
            returned: on success
            type: str
            sample: public_ip_example
        skip_source_dest_check:
            description:
                - Whether the source/destination check is disabled on the VNIC.
                  Defaults to `false`, which means the check is performed. For information
                  about why you would skip the source/destination check, see
                  L(Using a Private IP as a Route Target,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#privateip).
                - If the VNIC belongs to a VLAN as part of the Oracle Cloud VMware Solution (instead of
                  belonging to a subnet), the `skipSourceDestCheck` attribute is `true`.
                  This is because the source/destination check is always disabled for VNICs in a VLAN.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet the VNIC is in.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the VNIC was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "hostname_label": "hostname_label_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_primary": true,
        "lifecycle_state": "PROVISIONING",
        "mac_address": "mac_address_example",
        "nsg_ids": [],
        "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
        "private_ip": "private_ip_example",
        "public_ip": "public_ip_example",
        "skip_source_dest_check": true,
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00"
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


class VnicFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "vnic_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vnic, vnic_id=self.module.params.get("vnic_id"),
        )


VnicFactsHelperCustom = get_custom_class("VnicFactsHelperCustom")


class ResourceFactsHelper(VnicFactsHelperCustom, VnicFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            vnic_id=dict(aliases=["id"], type="str", required=True),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vnic",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(vnic=result)


if __name__ == "__main__":
    main()

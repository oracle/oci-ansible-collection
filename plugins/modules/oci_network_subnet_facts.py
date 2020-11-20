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
module: oci_network_subnet_facts
short_description: Fetches details about one or multiple Subnet resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Subnet resources in Oracle Cloud Infrastructure
    - Lists the subnets in the specified VCN and the specified compartment.
      If the VCN ID is not provided, then the list includes the subnets from all VCNs in the specified compartment.
    - If I(subnet_id) is specified, the details of a single Subnet will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    subnet_id:
        description:
            - The OCID of the subnet.
            - Required to get a specific subnet.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple subnets.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "TERMINATING"
            - "TERMINATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List subnets
  oci_network_subnet_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific subnet
  oci_network_subnet_facts:
    subnet_id: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
subnets:
    description:
        - List of Subnet resources
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The subnet's availability domain. This attribute will be null if this is a regional subnet
                  instead of an AD-specific subnet. Oracle recommends creating regional subnets.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        cidr_block:
            description:
                - The subnet's CIDR block.
                - "Example: `10.0.1.0/24`"
            returned: on success
            type: string
            sample: 10.0.1.0/24
        compartment_id:
            description:
                - The OCID of the compartment containing the subnet.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        dhcp_options_id:
            description:
                - The OCID of the set of DHCP options that the subnet uses.
            returned: on success
            type: string
            sample: ocid1.dhcpoptions.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        dns_label:
            description:
                - A DNS label for the subnet, used in conjunction with the VNIC's hostname and
                  VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC
                  within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`).
                  Must be an alphanumeric string that begins with a letter and is unique within the VCN.
                  The value cannot be changed.
                - The absence of this parameter means the Internet and VCN Resolver
                  will not resolve hostnames of instances in this subnet.
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
                - "Example: `subnet123`"
            returned: on success
            type: string
            sample: subnet123
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The subnet's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The subnet's current state.
            returned: on success
            type: string
            sample: PROVISIONING
        prohibit_public_ip_on_vnic:
            description:
                - Whether VNICs within this subnet can have public IP addresses.
                  Defaults to false, which means VNICs created in this subnet will
                  automatically be assigned public IP addresses unless specified
                  otherwise during instance launch or VNIC creation (with the
                  `assignPublicIp` flag in
                  L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/)).
                  If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
                  subnet cannot have public IP addresses (that is, it's a private
                  subnet).
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        route_table_id:
            description:
                - The OCID of the route table that the subnet uses.
            returned: on success
            type: string
            sample: ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx
        security_list_ids:
            description:
                - "The OCIDs of the security list or lists that the subnet uses. Remember
                  that security lists are associated *with the subnet*, but the
                  rules are applied to the individual VNICs in the subnet."
            returned: on success
            type: list
            sample: []
        subnet_domain_name:
            description:
                - The subnet's domain name, which consists of the subnet's DNS label,
                  the VCN's DNS label, and the `oraclevcn.com` domain.
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
                - "Example: `subnet123.vcn1.oraclevcn.com`"
            returned: on success
            type: string
            sample: subnet123.vcn1.oraclevcn.com
        time_created:
            description:
                - The date and time the subnet was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The OCID of the VCN the subnet is in.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
        virtual_router_ip:
            description:
                - The IP address of the virtual router.
                - "Example: `10.0.14.1`"
            returned: on success
            type: string
            sample: 10.0.14.1
        virtual_router_mac:
            description:
                - The MAC address of the virtual router.
                - "Example: `00:00:00:00:00:01`"
            returned: on success
            type: string
            sample: 00:00:00:00:00:01
    sample: [{
        "availability_domain": "Uocm:PHX-AD-1",
        "cidr_block": "10.0.1.0/24",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "dhcp_options_id": "ocid1.dhcpoptions.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "dns_label": "subnet123",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "prohibit_public_ip_on_vnic": true,
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "security_list_ids": [],
        "subnet_domain_name": "subnet123.vcn1.oraclevcn.com",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "virtual_router_ip": "10.0.14.1",
        "virtual_router_mac": "00:00:00:00:00:01"
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


class SubnetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "subnet_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subnet, subnet_id=self.module.params.get("subnet_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "vcn_id",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_subnets,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SubnetFactsHelperCustom = get_custom_class("SubnetFactsHelperCustom")


class ResourceFactsHelper(SubnetFactsHelperCustom, SubnetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            subnet_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="subnet",
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

    module.exit_json(subnets=result)


if __name__ == "__main__":
    main()

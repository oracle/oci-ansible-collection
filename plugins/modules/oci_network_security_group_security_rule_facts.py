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
module: oci_network_security_group_security_rule_facts
short_description: Fetches details about one or multiple NetworkSecurityGroupSecurityRule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NetworkSecurityGroupSecurityRule resources in Oracle Cloud Infrastructure
    - Lists the security rules in the specified network security group.
version_added: "2.5"
options:
    network_security_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security group.
        type: str
        required: true
    direction:
        description:
            - Direction of the security rule. Set to `EGRESS` for rules that allow outbound IP packets,
              or `INGRESS` for rules that allow inbound IP packets.
        type: str
        choices:
            - "EGRESS"
            - "INGRESS"
    sort_by:
        description:
            - The field to sort by.
        type: str
        choices:
            - "TIMECREATED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List network_security_group_security_rules
  oci_network_security_group_security_rule_facts:
    network_security_group_id: ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
network_security_group_security_rules:
    description:
        - List of NetworkSecurityGroupSecurityRule resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - An optional description of your choice for the rule.
            returned: on success
            type: string
            sample: description_example
        destination:
            description:
                - Conceptually, this is the range of IP addresses that a packet originating from the instance
                  can go to.
                - "Allowed values:"
                - " * An IP address range in CIDR notation. For example: `192.168.1.0/24`"
                - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/), if you're
                      setting up a security rule for traffic destined for a particular `Service` through
                      a service gateway. For example: `oci-phx-objectstorage`."
                - " * The OCID of a L(NetworkSecurityGroup,https://docs.cloud.oracle.com/#/en/iaas/20160918/NetworkSecurityGroup/) in the same
                      VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
                      traffic between VNICs in the same NSG."
            returned: on success
            type: string
            sample: destination_example
        destination_type:
            description:
                - Type of destination for the rule. Required if `direction` = `EGRESS`.
                - "Allowed values:"
                - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation."
                - " * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                      L(Service,https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/) (the rule is for traffic destined for a
                      particular `Service` through a service gateway)."
                - " * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the OCID of a
                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/#/en/iaas/20160918/NetworkSecurityGroup/)."
            returned: on success
            type: string
            sample: CIDR_BLOCK
        direction:
            description:
                - Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.
            returned: on success
            type: string
            sample: EGRESS
        icmp_options:
            description:
                - "Optional and valid only for ICMP and ICMPv6. Use to specify a particular ICMP type and code
                  as defined in:
                  - L(ICMP Parameters,http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)
                  - L(ICMPv6 Parameters,https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml)"
                - "If you specify ICMP or ICMPv6 as the protocol but omit this object, then all ICMP types and
                  codes are allowed. If you do provide this object, the type is required and the code is optional.
                  To enable MTU negotiation for ingress internet traffic via IPv4, make sure to allow type 3 (\\"Destination
                  Unreachable\\") code 4 (\\"Fragmentation Needed and Don't Fragment was Set\\"). If you need to specify
                  multiple codes for a single type, create a separate security rule for each."
            returned: on success
            type: complex
            contains:
                code:
                    description:
                        - The ICMP code (optional).
                    returned: on success
                    type: int
                    sample: 56
                type:
                    description:
                        - The ICMP type.
                    returned: on success
                    type: int
                    sample: 56
        id:
            description:
                - An Oracle-assigned identifier for the security rule. You specify this ID when you want to
                  update or delete the rule.
                - "Example: `04ABEC`"
            returned: on success
            type: string
            sample: 04ABEC
        is_stateless:
            description:
                - A stateless rule allows traffic in one direction. Remember to add a corresponding
                  stateless rule in the other direction if you need to support bidirectional traffic. For
                  example, if egress traffic allows TCP destination port 80, there should be an ingress
                  rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
                  and a corresponding rule is not necessary for bidirectional traffic.
            returned: on success
            type: bool
            sample: true
        is_valid:
            description:
                - Whether the rule is valid. The value is `True` when the rule is first created. If
                  the rule's `source` or `destination` is a network security group, the value changes to
                  `False` if that network security group is deleted.
            returned: on success
            type: bool
            sample: true
        protocol:
            description:
                - "The transport protocol. Specify either `all` or an IPv4 protocol number as
                  defined in
                  L(Protocol Numbers,http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
                  Options are supported only for ICMP (\\"1\\"), TCP (\\"6\\"), UDP (\\"17\\"), and ICMPv6 (\\"58\\")."
            returned: on success
            type: string
            sample: protocol_example
        source:
            description:
                - Conceptually, this is the range of IP addresses that a packet coming into the instance
                  can come from.
                - "Allowed values:"
                - " * An IP address range in CIDR notation. For example: `192.168.1.0/24`"
                - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/), if you're
                      setting up a security rule for traffic coming from a particular `Service` through
                      a service gateway. For example: `oci-phx-objectstorage`."
                - " * The OCID of a L(NetworkSecurityGroup,https://docs.cloud.oracle.com/#/en/iaas/20160918/NetworkSecurityGroup/) in the same
                      VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
                      traffic between VNICs in the same NSG."
            returned: on success
            type: string
            sample: source_example
        source_type:
            description:
                - Type of source for the rule. Required if `direction` = `INGRESS`.
                - " * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation."
                - " * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
                      L(Service,https://docs.cloud.oracle.com/#/en/iaas/20160918/Service/) (the rule is for traffic coming from a
                      particular `Service` through a service gateway)."
                - " * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the OCID of a
                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/#/en/iaas/20160918/NetworkSecurityGroup/)."
            returned: on success
            type: string
            sample: CIDR_BLOCK
        tcp_options:
            description:
                - Optional and valid only for TCP. Use to specify particular destination ports for TCP rules.
                  If you specify TCP as the protocol but omit this object, then all destination ports are allowed.
            returned: on success
            type: complex
            contains:
                destination_port_range:
                    description:
                        - An inclusive range of allowed destination ports. Use the same number for the min and max
                          to indicate a single port. Defaults to all ports if not specified.
                    returned: on success
                    type: complex
                    contains:
                        max:
                            description:
                                - The maximum port number. Must not be lower than the minimum port number. To specify
                                  a single port number, set both the min and max to the same value.
                            returned: on success
                            type: int
                            sample: 56
                        min:
                            description:
                                - The minimum port number. Must not be greater than the maximum port number.
                            returned: on success
                            type: int
                            sample: 56
                source_port_range:
                    description:
                        - An inclusive range of allowed source ports. Use the same number for the min and max to
                          indicate a single port. Defaults to all ports if not specified.
                    returned: on success
                    type: complex
                    contains:
                        max:
                            description:
                                - The maximum port number. Must not be lower than the minimum port number. To specify
                                  a single port number, set both the min and max to the same value.
                            returned: on success
                            type: int
                            sample: 56
                        min:
                            description:
                                - The minimum port number. Must not be greater than the maximum port number.
                            returned: on success
                            type: int
                            sample: 56
        time_created:
            description:
                - The date and time the security rule was created. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        udp_options:
            description:
                - Optional and valid only for UDP. Use to specify particular destination ports for UDP rules.
                  If you specify UDP as the protocol but omit this object, then all destination ports are allowed.
            returned: on success
            type: complex
            contains:
                destination_port_range:
                    description:
                        - An inclusive range of allowed destination ports. Use the same number for the min and max
                          to indicate a single port. Defaults to all ports if not specified.
                    returned: on success
                    type: complex
                    contains:
                        max:
                            description:
                                - The maximum port number. Must not be lower than the minimum port number. To specify
                                  a single port number, set both the min and max to the same value.
                            returned: on success
                            type: int
                            sample: 56
                        min:
                            description:
                                - The minimum port number. Must not be greater than the maximum port number.
                            returned: on success
                            type: int
                            sample: 56
                source_port_range:
                    description:
                        - An inclusive range of allowed source ports. Use the same number for the min and max to
                          indicate a single port. Defaults to all ports if not specified.
                    returned: on success
                    type: complex
                    contains:
                        max:
                            description:
                                - The maximum port number. Must not be lower than the minimum port number. To specify
                                  a single port number, set both the min and max to the same value.
                            returned: on success
                            type: int
                            sample: 56
                        min:
                            description:
                                - The minimum port number. Must not be greater than the maximum port number.
                            returned: on success
                            type: int
                            sample: 56
    sample: [{
        "description": "description_example",
        "destination": "destination_example",
        "destination_type": "CIDR_BLOCK",
        "direction": "EGRESS",
        "icmp_options": {
            "code": 56,
            "type": 56
        },
        "id": "04ABEC",
        "is_stateless": true,
        "is_valid": true,
        "protocol": "protocol_example",
        "source": "source_example",
        "source_type": "CIDR_BLOCK",
        "tcp_options": {
            "destination_port_range": {
                "max": 56,
                "min": 56
            },
            "source_port_range": {
                "max": 56,
                "min": 56
            }
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "udp_options": {
            "destination_port_range": {
                "max": 56,
                "min": 56
            },
            "source_port_range": {
                "max": 56,
                "min": 56
            }
        }
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


class NetworkSecurityGroupSecurityRuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "network_security_group_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "direction",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_network_security_group_security_rules,
            network_security_group_id=self.module.params.get(
                "network_security_group_id"
            ),
            **optional_kwargs
        )


NetworkSecurityGroupSecurityRuleFactsHelperCustom = get_custom_class(
    "NetworkSecurityGroupSecurityRuleFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkSecurityGroupSecurityRuleFactsHelperCustom,
    NetworkSecurityGroupSecurityRuleFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_security_group_id=dict(type="str", required=True),
            direction=dict(type="str", choices=["EGRESS", "INGRESS"]),
            sort_by=dict(type="str", choices=["TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="network_security_group_security_rule",
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

    module.exit_json(network_security_group_security_rules=result)


if __name__ == "__main__":
    main()

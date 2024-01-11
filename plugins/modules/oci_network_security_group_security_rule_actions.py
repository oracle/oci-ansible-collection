#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_network_security_group_security_rule_actions
short_description: Perform actions on a NetworkSecurityGroupSecurityRule resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a NetworkSecurityGroupSecurityRule resource in Oracle Cloud Infrastructure
    - For I(action=add), adds one or more security rules to the specified network security group.
    - For I(action=remove), removes one or more security rules from the specified network security group.
    - For I(action=update), updates one or more security rules in the specified network security group.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    security_rule_ids:
        description:
            - The Oracle-assigned ID of each L(SecurityRule,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/SecurityRule/) to be deleted.
            - Applicable only for I(action=remove).
        type: list
        elements: str
    network_security_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security group.
        type: str
        aliases: ["id"]
        required: true
    security_rules:
        description:
            - The NSG security rules to add.
            - Applicable only for I(action=add)I(action=update).
        type: list
        elements: dict
        suboptions:
            description:
                description:
                    - An optional description of your choice for the rule. Avoid entering confidential information.
                type: str
            destination:
                description:
                    - Conceptually, this is the range of IP addresses that a packet originating from the instance
                      can go to.
                    - "Allowed values:"
                    - " * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                          IPv6 addressing is supported for all commercial and government regions. See
                          L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)."
                    - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                          setting up a security rule for traffic destined for a particular `Service` through
                          a service gateway. For example: `oci-phx-objectstorage`."
                    - " * The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a
                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/) in the same
                          VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
                          traffic between VNICs in the same NSG."
                type: str
            destination_type:
                description:
                    - Type of destination for the rule. Required if `direction` = `EGRESS`.
                    - "Allowed values:"
                    - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation."
                    - " * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                          L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                          particular `Service` through a service gateway)."
                    - " * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the
                      L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a
                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/)."
                type: str
                choices:
                    - "CIDR_BLOCK"
                    - "SERVICE_CIDR_BLOCK"
                    - "NETWORK_SECURITY_GROUP"
            direction:
                description:
                    - Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets,
                      or `INGRESS` for rules to allow inbound IP packets.
                type: str
                choices:
                    - "EGRESS"
                    - "INGRESS"
                required: true
            icmp_options:
                description:
                    - ""
                type: dict
                suboptions:
                    code:
                        description:
                            - The ICMP code (optional).
                        type: int
                    type:
                        description:
                            - The ICMP type.
                        type: int
                        required: true
            id:
                description:
                    - The Oracle-assigned ID of the security rule that you want to update. You can't change this value.
                    - "Example: `04ABEC`"
                type: str
            is_stateless:
                description:
                    - A stateless rule allows traffic in one direction. Remember to add a corresponding
                      stateless rule in the other direction if you need to support bidirectional traffic. For
                      example, if egress traffic allows TCP destination port 80, there should be an ingress
                      rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
                      and a corresponding rule is not necessary for bidirectional traffic.
                type: bool
            protocol:
                description:
                    - "The transport protocol. Specify either `all` or an IPv4 protocol number as
                      defined in
                      L(Protocol Numbers,http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
                      Options are supported only for ICMP (\\"1\\"), TCP (\\"6\\"), UDP (\\"17\\"), and ICMPv6 (\\"58\\")."
                type: str
                required: true
            source:
                description:
                    - Conceptually, this is the range of IP addresses that a packet coming into the instance
                      can come from.
                    - "Allowed values:"
                    - " * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                          IPv6 addressing is supported for all commercial and government regions. See
                          L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)."
                    - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                          setting up a security rule for traffic coming from a particular `Service` through
                          a service gateway. For example: `oci-phx-objectstorage`."
                    - " * The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a
                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/) in the same
                          VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
                          traffic between VNICs in the same NSG."
                type: str
            source_type:
                description:
                    - Type of source for the rule. Required if `direction` = `INGRESS`.
                    - " * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation."
                    - " * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
                          L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic coming from a
                          particular `Service` through a service gateway)."
                    - " * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the
                      L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a
                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/)."
                type: str
                choices:
                    - "CIDR_BLOCK"
                    - "SERVICE_CIDR_BLOCK"
                    - "NETWORK_SECURITY_GROUP"
            tcp_options:
                description:
                    - ""
                type: dict
                suboptions:
                    destination_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number, which must not be less than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number, which must not be greater than the maximum port number.
                                type: int
                                required: true
                    source_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number, which must not be less than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number, which must not be greater than the maximum port number.
                                type: int
                                required: true
            udp_options:
                description:
                    - ""
                type: dict
                suboptions:
                    destination_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number, which must not be less than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number, which must not be greater than the maximum port number.
                                type: int
                                required: true
                    source_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number, which must not be less than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number, which must not be greater than the maximum port number.
                                type: int
                                required: true
    action:
        description:
            - The action to perform on the NetworkSecurityGroupSecurityRule.
        type: str
        required: true
        choices:
            - "add"
            - "remove"
            - "update"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action add on network_security_group_security_rule
  oci_network_security_group_security_rule_actions:
    # required
    network_security_group_id: "ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: add

    # optional
    security_rules:
    - # required
      direction: EGRESS
      protocol: protocol_example

      # optional
      description: description_example
      destination: destination_example
      destination_type: CIDR_BLOCK
      icmp_options:
        # required
        type: 56

        # optional
        code: 56
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      is_stateless: true
      source: source_example
      source_type: CIDR_BLOCK
      tcp_options:
        # optional
        destination_port_range:
          # required
          max: 56
          min: 56
        source_port_range:
          # required
          max: 56
          min: 56
      udp_options:
        # optional
        destination_port_range:
          # required
          max: 56
          min: 56
        source_port_range:
          # required
          max: 56
          min: 56

- name: Perform action remove on network_security_group_security_rule
  oci_network_security_group_security_rule_actions:
    # required
    network_security_group_id: "ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove

    # optional
    security_rule_ids: [ "security_rule_ids_example" ]

- name: Perform action update on network_security_group_security_rule
  oci_network_security_group_security_rule_actions:
    # required
    network_security_group_id: "ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: update

    # optional
    security_rules:
    - # required
      direction: EGRESS
      protocol: protocol_example

      # optional
      description: description_example
      destination: destination_example
      destination_type: CIDR_BLOCK
      icmp_options:
        # required
        type: 56

        # optional
        code: 56
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      is_stateless: true
      source: source_example
      source_type: CIDR_BLOCK
      tcp_options:
        # optional
        destination_port_range:
          # required
          max: 56
          min: 56
        source_port_range:
          # required
          max: 56
          min: 56
      udp_options:
        # optional
        destination_port_range:
          # required
          max: 56
          min: 56
        source_port_range:
          # required
          max: 56
          min: 56

"""

RETURN = """
network_security_group_security_rule:
    description:
        - Details of the NetworkSecurityGroupSecurityRule resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        security_rules:
            description:
                - The NSG security rules that were added.
            returned: on success
            type: complex
            contains:
                description:
                    description:
                        - An optional description of your choice for the rule.
                    returned: on success
                    type: str
                    sample: description_example
                destination:
                    description:
                        - Conceptually, this is the range of IP addresses that a packet originating from the instance
                          can go to.
                        - "Allowed values:"
                        - " * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                              IPv6 addressing is supported for all commercial and government regions.
                              See L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)."
                        - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                              setting up a security rule for traffic destined for a particular `Service` through
                              a service gateway. For example: `oci-phx-objectstorage`."
                        - " * The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a
                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/) in the same
                              VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
                              traffic between VNICs in the same NSG."
                    returned: on success
                    type: str
                    sample: destination_example
                destination_type:
                    description:
                        - Type of destination for the rule. Required if `direction` = `EGRESS`.
                        - "Allowed values:"
                        - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation."
                        - " * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                              L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                              particular `Service` through a service gateway)."
                        - " * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the
                          L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a
                              L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/)."
                    returned: on success
                    type: str
                    sample: CIDR_BLOCK
                direction:
                    description:
                        - Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets,
                          or `INGRESS` for rules to allow inbound IP packets.
                    returned: on success
                    type: str
                    sample: EGRESS
                icmp_options:
                    description:
                        - ""
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
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
                    type: str
                    sample: protocol_example
                source:
                    description:
                        - Conceptually, this is the range of IP addresses that a packet coming into the instance
                          can come from.
                        - "Allowed values:"
                        - " * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                              IPv6 addressing is supported for all commercial and government regions.
                              See L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)."
                        - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                              setting up a security rule for traffic coming from a particular `Service` through
                              a service gateway. For example: `oci-phx-objectstorage`."
                        - " * The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a
                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/) in the same
                              VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
                              traffic between VNICs in the same NSG."
                    returned: on success
                    type: str
                    sample: source_example
                source_type:
                    description:
                        - Type of source for the rule. Required if `direction` = `INGRESS`.
                        - " * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation."
                        - " * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
                              L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic coming from a
                              particular `Service` through a service gateway)."
                        - " * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the
                          L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a
                              L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/)."
                    returned: on success
                    type: str
                    sample: CIDR_BLOCK
                tcp_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        destination_port_range:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                max:
                                    description:
                                        - The maximum port number, which must not be less than the minimum port number. To specify
                                          a single port number, set both the min and max to the same value.
                                    returned: on success
                                    type: int
                                    sample: 56
                                min:
                                    description:
                                        - The minimum port number, which must not be greater than the maximum port number.
                                    returned: on success
                                    type: int
                                    sample: 56
                        source_port_range:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                max:
                                    description:
                                        - The maximum port number, which must not be less than the minimum port number. To specify
                                          a single port number, set both the min and max to the same value.
                                    returned: on success
                                    type: int
                                    sample: 56
                                min:
                                    description:
                                        - The minimum port number, which must not be greater than the maximum port number.
                                    returned: on success
                                    type: int
                                    sample: 56
                time_created:
                    description:
                        - The date and time the security rule was created. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                udp_options:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        destination_port_range:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                max:
                                    description:
                                        - The maximum port number, which must not be less than the minimum port number. To specify
                                          a single port number, set both the min and max to the same value.
                                    returned: on success
                                    type: int
                                    sample: 56
                                min:
                                    description:
                                        - The minimum port number, which must not be greater than the maximum port number.
                                    returned: on success
                                    type: int
                                    sample: 56
                        source_port_range:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                max:
                                    description:
                                        - The maximum port number, which must not be less than the minimum port number. To specify
                                          a single port number, set both the min and max to the same value.
                                    returned: on success
                                    type: int
                                    sample: 56
                                min:
                                    description:
                                        - The minimum port number, which must not be greater than the maximum port number.
                                    returned: on success
                                    type: int
                                    sample: 56
    sample: {
        "security_rules": [{
            "description": "description_example",
            "destination": "destination_example",
            "destination_type": "CIDR_BLOCK",
            "direction": "EGRESS",
            "icmp_options": {
                "code": 56,
                "type": 56
            },
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
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
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import AddNetworkSecurityGroupSecurityRulesDetails
    from oci.core.models import RemoveNetworkSecurityGroupSecurityRulesDetails
    from oci.core.models import UpdateNetworkSecurityGroupSecurityRulesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkSecurityGroupSecurityRuleActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add
        remove
        update
    """

    @staticmethod
    def get_module_resource_id_param():
        return "network_security_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("network_security_group_id")

    def add(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddNetworkSecurityGroupSecurityRulesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_network_security_group_security_rules,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_security_group_id=self.module.params.get(
                    "network_security_group_id"
                ),
                add_network_security_group_security_rules_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def remove(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveNetworkSecurityGroupSecurityRulesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_network_security_group_security_rules,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_security_group_id=self.module.params.get(
                    "network_security_group_id"
                ),
                remove_network_security_group_security_rules_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def update(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateNetworkSecurityGroupSecurityRulesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_network_security_group_security_rules,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_security_group_id=self.module.params.get(
                    "network_security_group_id"
                ),
                update_network_security_group_security_rules_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


NetworkSecurityGroupSecurityRuleActionsHelperCustom = get_custom_class(
    "NetworkSecurityGroupSecurityRuleActionsHelperCustom"
)


class ResourceHelper(
    NetworkSecurityGroupSecurityRuleActionsHelperCustom,
    NetworkSecurityGroupSecurityRuleActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            security_rule_ids=dict(type="list", elements="str"),
            network_security_group_id=dict(aliases=["id"], type="str", required=True),
            security_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    description=dict(type="str"),
                    destination=dict(type="str"),
                    destination_type=dict(
                        type="str",
                        choices=[
                            "CIDR_BLOCK",
                            "SERVICE_CIDR_BLOCK",
                            "NETWORK_SECURITY_GROUP",
                        ],
                    ),
                    direction=dict(
                        type="str", required=True, choices=["EGRESS", "INGRESS"]
                    ),
                    icmp_options=dict(
                        type="dict",
                        options=dict(
                            code=dict(type="int"), type=dict(type="int", required=True)
                        ),
                    ),
                    id=dict(type="str"),
                    is_stateless=dict(type="bool"),
                    protocol=dict(type="str", required=True),
                    source=dict(type="str"),
                    source_type=dict(
                        type="str",
                        choices=[
                            "CIDR_BLOCK",
                            "SERVICE_CIDR_BLOCK",
                            "NETWORK_SECURITY_GROUP",
                        ],
                    ),
                    tcp_options=dict(
                        type="dict",
                        options=dict(
                            destination_port_range=dict(
                                type="dict",
                                options=dict(
                                    max=dict(type="int", required=True),
                                    min=dict(type="int", required=True),
                                ),
                            ),
                            source_port_range=dict(
                                type="dict",
                                options=dict(
                                    max=dict(type="int", required=True),
                                    min=dict(type="int", required=True),
                                ),
                            ),
                        ),
                    ),
                    udp_options=dict(
                        type="dict",
                        options=dict(
                            destination_port_range=dict(
                                type="dict",
                                options=dict(
                                    max=dict(type="int", required=True),
                                    min=dict(type="int", required=True),
                                ),
                            ),
                            source_port_range=dict(
                                type="dict",
                                options=dict(
                                    max=dict(type="int", required=True),
                                    min=dict(type="int", required=True),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            action=dict(type="str", required=True, choices=["add", "remove", "update"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="network_security_group_security_rule",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

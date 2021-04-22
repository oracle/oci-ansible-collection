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
module: oci_network_security_list_facts
short_description: Fetches details about one or multiple SecurityList resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SecurityList resources in Oracle Cloud Infrastructure
    - Lists the security lists in the specified VCN and compartment.
      If the VCN ID is not provided, then the list includes the security lists from all VCNs in the specified compartment.
    - If I(security_list_id) is specified, the details of a single SecurityList will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    security_list_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the security list.
            - Required to get a specific security_list.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple security_lists.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
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
            - A filter to only return resources that match the given lifecycle
              state. The state value is case-insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "TERMINATING"
            - "TERMINATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List security_lists
  oci_network_security_list_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific security_list
  oci_network_security_list_facts:
    security_list_id: "ocid1.securitylist.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
security_lists:
    description:
        - List of SecurityList resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the security list.
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
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        egress_security_rules:
            description:
                - Rules for allowing egress IP packets.
            returned: on success
            type: complex
            contains:
                destination:
                    description:
                        - Conceptually, this is the range of IP addresses that a packet originating from the instance
                          can go to.
                        - "Allowed values:"
                        - " * IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
                              Note that IPv6 addressing is currently supported only in certain regions. See
                              L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)."
                        - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                              setting up a security list rule for traffic destined for a particular `Service` through
                              a service gateway. For example: `oci-phx-objectstorage`."
                    returned: on success
                    type: string
                    sample: destination_example
                destination_type:
                    description:
                        - Type of destination for the rule. The default is `CIDR_BLOCK`.
                        - "Allowed values:"
                        - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation."
                        - " * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                              L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                              particular `Service` through a service gateway)."
                    returned: on success
                    type: string
                    sample: CIDR_BLOCK
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
                protocol:
                    description:
                        - "The transport protocol. Specify either `all` or an IPv4 protocol number as
                          defined in
                          L(Protocol Numbers,http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
                          Options are supported only for ICMP (\\"1\\"), TCP (\\"6\\"), UDP (\\"17\\"), and ICMPv6 (\\"58\\")."
                    returned: on success
                    type: string
                    sample: protocol_example
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
                description:
                    description:
                        - An optional description of your choice for the rule.
                    returned: on success
                    type: string
                    sample: description_example
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
                - The security list's Oracle Cloud ID (OCID).
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ingress_security_rules:
            description:
                - Rules for allowing ingress IP packets.
            returned: on success
            type: complex
            contains:
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
                is_stateless:
                    description:
                        - A stateless rule allows traffic in one direction. Remember to add a corresponding
                          stateless rule in the other direction if you need to support bidirectional traffic. For
                          example, if ingress traffic allows TCP destination port 80, there should be an egress
                          rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
                          and a corresponding rule is not necessary for bidirectional traffic.
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
                        - " * IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
                              IPv6 addressing is supported for all commercial and government regions. See
                              L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)."
                        - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                              setting up a security list rule for traffic coming from a particular `Service` through
                              a service gateway. For example: `oci-phx-objectstorage`."
                    returned: on success
                    type: string
                    sample: source_example
                source_type:
                    description:
                        - Type of source for the rule. The default is `CIDR_BLOCK`.
                        - " * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation."
                        - " * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
                              L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic coming from a
                              particular `Service` through a service gateway)."
                    returned: on success
                    type: string
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
                description:
                    description:
                        - An optional description of your choice for the rule.
                    returned: on success
                    type: string
                    sample: description_example
        lifecycle_state:
            description:
                - The security list's current state.
            returned: on success
            type: string
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the security list was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The OCID of the VCN the security list belongs to.
            returned: on success
            type: string
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "egress_security_rules": [{
            "destination": "destination_example",
            "destination_type": "CIDR_BLOCK",
            "icmp_options": {
                "code": 56,
                "type": 56
            },
            "is_stateless": true,
            "protocol": "protocol_example",
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
            "udp_options": {
                "destination_port_range": {
                    "max": 56,
                    "min": 56
                },
                "source_port_range": {
                    "max": 56,
                    "min": 56
                }
            },
            "description": "description_example"
        }],
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ingress_security_rules": [{
            "icmp_options": {
                "code": 56,
                "type": 56
            },
            "is_stateless": true,
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
            "udp_options": {
                "destination_port_range": {
                    "max": 56,
                    "min": 56
                },
                "source_port_range": {
                    "max": 56,
                    "min": 56
                }
            },
            "description": "description_example"
        }],
        "lifecycle_state": "PROVISIONING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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


class SecurityListFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "security_list_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_security_list,
            security_list_id=self.module.params.get("security_list_id"),
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
            self.client.list_security_lists,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SecurityListFactsHelperCustom = get_custom_class("SecurityListFactsHelperCustom")


class ResourceFactsHelper(SecurityListFactsHelperCustom, SecurityListFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            security_list_id=dict(aliases=["id"], type="str"),
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
        resource_type="security_list",
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

    module.exit_json(security_lists=result)


if __name__ == "__main__":
    main()

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
module: oci_network_security_list
short_description: Manage a SecurityList resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a SecurityList resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new security list for the specified VCN. For more information
      about security lists, see L(Security Lists,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securitylists.htm).
      For information on the number of rules you can have in a security list, see
      L(Service Limits,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).
    - For the purposes of access control, you must provide the OCID of the compartment where you want the security
      list to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets,
      or other Networking Service components. If you're not sure which compartment to use, put the security
      list in the same compartment as the VCN. For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the security list, otherwise a default is provided.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to contain the security list.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    egress_security_rules:
        description:
            - Rules for allowing egress IP packets.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        suboptions:
            destination:
                description:
                    - Conceptually, this is the range of IP addresses that a packet originating from the instance
                      can go to.
                    - "Allowed values:"
                    - " * IP address range in CIDR notation. For example: `192.168.1.0/24`"
                    - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                          setting up a security list rule for traffic destined for a particular `Service` through
                          a service gateway. For example: `oci-phx-objectstorage`."
                type: str
                required: true
            destination_type:
                description:
                    - Type of destination for the rule. The default is `CIDR_BLOCK`.
                    - "Allowed values:"
                    - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation."
                    - " * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                          L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                          particular `Service` through a service gateway)."
                type: str
                choices:
                    - "CIDR_BLOCK"
                    - "SERVICE_CIDR_BLOCK"
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
                      Options are supported only for ICMP (\\"1\\"), TCP (\\"6\\"), and UDP (\\"17\\")."
                type: str
                required: true
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
                                    - The maximum port number. Must not be lower than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number. Must not be greater than the maximum port number.
                                type: int
                                required: true
                    source_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number. Must not be lower than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number. Must not be greater than the maximum port number.
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
                                    - The maximum port number. Must not be lower than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number. Must not be greater than the maximum port number.
                                type: int
                                required: true
                    source_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number. Must not be lower than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number. Must not be greater than the maximum port number.
                                type: int
                                required: true
            description:
                description:
                    - An optional description of your choice for the rule.
                type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    ingress_security_rules:
        description:
            - Rules for allowing ingress IP packets.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        suboptions:
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
            is_stateless:
                description:
                    - A stateless rule allows traffic in one direction. Remember to add a corresponding
                      stateless rule in the other direction if you need to support bidirectional traffic. For
                      example, if ingress traffic allows TCP destination port 80, there should be an egress
                      rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
                      and a corresponding rule is not necessary for bidirectional traffic.
                type: bool
            protocol:
                description:
                    - "The transport protocol. Specify either `all` or an IPv4 protocol number as
                      defined in
                      L(Protocol Numbers,http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
                      Options are supported only for ICMP (\\"1\\"), TCP (\\"6\\"), and UDP (\\"17\\")."
                type: str
                required: true
            source:
                description:
                    - Conceptually, this is the range of IP addresses that a packet coming into the instance
                      can come from.
                    - "Allowed values:"
                    - " * IP address range in CIDR notation. For example: `192.168.1.0/24`"
                    - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                          setting up a security list rule for traffic coming from a particular `Service` through
                          a service gateway. For example: `oci-phx-objectstorage`."
                type: str
                required: true
            source_type:
                description:
                    - Type of source for the rule. The default is `CIDR_BLOCK`.
                    - " * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation."
                    - " * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
                          L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic coming from a
                          particular `Service` through a service gateway)."
                type: str
                choices:
                    - "CIDR_BLOCK"
                    - "SERVICE_CIDR_BLOCK"
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
                                    - The maximum port number. Must not be lower than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number. Must not be greater than the maximum port number.
                                type: int
                                required: true
                    source_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number. Must not be lower than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number. Must not be greater than the maximum port number.
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
                                    - The maximum port number. Must not be lower than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number. Must not be greater than the maximum port number.
                                type: int
                                required: true
                    source_port_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            max:
                                description:
                                    - The maximum port number. Must not be lower than the minimum port number. To specify
                                      a single port number, set both the min and max to the same value.
                                type: int
                                required: true
                            min:
                                description:
                                    - The minimum port number. Must not be greater than the maximum port number.
                                type: int
                                required: true
            description:
                description:
                    - An optional description of your choice for the rule.
                type: str
    vcn_id:
        description:
            - The OCID of the VCN the security list belongs to.
            - Required for create using I(state=present).
        type: str
    security_list_id:
        description:
            - The OCID of the security list.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    purge_security_rules:
        description:
            - Purge security rules  from security list which are not present in the provided group security list.
              If I(purge_security_rules=no), provided security rules would be appended to existing security
              rules. I(purge_security_rules) and I(delete_security_rules) are mutually exclusive.
            - This parameter is updatable.
        type: bool
        default: "true"
    delete_security_rules:
        description:
            - Delete security rules from existing security list which are present in the
              security rules provided by I(ingress_security_rules) and/or I(egress_security_rules).
              If I(delete_security_rules=yes), security rules provided by I(ingress_security_rules)
              and/or I(egress_security_rules) would be deleted to existing security list, if they
              are part of existing security list. If they are not part of existing security list,
              they will be ignored. I(purge_security_rules) and I(delete_security_rules) are mutually
              exclusive.
            - This parameter is updatable.
        type: bool
        default: "false"
    state:
        description:
            - The state of the SecurityList.
            - Use I(state=present) to create or update a SecurityList.
            - Use I(state=absent) to delete a SecurityList.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create security_list
  oci_network_security_list:
    vcn_id: ocid1.vcn.oc1.phx.unique_ID
    display_name: MyPrivateSubnetSecurityList
    ingress_security_rules:
    - protocol: 6
      source: 10.0.1.0/24
      tcp_options:
        destination_port_range:
          min: 1521
          max: 1521
    - protocol: 6
      source: 10.0.2.0/24
      tcp_options:
        destination_port_range:
          min: 1521
          max: 1521
    egress_security_rules:
    - protocol: 6
      destination: 10.0.2.0/24
      tcp_options:
        destination_port_range:
          min: 1521
          max: 1521
    compartment_id: ocid1.compartment.oc1..unique_ID

- name: Update security_list using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_security_list:
    compartment_id: ocid1.compartment.oc1..unique_ID
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: MyPrivateSubnetSecurityList
    egress_security_rules:
    - destination: 10.0.2.0/24
      protocol: 6
    freeform_tags: {'Department': 'Finance'}
    ingress_security_rules:
    - protocol: 6
      source: 10.0.1.0/24
    purge_security_rules: false
    delete_security_rules: true

- name: Update security_list
  oci_network_security_list:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: MyPrivateSubnetSecurityList
    security_list_id: ocid1.securitylist.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete security_list
  oci_network_security_list:
    security_list_id: ocid1.securitylist.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete security_list using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_security_list:
    compartment_id: ocid1.compartment.oc1..unique_ID
    display_name: MyPrivateSubnetSecurityList
    state: absent

"""

RETURN = """
security_list:
    description:
        - Details of the SecurityList resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the security list.
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
                        - " * IP address range in CIDR notation. For example: `192.168.1.0/24`"
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
                          Options are supported only for ICMP (\\"1\\"), TCP (\\"6\\"), and UDP (\\"17\\")."
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
                                - ""
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
                                - ""
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
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The security list's Oracle Cloud ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
                          Options are supported only for ICMP (\\"1\\"), TCP (\\"6\\"), and UDP (\\"17\\")."
                    returned: on success
                    type: string
                    sample: protocol_example
                source:
                    description:
                        - Conceptually, this is the range of IP addresses that a packet coming into the instance
                          can come from.
                        - "Allowed values:"
                        - " * IP address range in CIDR notation. For example: `192.168.1.0/24`"
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
                                - ""
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
                                - ""
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
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateSecurityListDetails
    from oci.core.models import UpdateSecurityListDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecurityListHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "security_list_id"

    def get_module_resource_id(self):
        return self.module.params.get("security_list_id")

    def get_get_fn(self):
        return self.client.get_security_list

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_security_list,
            security_list_id=self.module.params.get("security_list_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["vcn_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_security_lists, **kwargs
        )

    def get_create_model_class(self):
        return CreateSecurityListDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_security_list,
            call_fn_args=(),
            call_fn_kwargs=dict(create_security_list_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateSecurityListDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_security_list,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_list_id=self.module.params.get("security_list_id"),
                update_security_list_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_security_list,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_list_id=self.module.params.get("security_list_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


SecurityListHelperCustom = get_custom_class("SecurityListHelperCustom")


class ResourceHelper(SecurityListHelperCustom, SecurityListHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            egress_security_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    destination=dict(type="str", required=True),
                    destination_type=dict(
                        type="str", choices=["CIDR_BLOCK", "SERVICE_CIDR_BLOCK"]
                    ),
                    icmp_options=dict(
                        type="dict",
                        options=dict(
                            code=dict(type="int"), type=dict(type="int", required=True)
                        ),
                    ),
                    is_stateless=dict(type="bool"),
                    protocol=dict(type="str", required=True),
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
                    description=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            ingress_security_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    icmp_options=dict(
                        type="dict",
                        options=dict(
                            code=dict(type="int"), type=dict(type="int", required=True)
                        ),
                    ),
                    is_stateless=dict(type="bool"),
                    protocol=dict(type="str", required=True),
                    source=dict(type="str", required=True),
                    source_type=dict(
                        type="str", choices=["CIDR_BLOCK", "SERVICE_CIDR_BLOCK"]
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
                    description=dict(type="str"),
                ),
            ),
            vcn_id=dict(type="str"),
            security_list_id=dict(aliases=["id"], type="str"),
            purge_security_rules=dict(type="bool", default="true"),
            delete_security_rules=dict(type="bool", default="false"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="security_list",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

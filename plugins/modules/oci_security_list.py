#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_security_list
short_description: Create,update and delete OCI Security List
description:
    - Creates OCI Security List
    - Update OCI Security List, if present, with a new display name
    - Update OCI Security List, if present, with ingress/egress security rules
    - Delete OCI Security List, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this security List would be created. Mandatory for create
                     operation.Optional for delete and update. Mutually exclusive with I(security_list_id).
        required: false
    vcn_id:
        description: Identifier of the Virtual Cloud Network to which the security List should be attached. Mandatory
                     for create operation. Optional for delete and update. Mutually exclusive with I(security_list_id).
        required: false
    security_list_id:
        description: Identifier of the Security List. Mandatory for delete and update.
        required: false
        aliases: ['id']
    display_name:
        description: Name of the Security List. A user friendly name. Does not have to be unique, and could be changed.
                     If not specified, a default name would be provided.
        required: false
        aliases: ['name']
    state:
        description: Create,update or delete Security List. For I(state=present), if it does not exists, it gets
                     created. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
    ingress_security_rules:
        description: Rules for allowing ingress IP packets. Required for create operation.
        required: false
        suboptions:
            source:
                description: The source CIDR block for the ingress rule. This is the range of IP addresses that a packet
                             coming into the instance can come from. Allowed values are either IP address range in CIDR
                             notation. For example 192.168.1.0/24 or the cidrBlock value for a Service, if you're
                             setting up a security list rule for traffic coming from a particular service through a
                             service gateway. For example oci-phx-objectstorage
                required: true
            source_type:
                description: Type of source for the rule. If the rule's source is an IP address range
                             in CIDR notation, then the value should be CIDR_BLOCK.  If the rule's source is
                             the cidr block value for a Service, then the value is SERVICE_CIDR_BLOCK.
                required: false
                choices: ['CIDR_BLOCK', 'SERVICE_CIDR_BLOCK']
                default: 'CIDR_BLOCK'
            icmp_options:
                description: Valid only for ICMP. Use to specify a particular ICMP type and code as defined in
                             U(u'https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml').
                             If you specify ICMP as the protocol but omit this object, then all ICMP types
                             and codes are allowed. If you do provide this object, the type is
                             required and the code is optional. To enable MTU negotiation for
                             ingress internet traffic, make sure to allow type 3 Destination Unreachable
                             code 4 Fragmentation Needed and Do not Fragment was Set. If you need to specify
                             multiple codes for a single type, create a separate security list rule for each.
                required: false
            is_stateless:
                description: A stateless rule allows traffic in one direction. Remember to add a
                             corresponding stateless rule in the other direction if you need to support bidirectional
                             traffic. For example, if ingress traffic allows TCP destination port 80, there should be
                             an egress rule to allow TCP source port 80. Defaults to false, which means the rule is
                             stateful and a corresponding rule is not necessary for bidirectional traffic.
                required: false
                default: 'no'
                choices: ['yes','no']
            protocol:
                description: Specify either all or an IPv4 protocol number as defined in
                             U(u'https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml')
                             Options are supported only for ICMP 1, TCP 6, and UDP 17.
                required: true
                choices: ['1', '6', '17']
            tcp_options:
                description: Valid only for TCP. Use to specify particular destination ports for TCP rules.
                            If TCP specified as the protocol but omit this object, then all destination ports
                            are allowed.
                required: no
                suboptions:
                    destination_port_range:
                        description: The destination port range for the ingress rule.
                                     Intger values for min port number and max port number should be provided.
                    source_port_range:
                        description: The source port range for the ingress rule.
                                     Intger values for min port number and max port number should be provided.
            udp_options:
                description: Valid only for UDP. Use to specify particular destination ports for UDP rules.
                             If UDP specified as the protocol but omit this object, then all destination ports
                             are allowed.
                required: no
    egress_security_rules:
        description: Rules for allowing egress IP packets. Required for create operation.
        required: false
        suboptions:
            destination:
                description: The destination CIDR block for the egress rule. This is the range of IP addresses
                             that a packet originating from the instance can go to. Allowed values are either IP
                             address range in CIDR notation. For example 192.168.1.0/24 or the cidrBlock value for a
                             Service, if you're setting up a security list rule for traffic going to a particular
                             service through a service gateway. For example oci-phx-objectstorage
                required: true
            destination_type:
                description: Type of destination for the rule. If the rule's destination is an IP address range
                             in CIDR notation, then the value should be CIDR_BLOCK.  If the rule's destination is
                             the cidr block value for a Service, then the value is SERVICE_CIDR_BLOCK.
                required: false
                choices: ['CIDR_BLOCK', 'SERVICE_CIDR_BLOCK']
                default: 'CIDR_BLOCK'
            icmp_options:
                description: Valid only for ICMP. Use to specify a particular ICMP type and code as defined in
                             U(u'https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml').
                             If you specify ICMP as the protocol but omit this object, then all ICMP types
                             and codes are allowed. If you do provide this object, the type is
                             required and the code is optional. To enable MTU negotiation for
                             ingress internet traffic, make sure to allow type 3 Destination Unreachable
                             code 4 Fragmentation Needed and Do not Fragment was Set. If you need to specify
                             multiple codes for a single type, create a separate security list rule for each.
                required: false
            is_stateless:
                description: A stateless rule allows traffic in one direction. Remember to add a
                             corresponding stateless rule in the other direction if you need to support
                             bidirectional traffic. For example, if egress traffic allows TCP destination
                             port 80, there should be an ingress rule to allow TCP source port 80.
                             Defaults to false, which means the rule is stateful and a corresponding rule
                             is not necessary for bidirectional traffic.
                required: false
                default: 'no'
                choices: ['yes','no']
            protocol:
                description: Specify either all or an IPv4 protocol number as defined in
                             U(u'https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml')
                             Options are supported only for ICMP 1, TCP 6, and UDP 17.
                required: true
                choices: ['1', '6', '17']
            tcp_options:
                description: Valid only for TCP. Use to specify particular destination ports for TCP rules.
                             If TCP specified as the protocol but omit this object, then all destination ports
                             are allowed.
                required: no
                suboptions:
                    destination_port_range:
                        description: The destination port range for the egress rule.
                                     Intger values for min port number and max port number should be provided.
                    source_port_range:
                        description: The source port range for the egress rule.
                                     Intger values for min port number and max port number should be provided.
            udp_options:
                description: Valid only for UDP. Use to specify particular destination ports for UDP rules.
                             If UDP specified as the protocol but omit this object, then all destination ports
                             are allowed.
                required: no
    purge_security_rules:
        description: Purge security rules  from security list which are not present in the provided group security list.
                     If I(purge_security_rules=no), provided security rules would be appended to existing security
                     rules. I(purge_security_rules) and I(delete_security_rules) are mutually exclusive.
        required: false
        default: 'yes'
        type: bool
    delete_security_rules:
        description: Delete security rules from existing security list which are present in the
                     security rules provided by I(ingress_security_rules) and/or I(egress_security_rules).
                     If I(delete_security_rules=yes), security rules provided by I(ingress_security_rules)
                     and/or I(egress_security_rules) would be deleted to existing security list, if they
                     are part of existing security list. If they are not part of existing security list,
                     they will be ignored. I(purge_security_rules) and I(delete_security_rules) are mutually
                     exclusive.
        required: false
        default: 'no'
        type: bool
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create/update Security List
- name: Create a security list with rules
  oci_security_list:
    name: 'ansible_sec_list'
    compartment_id: 'ocid.compartment..xxxxxEXAMPLExxxxx'
    vcn_id: 'ocid1.vcn..xxxxxEXAMPLExxxxx'
    state: 'present'
    freeform_tags:
        region: 'east'
    defined_tags:
        features:
            capacity: 'medium'
    ingress_security_rules:
      - source: '0.0.0.0/0'
        is_stateless: False
        protocol: '6'
        tcp_options:
            destination_port_range:
                min: 22
                max: 22
      - source: 'oci-iad-objectstorage'
        source_type: 'SERVICE_CIDR_BLOCK'
        is_stateless: False
        protocol: '6'
      - source: '0.0.0.0/0'
        is_stateless: False
        protocol: '1'
        icmp_options:
            code: 4
            type: 3
    egress_security_rules:
        - destination: '0.0.0.0/0'
          protocol: 'all'

- name: Update a security list by purging existing ingress rules
  oci_security_list:
    security_list_id: 'ocid1.securitylist.xxxxxEXAMPLExxxxx'
    ingress_security_rules:
        - source: '10.0.0.0/8'
          is_stateless: False
          protocol: '6'
          tcp_options:
              destination_port_range:
                 min: 25
                 max: 30
    purge_security_rules: 'yes'
    state: 'present'

- name: Update a security list by deleting existing ingress rules
  oci_security_list:
    security_list_id: 'ocid1.securitylist.xxxxxEXAMPLExxxxx'
    ingress_security_rules:
        - source: '10.0.0.0/8'
          is_stateless: False
          protocol: '6'
          tcp_options:
              destination_port_range:
                 min: 25
                 max: 30
    delete_security_rules: 'yes'
    state: 'present'

# Delete a security list
- name: Delete a security list
  oci_security_list:
    id: 'ocid1.securitylist.xxxxxEXAMPLExxxxx'
    state: 'absent'
"""

RETURN = """
    security_list:
        description: Attributes of the created/updated Security List.
                    For delete, deleted Security List description will
                    be returned.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Security List
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            display_name:
                description: Name assigned to the Security List during creation
                returned: always
                type: string
                sample: ansible_security_list
            id:
                description: Identifier of the Security List
                returned: always
                type: string
                sample: ocid1.securitylist.oc1.axdf
            vcn_id:
                description: Identifier of the Virtual Cloud Network to which the
                             Security List is attached.
                returned: always
                type: string
                sample: ocid1.vcn..ixcd
            lifecycle_state:
                description: The current state of the Security List
                returned: always
                type: string
                sample: AVAILABLE
            ingress_security_rules:
                description: Rules for allowing ingress IP packets
                returned: always
                type: list
                sample: [{"icmp_options": null,"is_stateless": null,"protocol": "6",
                "source": "0.0.0.0/0","source_type": "CIDR_BLOCK",tcp_options": {"destination_port_range":
                {"max": 22,"min": 22},"source_port_range": null},"udp_options": null}]
            egress_security_rules:
                description: Rules for allowing egress IP packets
                returned: always
                type: list
                sample:   [{"destination": "0.0.0.0/0","destination_type": "CIDR_BLOCK","icmp_options": null,
                "is_stateless": null,"protocol": "all","tcp_options": null,
                "udp_options": null}]
            time_created:
                description: Date and time when the Security List was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
        sample: {
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "freeform_tags":{"region":"east"},
                    "defined_tags":{"features":{"capacity":"medium"}},
                    "display_name":"ansible_security_list_one",
                    "egress_security_rules":[
                                                {
                                                    "destination":"0.0.0.0/0",
                                                    "destination_type":"CIDR_BLOCK",
                                                    "icmp_options":null,
                                                    "is_stateless":null,
                                                    "protocol":"all",
                                                    "tcp_options":null,
                                                    "udp_options":null
                                                  }
                                                ],
                    "id":"ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx",
                    "ingress_security_rules":[
                                                {
                                                    "icmp_options":null,
                                                    "is_stateless":false,
                                                    "protocol":"6",
                                                    "source":"0.0.0.0/0",
                                                    "source_type":"CIDR_BLOCK",
                                                    "tcp_options":{
                                                        "destination_port_range":{
                                                                                "max":22,
                                                                                "min":22
                                                                                },
                                                        "source_port_range":null
                                                    },
                                                    "udp_options":null
                                                },
                                                {
                                                    "icmp_options":{
                                                        "code":4,
                                                        "type":3
                                                    },
                                                    "is_stateless":false,
                                                    "protocol":"1",
                                                    "source":"0.0.0.0/0",
                                                    "source_type":"CIDR_BLOCK",
                                                    "tcp_options":null,
                                                    "udp_options":null
                                                },
                                                {
                                                    "icmp_options":{
                                                        "code":null,
                                                        "type":3
                                                    },
                                                    "is_stateless":false,
                                                    "protocol":"1",
                                                    "source":"oci-iad-objectstorage",
                                                    "source_type":"SERVICE_CIDR_BLOCK",
                                                    "tcp_options":null,
                                                    "udp_options":null
                                                }
                                            ],
                    "lifecycle_state":"AVAILABLE",
                    "time_created":"2017-11-24T05:33:44.779000+00:00",
                    "vcn_id":"ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded, ClientError
    from oci.util import to_dict
    from oci.core.models import (
        CreateSecurityListDetails,
        UpdateSecurityListDetails,
        IngressSecurityRule,
        EgressSecurityRule,
        IcmpOptions,
        TcpOptions,
        UdpOptions,
        PortRange,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_security_list(virtual_network_client, module):
    result = dict(changed=False, security_list="")
    security_list_id = module.params.get("security_list_id")
    exclude_attributes = {"display_name": True}
    default_attribute_values = {
        "egress_security_rules": {"is_stateless": False},
        "ingress_security_rules": {"is_stateless": False},
    }
    try:
        if security_list_id:
            existing_security_list = oci_utils.get_existing_resource(
                virtual_network_client.get_security_list,
                module,
                security_list_id=security_list_id,
            )
            result = update_security_list(
                virtual_network_client, existing_security_list, module
            )
        else:
            # ingress_security_rules and egress_security_rules are required for create operation
            if (
                module.params.get("ingress_security_rules") is None
                or module.params.get("egress_security_rules") is None
            ):
                module.fail_json(
                    msg="ingress_security_rules and egress_security_rules are required for creating security list."
                )
            result = oci_utils.check_and_create_resource(
                resource_type="security_list",
                create_fn=create_security_list,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_security_lists,
                kwargs_list={
                    "compartment_id": module.params.get("compartment_id"),
                    "vcn_id": module.params.get("vcn_id"),
                },
                exclude_attributes=exclude_attributes,
                default_attribute_values=default_attribute_values,
                module=module,
                model=CreateSecurityListDetails(),
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))

    return result


def create_security_list(virtual_network_client, module):
    input_ingress_security_rules = module.params["ingress_security_rules"]
    input_egress_security_rules = module.params["egress_security_rules"]
    ingress_security_rules = []
    egress_security_rules = []
    if input_ingress_security_rules:
        ingress_security_rules = get_security_rules(
            "ingress_security_rules", input_ingress_security_rules
        )
    if input_egress_security_rules:
        egress_security_rules = get_security_rules(
            "egress_security_rules", input_egress_security_rules
        )
    create_security_list_details = CreateSecurityListDetails()
    for attribute in create_security_list_details.attribute_map:
        create_security_list_details.__setattr__(
            attribute, module.params.get(attribute)
        )
    create_security_list_details.ingress_security_rules = ingress_security_rules
    create_security_list_details.egress_security_rules = egress_security_rules
    result = oci_utils.create_and_wait(
        resource_type="security_list",
        create_fn=virtual_network_client.create_security_list,
        kwargs_create={"create_security_list_details": create_security_list_details},
        client=virtual_network_client,
        get_fn=virtual_network_client.get_security_list,
        get_param="security_list_id",
        module=module,
    )
    return result


def update_security_list(virtual_network_client, existing_security_list, module):
    if existing_security_list is None:
        raise ClientError(
            Exception(
                "No Security List with id "
                + module.params.get("security_list_id")
                + " is found for update"
            )
        )
    result = dict(security_list=to_dict(existing_security_list), changed=False)
    input_ingress_security_rules = module.params.get("ingress_security_rules")
    input_egress_security_rules = module.params.get("egress_security_rules")
    purge_security_rules = module.params.get("purge_security_rules")
    delete_security_rules = module.params.get("delete_security_rules")
    name_tag_changed = False
    egress_security_rules_changed = False
    ingress_security_rules_changed = False
    update_security_list_details = UpdateSecurityListDetails()
    existing_egress_security_rule = existing_security_list.egress_security_rules
    existing_ingress_security_rule = existing_security_list.ingress_security_rules
    attributes_to_compare = ["display_name", "freeform_tags", "defined_tags"]
    for attribute in attributes_to_compare:
        name_tag_changed = oci_utils.check_and_update_attributes(
            update_security_list_details,
            attribute,
            module.params.get(attribute),
            getattr(existing_security_list, attribute),
            name_tag_changed,
        )

    if input_egress_security_rules is not None:
        input_egress_security_rules = get_security_rules(
            "egress_security_rules", input_egress_security_rules
        )
        egress_security_rules, egress_security_rules_changed = oci_utils.check_and_return_component_list_difference(
            input_egress_security_rules,
            get_hashed_security_rules(
                "egress_security_rules", existing_egress_security_rule
            ),
            purge_security_rules,
            delete_security_rules,
        )

    if input_ingress_security_rules is not None:
        input_ingress_security_rules = get_security_rules(
            "ingress_security_rules", input_ingress_security_rules
        )
        ingress_security_rules, ingress_security_rules_changed = oci_utils.check_and_return_component_list_difference(
            input_ingress_security_rules,
            get_hashed_security_rules(
                "ingress_security_rules", existing_ingress_security_rule
            ),
            purge_security_rules,
            delete_security_rules,
        )

    if egress_security_rules_changed:
        update_security_list_details.egress_security_rules = egress_security_rules
    else:
        update_security_list_details.egress_security_rules = (
            existing_egress_security_rule
        )

    if ingress_security_rules_changed:
        update_security_list_details.ingress_security_rules = ingress_security_rules
    else:
        update_security_list_details.ingress_security_rules = (
            existing_ingress_security_rule
        )

    if name_tag_changed or (
        egress_security_rules_changed or ingress_security_rules_changed
    ):
        result = oci_utils.update_and_wait(
            resource_type="security_list",
            update_fn=virtual_network_client.update_security_list,
            kwargs_update={
                "security_list_id": existing_security_list.id,
                "update_security_list_details": update_security_list_details,
            },
            client=virtual_network_client,
            get_fn=virtual_network_client.get_security_list,
            get_param="security_list_id",
            module=module,
        )
    return result


def get_hashed_security_rules(security_rules_type, security_rules):
    supported_security_rule_simple_attributes = [
        "source",
        "source_type",
        "destination",
        "destination_type",
        "is_stateless",
        "protocol",
    ]
    hashed_security_rules = []
    if security_rules is None:
        return hashed_security_rules
    for security_rule in security_rules:
        if security_rules_type == "ingress_security_rules":
            hashed_security_rule = oci_utils.create_hashed_instance(IngressSecurityRule)
        elif security_rules_type == "egress_security_rules":
            hashed_security_rule = oci_utils.create_hashed_instance(EgressSecurityRule)
        for field in hashed_security_rule.attribute_map:
            value = None
            if field == "icmp_options":
                if getattr(security_rule, field):
                    source_icmp_options = getattr(security_rule, field)
                    value = oci_utils.create_hashed_instance(IcmpOptions)
                    for sub_field in source_icmp_options.attribute_map.keys():
                        setattr(
                            value, sub_field, getattr(source_icmp_options, sub_field)
                        )
                setattr(hashed_security_rule, field, value)
            elif field == "tcp_options":
                if getattr(security_rule, field):
                    source_tcp_options = getattr(security_rule, field)
                    value = oci_utils.create_hashed_instance(TcpOptions)
                    set_port_range(source_tcp_options, value)
                setattr(hashed_security_rule, field, value)
            elif field == "udp_options":
                if getattr(security_rule, field):
                    source_udp_options = getattr(security_rule, field)
                    value = oci_utils.create_hashed_instance(UdpOptions)
                    set_port_range(source_udp_options, value)
                setattr(hashed_security_rule, field, value)
            else:
                if field in supported_security_rule_simple_attributes:
                    value = getattr(security_rule, field)
                    setattr(hashed_security_rule, field, value)
        hashed_security_rules.append(hashed_security_rule)

    return hashed_security_rules


def set_port_range(source_options, target_value):
    for sub_field in source_options.attribute_map.keys():
        source_port_range = getattr(source_options, sub_field)
        if source_port_range:
            setattr(target_value, sub_field, get_hashed_port_range(source_port_range))


def get_hashed_port_range(port_range):
    hashed_port_range = oci_utils.create_hashed_instance(PortRange)
    for field in port_range.attribute_map.keys():
        setattr(hashed_port_range, field, getattr(port_range, field))
    return hashed_port_range


def get_security_rules(security_rule_type, input_security_rules):
    security_rule = None
    security_rules = []
    for input_security_rule in input_security_rules:
        if security_rule_type == "ingress_security_rules":
            security_rule = oci_utils.create_hashed_instance(IngressSecurityRule)
            security_rule.source = input_security_rule["source"]
            security_rule.source_type = input_security_rule.get(
                "source_type", "CIDR_BLOCK"
            )
        elif security_rule_type == "egress_security_rules":
            security_rule = oci_utils.create_hashed_instance(EgressSecurityRule)
            security_rule.destination = input_security_rule["destination"]
            security_rule.destination_type = input_security_rule.get(
                "destination_type", "CIDR_BLOCK"
            )
        input_icmp_options = input_security_rule.get("icmp_options", None)
        if input_icmp_options:
            icmp_options = oci_utils.create_hashed_instance(IcmpOptions)
            icmp_options.type = input_icmp_options.get("type")
            icmp_options.code = input_icmp_options.get("code", None)
            security_rule.icmp_options = icmp_options

        input_tcp_options = input_security_rule.get("tcp_options", None)
        if input_tcp_options:
            tcp_options = oci_utils.create_hashed_instance(TcpOptions)
            get_protocol_option(input_tcp_options, tcp_options)
            security_rule.tcp_options = tcp_options
        input_udp_options = input_security_rule.get("udp_options", None)
        if input_udp_options:
            udp_options = oci_utils.create_hashed_instance(UdpOptions)
            get_protocol_option(input_udp_options, udp_options)
            security_rule.udp_options = udp_options

        security_rule.is_stateless = input_security_rule.get("is_stateless", False)
        if security_rule.is_stateless is None:
            security_rule.is_stateless = False
        security_rule.protocol = input_security_rule.get("protocol").lower()
        security_rules.append(security_rule)

    return security_rules


def get_protocol_option(input_protocol_options, protocol_options):
    port_range = None
    input_destination_port_range = input_protocol_options.get(
        "destination_port_range", None
    )
    if input_destination_port_range:
        port_range = oci_utils.create_hashed_instance(PortRange)
        port_range.min = int(input_destination_port_range["min"])
        port_range.max = int(input_destination_port_range["max"])
        protocol_options.destination_port_range = port_range
    input_source_port_range = input_protocol_options.get("source_port_range", None)
    if input_source_port_range:
        port_range = oci_utils.create_hashed_instance(PortRange)
        port_range.min = int(input_source_port_range["min"])
        port_range.max = int(input_source_port_range["max"])
        protocol_options.source_port_range = port_range


def delete_security_list(virtual_network_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="security_list",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_security_list,
        kwargs_get={"security_list_id": module.params["security_list_id"]},
        delete_fn=virtual_network_client.delete_security_list,
        kwargs_delete={"security_list_id": module.params["security_list_id"]},
        module=module,
    )
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            vcn_id=dict(type="str", required=False),
            security_list_id=dict(type="str", required=False, aliases=["id"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            ingress_security_rules=dict(type=list, required=False),
            egress_security_rules=dict(type=list, required=False),
            purge_security_rules=dict(type="bool", required=False, default=True),
            delete_security_rules=dict(type="bool", required=False, default=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["purge_security_rules", "delete_security_rules"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    state = module.params["state"]

    if state == "present":
        result = create_or_update_security_list(virtual_network_client, module)
    elif state == "absent":
        result = delete_security_list(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()

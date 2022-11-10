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
module: oci_vn_monitoring_path_analyzer_test
short_description: Manage a PathAnalyzerTest resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PathAnalyzerTest resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new `PathAnalyzerTest` resource.
    - "This resource has the following action operations in the M(oracle.oci.oci_vn_monitoring_path_analyzer_test_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the `PathAnalyzerTest` resource's compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    protocol:
        description:
            - The IP protocol to use in the `PathAnalyzerTest` resource.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    source_endpoint:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            instance_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compute instance.
                    - Required when type is 'COMPUTE_INSTANCE'
                type: str
            network_load_balancer_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the listener's network load balancer.
                    - Required when type is one of ['NETWORK_LOAD_BALANCER_LISTENER', 'NETWORK_LOAD_BALANCER']
                type: str
            vnic_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VNIC attached to the compute instance.
                    - Required when type is one of ['COMPUTE_INSTANCE', 'VNIC']
                type: str
            vlan_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN containing the IP address.
                      This can be used to disambiguate which VLAN is queried, in case the endpoint IP
                      address belongs to more than one VLAN (when there are VLANs with overlapping IP ranges).
                    - Required when type is 'VLAN'
                type: str
            address:
                description:
                    - The IPv4 address of the COMPUTE_INSTANCE-type `Endpoint` object.
                    - Required when type is one of ['SUBNET', 'COMPUTE_INSTANCE', 'VNIC', 'IP_ADDRESS', 'VLAN']
                type: str
            subnet_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet containing the IP address.
                      This can be used to disambiguate which subnet is intended, in case the IP address
                      is used in more than one subnet (when there are subnets with overlapping IP ranges).
                    - Required when type is 'SUBNET'
                type: str
            type:
                description:
                    - The type of the `Endpoint`.
                type: str
                choices:
                    - "NETWORK_LOAD_BALANCER_LISTENER"
                    - "COMPUTE_INSTANCE"
                    - "NETWORK_LOAD_BALANCER"
                    - "LOAD_BALANCER"
                    - "VNIC"
                    - "IP_ADDRESS"
                    - "VLAN"
                    - "SUBNET"
                    - "LOAD_BALANCER_LISTENER"
                required: true
            listener_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer listener.
                    - Required when type is one of ['NETWORK_LOAD_BALANCER_LISTENER', 'LOAD_BALANCER_LISTENER']
                type: str
            load_balancer_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer.
                    - Required when type is one of ['LOAD_BALANCER', 'LOAD_BALANCER_LISTENER']
                type: str
    destination_endpoint:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            instance_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compute instance.
                    - Required when type is 'COMPUTE_INSTANCE'
                type: str
            network_load_balancer_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the listener's network load balancer.
                    - Required when type is one of ['NETWORK_LOAD_BALANCER_LISTENER', 'NETWORK_LOAD_BALANCER']
                type: str
            vnic_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VNIC attached to the compute instance.
                    - Required when type is one of ['COMPUTE_INSTANCE', 'VNIC']
                type: str
            vlan_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN containing the IP address.
                      This can be used to disambiguate which VLAN is queried, in case the endpoint IP
                      address belongs to more than one VLAN (when there are VLANs with overlapping IP ranges).
                    - Required when type is 'VLAN'
                type: str
            address:
                description:
                    - The IPv4 address of the COMPUTE_INSTANCE-type `Endpoint` object.
                    - Required when type is one of ['SUBNET', 'COMPUTE_INSTANCE', 'VNIC', 'IP_ADDRESS', 'VLAN']
                type: str
            subnet_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet containing the IP address.
                      This can be used to disambiguate which subnet is intended, in case the IP address
                      is used in more than one subnet (when there are subnets with overlapping IP ranges).
                    - Required when type is 'SUBNET'
                type: str
            type:
                description:
                    - The type of the `Endpoint`.
                type: str
                choices:
                    - "NETWORK_LOAD_BALANCER_LISTENER"
                    - "COMPUTE_INSTANCE"
                    - "NETWORK_LOAD_BALANCER"
                    - "LOAD_BALANCER"
                    - "VNIC"
                    - "IP_ADDRESS"
                    - "VLAN"
                    - "SUBNET"
                    - "LOAD_BALANCER_LISTENER"
                required: true
            listener_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer listener.
                    - Required when type is one of ['NETWORK_LOAD_BALANCER_LISTENER', 'LOAD_BALANCER_LISTENER']
                type: str
            load_balancer_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer.
                    - Required when type is one of ['LOAD_BALANCER', 'LOAD_BALANCER_LISTENER']
                type: str
    protocol_parameters:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            source_port:
                description:
                    - The source port to use in a `PathAnalyzerTest` resource.
                    - Applicable when type is one of ['UDP', 'TCP']
                type: int
            destination_port:
                description:
                    - The destination port to use in a `PathAnalyzerTest` resource.
                    - Required when type is one of ['UDP', 'TCP']
                type: int
            type:
                description:
                    - The type of the `ProtocolParameters` object.
                type: str
                choices:
                    - "UDP"
                    - "TCP"
                    - "ICMP"
                required: true
            icmp_code:
                description:
                    - The L(ICMP,https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) code.
                    - Applicable when type is 'ICMP'
                type: int
            icmp_type:
                description:
                    - The L(ICMP,https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) type.
                    - Required when type is 'ICMP'
                type: int
    query_options:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_bi_directional_analysis:
                description:
                    - If true, a path analysis is done for both the forward and reverse routes.
                type: bool
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    path_analyzer_test_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the `PathAnalyzerTest` resource.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the PathAnalyzerTest.
            - Use I(state=present) to create or update a PathAnalyzerTest.
            - Use I(state=absent) to delete a PathAnalyzerTest.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create path_analyzer_test
  oci_vn_monitoring_path_analyzer_test:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    protocol: 56
    source_endpoint:
      # required
      network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      type: NETWORK_LOAD_BALANCER_LISTENER
      listener_id: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"
    destination_endpoint:
      # required
      network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      type: NETWORK_LOAD_BALANCER_LISTENER
      listener_id: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    protocol_parameters:
      # required
      destination_port: 56
      type: UDP

      # optional
      source_port: 56
    query_options:
      # optional
      is_bi_directional_analysis: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update path_analyzer_test
  oci_vn_monitoring_path_analyzer_test:
    # required
    path_analyzer_test_id: "ocid1.pathanalyzertest.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    protocol: 56
    source_endpoint:
      # required
      network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      type: NETWORK_LOAD_BALANCER_LISTENER
      listener_id: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"
    destination_endpoint:
      # required
      network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      type: NETWORK_LOAD_BALANCER_LISTENER
      listener_id: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"
    protocol_parameters:
      # required
      destination_port: 56
      type: UDP

      # optional
      source_port: 56
    query_options:
      # optional
      is_bi_directional_analysis: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update path_analyzer_test using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_vn_monitoring_path_analyzer_test:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    protocol: 56
    source_endpoint:
      # required
      network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      type: NETWORK_LOAD_BALANCER_LISTENER
      listener_id: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"
    destination_endpoint:
      # required
      network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      type: NETWORK_LOAD_BALANCER_LISTENER
      listener_id: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"
    protocol_parameters:
      # required
      destination_port: 56
      type: UDP

      # optional
      source_port: 56
    query_options:
      # optional
      is_bi_directional_analysis: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete path_analyzer_test
  oci_vn_monitoring_path_analyzer_test:
    # required
    path_analyzer_test_id: "ocid1.pathanalyzertest.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete path_analyzer_test using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_vn_monitoring_path_analyzer_test:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
path_analyzer_test:
    description:
        - Details of the PathAnalyzerTest resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - A unique identifier established when the resource is created. The identifier can't be changed later.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `PathAnalyzerTest` resource's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        protocol:
            description:
                - The IP protocol to use for the `PathAnalyzerTest` resource.
            returned: on success
            type: int
            sample: 56
        source_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                instance_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compute instance.
                    returned: on success
                    type: str
                    sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
                load_balancer_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                listener_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer listener.
                    returned: on success
                    type: str
                    sample: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"
                network_load_balancer_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet containing the IP address.
                          This can be used to disambiguate which subnet is intended, in case the IP address
                          is used in more than one subnet (when there are subnets with overlapping IP ranges).
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                vlan_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN containing the IP address.
                          This can be used to disambiguate which VLAN is queried, in case the endpoint IP
                          address belongs to more than one VLAN (when there are VLANs with overlapping IP ranges).
                    returned: on success
                    type: str
                    sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
                type:
                    description:
                        - The type of the `Endpoint`.
                    returned: on success
                    type: str
                    sample: IP_ADDRESS
                address:
                    description:
                        - The IPv4 address of the COMPUTE_INSTANCE-type `Endpoint` object.
                    returned: on success
                    type: str
                    sample: address_example
                vnic_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VNIC attached to the compute instance.
                    returned: on success
                    type: str
                    sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        destination_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                instance_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compute instance.
                    returned: on success
                    type: str
                    sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
                load_balancer_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                listener_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer listener.
                    returned: on success
                    type: str
                    sample: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"
                network_load_balancer_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet containing the IP address.
                          This can be used to disambiguate which subnet is intended, in case the IP address
                          is used in more than one subnet (when there are subnets with overlapping IP ranges).
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                vlan_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN containing the IP address.
                          This can be used to disambiguate which VLAN is queried, in case the endpoint IP
                          address belongs to more than one VLAN (when there are VLANs with overlapping IP ranges).
                    returned: on success
                    type: str
                    sample: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
                type:
                    description:
                        - The type of the `Endpoint`.
                    returned: on success
                    type: str
                    sample: IP_ADDRESS
                address:
                    description:
                        - The IPv4 address of the COMPUTE_INSTANCE-type `Endpoint` object.
                    returned: on success
                    type: str
                    sample: address_example
                vnic_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VNIC attached to the compute instance.
                    returned: on success
                    type: str
                    sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        protocol_parameters:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                icmp_code:
                    description:
                        - The L(ICMP,https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) code.
                    returned: on success
                    type: int
                    sample: 56
                icmp_type:
                    description:
                        - The L(ICMP,https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) type.
                    returned: on success
                    type: int
                    sample: 56
                type:
                    description:
                        - The type of the `ProtocolParameters` object.
                    returned: on success
                    type: str
                    sample: TCP
                source_port:
                    description:
                        - The source port to use in a `PathAnalyzerTest` resource.
                    returned: on success
                    type: int
                    sample: 56
                destination_port:
                    description:
                        - The destination port to use in a `PathAnalyzerTest` resource.
                    returned: on success
                    type: int
                    sample: 56
        query_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_bi_directional_analysis:
                    description:
                        - If true, a path analysis is done for both the forward and reverse routes.
                    returned: on success
                    type: bool
                    sample: true
        time_created:
            description:
                - The date and time the `PathAnalyzerTest` resource was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the `PathAnalyzerTest` resource was last updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the `PathAnalyzerTest` resource.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "protocol": 56,
        "source_endpoint": {
            "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "listener_id": "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx",
            "network_load_balancer_id": "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
            "type": "IP_ADDRESS",
            "address": "address_example",
            "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "destination_endpoint": {
            "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "listener_id": "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx",
            "network_load_balancer_id": "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "vlan_id": "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx",
            "type": "IP_ADDRESS",
            "address": "address_example",
            "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "protocol_parameters": {
            "icmp_code": 56,
            "icmp_type": 56,
            "type": "TCP",
            "source_port": 56,
            "destination_port": 56
        },
        "query_options": {
            "is_bi_directional_analysis": true
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.vn_monitoring import VnMonitoringClient
    from oci.vn_monitoring.models import CreatePathAnalyzerTestDetails
    from oci.vn_monitoring.models import UpdatePathAnalyzerTestDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PathAnalyzerTestHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(PathAnalyzerTestHelperGen, self).get_possible_entity_types() + [
            "pathanalyzertest",
            "pathanalyzertests",
            "vnMonitoringpathanalyzertest",
            "vnMonitoringpathanalyzertests",
            "pathanalyzertestresource",
            "pathanalyzertestsresource",
            "vnmonitoring",
        ]

    def get_module_resource_id_param(self):
        return "path_analyzer_test_id"

    def get_module_resource_id(self):
        return self.module.params.get("path_analyzer_test_id")

    def get_get_fn(self):
        return self.client.get_path_analyzer_test

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_path_analyzer_test, path_analyzer_test_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_path_analyzer_test,
            path_analyzer_test_id=self.module.params.get("path_analyzer_test_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_path_analyzer_tests, **kwargs
        )

    def get_create_model_class(self):
        return CreatePathAnalyzerTestDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_path_analyzer_test,
            call_fn_args=(),
            call_fn_kwargs=dict(create_path_analyzer_test_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdatePathAnalyzerTestDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_path_analyzer_test,
            call_fn_args=(),
            call_fn_kwargs=dict(
                path_analyzer_test_id=self.module.params.get("path_analyzer_test_id"),
                update_path_analyzer_test_details=update_details,
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
            call_fn=self.client.delete_path_analyzer_test,
            call_fn_args=(),
            call_fn_kwargs=dict(
                path_analyzer_test_id=self.module.params.get("path_analyzer_test_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


PathAnalyzerTestHelperCustom = get_custom_class("PathAnalyzerTestHelperCustom")


class ResourceHelper(PathAnalyzerTestHelperCustom, PathAnalyzerTestHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            protocol=dict(type="int"),
            source_endpoint=dict(
                type="dict",
                options=dict(
                    instance_id=dict(type="str"),
                    network_load_balancer_id=dict(type="str"),
                    vnic_id=dict(type="str"),
                    vlan_id=dict(type="str"),
                    address=dict(type="str"),
                    subnet_id=dict(type="str"),
                    type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "NETWORK_LOAD_BALANCER_LISTENER",
                            "COMPUTE_INSTANCE",
                            "NETWORK_LOAD_BALANCER",
                            "LOAD_BALANCER",
                            "VNIC",
                            "IP_ADDRESS",
                            "VLAN",
                            "SUBNET",
                            "LOAD_BALANCER_LISTENER",
                        ],
                    ),
                    listener_id=dict(type="str"),
                    load_balancer_id=dict(type="str"),
                ),
            ),
            destination_endpoint=dict(
                type="dict",
                options=dict(
                    instance_id=dict(type="str"),
                    network_load_balancer_id=dict(type="str"),
                    vnic_id=dict(type="str"),
                    vlan_id=dict(type="str"),
                    address=dict(type="str"),
                    subnet_id=dict(type="str"),
                    type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "NETWORK_LOAD_BALANCER_LISTENER",
                            "COMPUTE_INSTANCE",
                            "NETWORK_LOAD_BALANCER",
                            "LOAD_BALANCER",
                            "VNIC",
                            "IP_ADDRESS",
                            "VLAN",
                            "SUBNET",
                            "LOAD_BALANCER_LISTENER",
                        ],
                    ),
                    listener_id=dict(type="str"),
                    load_balancer_id=dict(type="str"),
                ),
            ),
            protocol_parameters=dict(
                type="dict",
                options=dict(
                    source_port=dict(type="int"),
                    destination_port=dict(type="int"),
                    type=dict(
                        type="str", required=True, choices=["UDP", "TCP", "ICMP"]
                    ),
                    icmp_code=dict(type="int"),
                    icmp_type=dict(type="int"),
                ),
            ),
            query_options=dict(
                type="dict", options=dict(is_bi_directional_analysis=dict(type="bool"))
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            path_analyzer_test_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="path_analyzer_test",
        service_client_class=VnMonitoringClient,
        namespace="vn_monitoring",
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

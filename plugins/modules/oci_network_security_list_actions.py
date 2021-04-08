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
module: oci_network_security_list_actions
short_description: Perform actions on a SecurityList resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a SecurityList resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a security list into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9"
author: Oracle (@oracle)
options:
    security_list_id:
        description:
            - The OCID of the security list.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              security list to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the SecurityList.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on security_list
  oci_network_security_list_actions:
    security_list_id: "ocid1.securitylist.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import ChangeSecurityListCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecurityListActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeSecurityListCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_security_list_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_list_id=self.module.params.get("security_list_id"),
                change_security_list_compartment_details=action_details,
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


SecurityListActionsHelperCustom = get_custom_class("SecurityListActionsHelperCustom")


class ResourceHelper(SecurityListActionsHelperCustom, SecurityListActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            security_list_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

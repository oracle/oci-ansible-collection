#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_network_load_balancer_actions
short_description: Perform actions on a NetworkLoadBalancer resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a NetworkLoadBalancer resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a network load balancer into a different compartment within the same tenancy. For information about moving
      resources
      between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to which to move the network load
              balancer.
        type: str
        required: true
    action:
        description:
            - The action to perform on the NetworkLoadBalancer.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on network_load_balancer
  oci_network_load_balancer_actions:
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    action: "change_compartment"

"""

RETURN = """
network_load_balancer:
    description:
        - Details of the NetworkLoadBalancer resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the network load balancer.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name, which does not have to be unique, and can be changed.
                - "Example: `example_load_balancer`"
            returned: on success
            type: str
            sample: example_load_balancer
        lifecycle_state:
            description:
                - The current state of the network load balancer.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a resource in Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the network load balancer was created, in the format defined by RFC3339.
                - "Example: `2020-05-01T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2020-05-01T21:10:29.600Z"
        time_updated:
            description:
                - The time the network load balancer was updated. An RFC3339 formatted date-time string.
                - "Example: `2020-05-01T22:10:29.600Z`"
            returned: on success
            type: str
            sample: "2020-05-01T22:10:29.600Z"
        ip_addresses:
            description:
                - An array of IP addresses.
            returned: on success
            type: complex
            contains:
                ip_address:
                    description:
                        - An IP address.
                        - "Example: `192.168.0.3`"
                    returned: on success
                    type: str
                    sample: 192.168.0.3
                is_public:
                    description:
                        - Whether the IP address is public or private.
                        - "If \\"true\\", then the IP address is public and accessible from the internet."
                        - "If \\"false\\", then the IP address is private and accessible only from within the associated virtual cloud network."
                    returned: on success
                    type: bool
                    sample: true
                reserved_ip:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - OCID of the reserved public IP address created with the virtual cloud network.
                                - Reserved public IP addresses are IP addresses that are registered using the virtual cloud network API.
                                - Create a reserved public IP address. When you create the network load balancer, enter the OCID of the reserved public IP
                                  address in the
                                  reservedIp field to attach the IP address to the network load balancer. This task configures the network load balancer to
                                  listen to traffic on this IP address.
                                - Reserved public IP addresses are not deleted when the network load balancer is deleted. The IP addresses become unattached
                                  from the network load balancer.
                                - "Example: \\"ocid1.publicip.oc1.phx.unique_ID\\""
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        is_private:
            description:
                - Whether the network load balancer has a virtual cloud network-local (private) IP address.
                - "If \\"true\\", then the service assigns a private IP address to the network load balancer."
                - "If \\"false\\", then the service assigns a public IP address to the network load balancer."
                - A public network load balancer is accessible from the internet, depending the
                  L(security list rules,https://docs.cloud.oracle.com/Content/network/Concepts/securitylists.htm) for your virtual cloudn network. For more
                  information about public and
                  private network load balancers,
                  see L(How Network Load Balancing Works,https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-network-load-balancing-
                  works).
                  This value is true by default.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        is_preserve_source_destination:
            description:
                - When enabled, the skipSourceDestinationCheck parameter is automatically enabled on the load balancer VNIC.
                  Packets are sent to the backend set without any changes to the source and destination IP.
            returned: on success
            type: bool
            sample: true
        subnet_id:
            description:
                - "The subnet in which the network load balancer is spawned L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).\\""
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        network_security_group_ids:
            description:
                - An array of network security groups L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated with the
                  network load
                  balancer.
                - During the creation of the network load balancer, the service adds the new load balancer to the specified network security groups.
                - "The benefits of associating the network load balancer with network security groups include:"
                - "*  Network security groups define network security rules to govern ingress and egress traffic for the network load balancer."
                - "*  The network security rules of other resources can reference the network security groups associated with the network load balancer
                     to ensure access."
                - "Example: [\\"ocid1.nsg.oc1.phx.unique_ID\\"]"
            returned: on success
            type: list
            sample: []
        listeners:
            description:
                - Listeners associated with the network load balancer.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A friendly name for the listener. It must be unique and it cannot be changed.
                        - "Example: `example_listener`"
                    returned: on success
                    type: str
                    sample: example_listener
                default_backend_set_name:
                    description:
                        - The name of the associated backend set.
                        - "Example: `example_backend_set`"
                    returned: on success
                    type: str
                    sample: example_backend_set
                port:
                    description:
                        - The communication port for the listener.
                        - "Example: `80`"
                    returned: on success
                    type: int
                    sample: 0
                protocol:
                    description:
                        - The protocol on which the listener accepts connection requests.
                          For public network load balancers, ANY protocol refers to TCP/UDP.
                          For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set
                          to true).
                          To get a list of valid protocols, use the L(ListNetworkLoadBalancersProtocols,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/NetworkLoadBalancer/20200501/networkLoadBalancerProtocol/ListNetworkLoadBalancersProtocols)
                          operation.
                        - "Example: `TCP`"
                    returned: on success
                    type: str
                    sample: TCP
        backend_sets:
            description:
                - Backend sets associated with the network load balancer.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A user-friendly name for the backend set that must be unique and cannot be changed.
                        - Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
                          contain spaces. Avoid entering confidential information.
                        - "Example: `example_backend_set`"
                    returned: on success
                    type: str
                    sample: example_backend_set
                policy:
                    description:
                        - The network load balancer policy for the backend set.
                        - "Example: `FIVE_TUPLE`"
                    returned: on success
                    type: str
                    sample: FIVE_TUPLE
                is_preserve_source:
                    description:
                        - If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends.
                          Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource,
                          then this parameter cannot be disabled.
                          The value is true by default.
                    returned: on success
                    type: bool
                    sample: true
                backends:
                    description:
                        - Array of backends.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - A read-only field showing the IP address/IP OCID and port that uniquely identify this backend server in the backend set.
                                - "Example: `10.0.0.3:8080`, or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:443` or `10.0.0.3:0`"
                            returned: on success
                            type: str
                            sample: 10.0.0.3:8080
                        ip_address:
                            description:
                                - "The IP address of the backend server.
                                  Example: `10.0.0.3`"
                            returned: on success
                            type: str
                            sample: 10.0.0.3
                        target_id:
                            description:
                                - "The IP OCID/Instance OCID associated with the backend server.
                                  Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`"
                            returned: on success
                            type: str
                            sample: "ocid1.privateip..oc1.unique_ID"
                        port:
                            description:
                                - The communication port for the backend server.
                                - "Example: `8080`"
                            returned: on success
                            type: int
                            sample: 8080
                        weight:
                            description:
                                - The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
                                  proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections
                                  as a server weighted '1'.
                                  For more information about load balancing policies, see
                                  L(How Network Load Balancing Policies Work,https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm).
                                - "Example: `3`"
                            returned: on success
                            type: int
                            sample: 3
                        is_drain:
                            description:
                                - "Whether the network load balancer should drain this server. Servers marked \\"isDrain\\" receive no
                                  incoming traffic."
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: false
                        is_backup:
                            description:
                                - "Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer
                                  forwards no ingress
                                  traffic to this backend server unless all other backend servers not marked as \\"isBackup\\" fail the health check policy."
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: false
                        is_offline:
                            description:
                                - Whether the network load balancer should treat this server as offline. Offline servers receive no incoming
                                  traffic.
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: false
                health_checker:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        protocol:
                            description:
                                - The protocol the health check must use; either HTTP or HTTPS, or UDP or TCP.
                                - "Example: `HTTP`"
                            returned: on success
                            type: str
                            sample: HTTP
                        port:
                            description:
                                - The backend server port against which to run the health check. If the port is not specified, then the network load balancer
                                  uses the
                                  port information from the `Backend` object. The port must be specified if the backend port is 0.
                                - "Example: `8080`"
                            returned: on success
                            type: int
                            sample: 8080
                        retries:
                            description:
                                - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                                  when recovering a server to the \\"healthy\\" state. The default value is 3."
                                - "Example: `3`"
                            returned: on success
                            type: int
                            sample: 3
                        timeout_in_millis:
                            description:
                                - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                                  returns within this timeout period. The default value is 3000 (3 seconds).
                                - "Example: `3000`"
                            returned: on success
                            type: int
                            sample: 3000
                        interval_in_millis:
                            description:
                                - The interval between health checks, in milliseconds. The default value is 10000 (10 seconds).
                                - "Example: `10000`"
                            returned: on success
                            type: int
                            sample: 10000
                        url_path:
                            description:
                                - The path against which to run the health check.
                                - "Example: `/healthcheck`"
                            returned: on success
                            type: str
                            sample: /healthcheck
                        response_body_regex:
                            description:
                                - A regular expression for parsing the response body from the backend server.
                                - "Example: `^((?!false).|\\\\s)*$`"
                            returned: on success
                            type: str
                            sample: "^((?!false).|\\\\s)*$"
                        return_code:
                            description:
                                - "The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
                                  then you can use common HTTP status codes such as \\"200\\"."
                                - "Example: `200`"
                            returned: on success
                            type: int
                            sample: 0
                        request_data:
                            description:
                                - Base64 encoded pattern to be sent as UDP or TCP health check probe.
                            returned: on success
                            type: str
                            sample: "example_request_data"
                        response_data:
                            description:
                                - Base64 encoded pattern to be validated as UDP or TCP health check probe response.
                            returned: on success
                            type: str
                            sample: "example_response_data"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Key-value pair representing system tags' keys and values scoped to a namespace.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "example_load_balancer",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2020-05-01T21:10:29.600Z",
        "time_updated": "2020-05-01T22:10:29.600Z",
        "ip_addresses": [{
            "ip_address": "192.168.0.3",
            "is_public": true,
            "reserved_ip": {
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            }
        }],
        "is_private": true,
        "is_preserve_source_destination": true,
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "network_security_group_ids": [],
        "listeners": {
            "name": "example_listener",
            "default_backend_set_name": "example_backend_set",
            "port": 0,
            "protocol": "TCP"
        },
        "backend_sets": {
            "name": "example_backend_set",
            "policy": "FIVE_TUPLE",
            "is_preserve_source": true,
            "backends": [{
                "name": "10.0.0.3:8080",
                "ip_address": "10.0.0.3",
                "target_id": "ocid1.privateip..oc1.unique_ID",
                "port": 8080,
                "weight": 3,
                "is_drain": false,
                "is_backup": false,
                "is_offline": false
            }],
            "health_checker": {
                "protocol": "HTTP",
                "port": 8080,
                "retries": 3,
                "timeout_in_millis": 3000,
                "interval_in_millis": 10000,
                "url_path": "/healthcheck",
                "response_body_regex": "^((?!false).|\\\\s)*$",
                "return_code": 0,
                "request_data": UNKNOWN TYPE - str,
                "response_data": UNKNOWN TYPE - str
            }
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.network_load_balancer import NetworkLoadBalancerClient
    from oci.network_load_balancer.models import (
        ChangeNetworkLoadBalancerCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkLoadBalancerActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "network_load_balancer_id"

    def get_module_resource_id(self):
        return self.module.params.get("network_load_balancer_id")

    def get_get_fn(self):
        return self.client.get_network_load_balancer

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_load_balancer,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeNetworkLoadBalancerCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_network_load_balancer_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                change_network_load_balancer_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkLoadBalancerActionsHelperCustom = get_custom_class(
    "NetworkLoadBalancerActionsHelperCustom"
)


class ResourceHelper(
    NetworkLoadBalancerActionsHelperCustom, NetworkLoadBalancerActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="network_load_balancer",
        service_client_class=NetworkLoadBalancerClient,
        namespace="network_load_balancer",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

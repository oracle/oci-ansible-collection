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
module: oci_network_load_balancer_facts
short_description: Fetches details about one or multiple NetworkLoadBalancer resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NetworkLoadBalancer resources in Oracle Cloud Infrastructure
    - Returns a list of network load balancers.
    - If I(network_load_balancer_id) is specified, the details of a single NetworkLoadBalancer will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
            - Required to get a specific network_load_balancer.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the network load balancers to
              list.
            - Required to list multiple network_load_balancers.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' (ascending) or 'desc' (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending.
              The default order for displayName is ascending. If no value is specified, then timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific network_load_balancer
  oci_network_load_balancer_facts:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: List network_load_balancers
  oci_network_load_balancer_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
network_load_balancers:
    description:
        - List of NetworkLoadBalancer resources
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
            sample: display_name_example
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
        nlb_ip_version:
            description:
                - IP version associated with the NLB.
            returned: on success
            type: str
            sample: IPV4
        time_created:
            description:
                - The date and time the network load balancer was created, in the format defined by RFC3339.
                - "Example: `2020-05-01T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the network load balancer was updated. An RFC3339 formatted date-time string.
                - "Example: `2020-05-01T22:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
                    sample: ip_address_example
                is_public:
                    description:
                        - Whether the IP address is public or private.
                        - "If \\"true\\", then the IP address is public and accessible from the internet."
                        - "If \\"false\\", then the IP address is private and accessible only from within the associated virtual cloud network."
                    returned: on success
                    type: bool
                    sample: true
                ip_version:
                    description:
                        - IP version associated with this IP address.
                    returned: on success
                    type: str
                    sample: IPV4
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
                    sample: name_example
                default_backend_set_name:
                    description:
                        - The name of the associated backend set.
                        - "Example: `example_backend_set`"
                    returned: on success
                    type: str
                    sample: default_backend_set_name_example
                port:
                    description:
                        - The communication port for the listener.
                        - "Example: `80`"
                    returned: on success
                    type: int
                    sample: 56
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
                    sample: ANY
                ip_version:
                    description:
                        - IP version associated with the listener.
                    returned: on success
                    type: str
                    sample: IPV4
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
                    sample: name_example
                policy:
                    description:
                        - The network load balancer policy for the backend set.
                        - "Example: `FIVE_TUPLE`"
                    returned: on success
                    type: str
                    sample: TWO_TUPLE
                is_preserve_source:
                    description:
                        - If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends.
                          Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource,
                          then this parameter cannot be disabled.
                          The value is true by default.
                    returned: on success
                    type: bool
                    sample: true
                ip_version:
                    description:
                        - IP version associated with the backend set.
                    returned: on success
                    type: str
                    sample: IPV4
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
                            sample: name_example
                        ip_address:
                            description:
                                - "The IP address of the backend server.
                                  Example: `10.0.0.3`"
                            returned: on success
                            type: str
                            sample: ip_address_example
                        target_id:
                            description:
                                - "The IP OCID/Instance OCID associated with the backend server.
                                  Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`"
                            returned: on success
                            type: str
                            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
                        port:
                            description:
                                - The communication port for the backend server.
                                - "Example: `8080`"
                            returned: on success
                            type: int
                            sample: 56
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
                            sample: 56
                        is_drain:
                            description:
                                - "Whether the network load balancer should drain this server. Servers marked \\"isDrain\\" receive no
                                  incoming traffic."
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: true
                        is_backup:
                            description:
                                - "Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer
                                  forwards no ingress
                                  traffic to this backend server unless all other backend servers not marked as \\"isBackup\\" fail the health check policy."
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: true
                        is_offline:
                            description:
                                - Whether the network load balancer should treat this server as offline. Offline servers receive no incoming
                                  traffic.
                                - "Example: `false`"
                            returned: on success
                            type: bool
                            sample: true
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
                            sample: 56
                        retries:
                            description:
                                - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                                  when recovering a server to the \\"healthy\\" state. The default value is 3."
                                - "Example: `3`"
                            returned: on success
                            type: int
                            sample: 56
                        timeout_in_millis:
                            description:
                                - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                                  returns within this timeout period. The default value is 3000 (3 seconds).
                                - "Example: `3000`"
                            returned: on success
                            type: int
                            sample: 56
                        interval_in_millis:
                            description:
                                - The interval between health checks, in milliseconds. The default value is 10000 (10 seconds).
                                - "Example: `10000`"
                            returned: on success
                            type: int
                            sample: 56
                        url_path:
                            description:
                                - The path against which to run the health check.
                                - "Example: `/healthcheck`"
                            returned: on success
                            type: str
                            sample: url_path_example
                        response_body_regex:
                            description:
                                - A regular expression for parsing the response body from the backend server.
                                - "Example: `^((?!false).|\\\\s)*$`"
                            returned: on success
                            type: str
                            sample: response_body_regex_example
                        return_code:
                            description:
                                - "The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
                                  then you can use common HTTP status codes such as \\"200\\"."
                                - "Example: `200`"
                            returned: on success
                            type: int
                            sample: 56
                        request_data:
                            description:
                                - Base64 encoded pattern to be sent as UDP or TCP health check probe.
                            returned: on success
                            type: str
                            sample: "null"

                        response_data:
                            description:
                                - Base64 encoded pattern to be validated as UDP or TCP health check probe response.
                            returned: on success
                            type: str
                            sample: "null"

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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "nlb_ip_version": "IPV4",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "ip_addresses": [{
            "ip_address": "ip_address_example",
            "is_public": true,
            "ip_version": "IPV4",
            "reserved_ip": {
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            }
        }],
        "is_private": true,
        "is_preserve_source_destination": true,
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "network_security_group_ids": [],
        "listeners": {
            "name": "name_example",
            "default_backend_set_name": "default_backend_set_name_example",
            "port": 56,
            "protocol": "ANY",
            "ip_version": "IPV4"
        },
        "backend_sets": {
            "name": "name_example",
            "policy": "TWO_TUPLE",
            "is_preserve_source": true,
            "ip_version": "IPV4",
            "backends": [{
                "name": "name_example",
                "ip_address": "ip_address_example",
                "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
                "port": 56,
                "weight": 56,
                "is_drain": true,
                "is_backup": true,
                "is_offline": true
            }],
            "health_checker": {
                "protocol": "HTTP",
                "port": 56,
                "retries": 56,
                "timeout_in_millis": 56,
                "interval_in_millis": 56,
                "url_path": "url_path_example",
                "response_body_regex": "response_body_regex_example",
                "return_code": 56,
                "request_data": null,
                "response_data": null
            }
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.network_load_balancer import NetworkLoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkLoadBalancerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "network_load_balancer_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_load_balancer,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_network_load_balancers,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


NetworkLoadBalancerFactsHelperCustom = get_custom_class(
    "NetworkLoadBalancerFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkLoadBalancerFactsHelperCustom, NetworkLoadBalancerFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="network_load_balancer",
        service_client_class=NetworkLoadBalancerClient,
        namespace="network_load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(network_load_balancers=result)


if __name__ == "__main__":
    main()

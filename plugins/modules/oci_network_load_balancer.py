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
module: oci_network_load_balancer
short_description: Manage a NetworkLoadBalancer resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a NetworkLoadBalancer resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a network load balancer.
    - "This resource has the following action operations in the M(oracle.oci.oci_network_load_balancer_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the network load balancer.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - Network load balancer identifier, which can be renamed.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    is_preserve_source_destination:
        description:
            - This parameter can be enabled only if backends are compute OCIDs. When enabled, the skipSourceDestinationCheck parameter is automatically
              enabled on the load balancer VNIC, and packets are sent to the backend with the entire IP header intact.
            - This parameter is updatable.
        type: bool
    reserved_ips:
        description:
            - An array of reserved Ips.
        type: list
        elements: dict
        suboptions:
            id:
                description:
                    - OCID of the reserved public IP address created with the virtual cloud network.
                    - Reserved public IP addresses are IP addresses that are registered using the virtual cloud network API.
                    - Create a reserved public IP address. When you create the network load balancer, enter the OCID of the reserved public IP address in the
                      reservedIp field to attach the IP address to the network load balancer. This task configures the network load balancer to listen to
                      traffic on this IP address.
                    - Reserved public IP addresses are not deleted when the network load balancer is deleted. The IP addresses become unattached from the
                      network load balancer.
                    - "Example: \\"ocid1.publicip.oc1.phx.unique_ID\\""
                type: str
    is_private:
        description:
            - Whether the network load balancer has a virtual cloud network-local (private) IP address.
            - "If \\"true\\", then the service assigns a private IP address to the network load balancer."
            - "If \\"false\\", then the service assigns a public IP address to the network load balancer."
            - A public network load balancer is accessible from the internet, depending on the
              L(security list rules,https://docs.cloud.oracle.com/Content/network/Concepts/securitylists.htm) for your virtual cloud network. For more
              information about public and
              private network load balancers,
              see L(How Network Load Balancing Works,https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-network-load-balancing-
              works).
              This value is true by default.
            - "Example: `true`"
        type: bool
    subnet_id:
        description:
            - The subnet in which the network load balancer is spawned L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    network_load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the NetworkLoadBalancer.
            - Use I(state=present) to create or update a NetworkLoadBalancer.
            - Use I(state=absent) to delete a NetworkLoadBalancer.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create network_load_balancer
  oci_network_load_balancer:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_preserve_source_destination: true
    reserved_ips:
    - # optional
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    is_private: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update network_load_balancer
  oci_network_load_balancer:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    is_preserve_source_destination: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update network_load_balancer using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_load_balancer:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    is_preserve_source_destination: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete network_load_balancer
  oci_network_load_balancer:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete network_load_balancer using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_load_balancer:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "ip_addresses": [{
            "ip_address": "ip_address_example",
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
            "name": "name_example",
            "default_backend_set_name": "default_backend_set_name_example",
            "port": 56,
            "protocol": "ANY"
        },
        "backend_sets": {
            "name": "name_example",
            "policy": "TWO_TUPLE",
            "is_preserve_source": true,
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
    from oci.network_load_balancer import NetworkLoadBalancerClient
    from oci.network_load_balancer.models import CreateNetworkLoadBalancerDetails
    from oci.network_load_balancer.models import UpdateNetworkLoadBalancerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkLoadBalancerHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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
            self.client.list_network_load_balancers, **kwargs
        )

    def get_create_model_class(self):
        return CreateNetworkLoadBalancerDetails

    def get_exclude_attributes(self):
        return ["reserved_ips"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_network_load_balancer,
            call_fn_args=(),
            call_fn_kwargs=dict(create_network_load_balancer_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateNetworkLoadBalancerDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_network_load_balancer,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                update_network_load_balancer_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_network_load_balancer,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkLoadBalancerHelperCustom = get_custom_class("NetworkLoadBalancerHelperCustom")


class ResourceHelper(NetworkLoadBalancerHelperCustom, NetworkLoadBalancerHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_preserve_source_destination=dict(type="bool"),
            reserved_ips=dict(
                type="list", elements="dict", options=dict(id=dict(type="str"))
            ),
            is_private=dict(type="bool"),
            subnet_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            network_load_balancer_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

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
module: oci_network_load_balancer_backend_set_facts
short_description: Fetches details about one or multiple BackendSet resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BackendSet resources in Oracle Cloud Infrastructure
    - Lists all backend sets associated with a given network load balancer.
    - If I(backend_set_name) is specified, the details of a single BackendSet will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        type: str
        aliases: ["id"]
        required: true
    backend_set_name:
        description:
            - The name of the backend set to retrieve.
            - "Example: `example_backend_set`"
            - Required to get a specific backend_set.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' (ascending) or 'desc' (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific backend_set
  oci_network_load_balancer_backend_set_facts:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: backend_set_name_example

- name: List backend_sets
  oci_network_load_balancer_backend_set_facts:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC

"""

RETURN = """
backend_sets:
    description:
        - List of BackendSet resources
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
                  Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this
                  parameter cannot be disabled.
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
                        - "Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no
                          ingress
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
                        - The backend server port against which to run the health check. If the port is not specified, then the network load balancer uses the
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

    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.network_load_balancer import NetworkLoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkLoadBalancerBackendSetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "network_load_balancer_id",
            "backend_set_name",
        ]

    def get_required_params_for_list(self):
        return [
            "network_load_balancer_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend_set,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_backend_sets,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            **optional_kwargs
        )


NetworkLoadBalancerBackendSetFactsHelperCustom = get_custom_class(
    "NetworkLoadBalancerBackendSetFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkLoadBalancerBackendSetFactsHelperCustom,
    NetworkLoadBalancerBackendSetFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str", required=True),
            backend_set_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backend_set",
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

    module.exit_json(backend_sets=result)


if __name__ == "__main__":
    main()

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
module: oci_network_load_balancer_listener_facts
short_description: Fetches details about one or multiple Listener resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Listener resources in Oracle Cloud Infrastructure
    - Lists all listeners associated with a given network load balancer.
    - If I(listener_name) is specified, the details of a single Listener will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        type: str
        required: true
    listener_name:
        description:
            - The name of the listener to get.
            - "Example: `example_listener`"
            - Required to get a specific listener.
        type: str
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
- name: Get a specific listener
  oci_network_load_balancer_listener_facts:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    listener_name: listener_name_example

- name: List listeners
  oci_network_load_balancer_listener_facts:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC

"""

RETURN = """
listeners:
    description:
        - List of Listener resources
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
                  For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to
                  true).
                  To get a list of valid protocols, use the L(ListNetworkLoadBalancersProtocols,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/NetworkLoadBalancer/20200501/networkLoadBalancerProtocol/ListNetworkLoadBalancersProtocols)
                  operation.
                - "Example: `TCP`"
            returned: on success
            type: str
            sample: ANY
    sample: [{
        "name": "name_example",
        "default_backend_set_name": "default_backend_set_name_example",
        "port": 56,
        "protocol": "ANY"
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


class NetworkLoadBalancerListenerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "network_load_balancer_id",
            "listener_name",
        ]

    def get_required_params_for_list(self):
        return [
            "network_load_balancer_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_listener,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            listener_name=self.module.params.get("listener_name"),
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
            self.client.list_listeners,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            **optional_kwargs
        )


NetworkLoadBalancerListenerFactsHelperCustom = get_custom_class(
    "NetworkLoadBalancerListenerFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkLoadBalancerListenerFactsHelperCustom,
    NetworkLoadBalancerListenerFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_load_balancer_id=dict(type="str", required=True),
            listener_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="listener",
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

    module.exit_json(listeners=result)


if __name__ == "__main__":
    main()

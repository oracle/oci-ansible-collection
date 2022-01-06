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
module: oci_network_load_balancer_backend_facts
short_description: Fetches details about one or multiple Backend resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Backend resources in Oracle Cloud Infrastructure
    - Lists the backend servers for a given network load balancer and backend set.
    - If I(backend_name) is specified, the details of a single Backend will be returned.
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
            - The name of the backend set that includes the backend server.
            - "Example: `example_backend_set`"
        type: str
        required: true
    backend_name:
        description:
            - The name of the backend server to retrieve. This is specified as <ip>:<port>, or as <ip> <OCID>:<port>.
            - "Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`"
            - Required to get a specific backend.
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
- name: Get a specific backend
  oci_network_load_balancer_backend_facts:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: backend_set_name_example
    backend_name: backend_name_example

- name: List backends
  oci_network_load_balancer_backend_facts:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: backend_set_name_example

    # optional
    sort_order: ASC

"""

RETURN = """
backends:
    description:
        - List of Backend resources
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
                - "Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress
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
    sample: [{
        "name": "name_example",
        "ip_address": "ip_address_example",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "port": 56,
        "weight": 56,
        "is_drain": true,
        "is_backup": true,
        "is_offline": true
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


class NetworkLoadBalancerBackendFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "network_load_balancer_id",
            "backend_set_name",
            "backend_name",
        ]

    def get_required_params_for_list(self):
        return [
            "network_load_balancer_id",
            "backend_set_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
            backend_name=self.module.params.get("backend_name"),
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
            self.client.list_backends,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
            **optional_kwargs
        )


NetworkLoadBalancerBackendFactsHelperCustom = get_custom_class(
    "NetworkLoadBalancerBackendFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkLoadBalancerBackendFactsHelperCustom,
    NetworkLoadBalancerBackendFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str", required=True),
            backend_set_name=dict(type="str", required=True),
            backend_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backend",
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

    module.exit_json(backends=result)


if __name__ == "__main__":
    main()

#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_loadbalancer_backend_facts
short_description: Fetches details about one or multiple Backend resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Backend resources in Oracle Cloud Infrastructure
    - Lists the backend servers for a given load balancer and backend set.
    - If I(backend_name) is specified, the details of a single Backend will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    backend_name:
        description:
            - The IP address and port of the backend server to retrieve.
            - "Example: `10.0.0.3:8080`"
            - Required to get a specific backend.
        type: str
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer associated with the backend set and
              server.
        type: str
        aliases: ["id"]
        required: true
    backend_set_name:
        description:
            - The name of the backend set that includes the backend server.
            - "Example: `example_backend_set`"
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific backend
  oci_loadbalancer_backend_facts:
    # required
    backend_name: backend_name_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: backend_set_name_example

- name: List backends
  oci_loadbalancer_backend_facts:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: backend_set_name_example

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
                - A read-only field showing the IP address and port that uniquely identify this backend server in the backend set.
                - "Example: `10.0.0.3:8080`"
            returned: on success
            type: str
            sample: name_example
        ip_address:
            description:
                - The IP address of the backend server.
                - "Example: `10.0.0.3`"
            returned: on success
            type: str
            sample: ip_address_example
        port:
            description:
                - The communication port for the backend server.
                - "Example: `8080`"
            returned: on success
            type: int
            sample: 56
        weight:
            description:
                - The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
                  proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
                  as a server weighted '1'.
                  For more information on load balancing policies, see
                  L(How Load Balancing Policies Work,https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm).
                - "Example: `3`"
            returned: on success
            type: int
            sample: 56
        drain:
            description:
                - "Whether the load balancer should drain this server. Servers marked \\"drain\\" receive no new
                  incoming traffic."
                - "Example: `false`"
            returned: on success
            type: bool
            sample: true
        backup:
            description:
                - "Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
                  traffic to this backend server unless all other backend servers not marked as \\"backup\\" fail the health check policy."
                - "**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy."
                - "Example: `false`"
            returned: on success
            type: bool
            sample: true
        offline:
            description:
                - Whether the load balancer should treat this server as offline. Offline servers receive no incoming
                  traffic.
                - "Example: `false`"
            returned: on success
            type: bool
            sample: true
    sample: [{
        "name": "name_example",
        "ip_address": "ip_address_example",
        "port": 56,
        "weight": 56,
        "drain": true,
        "backup": true,
        "offline": true
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackendFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "backend_set_name",
            "backend_name",
        ]

    def get_required_params_for_list(self):
        return [
            "load_balancer_id",
            "backend_set_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
            backend_name=self.module.params.get("backend_name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_backends,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
            **optional_kwargs
        )


BackendFactsHelperCustom = get_custom_class("BackendFactsHelperCustom")


class ResourceFactsHelper(BackendFactsHelperCustom, BackendFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            backend_name=dict(type="str"),
            load_balancer_id=dict(aliases=["id"], type="str", required=True),
            backend_set_name=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backend",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
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

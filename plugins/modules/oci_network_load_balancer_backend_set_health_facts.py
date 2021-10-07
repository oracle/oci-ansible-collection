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
module: oci_network_load_balancer_backend_set_health_facts
short_description: Fetches details about a BackendSetHealth resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a BackendSetHealth resource in Oracle Cloud Infrastructure
    - Retrieves the health status for the specified backend set.
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
            - The name of the backend set for which to retrieve the health status.
            - "Example: `example_backend_set`"
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific backend_set_health
  oci_network_load_balancer_backend_set_health_facts:
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: example_backend_set

"""

RETURN = """
backend_set_health:
    description:
        - BackendSetHealth resource
    returned: on success
    type: complex
    contains:
        status:
            description:
                - Overall health status of the backend set.
                - "*  **OK:** All backend servers in the backend set return a status of `OK`."
                - "*  **WARNING:** Half or more of the backend servers in a backend set return a status of `OK` and at least one backend
                  server returns a status of `WARNING`, `CRITICAL`, or `UNKNOWN`."
                - "*  **CRITICAL:** Fewer than half of the backend servers in a backend set return a status of `OK`."
                - "*  **UNKNOWN:** If no probes have yet been sent to the backends, or the system is
                  unable to retrieve metrics from the backends."
            returned: on success
            type: str
            sample: OK
        warning_state_backend_names:
            description:
                - A list of backend servers that are currently in the `WARNING` health state. The list identifies each backend server by
                  IP address or OCID and port.
                - "Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`"
            returned: on success
            type: list
            sample: []
        critical_state_backend_names:
            description:
                - A list of backend servers that are currently in the `CRITICAL` health state. The list identifies each backend server by
                  IP address and port.
                - "Example: `10.0.0.4:8080`"
            returned: on success
            type: list
            sample: []
        unknown_state_backend_names:
            description:
                - A list of backend servers that are currently in the `UNKNOWN` health state. The list identifies each backend server by
                  IP address and port.
                - "Example: `10.0.0.5:8080`"
            returned: on success
            type: list
            sample: []
        total_backend_count:
            description:
                - The total number of backend servers in this backend set.
                - "Example: `7`"
            returned: on success
            type: int
            sample: 7
    sample: {
        "status": "OK",
        "warning_state_backend_names": [],
        "critical_state_backend_names": [],
        "unknown_state_backend_names": [],
        "total_backend_count": 7
    }
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


class NetworkLoadBalancerBackendSetHealthFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "network_load_balancer_id",
            "backend_set_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend_set_health,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
        )


NetworkLoadBalancerBackendSetHealthFactsHelperCustom = get_custom_class(
    "NetworkLoadBalancerBackendSetHealthFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkLoadBalancerBackendSetHealthFactsHelperCustom,
    NetworkLoadBalancerBackendSetHealthFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str", required=True),
            backend_set_name=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backend_set_health",
        service_client_class=NetworkLoadBalancerClient,
        namespace="network_load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(backend_set_health=result)


if __name__ == "__main__":
    main()

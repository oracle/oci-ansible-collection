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
module: oci_network_load_balancer_backend_health_facts
short_description: Fetches details about a BackendHealth resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a BackendHealth resource in Oracle Cloud Infrastructure
    - Retrieves the current health status of the specified backend server.
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
            - The name of the backend set associated with the backend server for which to retrieve the health status.
            - "Example: `example_backend_set`"
        type: str
        required: true
    backend_name:
        description:
            - The name of the backend server for which to retrieve the health status, specified as <ip>:<port> or as <ip> <OCID>:<port>.
            - "Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`"
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific backend_health
  oci_network_load_balancer_backend_health_facts:
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: example_backend_set
    backend_name: 10.0.0.3:8080

"""

RETURN = """
backend_health:
    description:
        - BackendHealth resource
    returned: on success
    type: complex
    contains:
        status:
            description:
                - The general health status of the specified backend server.
                - "*   **OK:**  All health check probes return `OK`"
                - "*   **WARNING:** At least one of the health check probes does not return `OK`"
                - "*   **CRITICAL:** None of the health check probes return `OK`.
                  *
                  *   **UNKNOWN:** One of the health checks probes return `UNKNOWN`,
                  *   or the system is unable to retrieve metrics at this time."
            returned: on success
            type: str
            sample: OK
        health_check_results:
            description:
                - A list of the most recent health check results returned for the specified backend server.
            returned: on success
            type: complex
            contains:
                timestamp:
                    description:
                        - The date and time the data was retrieved, in the format defined by RFC3339.
                        - "Example: `2020-05-01T18:28:11+00:00`"
                    returned: on success
                    type: str
                    sample: "2020-05-01T18:28:11+00:00"
                health_check_status:
                    description:
                        - The result of the most recent health check.
                    returned: on success
                    type: str
                    sample: OK
    sample: {
        "status": "OK",
        "health_check_results": [{
            "timestamp": "2020-05-01T18:28:11+00:00",
            "health_check_status": "OK"
        }]
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


class NetworkLoadBalancerBackendHealthFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "network_load_balancer_id",
            "backend_set_name",
            "backend_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend_health,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
            backend_name=self.module.params.get("backend_name"),
        )


NetworkLoadBalancerBackendHealthFactsHelperCustom = get_custom_class(
    "NetworkLoadBalancerBackendHealthFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkLoadBalancerBackendHealthFactsHelperCustom,
    NetworkLoadBalancerBackendHealthFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str", required=True),
            backend_set_name=dict(type="str", required=True),
            backend_name=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backend_health",
        service_client_class=NetworkLoadBalancerClient,
        namespace="network_load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(backend_health=result)


if __name__ == "__main__":
    main()

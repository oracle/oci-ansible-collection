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
module: oci_loadbalancer_backend_set_health_facts
short_description: Fetches details about a BackendSetHealth resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a BackendSetHealth resource in Oracle Cloud Infrastructure
    - Gets the health status for the specified backend set.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer associated with the backend set health
              status to be retrieved.
        type: str
        aliases: ["id"]
        required: true
    backend_set_name:
        description:
            - The name of the backend set to retrieve the health status for.
            - "Example: `example_backend_set`"
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific backend_set_health
  oci_loadbalancer_backend_set_health_facts:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: backend_set_name_example

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
                - "*  **WARNING:** Half or more of the backend set's backend servers return a status of `OK` and at least one backend
                  server returns a status of `WARNING`, `CRITICAL`, or `UNKNOWN`."
                - "*  **CRITICAL:** Fewer than half of the backend set's backend servers return a status of `OK`."
                - "*  **UNKNOWN:** More than half of the backend set's backend servers return a status of `UNKNOWN`, the system was
                  unable to retrieve metrics, or the backend set does not have a listener attached."
            returned: on success
            type: str
            sample: OK
        warning_state_backend_names:
            description:
                - A list of backend servers that are currently in the `WARNING` health state. The list identifies each backend server by
                  IP address and port.
                - "Example: `10.0.0.3:8080`"
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
            sample: 56
    sample: {
        "status": "OK",
        "warning_state_backend_names": [],
        "critical_state_backend_names": [],
        "unknown_state_backend_names": [],
        "total_backend_count": 56
    }
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


class BackendSetHealthFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "backend_set_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend_set_health,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
        )


BackendSetHealthFactsHelperCustom = get_custom_class(
    "BackendSetHealthFactsHelperCustom"
)


class ResourceFactsHelper(
    BackendSetHealthFactsHelperCustom, BackendSetHealthFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(aliases=["id"], type="str", required=True),
            backend_set_name=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backend_set_health",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(backend_set_health=result)


if __name__ == "__main__":
    main()

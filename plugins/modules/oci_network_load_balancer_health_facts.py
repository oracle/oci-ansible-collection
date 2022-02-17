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
module: oci_network_load_balancer_health_facts
short_description: Fetches details about one or multiple NetworkLoadBalancerHealth resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NetworkLoadBalancerHealth resources in Oracle Cloud Infrastructure
    - Lists the summary health statuses for all network load balancers in the specified compartment.
    - If I(network_load_balancer_id) is specified, the details of a single NetworkLoadBalancerHealth will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
            - Required to get a specific network_load_balancer_health.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the network load balancers to
              list.
            - Required to list multiple network_load_balancer_healths.
        type: str
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
- name: Get a specific network_load_balancer_health
  oci_network_load_balancer_health_facts:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: List network_load_balancer_healths
  oci_network_load_balancer_health_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
network_load_balancer_healths:
    description:
        - List of NetworkLoadBalancerHealth resources
    returned: on success
    type: complex
    contains:
        status:
            description:
                - The overall health status of the network load balancer.
                - "*  **OK:** All backend sets associated with the network load balancer return a status of `OK`."
                - "*  **WARNING:** At least one of the backend sets associated with the network load balancer returns a status of `WARNING`,
                  no backend sets return a status of `CRITICAL`, and the network load balancer life cycle state is `ACTIVE`."
                - "*  **CRITICAL:** One or more of the backend sets associated with the network load balancer return a status of `CRITICAL`."
                - "*  **UNKNOWN:** If any one of the following conditions is true:"
                - "   *  The network load balancer life cycle state is not `ACTIVE`."
                - "   *  No backend sets are defined for the network load balancer."
                - "   *  More than half of the backend sets associated with the network load balancer return a status of `UNKNOWN`, none of the backend
                         sets return a status of `WARNING` or `CRITICAL`, and the network load balancer life cycle state is `ACTIVE`."
                - "   *  The system could not retrieve metrics for any reason."
            returned: on success
            type: str
            sample: OK
        warning_state_backend_set_names:
            description:
                - A list of backend sets that are currently in the `WARNING` health state. The list identifies each backend set by the
                  user-friendly name you assigned when you created the backend set.
                - "Example: `example_backend_set3`"
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        critical_state_backend_set_names:
            description:
                - A list of backend sets that are currently in the `CRITICAL` health state. The list identifies each backend set by the
                  user-friendly name you assigned when you created the backend set.
                - "Example: `example_backend_set`"
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        unknown_state_backend_set_names:
            description:
                - A list of backend sets that are currently in the `UNKNOWN` health state. The list identifies each backend set by the
                  user-friendly name you assigned when you created the backend set.
                - "Example: `example_backend_set2`"
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        total_backend_set_count:
            description:
                - The total number of backend sets associated with this network load balancer.
                - "Example: `4`"
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        network_load_balancer_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer with which the health status
                  is associated.
                - Returned for list operation
            returned: on success
            type: str
            sample: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "status": "OK",
        "warning_state_backend_set_names": [],
        "critical_state_backend_set_names": [],
        "unknown_state_backend_set_names": [],
        "total_backend_set_count": 56,
        "network_load_balancer_id": "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
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


class NetworkLoadBalancerHealthFactsHelperGen(OCIResourceFactsHelperBase):
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
            self.client.get_network_load_balancer_health,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_network_load_balancer_healths,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


NetworkLoadBalancerHealthFactsHelperCustom = get_custom_class(
    "NetworkLoadBalancerHealthFactsHelperCustom"
)


class ResourceFactsHelper(
    NetworkLoadBalancerHealthFactsHelperCustom, NetworkLoadBalancerHealthFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="network_load_balancer_health",
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

    module.exit_json(network_load_balancer_healths=result)


if __name__ == "__main__":
    main()

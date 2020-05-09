#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_loadbalancer_health_facts
short_description: Fetches details about one or multiple LoadBalancerHealth resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LoadBalancerHealth resources in Oracle Cloud Infrastructure
    - Lists the summary health statuses for all load balancers in the specified compartment.
    - If I(load_balancer_id) is specified, the details of a single LoadBalancerHealth will be returned.
version_added: "2.5"
options:
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer to return health status for.
            - Required to get a specific load_balancer_health.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the load balancers to return
              health status information for.
            - Required to list multiple load_balancer_healths.
        type: str
        aliases: ["id"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List load_balancer_healths
  oci_loadbalancer_health_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific load_balancer_health
  oci_loadbalancer_health_facts:
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
load_balancer_healths:
    description:
        - List of LoadBalancerHealth resources
    returned: on success
    type: complex
    contains:
        status:
            description:
                - The overall health status of the load balancer.
                - "*  **OK:** All backend sets associated with the load balancer return a status of `OK`."
                - "*  **WARNING:** At least one of the backend sets associated with the load balancer returns a status of `WARNING`,
                  no backend sets return a status of `CRITICAL`, and the load balancer life cycle state is `ACTIVE`."
                - "*  **CRITICAL:** One or more of the backend sets associated with the load balancer return a status of `CRITICAL`."
                - "*  **UNKNOWN:** If any one of the following conditions is true:"
                - "   *  The load balancer life cycle state is not `ACTIVE`."
                - "   *  No backend sets are defined for the load balancer."
                - "   *  More than half of the backend sets associated with the load balancer return a status of `UNKNOWN`, none of the backend
                         sets return a status of `WARNING` or `CRITICAL`, and the load balancer life cycle state is `ACTIVE`."
                - "   *  The system could not retrieve metrics for any reason."
            returned: on success
            type: string
            sample: OK
        warning_state_backend_set_names:
            description:
                - A list of backend sets that are currently in the `WARNING` health state. The list identifies each backend set by the
                  friendly name you assigned when you created it.
                - "Example: `example_backend_set3`"
            returned: on success
            type: list
            sample: []
        critical_state_backend_set_names:
            description:
                - A list of backend sets that are currently in the `CRITICAL` health state. The list identifies each backend set by the
                  friendly name you assigned when you created it.
                - "Example: `example_backend_set`"
            returned: on success
            type: list
            sample: []
        unknown_state_backend_set_names:
            description:
                - A list of backend sets that are currently in the `UNKNOWN` health state. The list identifies each backend set by the
                  friendly name you assigned when you created it.
                - "Example: `example_backend_set2`"
            returned: on success
            type: list
            sample: []
        total_backend_set_count:
            description:
                - The total number of backend sets associated with this load balancer.
                - "Example: `4`"
            returned: on success
            type: int
            sample: 4
        load_balancer_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer the health status is associated with.
            returned: on success
            type: string
            sample: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
    sample: [{
        "status": "OK",
        "warning_state_backend_set_names": [],
        "critical_state_backend_set_names": [],
        "unknown_state_backend_set_names": [],
        "total_backend_set_count": 4,
        "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LoadBalancerHealthFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_load_balancer_health,
            load_balancer_id=self.module.params.get("load_balancer_id"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_load_balancer_healths,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LoadBalancerHealthFactsHelperCustom = get_custom_class(
    "LoadBalancerHealthFactsHelperCustom"
)


class ResourceFactsHelper(
    LoadBalancerHealthFactsHelperCustom, LoadBalancerHealthFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(aliases=["id"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="load_balancer_health",
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

    module.exit_json(load_balancer_healths=result)


if __name__ == "__main__":
    main()

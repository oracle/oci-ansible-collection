#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["deprecated"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_load_balancer_routing_policy_facts
short_description: Fetches details about one or multiple RoutingPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RoutingPolicy resources in Oracle Cloud Infrastructure
    - Lists all routing policies associated with the specified load balancer.
    - If I(routing_policy_name) is specified, the details of a single RoutingPolicy will be returned.
version_added: "2.9.0"
deprecated:
    removed_in: "3.0.0"
    why: The naming and the return value in the module is confusing and not consistent with other modules in the collection.
    alternative: Use M(oci_loadbalancer_routing_policy_facts) instead.
author: Oracle (@oracle)
options:
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the specified load balancer.
        type: str
        required: true
    routing_policy_name:
        description:
            - The name of the routing policy to retrieve.
            - "Example: `example_routing_policy`"
            - Required to get a specific routing_policy.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List routing_policies
  oci_load_balancer_routing_policy_facts:
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific routing_policy
  oci_load_balancer_routing_policy_facts:
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
    routing_policy_name: example_routing_policy

"""

RETURN = """
routing_policies:
    description:
        - List of RoutingPolicy resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The unique name for this list of routing rules. Avoid entering confidential information.
                - "Example: `example_routing_policy`"
            returned: on success
            type: str
            sample: example_routing_policy
        condition_language_version:
            description:
                - The version of the language in which `condition` of `rules` are composed.
            returned: on success
            type: str
            sample: V1
        rules:
            description:
                - The ordered list of routing rules.
            returned: on success
            type: complex
            elements: dict
            contains:
                name:
                    description:
                        - A unique name for the routing policy rule. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: name_example
                condition:
                    description:
                        - A routing rule to evaluate defined conditions against the incoming HTTP request and perform an action.
                    returned: on success
                    type: str
                    sample: condition_example
                actions:
                    description:
                        - A list of actions to be applied when conditions of the routing rule are met.
                    returned: on success
                    type: complex
                    elements: dict
                    contains:
                        name:
                            description:
                                - ""
                            returned: on success
                            type: str
                            sample: FORWARD_TO_BACKENDSET
                        backend_set_name:
                            description:
                                - Name of the backend set the listener will forward the traffic to.
                                - "Example: `backendSetForImages`"
                            returned: on success
                            type: str
                            sample: backendSetForImages
    sample: [{
        "name": "example_routing_policy",
        "condition_language_version": "V1",
        "rules": [{
            "name": "name_example",
            "condition": "condition_example",
            "actions": [{
                "name": "FORWARD_TO_BACKENDSET",
                "backend_set_name": "backendSetForImages"
            }]
        }]
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


class RoutingPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "routing_policy_name",
        ]

    def get_required_params_for_list(self):
        return [
            "load_balancer_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_routing_policy,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            routing_policy_name=self.module.params.get("routing_policy_name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_routing_policies,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            **optional_kwargs
        )


RoutingPolicyFactsHelperCustom = get_custom_class("RoutingPolicyFactsHelperCustom")


class ResourceFactsHelper(RoutingPolicyFactsHelperCustom, RoutingPolicyFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(type="str", required=True),
            routing_policy_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="routing_policy",
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

    module.exit_json(routing_policies=result)


if __name__ == "__main__":
    main()

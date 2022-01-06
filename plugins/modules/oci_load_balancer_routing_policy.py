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
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_load_balancer_routing_policy
short_description: Manage a RoutingPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a RoutingPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), adds a routing policy to a load balancer. For more information, see
      L(Managing Request Routing,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm).
version_added: "2.9.0"
deprecated:
    removed_in: "3.0.0"
    why: The naming and the return value in the module is confusing and not consistent with other modules in the collection.
    alternative: Use M(oci_loadbalancer_routing_policy) instead.
author: Oracle (@oracle)
options:
    name:
        description:
            - The name for this list of routing rules. It must be unique and it cannot be changed. Avoid entering
              confidential information.
            - "Example: `example_routing_rules`"
        type: str
        required: true
    condition_language_version:
        description:
            - The version of the language in which `condition` of `rules` are composed.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "V1"
    rules:
        description:
            - The list of routing rules.
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - A unique name for the routing policy rule. Avoid entering confidential information.
                type: str
                required: true
            condition:
                description:
                    - A routing rule to evaluate defined conditions against the incoming HTTP request and perform an action.
                type: str
                required: true
            actions:
                description:
                    - A list of actions to be applied when conditions of the routing rule are met.
                type: list
                elements: dict
                required: true
                suboptions:
                    name:
                        description:
                            - ""
                        type: str
                        choices:
                            - "FORWARD_TO_BACKENDSET"
                        required: true
                    backend_set_name:
                        description:
                            - Name of the backend set the listener will forward the traffic to.
                            - "Example: `backendSetForImages`"
                        type: str
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer to add the routing policy rule list to.
        type: str
        required: true
    state:
        description:
            - The state of the RoutingPolicy.
            - Use I(state=present) to create or update a RoutingPolicy.
            - Use I(state=absent) to delete a RoutingPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create routing_policy
  oci_load_balancer_routing_policy:
    name: example_routing_rules
    condition_language_version: V1
    rules:
    - name: name_example
      condition: condition_example
      actions:
      - name: FORWARD_TO_BACKENDSET
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

- name: Update routing_policy
  oci_load_balancer_routing_policy:
    name: example_routing_rules
    condition_language_version: V1
    rules:
    - name: name_example
      condition: condition_example
      actions:
      - name: FORWARD_TO_BACKENDSET
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete routing_policy
  oci_load_balancer_routing_policy:
    name: example_routing_rules
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
routing_policy:
    description:
        - Details of the RoutingPolicy resource acted upon by the current operation
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
    sample: {
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.load_balancer import LoadBalancerClient
    from oci.load_balancer.models import CreateRoutingPolicyDetails
    from oci.load_balancer.models import UpdateRoutingPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RoutingPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_routing_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_routing_policy,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            routing_policy_name=self.module.params.get("name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "load_balancer_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_routing_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateRoutingPolicyDetails

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_routing_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_routing_policy_details=create_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateRoutingPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_routing_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_routing_policy_details=update_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
                routing_policy_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_routing_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                routing_policy_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


RoutingPolicyHelperCustom = get_custom_class("RoutingPolicyHelperCustom")


class ResourceHelper(RoutingPolicyHelperCustom, RoutingPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str", required=True),
            condition_language_version=dict(type="str", choices=["V1"]),
            rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    condition=dict(type="str", required=True),
                    actions=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                                choices=["FORWARD_TO_BACKENDSET"],
                            ),
                            backend_set_name=dict(type="str"),
                        ),
                    ),
                ),
            ),
            load_balancer_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="routing_policy",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

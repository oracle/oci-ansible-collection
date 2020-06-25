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
module: oci_loadbalancer_rule_set
short_description: Manage a RuleSet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a RuleSet resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new rule set associated with the specified load balancer. For more information, see
      L(Managing Rule Sets,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the specified load balancer.
        type: str
        required: true
    name:
        description:
            - The name for this set of rules. It must be unique and it cannot be changed. Avoid entering
              confidential information.
            - "Example: `example_rule_set`"
        type: str
        required: true
    items:
        description:
            - An array of rules that compose the rule set.
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: list
        suboptions:
            action:
                description:
                    - ""
                type: str
                choices:
                    - "ADD_HTTP_REQUEST_HEADER"
                    - "REMOVE_HTTP_REQUEST_HEADER"
                    - "EXTEND_HTTP_REQUEST_HEADER_VALUE"
                    - "REMOVE_HTTP_RESPONSE_HEADER"
                    - "ADD_HTTP_RESPONSE_HEADER"
                    - "EXTEND_HTTP_RESPONSE_HEADER_VALUE"
                required: true
            header:
                description:
                    - A header name that conforms to RFC 7230.
                    - "Example: `example_header_name`"
                type: str
                required: true
            value:
                description:
                    - A header value that conforms to RFC 7230.
                    - "Example: `example_value`"
                    - Required when action is one of ['ADD_HTTP_RESPONSE_HEADER', 'ADD_HTTP_REQUEST_HEADER']
                type: str
            prefix:
                description:
                    - A string to prepend to the header value. The resulting header value must conform to RFC 7230.
                    - "Example: `example_prefix_value`"
                    - Applicable when action is one of ['EXTEND_HTTP_REQUEST_HEADER_VALUE', 'EXTEND_HTTP_RESPONSE_HEADER_VALUE']
                type: str
            suffix:
                description:
                    - A string to append to the header value. The resulting header value must conform to RFC 7230.
                    - "Example: `example_suffix_value`"
                    - Applicable when action is one of ['EXTEND_HTTP_REQUEST_HEADER_VALUE', 'EXTEND_HTTP_RESPONSE_HEADER_VALUE']
                type: str
    state:
        description:
            - The state of the RuleSet.
            - Use I(state=present) to create or update a RuleSet.
            - Use I(state=absent) to delete a RuleSet.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create rule_set
  oci_loadbalancer_rule_set:
    name: example_rule_set
    items:
    - action: ADD_HTTP_REQUEST_HEADER
      header: example_header_name
      value: example_value
    - action: EXTEND_HTTP_REQUEST_HEADER_VALUE
      header: example_header_name2
      prefix: example_prefix_value
      suffix: example_suffix_value
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

- name: Update rule_set
  oci_loadbalancer_rule_set:
    items:
    - action: ADD_HTTP_REQUEST_HEADER
      header: example_header_name
      value: example_value
    - action: EXTEND_HTTP_REQUEST_HEADER_VALUE
      header: example_header_name2
      prefix: example_prefix_value
      suffix: example_suffix_value
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete rule_set
  oci_loadbalancer_rule_set:
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
    name: example_rule_set
    state: absent

"""

RETURN = """
rule_set:
    description:
        - Details of the RuleSet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name for this set of rules. It must be unique and it cannot be changed. Avoid entering
                  confidential information.
                - "Example: `example_rule_set`"
            returned: on success
            type: string
            sample: example_rule_set
        items:
            description:
                - An array of rules that compose the rule set.
            returned: on success
            type: complex
            contains:
                action:
                    description:
                        - ""
                    returned: on success
                    type: string
                    sample: ADD_HTTP_REQUEST_HEADER
                header:
                    description:
                        - A header name that conforms to RFC 7230.
                        - "Example: `example_header_name`"
                    returned: on success
                    type: string
                    sample: example_header_name
                value:
                    description:
                        - A header value that conforms to RFC 7230.
                        - "Example: `example_value`"
                    returned: on success
                    type: string
                    sample: example_value
                prefix:
                    description:
                        - A string to prepend to the header value. The resulting header value must conform to RFC 7230.
                        - "Example: `example_prefix_value`"
                    returned: on success
                    type: string
                    sample: example_prefix_value
                suffix:
                    description:
                        - A string to append to the header value. The resulting header value must conform to RFC 7230.
                        - "Example: `example_suffix_value`"
                    returned: on success
                    type: string
                    sample: example_suffix_value
    sample: {
        "name": "example_rule_set",
        "items": [{
            "action": "ADD_HTTP_REQUEST_HEADER",
            "header": "example_header_name",
            "value": "example_value",
            "prefix": "example_prefix_value",
            "suffix": "example_suffix_value"
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
    from oci.load_balancer.models import CreateRuleSetDetails
    from oci.load_balancer.models import UpdateRuleSetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RuleSetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_rule_set

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rule_set,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            rule_set_name=self.module.params.get("name"),
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
        return oci_common_utils.list_all_resources(self.client.list_rule_sets, **kwargs)

    def get_create_model_class(self):
        return CreateRuleSetDetails

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
            call_fn=self.client.create_rule_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                create_rule_set_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateRuleSetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_rule_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                rule_set_name=self.module.params.get("name"),
                update_rule_set_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_rule_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                rule_set_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


RuleSetHelperCustom = get_custom_class("RuleSetHelperCustom")


class ResourceHelper(RuleSetHelperCustom, RuleSetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            load_balancer_id=dict(type="str", required=True),
            name=dict(type="str", required=True),
            items=dict(
                type="list",
                elements="dict",
                options=dict(
                    action=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ADD_HTTP_REQUEST_HEADER",
                            "REMOVE_HTTP_REQUEST_HEADER",
                            "EXTEND_HTTP_REQUEST_HEADER_VALUE",
                            "REMOVE_HTTP_RESPONSE_HEADER",
                            "ADD_HTTP_RESPONSE_HEADER",
                            "EXTEND_HTTP_RESPONSE_HEADER_VALUE",
                        ],
                    ),
                    header=dict(type="str", required=True),
                    value=dict(type="str"),
                    prefix=dict(type="str"),
                    suffix=dict(type="str"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="rule_set",
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

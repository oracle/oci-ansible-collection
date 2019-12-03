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
module: oci_loadbalancer_rule_set_facts
short_description: Fetches details about one or multiple RuleSet resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RuleSet resources in Oracle Cloud Infrastructure
    - Lists all rule sets associated with the specified load balancer.
    - If I(rule_set_name) is specified, the details of a single RuleSet will be returned.
version_added: "2.5"
options:
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the specified load balancer.
        type: str
        required: true
    rule_set_name:
        description:
            - The name of the rule set to retrieve.
            - "Example: `example_rule_set`"
            - Required to get a specific rule_set.
        type: str
        aliases: ["name"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List rule_sets
  oci_loadbalancer_rule_set_facts:
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific rule_set
  oci_loadbalancer_rule_set_facts:
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
    rule_set_name: example_rule_set

"""

RETURN = """
rule_sets:
    description:
        - List of RuleSet resources
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
    sample: [{
        "name": "example_rule_set",
        "items": [{
            "action": "ADD_HTTP_REQUEST_HEADER",
            "header": "example_header_name",
            "value": "example_value",
            "prefix": "example_prefix_value",
            "suffix": "example_suffix_value"
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


class RuleSetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "rule_set_name",
        ]

    def get_required_params_for_list(self):
        return [
            "load_balancer_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rule_set,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            rule_set_name=self.module.params.get("rule_set_name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_rule_sets,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            **optional_kwargs
        )


RuleSetFactsHelperCustom = get_custom_class("RuleSetFactsHelperCustom")


class ResourceFactsHelper(RuleSetFactsHelperCustom, RuleSetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(type="str", required=True),
            rule_set_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="rule_set",
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

    module.exit_json(rule_sets=result)


if __name__ == "__main__":
    main()

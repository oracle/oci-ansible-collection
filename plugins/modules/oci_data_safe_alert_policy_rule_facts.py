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
module: oci_data_safe_alert_policy_rule_facts
short_description: Fetches details about one or multiple AlertPolicyRule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AlertPolicyRule resources in Oracle Cloud Infrastructure
    - "Lists the rules of the specified alert policy. The alert policy is said to be satisfied when all rules in the policy evaulate to true.
      If there are three rules: rule1,rule2 and rule3, the policy is satisfied if rule1 AND rule2 AND rule3 is True."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    alert_policy_id:
        description:
            - The OCID of the alert policy.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List alert_policy_rules
  oci_data_safe_alert_policy_rule_facts:
    # required
    alert_policy_id: "ocid1.alertpolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
alert_policy_rules:
    description:
        - List of AlertPolicyRule resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The unique key of the alert policy rule.
            returned: on success
            type: str
            sample: key_example
        description:
            description:
                - Describes the alert policy rule.
            returned: on success
            type: str
            sample: description_example
        expression:
            description:
                - The conditional expression of the alert policy rule which evaluates to boolean value.
            returned: on success
            type: str
            sample: expression_example
    sample: [{
        "key": "key_example",
        "description": "description_example",
        "expression": "expression_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeAlertPolicyRuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "alert_policy_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_alert_policy_rules,
            alert_policy_id=self.module.params.get("alert_policy_id"),
            **optional_kwargs
        )


DataSafeAlertPolicyRuleFactsHelperCustom = get_custom_class(
    "DataSafeAlertPolicyRuleFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSafeAlertPolicyRuleFactsHelperCustom, DataSafeAlertPolicyRuleFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(alert_policy_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="alert_policy_rule",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(alert_policy_rules=result)


if __name__ == "__main__":
    main()

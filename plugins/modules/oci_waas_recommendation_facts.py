#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_waas_recommendation_facts
short_description: Fetches details about one or multiple WaasRecommendation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WaasRecommendation resources in Oracle Cloud Infrastructure
    - Gets the list of recommended Web Application Firewall protection rules.
    - Use the `POST /waasPolicies/{waasPolicyId}/actions/acceptWafConfigRecommendations` method to accept recommended Web Application Firewall protection rules.
      For more information, see L(WAF Protection Rules,https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/wafprotectionrules.htm).
      The list is sorted by `key`, in ascending order.
version_added: "2.9"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        required: true
    recommended_action:
        description:
            - A filter that matches recommended protection rules based on the selected action. If unspecified, rules with any action type are returned.
        type: str
        choices:
            - "DETECT"
            - "BLOCK"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List waas_recommendations
  oci_waas_recommendation_facts:
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
waas_recommendations:
    description:
        - List of WaasRecommendation resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The unique key for the recommended protection rule.
            returned: on success
            type: string
            sample: key_example
        mod_security_rule_ids:
            description:
                - The list of the ModSecurity rule IDs associated with the protection rule.
                  For more information about ModSecurity's open source WAF rules, see L(Mod Security's
                  documentation,https://www.modsecurity.org/CRS/Documentation/index.html).
            returned: on success
            type: list
            sample: []
        name:
            description:
                - The name of the recommended protection rule.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - The description of the recommended protection rule.
            returned: on success
            type: string
            sample: description_example
        labels:
            description:
                - The list of labels for the recommended protection rule.
            returned: on success
            type: list
            sample: []
        recommended_action:
            description:
                - The recommended action to apply to the protection rule.
            returned: on success
            type: string
            sample: recommended_action_example
    sample: [{
        "key": "key_example",
        "mod_security_rule_ids": [],
        "name": "name_example",
        "description": "description_example",
        "labels": [],
        "recommended_action": "recommended_action_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WaasRecommendationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "recommended_action",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_recommendations,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


WaasRecommendationFactsHelperCustom = get_custom_class(
    "WaasRecommendationFactsHelperCustom"
)


class ResourceFactsHelper(
    WaasRecommendationFactsHelperCustom, WaasRecommendationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            waas_policy_id=dict(type="str", required=True),
            recommended_action=dict(type="str", choices=["DETECT", "BLOCK"]),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="waas_recommendation",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(waas_recommendations=result)


if __name__ == "__main__":
    main()

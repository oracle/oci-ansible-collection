#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
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
module: oci_waas_recommendation_facts
short_description: Retrieve details about WAAS policy recommendations.
description:
    - This module retrieves information of recommended Web Application Firewall protection rules for a WAAS policy.
version_added: "2.5"
options:
    waas_policy_id:
        description: The OCID of the WAAS policy.
        type: str
        required: true
    recommended_action:
        description: A filter that matches recommended protection rules based on the selected action.
                     If unspecified, rules with any action type are returned.
        type: str
        choices:
            - DETECT
            - BLOCK
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Get the recommendations for a waas policy
  oci_waas_recommendation_facts:
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx

- name: Get the recommendations of specific action for a waas policy
  oci_waas_recommendation_facts:
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx
    recommended_action: DETECT
"""

RETURN = """
waas_recommendations:
    description: List of recommended Web Application Firewall protection rules for a WAAS policy.
    returned: on success
    type: complex
    contains:
        description:
            description: The description of the recommended protection rule.
            returned: success
            type: str
            sample: "Cross-Site Scripting (XSS) Attempt: XSS Filters from IE"
        key:
            description: The unique key for the recommended protection rule.
            returned: success
            type: str
            sample: 941340
        labels:
            description: The list of labels for the recommended protection rule.
            returned: success
            type: list
            sample: [
                "OWASP",
                "OWASP-2017",
                "CRS3",
                "WASCTC",
                "PCI",
                "HTTP",
                "A2",
                "A2-2017",
                "XSS",
                "Cross-Site Scripting"
            ]
        mod_security_rule_ids:
            description: The list of the ModSecurity rule IDs associated with the protection rule.
            returned: success
            type: list
            sample: ["941340"]
        name:
            description: The name of the recommended protection rule.
            returned: success
            type: str
            sample: "Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer"
        recommended_action:
            description: The recommended action to apply to the protection rule.
            returned: success
            type: str
            sample: BLOCK
    sample: [{
            "description": "Cross-Site Scripting (XSS) Attempt: XSS Filters from IE",
            "key": "941340",
            "labels": [
                "OWASP",
                "OWASP-2017",
                "CRS3",
                "WASCTC",
                "PCI",
                "HTTP",
                "A2",
                "A2-2017",
                "XSS",
                "Cross-Site Scripting"
              ],
            "mod_security_rule_ids": ["941340"],
            "name": "Cross-Site Scripting (XSS) Attempt: XSS Filters from Internet Explorer",
            "recommended_action": "BLOCK"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.waas.waas_client import WaasClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def list_recommendations(waas_client, module):
    optional_list_method_params = ["recommended_action"]
    optional_kwargs = dict(
        (param, module.params[param])
        for param in optional_list_method_params
        if module.params.get(param) is not None
    )
    return to_dict(
        oci_utils.list_all_resources(
            waas_client.list_recommendations,
            waas_policy_id=module.params["waas_policy_id"],
            **optional_kwargs
        )
    )


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_display_name=False)
    module_args.update(
        dict(
            waas_policy_id=dict(type="str", required=True),
            recommended_action=dict(type="str", choices=["DETECT", "BLOCK"]),
        )
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    waas_client = oci_utils.create_service_client(module, WaasClient)

    try:
        result = list_recommendations(waas_client, module)
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(waas_recommendations=result)


if __name__ == "__main__":
    main()

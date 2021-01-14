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
module: oci_waas_policy_custom_protection_rules_facts
short_description: Fetches details about one or multiple WaasPolicyCustomProtectionRules resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WaasPolicyCustomProtectionRules resources in Oracle Cloud Infrastructure
    - Gets the list of currently configured custom protection rules for a WAAS policy.
version_added: "2.9"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        required: true
    mod_security_rule_id:
        description:
            - Filter rules using a list of ModSecurity rule IDs.
        type: list
    action:
        description:
            - Filter rules using a list of actions.
        type: list
        choices:
            - "DETECT"
            - "BLOCK"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List waas_policy_custom_protection_rules
  oci_waas_policy_custom_protection_rules_facts:
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
waas_policy_custom_protection_rules:
    description:
        - List of WaasPolicyCustomProtectionRules resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the custom protection rule.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-friendly name of the custom protection rule.
            returned: on success
            type: string
            sample: display_name_example
        action:
            description:
                - "The action to take when the custom protection rule is triggered.
                  `DETECT` - Logs the request when the criteria of the custom protection rule are met. `BLOCK` - Blocks the request when the criteria of the
                  custom protection rule are met."
            returned: on success
            type: string
            sample: DETECT
        mod_security_rule_ids:
            description:
                - The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF rules, see
                  L(Mod Security's documentation,https://www.modsecurity.org/CRS/Documentation/index.html).
            returned: on success
            type: list
            sample: []
        exclusions:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                target:
                    description:
                        - The target of the exclusion.
                    returned: on success
                    type: string
                    sample: REQUEST_COOKIES
                exclusions:
                    description:
                        - ""
                    returned: on success
                    type: list
                    sample: []
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "action": "DETECT",
        "mod_security_rule_ids": [],
        "exclusions": [{
            "target": "REQUEST_COOKIES",
            "exclusions": []
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
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WaasPolicyCustomProtectionRulesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "mod_security_rule_id",
            "action",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_waas_policy_custom_protection_rules,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


WaasPolicyCustomProtectionRulesFactsHelperCustom = get_custom_class(
    "WaasPolicyCustomProtectionRulesFactsHelperCustom"
)


class ResourceFactsHelper(
    WaasPolicyCustomProtectionRulesFactsHelperCustom,
    WaasPolicyCustomProtectionRulesFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            waas_policy_id=dict(type="str", required=True),
            mod_security_rule_id=dict(type="list"),
            action=dict(type="list", choices=["DETECT", "BLOCK"]),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="waas_policy_custom_protection_rules",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(waas_policy_custom_protection_rules=result)


if __name__ == "__main__":
    main()

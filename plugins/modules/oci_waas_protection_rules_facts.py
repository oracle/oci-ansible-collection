#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_waas_protection_rules_facts
short_description: Fetches details about one or multiple ProtectionRules resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ProtectionRules resources in Oracle Cloud Infrastructure
    - Gets the list of available protection rules for a WAAS policy. Use the `GetWafConfig` operation to view a list of currently configured protection rules
      for the Web Application Firewall, or use the `ListRecommendations` operation to get a list of recommended protection rules for the Web Application
      Firewall.
      The list is sorted by `key`, in ascending order.
    - If I(protection_rule_key) is specified, the details of a single ProtectionRules will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    protection_rule_key:
        description:
            - The protection rule key.
            - Required to get a specific protection_rules.
        type: str
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        required: true
    mod_security_rule_id:
        description:
            - Filter rules using a list of ModSecurity rule IDs.
        type: list
        elements: str
    action:
        description:
            - Filter rules using a list of actions.
        type: list
        elements: str
        choices:
            - "OFF"
            - "DETECT"
            - "BLOCK"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific protection_rules
  oci_waas_protection_rules_facts:
    # required
    protection_rule_key: protection_rule_key_example
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

- name: List protection_rules
  oci_waas_protection_rules_facts:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    mod_security_rule_id: [ "ocid1.modsecurityrule.oc1..xxxxxxEXAMPLExxxxxx" ]
    action: [ "OFF" ]

"""

RETURN = """
protection_rules:
    description:
        - List of ProtectionRules resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The unique key of the protection rule.
            returned: on success
            type: str
            sample: key_example
        mod_security_rule_ids:
            description:
                - The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF rules, see
                  L(Mod Security's documentation,https://www.modsecurity.org/CRS/Documentation/index.html).
            returned: on success
            type: list
            sample: []
        name:
            description:
                - The name of the protection rule.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The description of the protection rule.
            returned: on success
            type: str
            sample: description_example
        action:
            description:
                - The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
            returned: on success
            type: str
            sample: OFF
        labels:
            description:
                - The list of labels for the protection rule.
                - "**Note:** Protection rules with a `ResponseBody` label will have no effect unless `isResponseInspected` is true."
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
                    type: str
                    sample: REQUEST_COOKIES
                exclusions:
                    description:
                        - ""
                    returned: on success
                    type: list
                    sample: []
    sample: [{
        "key": "key_example",
        "mod_security_rule_ids": [],
        "name": "name_example",
        "description": "description_example",
        "action": "OFF",
        "labels": [],
        "exclusions": [{
            "target": "REQUEST_COOKIES",
            "exclusions": []
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProtectionRulesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "waas_policy_id",
            "protection_rule_key",
        ]

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
        ]

    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.get_protection_rule,
                waas_policy_id=self.module.params.get("waas_policy_id"),
                protection_rule_key=self.module.params.get("protection_rule_key"),
            )
        )

    def list_resources(self):
        optional_list_method_params = [
            "mod_security_rule_id",
            "action",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_protection_rules,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


ProtectionRulesFactsHelperCustom = get_custom_class("ProtectionRulesFactsHelperCustom")


class ResourceFactsHelper(
    ProtectionRulesFactsHelperCustom, ProtectionRulesFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            protection_rule_key=dict(type="str", no_log=True),
            waas_policy_id=dict(type="str", required=True),
            mod_security_rule_id=dict(type="list", elements="str"),
            action=dict(
                type="list", elements="str", choices=["OFF", "DETECT", "BLOCK"]
            ),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="protection_rules",
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

    module.exit_json(protection_rules=result)


if __name__ == "__main__":
    main()

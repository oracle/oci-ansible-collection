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
module: oci_waas_custom_protection_rule_facts
short_description: Fetches details about one or multiple CustomProtectionRule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CustomProtectionRule resources in Oracle Cloud Infrastructure
    - Gets a list of custom protection rules for the specified Web Application Firewall.
    - If I(custom_protection_rule_id) is specified, the details of a single CustomProtectionRule will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    custom_protection_rule_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the custom protection rule. This number is generated when
              the custom protection rule is added to the compartment.
            - Required to get a specific custom_protection_rule.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This number is generated when the
              compartment is created.
            - Required to list multiple custom_protection_rules.
        type: str
    sort_by:
        description:
            - The value by which custom protection rules are sorted in a paginated 'List' call. If unspecified, defaults to `timeCreated`.
        type: str
        choices:
            - "id"
            - "compartmentId"
            - "displayName"
            - "modSecurityRuleId"
            - "timeCreated"
    sort_order:
        description:
            - The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - Filter custom protection rules using a list of display names.
        type: list
        aliases: ["name"]
    lifecycle_state:
        description:
            - Filter Custom Protection rules using a list of lifecycle states.
        type: list
        choices:
            - "CREATING"
            - "ACTIVE"
            - "FAILED"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
    time_created_greater_than_or_equal_to:
        description:
            - A filter that matches Custom Protection rules created on or after the specified date-time.
        type: str
    time_created_less_than:
        description:
            - A filter that matches custom protection rules created before the specified date-time.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List custom_protection_rules
  oci_waas_custom_protection_rule_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific custom_protection_rule
  oci_waas_custom_protection_rule_facts:
    custom_protection_rule_id: ocid1.customprotectionrule.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
custom_protection_rules:
    description:
        - List of CustomProtectionRule resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the custom protection rule.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the custom protection rule's compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-friendly name of the custom protection rule.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - The description of the custom protection rule.
            returned: on success
            type: string
            sample: description_example
        mod_security_rule_ids:
            description:
                - The auto-generated ID for the custom protection rule. These IDs are referenced in logs.
            returned: on success
            type: list
            sample: []
        template:
            description:
                - The template text of the custom protection rule. All custom protection rules are expressed in ModSecurity Rule Language.
                - Additionally, each rule must include two placeholder variables that are updated by the WAF service upon publication of the rule.
                - "`id: {{id_1}}` - This field is populated with a unique rule ID generated by the WAF service which identifies a `SecRule`. More than one
                  `SecRule` can be defined in the `template` field of a CreateCustomSecurityRule call. The value of the first `SecRule` must be `id: {{id_1}}`
                  and the `id` field of each subsequent `SecRule` should increase by one, as shown in the example."
                - "`ctl:ruleEngine={{mode}}` - The action to be taken when the criteria of the `SecRule` are met, either `OFF`, `DETECT` or `BLOCK`. This field
                  is automatically populated with the corresponding value of the `action` field of the `CustomProtectionRuleSetting` schema when the `WafConfig`
                  is updated."
                - "*Example:*
                    ```
                    SecRule REQUEST_COOKIES \\"regex matching SQL injection - part 1/2\\" \\\\
                            \\"phase:2,                                                 \\\\
                            msg:'Detects chained SQL injection attempts 1/2.',        \\\\
                            id: {{id_1}},                                             \\\\
                            ctl:ruleEngine={{mode}},                                  \\\\
                            deny\\"
                    SecRule REQUEST_COOKIES \\"regex matching SQL injection - part 2/2\\" \\\\
                            \\"phase:2,                                                 \\\\
                            msg:'Detects chained SQL injection attempts 2/2.',        \\\\
                            id: {{id_2}},                                             \\\\
                            ctl:ruleEngine={{mode}},                                  \\\\
                            deny\\"
                    ```"
                - The example contains two `SecRules` each having distinct regex expression to match the `Cookie` header value during the second input analysis
                  phase.
                - For more information about custom protection rules, see L(Custom Protection
                  Rules,https://docs.cloud.oracle.com/Content/WAF/tasks/customprotectionrules.htm).
                - "For more information about ModSecurity syntax, see L(Making Rules: The Basic
                  Syntax,https://www.modsecurity.org/CRS/Documentation/making.html)."
                - For more information about ModSecurity's open source WAF rules, see L(Mod Security's OWASP Core Rule Set
                  documentation,https://www.modsecurity.org/CRS/Documentation/index.html).
            returned: on success
            type: string
            sample: template_example
        lifecycle_state:
            description:
                - The current lifecycle state of the custom protection rule.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - The date and time the protection rule was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: string
            sample: 2018-11-16T21:10:29Z
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "mod_security_rule_ids": [],
        "template": "template_example",
        "lifecycle_state": "CREATING",
        "time_created": "2018-11-16T21:10:29Z",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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


class CustomProtectionRuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "custom_protection_rule_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_protection_rule,
            custom_protection_rule_id=self.module.params.get(
                "custom_protection_rule_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "display_name",
            "lifecycle_state",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_custom_protection_rules,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


CustomProtectionRuleFactsHelperCustom = get_custom_class(
    "CustomProtectionRuleFactsHelperCustom"
)


class ResourceFactsHelper(
    CustomProtectionRuleFactsHelperCustom, CustomProtectionRuleFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            custom_protection_rule_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(
                type="str",
                choices=[
                    "id",
                    "compartmentId",
                    "displayName",
                    "modSecurityRuleId",
                    "timeCreated",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="list"),
            lifecycle_state=dict(
                type="list",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "FAILED",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                ],
            ),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="custom_protection_rule",
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

    module.exit_json(custom_protection_rules=result)


if __name__ == "__main__":
    main()

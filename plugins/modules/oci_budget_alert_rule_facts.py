#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_budget_alert_rule_facts
short_description: Fetches details about one or multiple BudgetAlertRule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BudgetAlertRule resources in Oracle Cloud Infrastructure
    - Returns a list of Alert Rules for a specified Budget.
    - If I(alert_rule_id) is specified, the details of a single BudgetAlertRule will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    budget_id:
        description:
            - The unique Budget OCID
        type: str
        required: true
    alert_rule_id:
        description:
            - The unique Alert Rule OCID
            - Required to get a specific budget_alert_rule.
        type: str
        aliases: ["id"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. If not specified, the default is timeCreated.
              The default sort order for timeCreated is DESC.
              The default sort order for displayName is ASC in alphanumeric order.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    lifecycle_state:
        description:
            - The current state of the resource to filter by.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific budget_alert_rule
  oci_budget_alert_rule_facts:
    # required
    budget_id: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"
    alert_rule_id: "ocid1.alertrule.oc1..xxxxxxEXAMPLExxxxxx"

- name: List budget_alert_rules
  oci_budget_alert_rule_facts:
    # required
    budget_id: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: timeCreated
    lifecycle_state: ACTIVE
    display_name: My new resource

"""

RETURN = """
budget_alert_rules:
    description:
        - List of BudgetAlertRule resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the alert rule
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        budget_id:
            description:
                - The OCID of the budget
            returned: on success
            type: str
            sample: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the alert rule.
            returned: on success
            type: str
            sample: display_name_example
        type:
            description:
                - The type of alert. Valid values are ACTUAL (the alert will trigger based on actual usage) or
                  FORECAST (the alert will trigger based on predicted usage).
            returned: on success
            type: str
            sample: ACTUAL
        threshold:
            description:
                - The threshold for triggering the alert. If thresholdType is PERCENTAGE, the maximum value is 10000.
            returned: on success
            type: float
            sample: 10
        threshold_type:
            description:
                - The type of threshold.
            returned: on success
            type: str
            sample: PERCENTAGE
        lifecycle_state:
            description:
                - The current state of the alert rule.
            returned: on success
            type: str
            sample: ACTIVE
        message:
            description:
                - Custom message sent when alert is triggered
            returned: on success
            type: str
            sample: message_example
        description:
            description:
                - The description of the alert rule.
            returned: on success
            type: str
            sample: description_example
        version:
            description:
                - Version of the alert rule. Starts from 1 and increments by 1.
            returned: on success
            type: int
            sample: 56
        recipients:
            description:
                - Delimited list of email addresses to receive the alert when it triggers.
                  Delimiter character can be comma, space, TAB, or semicolon.
            returned: on success
            type: str
            sample: recipients_example
        time_created:
            description:
                - Time budget was created
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time budget was updated
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "budget_id": "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "type": "ACTUAL",
        "threshold": 10,
        "threshold_type": "PERCENTAGE",
        "lifecycle_state": "ACTIVE",
        "message": "message_example",
        "description": "description_example",
        "version": 56,
        "recipients": "recipients_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.budget import BudgetClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BudgetAlertRuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "budget_id",
            "alert_rule_id",
        ]

    def get_required_params_for_list(self):
        return [
            "budget_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_alert_rule,
            budget_id=self.module.params.get("budget_id"),
            alert_rule_id=self.module.params.get("alert_rule_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_alert_rules,
            budget_id=self.module.params.get("budget_id"),
            **optional_kwargs
        )


BudgetAlertRuleFactsHelperCustom = get_custom_class("BudgetAlertRuleFactsHelperCustom")


class ResourceFactsHelper(
    BudgetAlertRuleFactsHelperCustom, BudgetAlertRuleFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            budget_id=dict(type="str", required=True),
            alert_rule_id=dict(aliases=["id"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "INACTIVE"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="budget_alert_rule",
        service_client_class=BudgetClient,
        namespace="budget",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(budget_alert_rules=result)


if __name__ == "__main__":
    main()

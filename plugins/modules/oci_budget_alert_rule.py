#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_budget_alert_rule
short_description: Manage a BudgetAlertRule resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BudgetAlertRule resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Alert Rule.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The name of the alert rule. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    type:
        description:
            - The type of the alert. Valid values are ACTUAL (the alert triggers based on actual usage), or
              FORECAST (the alert triggers based on predicted usage).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "ACTUAL"
            - "FORECAST"
    threshold:
        description:
            - The threshold for triggering the alert, expressed as a whole number or decimal value.
              If the thresholdType is ABSOLUTE, the threshold can have at most 12 digits before the decimal point, and up to two digits after the decimal point.
              If the thresholdType is PERCENTAGE, the maximum value is 10000 and can have up to two digits after the decimal point.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: float
    threshold_type:
        description:
            - The type of threshold.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "PERCENTAGE"
            - "ABSOLUTE"
    recipients:
        description:
            - The audience that receives the alert when it triggers. An empty string is interpreted as null.
            - This parameter is updatable.
        type: str
    description:
        description:
            - The description of the alert rule.
            - This parameter is updatable.
        type: str
    msg:
        description:
            - The message to be sent to the recipients when the alert rule is triggered.
            - This parameter is updatable.
        type: str
        aliases: ["message"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    budget_id:
        description:
            - The unique budget OCID.
        type: str
        required: true
    alert_rule_id:
        description:
            - The unique Alert Rule OCID.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the BudgetAlertRule.
            - Use I(state=present) to create or update a BudgetAlertRule.
            - Use I(state=absent) to delete a BudgetAlertRule.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create budget_alert_rule
  oci_budget_alert_rule:
    # required
    type: ACTUAL
    threshold: 3.4
    threshold_type: PERCENTAGE
    budget_id: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    recipients: recipients_example
    description: description_example
    msg: msg_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update budget_alert_rule
  oci_budget_alert_rule:
    # required
    budget_id: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"
    alert_rule_id: "ocid1.alertrule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    type: ACTUAL
    threshold: 3.4
    threshold_type: PERCENTAGE
    recipients: recipients_example
    description: description_example
    msg: msg_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update budget_alert_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_budget_alert_rule:
    # required
    display_name: display_name_example
    budget_id: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    type: ACTUAL
    threshold: 3.4
    threshold_type: PERCENTAGE
    recipients: recipients_example
    description: description_example
    msg: msg_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete budget_alert_rule
  oci_budget_alert_rule:
    # required
    budget_id: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"
    alert_rule_id: "ocid1.alertrule.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete budget_alert_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_budget_alert_rule:
    # required
    display_name: display_name_example
    budget_id: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
budget_alert_rule:
    description:
        - Details of the BudgetAlertRule resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the alert rule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        budget_id:
            description:
                - The OCID of the budget.
            returned: on success
            type: str
            sample: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the alert rule. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        type:
            description:
                - The type of the alert. Valid values are ACTUAL (the alert triggers based on actual usage), or
                  FORECAST (the alert triggers based on predicted usage).
            returned: on success
            type: str
            sample: ACTUAL
        threshold:
            description:
                - The threshold for triggering the alert. If the thresholdType is PERCENTAGE, the maximum value is 10000.
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
                - Custom message sent when an alert is triggered.
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
                - The version of the alert rule. Starts from 1 and increments by 1.
            returned: on success
            type: int
            sample: 56
        recipients:
            description:
                - The delimited list of email addresses to receive the alert when it triggers.
                  Delimiter characters can be a comma, space, TAB, or semicolon.
            returned: on success
            type: str
            sample: recipients_example
        time_created:
            description:
                - The time the budget was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the budget was updated.
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
    sample: {
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
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.budget import BudgetClient
    from oci.budget.models import CreateAlertRuleDetails
    from oci.budget.models import UpdateAlertRuleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BudgetAlertRuleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(BudgetAlertRuleHelperGen, self).get_possible_entity_types() + [
            "budgetalertrule",
            "budgetalertrules",
            "budgetbudgetalertrule",
            "budgetbudgetalertrules",
            "budgetalertruleresource",
            "budgetalertrulesresource",
            "alertrule",
            "alertrules",
            "alertruleresource",
            "alertrulesresource",
            "budget",
        ]

    def get_module_resource_id_param(self):
        return "alert_rule_id"

    def get_module_resource_id(self):
        return self.module.params.get("alert_rule_id")

    def get_get_fn(self):
        return self.client.get_alert_rule

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_alert_rule,
            alert_rule_id=summary_model.id,
            budget_id=self.module.params.get("budget_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_alert_rule,
            budget_id=self.module.params.get("budget_id"),
            alert_rule_id=self.module.params.get("alert_rule_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "budget_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_alert_rules, **kwargs
        )

    def get_create_model_class(self):
        return CreateAlertRuleDetails

    def get_create_model(self):
        create_model = super(BudgetAlertRuleHelperGen, self).get_create_model()
        setattr(create_model, "message", self.module.params.get("msg"))
        return create_model

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_alert_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                budget_id=self.module.params.get("budget_id"),
                create_alert_rule_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAlertRuleDetails

    def get_update_model(self):
        update_model = super(BudgetAlertRuleHelperGen, self).get_update_model()
        setattr(update_model, "message", self.module.params.get("msg"))
        return update_model

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_alert_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                budget_id=self.module.params.get("budget_id"),
                alert_rule_id=self.module.params.get("alert_rule_id"),
                update_alert_rule_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_alert_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                budget_id=self.module.params.get("budget_id"),
                alert_rule_id=self.module.params.get("alert_rule_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


BudgetAlertRuleHelperCustom = get_custom_class("BudgetAlertRuleHelperCustom")


class ResourceHelper(BudgetAlertRuleHelperCustom, BudgetAlertRuleHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            type=dict(type="str", choices=["ACTUAL", "FORECAST"]),
            threshold=dict(type="float"),
            threshold_type=dict(type="str", choices=["PERCENTAGE", "ABSOLUTE"]),
            recipients=dict(type="str"),
            description=dict(type="str"),
            msg=dict(aliases=["message"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            budget_id=dict(type="str", required=True),
            alert_rule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="budget_alert_rule",
        service_client_class=BudgetClient,
        namespace="budget",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

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
module: oci_budget
short_description: Manage a Budget resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Budget resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new budget.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    target_compartment_id:
        description:
            - This is DEPRECATED. Set the target compartment ID in targets instead.
        type: str
    target_type:
        description:
            - The type of target on which the budget is applied.
        type: str
        choices:
            - "COMPARTMENT"
            - "TAG"
    targets:
        description:
            - "The list of targets on which the budget is applied.
                If targetType is \\"COMPARTMENT\\", the targets contain the list of compartment OCIDs.
                If targetType is \\"TAG\\", the targets contain the list of cost tracking tag identifiers in the form of
                \\"{tagNamespace}.{tagKey}.{tagValue}\\".
              Curerntly, the array should contain exactly one item."
        type: list
        elements: str
    display_name:
        description:
            - The displayName of the budget. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - The description of the budget.
            - This parameter is updatable.
        type: str
    amount:
        description:
            - The amount of the budget expressed as a whole number in the currency of the customer's rate card.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: float
    budget_processing_period_start_offset:
        description:
            - The number of days offset from the first day of the month, at which the budget processing period starts. In months that have fewer days than this
              value, processing will begin on the last day of that month. For example, for a value of 12, processing starts every month on the 12th at midnight.
            - This parameter is updatable.
        type: int
    processing_period_type:
        description:
            - The type of the budget processing period. Valid values are INVOICE, MONTH, and SINGLE_USE.
            - This parameter is updatable.
        type: str
        choices:
            - "INVOICE"
            - "MONTH"
            - "SINGLE_USE"
    start_date:
        description:
            - The date when the one-time budget begins. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the
              starting point of the date provided after being converted to UTC time.
            - This parameter is updatable.
        type: str
    end_date:
        description:
            - The date when the one-time budget concludes. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the
              starting point of the date provided after being converted to UTC time.
            - This parameter is updatable.
        type: str
    reset_period:
        description:
            - The reset period for the budget.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "MONTHLY"
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
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Budget.
            - Use I(state=present) to create or update a Budget.
            - Use I(state=absent) to delete a Budget.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create budget
  oci_budget:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    amount: 3.4
    reset_period: MONTHLY

    # optional
    target_compartment_id: "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    target_type: COMPARTMENT
    targets: [ "targets_example" ]
    display_name: display_name_example
    description: description_example
    budget_processing_period_start_offset: 56
    processing_period_type: INVOICE
    start_date: start_date_example
    end_date: end_date_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update budget
  oci_budget:
    # required
    budget_id: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    amount: 3.4
    budget_processing_period_start_offset: 56
    processing_period_type: INVOICE
    start_date: start_date_example
    end_date: end_date_example
    reset_period: MONTHLY
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update budget using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_budget:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    amount: 3.4
    budget_processing_period_start_offset: 56
    processing_period_type: INVOICE
    start_date: start_date_example
    end_date: end_date_example
    reset_period: MONTHLY
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete budget
  oci_budget:
    # required
    budget_id: "ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete budget using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_budget:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
budget:
    description:
        - Details of the Budget resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the budget.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        target_compartment_id:
            description:
                - "This is DEPRECATED. For backwards compatability, the property is populated when
                  the targetType is \\"COMPARTMENT\\", and targets contain the specific target compartment OCID.
                  For all other scenarios, this property will be left empty."
            returned: on success
            type: str
            sample: "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the budget. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of the budget.
            returned: on success
            type: str
            sample: description_example
        amount:
            description:
                - The amount of the budget expressed in the currency of the customer's rate card.
            returned: on success
            type: float
            sample: 10
        reset_period:
            description:
                - The reset period for the budget.
            returned: on success
            type: str
            sample: MONTHLY
        budget_processing_period_start_offset:
            description:
                - The number of days offset from the first day of the month, at which the budget processing period starts. In months that have fewer days than
                  this value, processing will begin on the last day of that month. For example, for a value of 12, processing starts every month on the 12th at
                  midnight.
            returned: on success
            type: int
            sample: 56
        processing_period_type:
            description:
                - The budget processing period type. Valid values are INVOICE, MONTH, and SINGLE_USE.
            returned: on success
            type: str
            sample: INVOICE
        start_date:
            description:
                - The date when the one-time budget begins. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to the
                  starting point of the date provided after being converted to UTC time.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        end_date:
            description:
                - The time when the one-time budget concludes. For example, `2023-03-23`. The date-time format conforms to RFC 3339, and will be truncated to
                  the starting point of the date provided after being converted to UTC time.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        target_type:
            description:
                - The type of target on which the budget is applied.
            returned: on success
            type: str
            sample: COMPARTMENT
        targets:
            description:
                - "The list of targets on which the budget is applied.
                    If the targetType is \\"COMPARTMENT\\", the targets contain the list of compartment OCIDs.
                    If the targetType is \\"TAG\\", the targets contain the list of cost tracking tag identifiers in the form of
                    \\"{tagNamespace}.{tagKey}.{tagValue}\\"."
            returned: on success
            type: list
            sample: []
        lifecycle_state:
            description:
                - The current state of the budget.
            returned: on success
            type: str
            sample: ACTIVE
        alert_rule_count:
            description:
                - The total number of alert rules in the budget.
            returned: on success
            type: int
            sample: 56
        version:
            description:
                - The version of the budget. Starts from 1 and increments by 1.
            returned: on success
            type: int
            sample: 56
        actual_spend:
            description:
                - The actual spend in currency for the current budget cycle.
            returned: on success
            type: float
            sample: 10
        forecasted_spend:
            description:
                - The forecasted spend in currency by the end of the current budget cycle.
            returned: on success
            type: float
            sample: 10
        time_spend_computed:
            description:
                - The time that the budget spend was last computed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The time that the budget was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time that the budget was updated.
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "target_compartment_id": "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "amount": 10,
        "reset_period": "MONTHLY",
        "budget_processing_period_start_offset": 56,
        "processing_period_type": "INVOICE",
        "start_date": "2013-10-20T19:20:30+01:00",
        "end_date": "2013-10-20T19:20:30+01:00",
        "target_type": "COMPARTMENT",
        "targets": [],
        "lifecycle_state": "ACTIVE",
        "alert_rule_count": 56,
        "version": 56,
        "actual_spend": 10,
        "forecasted_spend": 10,
        "time_spend_computed": "2013-10-20T19:20:30+01:00",
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
    from oci.budget.models import CreateBudgetDetails
    from oci.budget.models import UpdateBudgetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BudgetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(BudgetHelperGen, self).get_possible_entity_types() + [
            "budget",
            "budgets",
            "budgetbudget",
            "budgetbudgets",
            "budgetresource",
            "budgetsresource",
        ]

    def get_module_resource_id_param(self):
        return "budget_id"

    def get_module_resource_id(self):
        return self.module.params.get("budget_id")

    def get_get_fn(self):
        return self.client.get_budget

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_budget, budget_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_budget, budget_id=self.module.params.get("budget_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "target_type"]

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
        return oci_common_utils.list_all_resources(self.client.list_budgets, **kwargs)

    def get_create_model_class(self):
        return CreateBudgetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_budget,
            call_fn_args=(),
            call_fn_kwargs=dict(create_budget_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateBudgetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_budget,
            call_fn_args=(),
            call_fn_kwargs=dict(
                budget_id=self.module.params.get("budget_id"),
                update_budget_details=update_details,
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
            call_fn=self.client.delete_budget,
            call_fn_args=(),
            call_fn_kwargs=dict(budget_id=self.module.params.get("budget_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


BudgetHelperCustom = get_custom_class("BudgetHelperCustom")


class ResourceHelper(BudgetHelperCustom, BudgetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            target_compartment_id=dict(type="str"),
            target_type=dict(type="str", choices=["COMPARTMENT", "TAG"]),
            targets=dict(type="list", elements="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            amount=dict(type="float"),
            budget_processing_period_start_offset=dict(type="int"),
            processing_period_type=dict(
                type="str", choices=["INVOICE", "MONTH", "SINGLE_USE"]
            ),
            start_date=dict(type="str"),
            end_date=dict(type="str"),
            reset_period=dict(type="str", choices=["MONTHLY"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            budget_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="budget",
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

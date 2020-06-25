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
module: oci_budget_facts
short_description: Fetches details about one or multiple Budget resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Budget resources in Oracle Cloud Infrastructure
    - Lists budgets in the specified compartment.
    - If I(budget_id) is specified, the details of a single Budget will be returned.
version_added: "2.5"
options:
    budget_id:
        description:
            - The unique Budget OCID
            - Required to get a specific budget.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple budgets.
        type: str
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
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List budgets
  oci_budget_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific budget
  oci_budget_facts:
    budget_id: ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
budgets:
    description:
        - List of Budget resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the budget
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        target_compartment_id:
            description:
                - The OCID of the compartment on which budget is applied
            returned: on success
            type: string
            sample: ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The display name of the budget.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - The description of the budget.
            returned: on success
            type: string
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
            type: string
            sample: MONTHLY
        lifecycle_state:
            description:
                - The current state of the budget.
            returned: on success
            type: string
            sample: ACTIVE
        alert_rule_count:
            description:
                - Total number of alert rules in the budget
            returned: on success
            type: int
            sample: 56
        version:
            description:
                - Version of the budget. Starts from 1 and increments by 1.
            returned: on success
            type: int
            sample: 56
        actual_spend:
            description:
                - The actual spend in currency for the current budget cycle
            returned: on success
            type: float
            sample: 10
        forecasted_spend:
            description:
                - The forecasted spend in currency by the end of the current budget cycle
            returned: on success
            type: float
            sample: 10
        time_spend_computed:
            description:
                - The time that the budget spend was last computed
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_created:
            description:
                - Time that budget was created
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - Time that budget was updated
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
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
        "target_compartment_id": "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "amount": 10,
        "reset_period": "MONTHLY",
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


class BudgetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "budget_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_budget, budget_id=self.module.params.get("budget_id"),
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
            self.client.list_budgets,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


BudgetFactsHelperCustom = get_custom_class("BudgetFactsHelperCustom")


class ResourceFactsHelper(BudgetFactsHelperCustom, BudgetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            budget_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
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
        resource_type="budget",
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

    module.exit_json(budgets=result)


if __name__ == "__main__":
    main()

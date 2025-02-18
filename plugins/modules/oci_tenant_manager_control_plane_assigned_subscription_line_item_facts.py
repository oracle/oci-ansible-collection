#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_tenant_manager_control_plane_assigned_subscription_line_item_facts
short_description: Fetches details about one or multiple AssignedSubscriptionLineItem resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AssignedSubscriptionLineItem resources in Oracle Cloud Infrastructure
    - List line item summaries that a assigned subscription owns.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    assigned_subscription_id:
        description:
            - OCID of the assigned Oracle Cloud Subscription.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - "The field to sort by. Only one sort order can be provided.
              * The default order for timeCreated is descending.
              * The default order for displayName is ascending.
              * If no value is specified, timeCreated is the default."
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List assigned_subscription_line_items
  oci_tenant_manager_control_plane_assigned_subscription_line_item_facts:
    # required
    assigned_subscription_id: "ocid1.assignedsubscription.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
assigned_subscription_line_items:
    description:
        - List of AssignedSubscriptionLineItem resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Subscription line item identifier.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        product_code:
            description:
                - Product code.
            returned: on success
            type: str
            sample: product_code_example
        quantity:
            description:
                - Product number.
            returned: on success
            type: float
            sample: 3.4
        billing_model:
            description:
                - Billing model supported by the associated line item.
            returned: on success
            type: str
            sample: COMMITMENT
        time_started:
            description:
                - The time the subscription item and associated products should start. An RFC 3339 formatted date and time string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - The time the subscription item and associated products should end. An RFC 3339 formatted date and time string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "product_code": "product_code_example",
        "quantity": 3.4,
        "billing_model": "COMMITMENT",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import SubscriptionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssignedSubscriptionLineItemFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "assigned_subscription_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_assigned_subscription_line_items,
            assigned_subscription_id=self.module.params.get("assigned_subscription_id"),
            **optional_kwargs
        )


AssignedSubscriptionLineItemFactsHelperCustom = get_custom_class(
    "AssignedSubscriptionLineItemFactsHelperCustom"
)


class ResourceFactsHelper(
    AssignedSubscriptionLineItemFactsHelperCustom,
    AssignedSubscriptionLineItemFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            assigned_subscription_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="assigned_subscription_line_item",
        service_client_class=SubscriptionClient,
        namespace="tenant_manager_control_plane",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(assigned_subscription_line_items=result)


if __name__ == "__main__":
    main()

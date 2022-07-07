#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_onesubscription_organization_subscription_facts
short_description: Fetches details about one or multiple OrganizationSubscription resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OrganizationSubscription resources in Oracle Cloud Infrastructure
    - API that returns data for the list of subscription ids returned from Organizations API
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the root compartment.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending ('ASC') or descending ('DESC').
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order ('sortOrder').
        type: str
        choices:
            - "ORDERNUMBER"
            - "TIMEINVOICING"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List organization_subscriptions
  oci_onesubscription_organization_subscription_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: ORDERNUMBER

"""

RETURN = """
organization_subscriptions:
    description:
        - List of OrganizationSubscription resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - SPM internal Subscription ID
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        service_name:
            description:
                - Customer friendly service name provided by PRG
            returned: on success
            type: str
            sample: service_name_example
        type:
            description:
                - Subscription Type i.e. IAAS,SAAS,PAAS
            returned: on success
            type: str
            sample: type_example
        status:
            description:
                - Status of the plan
            returned: on success
            type: str
            sample: status_example
        time_start:
            description:
                - Represents the date when the first service of the subscription was activated
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_end:
            description:
                - Represents the date when the last service of the subscription ends
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        currency:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Currency name
                    returned: on success
                    type: str
                    sample: name_example
                iso_code:
                    description:
                        - Currency Code
                    returned: on success
                    type: str
                    sample: iso_code_example
                std_precision:
                    description:
                        - Standard Precision of the Currency
                    returned: on success
                    type: int
                    sample: 56
        total_value:
            description:
                - Total aggregate TCLV of all lines for the subscription including expired, active, and signed
            returned: on success
            type: str
            sample: total_value_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "service_name": "service_name_example",
        "type": "type_example",
        "status": "status_example",
        "time_start": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "currency": {
            "name": "name_example",
            "iso_code": "iso_code_example",
            "std_precision": 56
        },
        "total_value": "total_value_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.onesubscription import OrganizationSubscriptionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OrganizationSubscriptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
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
            self.client.list_organization_subscriptions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OrganizationSubscriptionFactsHelperCustom = get_custom_class(
    "OrganizationSubscriptionFactsHelperCustom"
)


class ResourceFactsHelper(
    OrganizationSubscriptionFactsHelperCustom, OrganizationSubscriptionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["ORDERNUMBER", "TIMEINVOICING"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="organization_subscription",
        service_client_class=OrganizationSubscriptionClient,
        namespace="onesubscription",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(organization_subscriptions=result)


if __name__ == "__main__":
    main()

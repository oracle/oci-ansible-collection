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
module: oci_osub_subscription_commitment_facts
short_description: Fetches details about one or multiple Commitment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Commitment resources in Oracle Cloud Infrastructure
    - This list API returns all commitments for a particular Subscribed Service
    - If I(commitment_id) is specified, the details of a single Commitment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    commitment_id:
        description:
            - The Commitment Id
            - Required to get a specific commitment.
        type: str
        aliases: ["id"]
    subscribed_service_id:
        description:
            - This param is used to get the commitments for a particular subscribed service
            - Required to list multiple commitments.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple commitments.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
        type: str
        choices:
            - "TIMECREATED"
            - "TIMESTART"
    x_one_gateway_subscription_id:
        description:
            - This header is meant to be used only for internal purposes and will be ignored on any public request. The purpose of this header is
              to help on Gateway to API calls identification.
        type: str
    x_one_origin_region:
        description:
            - The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific commitment
  oci_osub_subscription_commitment_facts:
    # required
    commitment_id: "ocid1.commitment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    x_one_gateway_subscription_id: "ocid1.xonegatewaysubscription.oc1..xxxxxxEXAMPLExxxxxx"
    x_one_origin_region: us-phoenix-1

- name: List commitments
  oci_osub_subscription_commitment_facts:
    # required
    subscribed_service_id: "ocid1.subscribedservice.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: TIMECREATED
    x_one_gateway_subscription_id: "ocid1.xonegatewaysubscription.oc1..xxxxxxEXAMPLExxxxxx"
    x_one_origin_region: us-phoenix-1

"""

RETURN = """
commitments:
    description:
        - List of Commitment resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - SPM internal Commitment ID
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_start:
            description:
                - Commitment start date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_end:
            description:
                - Commitment end date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        quantity:
            description:
                - Commitment quantity
            returned: on success
            type: str
            sample: quantity_example
        used_amount:
            description:
                - Commitment used amount
            returned: on success
            type: str
            sample: used_amount_example
        available_amount:
            description:
                - Commitment available amount
            returned: on success
            type: str
            sample: available_amount_example
        funded_allocation_value:
            description:
                - "Funded Allocation line value
                  example: 12000.00"
            returned: on success
            type: str
            sample: funded_allocation_value_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_start": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "quantity": "quantity_example",
        "used_amount": "used_amount_example",
        "available_amount": "available_amount_example",
        "funded_allocation_value": "funded_allocation_value_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.osub_subscription import CommitmentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CommitmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "commitment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "subscribed_service_id",
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "x_one_gateway_subscription_id",
            "x_one_origin_region",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_commitment,
            commitment_id=self.module.params.get("commitment_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "x_one_gateway_subscription_id",
            "x_one_origin_region",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_commitments,
            subscribed_service_id=self.module.params.get("subscribed_service_id"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


CommitmentFactsHelperCustom = get_custom_class("CommitmentFactsHelperCustom")


class ResourceFactsHelper(CommitmentFactsHelperCustom, CommitmentFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            commitment_id=dict(aliases=["id"], type="str"),
            subscribed_service_id=dict(type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "TIMESTART"]),
            x_one_gateway_subscription_id=dict(type="str"),
            x_one_origin_region=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="commitment",
        service_client_class=CommitmentClient,
        namespace="osub_subscription",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(commitments=result)


if __name__ == "__main__":
    main()

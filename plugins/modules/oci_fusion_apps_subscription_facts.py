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
module: oci_fusion_apps_subscription_facts
short_description: Fetches details about a Subscription resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Subscription resource in Oracle Cloud Infrastructure
    - Gets the subscription details of an fusion environment family.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    fusion_environment_family_id:
        description:
            - The unique identifier (OCID) of the FusionEnvironmentFamily.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific subscription
  oci_fusion_apps_subscription_facts:
    # required
    fusion_environment_family_id: "ocid1.fusionenvironmentfamily.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
subscription:
    description:
        - Subscription resource
    returned: on success
    type: complex
    contains:
        subscriptions:
            description:
                - List of subscriptions.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - OCID of the subscription details for particular root compartment or tenancy.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                classic_subscription_id:
                    description:
                        - Subscription id.
                    returned: on success
                    type: str
                    sample: "ocid1.classicsubscription.oc1..xxxxxxEXAMPLExxxxxx"
                service_name:
                    description:
                        - The type of subscription, such as 'CLOUDCM'/'SAAS'/'CRM', etc.
                    returned: on success
                    type: str
                    sample: service_name_example
                skus:
                    description:
                        - Stock keeping unit.
                    returned: on success
                    type: complex
                    contains:
                        sku:
                            description:
                                - Stock keeping unit id.
                            returned: on success
                            type: str
                            sample: sku_example
                        license_part_description:
                            description:
                                - Description of the covered product belonging to this Sku.
                            returned: on success
                            type: str
                            sample: license_part_description_example
                        metric_name:
                            description:
                                - Base metric for billing the service.
                            returned: on success
                            type: str
                            sample: metric_name_example
                        quantity:
                            description:
                                - Quantity of the stock units.
                            returned: on success
                            type: int
                            sample: 56
                        description:
                            description:
                                - Description of the stock units.
                            returned: on success
                            type: str
                            sample: description_example
    sample: {
        "subscriptions": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "classic_subscription_id": "ocid1.classicsubscription.oc1..xxxxxxEXAMPLExxxxxx",
            "service_name": "service_name_example",
            "skus": [{
                "sku": "sku_example",
                "license_part_description": "license_part_description_example",
                "metric_name": "metric_name_example",
                "quantity": 56,
                "description": "description_example"
            }]
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.fusion_apps import FusionApplicationsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "fusion_environment_family_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fusion_environment_family_subscription_detail,
            fusion_environment_family_id=self.module.params.get(
                "fusion_environment_family_id"
            ),
        )


SubscriptionFactsHelperCustom = get_custom_class("SubscriptionFactsHelperCustom")


class ResourceFactsHelper(SubscriptionFactsHelperCustom, SubscriptionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            fusion_environment_family_id=dict(
                aliases=["id"], type="str", required=True
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="subscription",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(subscription=result)


if __name__ == "__main__":
    main()

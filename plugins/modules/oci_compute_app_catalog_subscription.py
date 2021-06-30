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
module: oci_compute_app_catalog_subscription
short_description: Manage an AppCatalogSubscription resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete an AppCatalogSubscription resource in Oracle Cloud Infrastructure
    - For I(state=present), create a subscription for listing resource version for a compartment. It will take some time to propagate to all regions.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartmentID for the subscription.
        type: str
        required: true
    listing_id:
        description:
            - The OCID of the listing.
        type: str
        required: true
    listing_resource_version:
        description:
            - Listing resource version.
        type: str
        required: true
    oracle_terms_of_use_link:
        description:
            - Oracle TOU link
            - Required for create using I(state=present).
        type: str
    eula_link:
        description:
            - EULA link
        type: str
    time_retrieved:
        description:
            - "Date and time the agreements were retrieved, in L(RFC3339,https://tools.ietf.org/html/rfc3339) format.
              Example: `2018-03-20T12:32:53.532Z`"
            - Required for create using I(state=present).
        type: str
    signature:
        description:
            - A generated signature for this listing resource version retrieved the agreements API.
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the AppCatalogSubscription.
            - Use I(state=present) to create an AppCatalogSubscription.
            - Use I(state=absent) to delete an AppCatalogSubscription.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create app_catalog_subscription
  oci_compute_app_catalog_subscription:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
    listing_resource_version: listing_resource_version_example
    oracle_terms_of_use_link: oracle_terms_of_use_link_example
    time_retrieved: 2018-03-20T12:32:53.532Z
    signature: signature_example

- name: Delete app_catalog_subscription
  oci_compute_app_catalog_subscription:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
    listing_resource_version: listing_resource_version_example
    state: absent

"""

RETURN = """
app_catalog_subscription:
    description:
        - Details of the AppCatalogSubscription resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        publisher_name:
            description:
                - Name of the publisher who published this listing.
            returned: on success
            type: string
            sample: publisher_name_example
        listing_id:
            description:
                - The ocid of the listing resource.
            returned: on success
            type: string
            sample: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
        listing_resource_version:
            description:
                - Listing resource version.
            returned: on success
            type: string
            sample: listing_resource_version_example
        listing_resource_id:
            description:
                - Listing resource id.
            returned: on success
            type: string
            sample: "ocid1.listingresource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the listing.
            returned: on success
            type: string
            sample: display_name_example
        summary:
            description:
                - The short summary to the listing.
            returned: on success
            type: string
            sample: summary_example
        compartment_id:
            description:
                - The compartmentID of the subscription.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "Date and time at which the subscription was created, in L(RFC3339,https://tools.ietf.org/html/rfc3339) format.
                  Example: `2018-03-20T12:32:53.532Z`"
            returned: on success
            type: string
            sample: 2018-03-20T12:32:53.532Z
    sample: {
        "publisher_name": "publisher_name_example",
        "listing_id": "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx",
        "listing_resource_version": "listing_resource_version_example",
        "listing_resource_id": "ocid1.listingresource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "summary": "summary_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2018-03-20T12:32:53.532Z"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient
    from oci.core.models import CreateAppCatalogSubscriptionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AppCatalogSubscriptionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, list and delete"""

    # needs custom GET via LIST implementation because resource does not have an 'id' field

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["listing_id"]

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
            self.client.list_app_catalog_subscriptions, **kwargs
        )

    def get_create_model_class(self):
        return CreateAppCatalogSubscriptionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_app_catalog_subscription,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_app_catalog_subscription_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_app_catalog_subscription,
            call_fn_args=(),
            call_fn_kwargs=dict(
                listing_id=self.module.params.get("listing_id"),
                compartment_id=self.module.params.get("compartment_id"),
                resource_version=self.module.params.get("resource_version"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AppCatalogSubscriptionHelperCustom = get_custom_class(
    "AppCatalogSubscriptionHelperCustom"
)


class ResourceHelper(
    AppCatalogSubscriptionHelperCustom, AppCatalogSubscriptionHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            listing_id=dict(type="str", required=True),
            listing_resource_version=dict(type="str", required=True),
            oracle_terms_of_use_link=dict(type="str"),
            eula_link=dict(type="str"),
            time_retrieved=dict(type="str"),
            signature=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="app_catalog_subscription",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

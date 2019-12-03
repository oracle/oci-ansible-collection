#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_app_catalog_subscription
short_description: Manage app catalog subscriptions in OCI
description:
    - This module allows the user to create, delete app catalog subscriptions in OCI. When created, it will take some
      time to propagate to all regions.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment.
        required: true
    eula_link:
        description: EULA link. Required if the I(listing_resource_version) has one.
        required: false
    listing_id:
        description: The OCID of the listing.
        required: true
    listing_resource_version:
        description: Listing resource version.
        required: true
    oracle_terms_of_use_link:
        description: Oracle TOU link. Required for creating an app catalog subscription with I(state=present).
        required: false
    signature:
        description: A generated signature for this listing resource version retrieved the agreements API.
                     Required when I(state=present).
        required: false
    time_retrieved:
        description: Date and time the agreements were retrieved, in RFC3339 format. Required when I(state=present).
        required: false
    state:
        description: Create an app catalog subscription when I(state=present). Use I(state=absent) to delete
                     a subscription.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Create a subscription
  oci_app_catalog_subscription:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    eula_link: "https://objectstorage.region.oraclecloud.com/n/partnerimagecatalog/b/eulas/o/xxxxxx/xxxxxxx/eula.txt"
    listing_id: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
    listing_resource_version: "1.0.0"
    oracle_terms_of_use_link: "https://objectstorage.region.oraclecloud.com/n/partnerimagecatalog/b/eulas/o/oracle-terms-of-use.txt"
    signature: "xxxxxxxxxxxxxxexamplesignaturexxxxxxxxxxxx"
    time_retrieved: 2019-02-14T19:53:30.878Z
- name: Delete a subscription
  oci_app_catalog_subscription:
    listing_id: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    listing_resource_version: "1.0.0"
    state: absent
"""

RETURN = """
app_catalog_subscription:
    description: Information about the app catalog subscription. Applicable only for create.
    returned: on success
    type: complex
    contains:
        compartment_id:
            description: The compartmentID of the subscription.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        display_name:
            description: The display name of the listing.
            returned: always
            type: string
            sample: Test app catalog
        listing_id:
            description: The ocid of the listing resource.
            returned: always
            type: string
            sample: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
        listing_resource_id:
            description: Listing resource id.
            returned: always
            type: string
            sample: ocid1.image.oc1..xxxxxEXAMPLExxxxx
        listing_resource_version:
            description: Listing resource version.
            returned: always
            type: string
            sample: "1.0.0"
        publisher_name:
            description: Name of the publisher who published this listing.
            returned: always
            type: string
            sample: Test Publisher
        summary:
            description: Summary of the listing.
            returned: always
            type: string
            sample: Test app catalog listing
        time_created:
            description: Date and time at which the subscription was created, in RFC3339 format.
            returned: always
            type: string
            sample: 2019-02-14T19:53:30.878000+00:00
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "Test app catalog",
            "listing_id": "ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx",
            "listing_resource_id": "ocid1.image.oc1..xxxxxEXAMPLExxxxx",
            "listing_resource_version": "1.0.0",
            "publisher_name": "Test Publisher",
            "summary": "Test app catalog listing",
            "time_created": "2019-02-14T19:53:30.878000+00:00"
            }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_date_utils

try:
    from oci.core.compute_client import ComputeClient
    from oci.core.models import CreateAppCatalogSubscriptionDetails
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_app_catalog_subscription(compute_client, module):
    result = dict()
    try:
        existing_app_catalog_subscription = get_app_catalog_subscription(
            compute_client, module
        )
        if not existing_app_catalog_subscription:
            raise ServiceError(
                404,
                "NotAuthorizedOrNotFound",
                dict(),
                "The app catalog subscription does not exist.",
            )
        # Directly calling delete_app_catalog_subscription instead of
        # ansible.module_utils.oracle.oci_utils.delete_and_wait as app catalog subscriptions do not offer a GET function
        oci_utils.call_with_backoff(
            compute_client.delete_app_catalog_subscription,
            listing_id=module.params["listing_id"],
            compartment_id=module.params["compartment_id"],
            resource_version=module.params["listing_resource_version"],
        )
    except ServiceError as se:
        if se.status == 404:
            result["changed"] = False
            result["msg"] = "The app catalog subscription does not exist."
            result["app_catalog_subscription"] = dict()
        else:
            raise
    else:
        result["changed"] = True
        result["app_catalog_subscription"] = existing_app_catalog_subscription
    return result


def create_app_catalog_subscription(compute_client, module):
    existing_app_catalog_subscription = get_app_catalog_subscription(
        compute_client, module
    )
    if existing_app_catalog_subscription:
        return dict(
            changed=False, app_catalog_subscription=existing_app_catalog_subscription
        )
    create_app_catalog_subscription_details = CreateAppCatalogSubscriptionDetails()
    for attr in create_app_catalog_subscription_details.swagger_types:
        setattr(create_app_catalog_subscription_details, attr, module.params.get(attr))
    # The time retrieved passed to the ansible module as string. Convert to datetime.
    # If there is an error converting to date, pass the original string to the API.
    create_app_catalog_subscription_details.time_retrieved = oci_date_utils.parse_iso8601_str_as_datetime(
        create_app_catalog_subscription_details.time_retrieved
    )
    oci_utils.to_dict(
        oci_utils.call_with_backoff(
            compute_client.create_app_catalog_subscription,
            create_app_catalog_subscription_details=create_app_catalog_subscription_details,
        ).data
    )
    app_catalog_subscription = get_app_catalog_subscription(compute_client, module)
    return dict(changed=True, app_catalog_subscription=app_catalog_subscription)


def get_app_catalog_subscription(compute_client, module):
    app_catalog_subscriptions = oci_utils.list_all_resources(
        compute_client.list_app_catalog_subscriptions,
        compartment_id=module.params["compartment_id"],
        listing_id=module.params["listing_id"],
    )
    for app_catalog_subscription in app_catalog_subscriptions:
        if (
            app_catalog_subscription.listing_resource_version
            == module.params["listing_resource_version"]
        ):
            return oci_utils.to_dict(app_catalog_subscription)
    return None


def main():
    module_args = oci_utils.get_common_arg_spec(supports_create=False)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            eula_link=dict(type="str", required=False),
            listing_id=dict(type="str", required=True),
            listing_resource_version=dict(type="str", required=True),
            oracle_terms_of_use_link=dict(type="str", required=False),
            signature=dict(type="str", required=False, no_log=True),
            time_retrieved=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)
    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    try:
        state = module.params["state"]
        if state == "absent":
            result = delete_app_catalog_subscription(compute_client, module)
        else:
            result = create_app_catalog_subscription(compute_client, module)

    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(**result)


if __name__ == "__main__":
    main()

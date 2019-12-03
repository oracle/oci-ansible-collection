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
module: oci_app_catalog_listing_resource_version_facts
short_description: Retrieve details about App Catalog listing resource versions in OCI Compute Service
description:
    - This module retrieves information of all resource versions or a specific resource version of the specified
      app catalog listing.
version_added: "2.5"
options:
    listing_id:
        description: The OCID of the listing.
        required: true
        aliases: ["id"]
    resource_version:
        description: Listing Resource Version. Required to get a specific resource version of I(listing_id).
        required: false
        aliases: ["version"]
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Get all the resource versions for an app catalog listing
  oci_app_catalog_listing_resource_version_facts:
    listing_id: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
- name: Get a specific resource version for an app catalog listing
  oci_app_catalog_listing_resource_version_facts:
    listing_id: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
    resource_version: "1.0.0"
"""

RETURN = """
app_catalog_listing_resource_versions:
    description: List of resource versions for a particular listing
    returned: always
    type: complex
    contains:
        accessible_ports:
            description: List of accessible ports for instances launched with this listing resource version..
            returned: always
            type: list
            sample: []
        allowed_actions:
            description: Allowed actions for the listing resource.
            returned: always
            type: list
            sample: []
        available_regions:
            description: List of regions that this listing resource version is available.
            returned: always
            type: list
            sample: ["us-ashburn-1", "us-phoenix-1"]
        compatible_shapes:
            description: List of shapes compatible with this resource.
            returned: always
            type: list
            sample: ["VM.Standard2.1", "VM.Standard2.2"]
        listing_id:
            description: The OCID of the listing this resource version belongs to.
            returned: always
            type: string
            sample: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
        listing_resource_id:
            description: OCID of the listing resource.
            returned: always
            type: string
            sample: ocid1.image.oc1..xxxxxEXAMPLExxxxx
        listing_resource_version:
            description: Resource Version.
            returned: always
            type: string
            sample: "1.0.0"
        time_published:
            description: Date and time the listing resource version was published, in RFC3339 format.
            returned: always
            type: string
            sample: 2019-02-14T19:53:30.878000+00:00
    sample: [{
            "accessible_ports": [],
            "allowed_actions": [],
            "available_regions": [
                "us-ashburn-1",
                "us-phoenix-1"
            ],
            "compatible_shapes": [
                "VM.Standard2.1",
                "VM.Standard2.2",
            ],
            "listing_id": "ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx",
            "listing_resource_id": "ocid1.image.oc1..xxxxxEXAMPLExxxxx",
            "listing_resource_version": "1.0.0",
            "time_published": "2019-02-14T19:53:30.878000+00:00"
            }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_client import ComputeClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_app_catalog_listing_resource_versions(compute_client, module):

    return to_dict(
        [
            oci_utils.call_with_backoff(
                compute_client.get_app_catalog_listing_resource_version,
                listing_id=app_catalog_listing.listing_id,
                resource_version=app_catalog_listing.listing_resource_version,
            ).data
            for app_catalog_listing in oci_utils.list_all_resources(
                compute_client.list_app_catalog_listing_resource_versions,
                listing_id=module.params["listing_id"],
            )
        ]
    )


def get_app_catalog_listing_resource_version(compute_client, module):
    return to_dict(
        [
            oci_utils.call_with_backoff(
                compute_client.get_app_catalog_listing_resource_version,
                listing_id=module.params["listing_id"],
                resource_version=module.params["resource_version"],
            ).data
        ]
    )


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            listing_id=dict(type="str", required=True, aliases=["id"]),
            resource_version=dict(type="str", required=False, aliases=["version"]),
        )
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)
    try:
        resource_version = module.params["resource_version"]
        if resource_version:
            result = get_app_catalog_listing_resource_version(compute_client, module)
        else:
            result = list_app_catalog_listing_resource_versions(compute_client, module)
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(app_catalog_listing_resource_versions=result)


if __name__ == "__main__":
    main()

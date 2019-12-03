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
module: oci_app_catalog_listing_agreement
short_description: Creates an agreement for a particular app catalog listing resource version in OCI Compute Service
description:
    - This module Creates an agreement for a particular app catalog listing resource version.
version_added: "2.5"
options:
    listing_id:
        description: The OCID of the listing.
        required: true
        aliases: ["id"]
    resource_version:
        description: Listing Resource Version.
        required: true
        aliases: ["version"]
    state:
        description: Create an app catalog listing agreement.
        required: false
        default: present
        choices: ['present']
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Create an agreement for a particular app catalog listing resource version
  oci_app_catalog_listing_agreement:
    listing_id: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
    resource_version: "1.0.0"
"""

RETURN = """
app_catalog_listing_agreement:
    description: Agreement for a listing resource version
    returned: always
    type: complex
    contains:
        eula_link:
            description: EULA link.
            returned: always
            type: string
            sample: "https://objectstorage.region.oraclecloud.com/n/partnerimagecatalog/b/eulas/o/xxxxxx/xxxxxxx/eula.txt"
        listing_id:
            description: The ocid of the listing resource.
            returned: always
            type: string
            sample: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
        listing_resource_version:
            description: Listing resource version.
            returned: always
            type: string
            sample: "1.0.0"
        oracle_terms_of_use_link:
            description: Oracle TOU link.
            returned: always
            type: string
            sample: "https://objectstorage.region.oraclecloud.com/n/partnerimagecatalog/b/eulas/o/oracle-terms-of-use.txt"
        signature:
            description: A generated signature for this agreement retrieval operation which should be used
                         in the create subscription call.
            returned: always
            type: string
            sample: xxxxxxxxxxxexamplesignaturexxxxxxxxxxxxxxx
        time_retrieved:
            description: Date and time the agreements were retrieved, in RFC3339 format.
            returned: always
            type: string
            sample: 2019-02-14T19:53:30.878000+00:00
    sample: {
            "eula_link": "https://objectstorage.region.oraclecloud.com/n/partnerimagecatalog/b/eulas/o/xxxxxx/xxxxxxx/eula.txt",
            "listing_id": "ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx",
            "listing_resource_version": "1.0.0",
            "oracle_terms_of_use_link": "https://objectstorage.region.oraclecloud.com/n/partnerimagecatalog/b/eulas/o/oracle-terms-of-use.txt",
            "signature": "xxxxxxxxxxxexamplesignaturexxxxxxxxxxxxxxx",
            "time_retrieved": "2019-02-14T19:53:30.878000+00:00"
            }
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


def create_app_catalog_listing_agreement(compute_client, module):
    app_catalog_listing_agreement = to_dict(
        oci_utils.call_with_backoff(
            compute_client.get_app_catalog_listing_agreements,
            listing_id=module.params["listing_id"],
            resource_version=module.params["resource_version"],
        ).data
    )

    return dict(
        changed=True, app_catalog_listing_agreement=app_catalog_listing_agreement
    )


def main():
    module_args = oci_utils.get_common_arg_spec(supports_create=False)
    module_args.update(
        dict(
            listing_id=dict(type="str", required=True, aliases=["id"]),
            resource_version=dict(type="str", required=True, aliases=["version"]),
            state=dict(
                type="str", required=False, default="present", choices=["present"]
            ),
        )
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)
    try:
        result = create_app_catalog_listing_agreement(compute_client, module)
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(**result)


if __name__ == "__main__":
    main()

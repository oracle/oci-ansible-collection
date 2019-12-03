#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
module: oci_region_subscription_facts
short_description: Retrieve details of the region subscriptions for the specified tenancy.
description:
    - This module retrieves details about the region subscriptions of the specified tenancy in Oracle Cloud
      Infrastructure.
options:
    tenancy_id:
        description: The OCID of the tenancy for which region subscriptions needs to be retrieved
        required: true
        aliases: [ 'id' ]
version_added: "2.5"
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get region subscription details of the specified tenancy
  oci_region_subscription_facts:
    id: "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx...o244pucq"
"""

RETURN = """
region_subscriptions:
    description: Region subscription information about the specified tenancy
    returned: on success
    type: complex
    contains:
        region_key:
            description: The region's key.
            returned: always
            type: string
            sample: "PHX"
        region_name:
            description: The name of the region
            returned: always
            type: string
            sample: "us-ashburn-1"
        status:
            description: The region subscription status.
            returned: always
            type: string
            sample: "READY"
        is_home_region:
            description: Indicates if the region is the home region or not.
            returned: always
            type: boolean
            sample: true

    sample: [
                {
                  "region_key": "IAD",
                  "status": "READY",
                  "is_home_region": true,
                  "region_name": "us-ashburn-1"
                },
                {
                  "region_key": "PHX",
                  "status": "READY",
                  "is_home_region": false,
                  "region_name": "us-phoenix-1"
                }
          ]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_region_subscriptions(identity_client, module):
    try:
        tenancy_ocid = module.params["tenancy_id"]
        region_subscriptions = oci_utils.call_with_backoff(
            identity_client.list_region_subscriptions, tenancy_id=tenancy_ocid
        ).data
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    return to_dict(region_subscriptions)


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(tenancy_id=dict(type="str", required=True, aliases=["id"])))

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    result = list_region_subscriptions(identity_client, module)
    module.exit_json(region_subscriptions=result)


if __name__ == "__main__":
    main()

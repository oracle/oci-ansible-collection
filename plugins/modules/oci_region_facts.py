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
module: oci_region_facts
short_description: Retrieve details about all Regions offered by Oracle Cloud Infrastructure
description:
    - This module retrieves details about all Regions offered by Oracle Cloud Infrastructure.
version_added: "2.5"
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
- name: Get details of all regions offered by OCI
  oci_region_facts:
"""

RETURN = """
regions:
    description: Information about regions offered by OCI
    returned: on success
    type: complex
    contains:
        key:
            description: The key of the region.
            returned: always
            type: string
            sample: PHX
        name:
            description: The name of the region.
            returned: always
            type: string
            sample: us-phoenix-1

    sample: [
                {
                  "key": "FRA",
                  "name": "eu-frankfurt-1"
                },
                {
                  "key": "IAD",
                  "name": "us-ashburn-1"
                },
                {
                  "key": "PHX",
                  "name": "us-phoenix-1"
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


def list_regions(identity_client, module):
    try:
        regions = oci_utils.list_all_resources(
            identity_client.list_regions, name=module.params["name"]
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    return to_dict(regions)


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    result = list_regions(identity_client, module)
    module.exit_json(regions=result)


if __name__ == "__main__":
    main()

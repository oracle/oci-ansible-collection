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
module: oci_tenancy_facts
short_description: Retrieve details about a tenancy in Oracle Cloud Infrastructure
description:
    - This module retrieves details about a tenancy in Oracle Cloud Infrastructure.
version_added: "2.5"
options:
    tenancy_id:
        description: The OCID of the tenancy for which details needs to be retrieved
        required: true
        aliases: [ 'id' ]
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get details of the specified tenancy
  oci_tenancy_facts:
    id: "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx...o244pucq"
"""

RETURN = """
tenancy:
    description: Information about the specified tenancy
    returned: on success
    type: complex
    contains:
        id:
            description: The OCID of the tenancy.
            returned: always
            type: string
            sample: "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx...o244pucq"
        name:
            description: The name of the tenancy.
            returned: always
            type: string
            sample: "Acme corp"
        description:
            description: The description of the tenancy.
            returned: always
            type: string
            sample: "Acme corp's tenancy"
        home_region_key:
            description: The region key for the tenancy's home region.
            returned: always
            type: string
            sample: "IAD"

    sample: {
                "home_region_key": null,
                "description": "Acme Corp's tenancy",
                "name": "acme-corp",
                "id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx...o244pucq"
            }
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


def get_tenancy_details(identity_client, module):
    try:
        tenancy_ocid = module.params["tenancy_id"]
        tenancy = oci_utils.call_with_backoff(
            identity_client.get_tenancy, tenancy_id=tenancy_ocid
        ).data
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    return to_dict(tenancy)


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(tenancy_id=dict(type="str", required=True, aliases=["id"])))

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    result = get_tenancy_details(identity_client, module)
    module.exit_json(tenancy=result)


if __name__ == "__main__":
    main()

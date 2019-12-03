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
module: oci_instance_credentials_facts
short_description: Retrieve initial credentials assigned to a windows instance in OCI Compute Service
description:
    - This module retrieves initial credential details of a windows instance in OCI compute service
version_added: "2.5"
options:
    instance_id:
        description: The OCID of the instance. Required for retrieving initial credentials for a specific instance.
        required: true
        aliases: ['id']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Get initial credentials assigned to a windows instance in OCI
  oci_instance_credentials_facts:
    id:"ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
"""

RETURN = """
instance_credentials:
    description: Initial credential information for a windows instance
    returned: on success
    type: complex
    contains:
        username:
            description: The username
            returned: always
            type: string
            sample: opc
        password:
            description: The password for the username.
            returned: always
            type: string
            sample: "etR)wpP4m;,vv6m"
    sample: {
        "username": "opc",
        "password": "etR)wpP4m;,vv6m"
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


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(instance_id=dict(type="str", required=True, aliases=["id"]))
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    instance_id = module.params["instance_id"]

    result = dict(changed=False)

    try:
        result["instance_credentials"] = to_dict(
            oci_utils.call_with_backoff(
                compute_client.get_windows_instance_initial_credentials,
                instance_id=instance_id,
            ).data
        )
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(**result)


if __name__ == "__main__":
    main()

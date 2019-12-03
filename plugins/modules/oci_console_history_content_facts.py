#!/usr/bin/python

# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
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
module: oci_console_history_content_facts
short_description: Retrieve the actual console history data of an OCI instance
description:
    - This module retrieves the actual console history data (not the metadata) of an OCI instance
version_added: "2.5"
options:
    instance_console_history_id:
        description: OCID of the target console history.
        required: true
        aliases: ['id']
    offset:
        description: Offset of the snapshot data to retrieve.
        type: int
        required: false
    length:
        description: Length of the snapshot data to retrieve.
        type: int
        required: false
    dest:
        description: The complete file path of the file to which console history data should be written to.
        required: true
    force:
        description: Whether to force overwrite an existing kubeconfig file.
        required: false
        default: false
        aliases: ['overwrite']
        type: bool
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [oracle]
"""

EXAMPLES = """
- name: Get the console history data and write it to the specified file
  oci_console_history_content_facts:
    instance_console_history_id: ocid1.consolehistory.oc1.iad.xxxxxEXAMPLExxxxx...tc7a
    dest: /tmp/my_instance_console_history.txt
"""

RETURN = """
console_history_content:
    description: Details of fetching console history content
    returned: always
    type: dict
    sample: {}
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils._text import to_bytes
import os

try:
    from oci.core.compute_client import ComputeClient
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            instance_console_history_id=dict(type="str", required=True, aliases=["id"]),
            offset=dict(type="int", required=False),
            length=dict(type="int", required=False),
            dest=dict(type="str", required=True),
            force=dict(
                type="bool", required=False, default=False, aliases=["overwrite"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    instance_console_history_id = module.params["instance_console_history_id"]
    try:
        optional_list_method_params = ["offset", "length"]
        optional_kwargs = dict(
            (param, module.params[param])
            for param in optional_list_method_params
            if module.params.get(param) is not None
        )
        console_history_data = oci_utils.call_with_backoff(
            compute_client.get_console_history_content,
            instance_console_history_id=instance_console_history_id,
            **optional_kwargs
        ).data
        dest = module.params["dest"]
        if module.params.get("force") or not os.path.isfile(to_bytes(dest)):
            oci_utils.write_to_file(dest, console_history_data)
        else:
            module.fail_json(
                msg="Destination file {0} already exists, but force is false and so cannot "
                "overwrite the file.".format(dest)
            )

        result = []

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(console_history_content=result)


if __name__ == "__main__":
    main()

#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_cluster_options_facts
short_description: Retrieve options available for clusters in OCI Container Engine for Kubernetes Service
description:
    - This module retrieves options available for clusters in OCI Container Engine for Kubernetes Service.
version_added: "2.5"
options:
    cluster_option_id:
        description: The id of the option set to retrieve. Only "all" is supported.
        choices: ["all"]
        required: true
        aliases: [ 'id' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get all options available for clusters
  oci_cluster_options_facts:
    cluster_option_id: all
"""

RETURN = """
cluster_options:
    description: Options available for clusters
    returned: always
    type: complex
    contains:
        kubernetes_versions:
            description: Available Kubernetes versions.
            returned: always
            type: list
    sample: {
            "kubernetes_versions": [
                "v1.8.11",
                "v1.9.7",
                "v1.10.3",
                "v1.11.1"
            ]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.container_engine.container_engine_client import ContainerEngineClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            cluster_option_id=dict(
                type="str", required=True, choices=["all"], aliases=["id"]
            )
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    container_engine_client = oci_utils.create_service_client(
        module, ContainerEngineClient
    )

    try:
        result = to_dict(
            oci_utils.call_with_backoff(
                container_engine_client.get_cluster_options,
                cluster_option_id=module.params["cluster_option_id"],
            ).data
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(cluster_options=result)


if __name__ == "__main__":
    main()

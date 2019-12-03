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
module: oci_oke_work_request_error_facts
short_description: Retrieve errors of a work request in OCI Container Engine for Kubernetes Service
description:
    - This module retrieves errors of a work request in OCI Container Engine for Kubernetes Service.
version_added: "2.5"
options:
    work_request_id:
        description: The OCID of the work request.
        required: true
    compartment_id:
        description: The OCID of the compartment.
        required: true
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get the errors of a work request
  oci_oke_work_request_error_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    work_request_id: "ocid1.clustersworkrequest.oc1..xxxxxEXAMPLExxxxx"
"""

RETURN = """
work_request_errors:
    description: List of work request errors
    returned: always
    type: complex
    contains:
        code:
            description:  A short error code that defines the error, meant for programmatic parsing.
            returned: always
            type: string
        message:
            description: A human-readable error string.
            returned: always
            type: string
        timestamp:
            description: The date and time the error occurred.
            returned: always
            type: string
    sample: [{
            "code": "GetWorkRequestGeneric",
            "message": "failed to get DNS record from OCI API",
            "timestamp": "2018-08-16T12:20:48Z"
    }]
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
            work_request_id=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
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
            oci_utils.list_all_resources(
                container_engine_client.list_work_request_errors,
                compartment_id=module.params["compartment_id"],
                work_request_id=module.params["work_request_id"],
            )
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(work_request_errors=result)


if __name__ == "__main__":
    main()

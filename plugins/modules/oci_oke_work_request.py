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
module: oci_oke_work_request
short_description: Manage work requests in OCI Container Engine for Kubernetes Service
description:
    - This module allows the user to cancel a work request that has not started in OCI Container Engine for Kubernetes
      Service.
version_added: "2.5"
options:
    work_request_id:
        description: The OCID of the work request. Required to delete a work request.
        required: true
        aliases: [ 'id' ]
    state:
        description: Use I(state=absent) to delete a work request.
        required: false
        default: absent
        choices: ["absent"]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
- name: Cancel a work request
  oci_oke_work_request:
    id: "ocid1.clustersworkrequest.oc1..xxxxxEXAMPLExxxxx"
"""

RETURN = """
work_request:
    description: Information of work request
    returned: On successful delete
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment in which the work request exists.
            returned: always
            type: string
        id:
            description: The OCID of the work request.
            returned: always
            type: string
        operation_type:
            description: The type of work the work request is doing.
            returned: always
            type: string
        resources:
            description: The resources this work request affects.
            returned: always
            type: list
        status:
            description: The current status of the work request.
            returned: always
            type: string
        time_accepted:
            description: The time the work request was accepted.
            returned: always
            type: datetime
        time_finished:
            description: The time the work request was finished.
            returned: always
            type: datetime
        time_started:
            description: The time the work request was started.
            returned: always
            type: datetime
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "id": "ocid1.clustersworkrequest.oc1..xxxxxEXAMPLExxxxx",
            "operation_type": "CLUSTER_CREATE",
            "resources": [],
            "status": "CANCELED",
            "time_accepted": "2018-07-26T18:42:26+00:00",
            "time_finished": "2018-07-26T18:44:13+00:00",
            "time_started": "2018-07-26T18:43:26+00:00"

    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle import oci_ce_utils

try:
    from oci.container_engine.container_engine_client import ContainerEngineClient

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def delete_work_request(container_engine_client, module):
    result = oci_ce_utils.delete_and_wait(
        resource_type="work_request",
        client=container_engine_client,
        get_fn=container_engine_client.get_work_request,
        kwargs_get={"work_request_id": module.params["work_request_id"]},
        delete_fn=container_engine_client.delete_work_request,
        kwargs_delete={"work_request_id": module.params["work_request_id"]},
        module=module,
    )
    return result


def main():
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            work_request_id=dict(type="str", required=True, aliases=["id"]),
            state=dict(
                type="str", required=False, default="absent", choices=["absent"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    container_engine_client = oci_utils.create_service_client(
        module, ContainerEngineClient
    )

    result = delete_work_request(container_engine_client, module)
    module.exit_json(**result)


if __name__ == "__main__":
    main()

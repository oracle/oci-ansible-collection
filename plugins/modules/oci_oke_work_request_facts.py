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
module: oci_oke_work_request_facts
short_description: Retrieve facts of work requests in OCI Container Engine for Kubernetes Service
description:
    - This module retrieves information of a specified work request or lists work requests in a compartment.
version_added: "2.5"
options:
    work_request_id:
        description: The OCID of the work request. I(work_request_id) is required to get a specific work request's
                     information.
        required: false
        aliases: [ 'id' ]
    compartment_id:
        description: The OCID of the compartment. Required to list all the work requests in a compartment.
        required: false
    cluster_id:
        description: The OCID of the cluster. Use I(cluster_id) with I(compartment_id) to filter work requests related
                     to a cluster in the specified compartment.
        required: false
    resource_id:
        description: The OCID of the resource associated with a work request. Use I(resource_id) with I(compartment_id)
                     to filter work requests related to a resource in the specified compartment.
        required: false
    resource_type:
        description: Type of the resource associated with a work request. Use I(resource_type) with I(compartment_id)
                     to filter work requests related to the resource type in the specified compartment.
        required: false
        choices: ["CLUSTER", "NODEPOOL"]
    status:
        description: A work request status to filter on. Can have multiple parameters of this name. Allowed values are
                     "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED".
        required: false
        type: list
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get all the work requests in a specific compartment
  oci_oke_work_request_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get a specific work request
  oci_oke_work_request_facts:
    id: ocid1.clustersworkrequest.oc1..xxxxxEXAMPLExxxxx

- name: Get all the work requests in compartment associated with a particular cluster
  oci_oke_work_request_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    cluster_id: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx

- name: Get all work requests in a compartment for a specified cluster in which resource of type NODEPOOL is associated
  oci_oke_work_request_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    cluster_id: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx
    resource_type: NODEPOOL
"""

RETURN = """
work_requests:
    description: List of work request details
    returned: always
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
    sample: [{
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "id": "ocid1.clustersworkrequest.oc1..xxxxxEXAMPLExxxxx",
            "operation_type": "CLUSTER_CREATE",
            "resources": [
                {
                    "action_type": "IN_PROGRESS",
                    "entity_type": "cluster",
                    "entity_uri": "/clusters/ocid1.cluster.oc1..xxxxxEXAMPLExxxxx",
                    "identifier": "ocid1.cluster.oc1..xxxxxEXAMPLExxxxx"
                }
            ],
            "status": "ACCEPTED",
            "time_accepted": "2018-07-26T18:42:26+00:00",
            "time_finished": "2018-07-26T18:44:13+00:00",
            "time_started": "2018-07-26T18:43:26+00:00"

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
            work_request_id=dict(type="str", required=False, aliases=["id"]),
            compartment_id=dict(type="str", required=False),
            cluster_id=dict(type="str", required=False),
            resource_id=dict(type="str", required=False),
            resource_type=dict(
                type="str", required=False, choices=["CLUSTER", "NODEPOOL"]
            ),
            status=dict(type="list", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "work_request_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    container_engine_client = oci_utils.create_service_client(
        module, ContainerEngineClient
    )

    work_request_id = module.params["work_request_id"]

    try:
        if work_request_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        container_engine_client.get_work_request,
                        work_request_id=work_request_id,
                    ).data
                )
            ]
        else:
            kwargs_list = {"compartment_id": module.params["compartment_id"]}
            list_args = ["cluster_id", "resource_id", "resource_type", "status"]
            for arg in list_args:
                if module.params[arg]:
                    kwargs_list[arg] = module.params[arg]
            result = to_dict(
                oci_utils.list_all_resources(
                    container_engine_client.list_work_requests, **kwargs_list
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(work_requests=result)


if __name__ == "__main__":
    main()

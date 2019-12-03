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
module: oci_load_balancer_work_request_facts
short_description: Fetch details of all work_requests of a load balancer
description:
    - Fetch details of all work_requests of a load balancer.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer to which the Work Requests belongs.
                     Mutually exclusive with work_request_id.
        required: false
        aliases: ['id']
    work_request_id:
        description: Identifier of the Work Request whose details needs to be fetched.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch details of all Work Request of a Load Balancer
- name: List all Work Requests
  oci_load_balancer_work_request_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'

#Fetch details of a specific Work Request in a Load Balancer
- name: List a specific Work Request
  oci_load_balancer_work_request_facts:
      work_request_id: 'ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
work_requests:
    description: Attributes of the Work Requests fetched.
    returned: success
    type: complex
    contains:
        error_details:
            description: Error details of the work request
            returned: always
            type: list
            sample: [{
                       "errorCode" : "BAD_INPUT",
                       "message" : "Default Listener on port '80' refer to VIP 'private-vip' twice"
                     }
                    ]
        id:
            description: Identifier of the Work Request
            returned: always
            type: string
            sample: ocid1.loadbalancerworkrequest.oc1.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: The current state of the Load Balancer
            returned: always
            type: string
            sample: ACCEPTED
        load_balancer_id:
            description: The OCID of the load balancer the Work Request is associated with.
            returned: always
            type: string
            sample: ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx
        message:
            description: A collection of data, related to the load balancer provisioning process, that helps with
                         debugging in the event of failure. Possible data elements include
                         - workflow name
                         - event ID
                         - work request ID
                         - load balancer ID
                         - workflow completion message
            returned: always
            type: string
            sample: { "eventId" : "43644f81-8724-1324",
                      "loadBalancerId" : "ocid1.loadbalancer..aaaa",
                      "workflowName" : "AddHostnameWorkflow",
                      "type" : "SUCCESS","message" : "OK",
                      "workRequestId" : "ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx"
                    }
        time_accepted:
            description: The date and time the work request was created, in the format defined by RFC3339.
            returned: always
            type: datetime
            sample: 2018-06-26T21:10:29.600Z
        time_finished:
            description: The date and time the work request was completed, in the format defined by RFC3339.
            returned: always
            type: datetime
            sample: 2018-06-26T21:112:29.600Z
        type:
            description: The type of action the work request represents.
            returned: always
            type: string
            sample: [
                        {
                          "error_details":[],
                          "id":"ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx",
                          "lifecycle_state":"SUCCEEDED",
                          "load_balancer_id":"ocid1.loadbalancer..aaaa",
                          "message": {
                            "eventId" : "43644f81-8724-44b0-a13",
                            "loadBalancerId" : "ocid1.loadbalancer..aaaa",
                            "workflowName" : "AddHostnameWorkflow",
                            "type" : "SUCCESS",
                            "message" : "OK",
                            "workRequestId" : "ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx"
                            },
                            "time_accepted":"2018-06-22T09:02:38.505000+00:00",
                            "time_finished":"2018-06-22T09:02:54.687000+00:00",
                            "type":"CreateHostname"
                        },
                        {
                          "error_details":[],
                          "id":"ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx",
                          "lifecycle_state":"SUCCEEDED",
                          "load_balancer_id":"ocid1.loadbalancer..aaaa",
                          "message": {
                            "eventId" : "43644f81-8724-44b0-a14",
                            "loadBalancerId" : "ocid1.loadbalancer..aaaa",
                            "workflowName" : "AddHostnameWorkflow",
                            "type" : "SUCCESS",
                            "message" : "OK",
                            "workRequestId" : "ocid1.loadbalancerworkrequest.oc1.iad.xxxxxEXAMPLExxxxx"
                            },
                            "time_accepted":"2018-06-22T09:02:38.505000+00:00",
                            "time_finished":"2018-06-22T09:02:54.687000+00:00",
                            "type":"CreateHostname"
                        }
                    ]
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_load_balancer_work_requests(lb_client, module):
    result = dict(work_requests="")
    work_request_id = module.params.get("work_request_id")
    load_balancer_id = module.params.get("load_balancer_id")
    try:
        if load_balancer_id:
            get_logger().debug(
                "Listing all Work Requests under load balancer %s", load_balancer_id
            )
            existing_work_requests = oci_utils.list_all_resources(
                lb_client.list_work_requests, load_balancer_id=load_balancer_id
            )
        else:
            get_logger().debug("Listing Work Request %s ", work_request_id)
            response = oci_utils.call_with_backoff(
                lb_client.get_work_request, work_request_id=work_request_id
            )
            existing_work_requests = [response.data]
    except ServiceError as ex:
        get_logger().error("Unable to list Work Request due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["work_requests"] = to_dict(existing_work_requests)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_work_request_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            work_request_id=dict(type="str", required=False),
            load_balancer_id=dict(type="str", required=False, aliases=["id"]),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args, mutually_exclusive=[["work_request_id", "id"]]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    result = list_load_balancer_work_requests(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()

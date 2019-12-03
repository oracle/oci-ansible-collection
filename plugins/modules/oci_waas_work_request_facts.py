#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
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
module: oci_waas_work_request_facts
short_description: Retrieve details about WAAS policy work requests.
description:
    - This module retrieves information of a specific work request or lists all the work requests in the given WAAS
      policy and compartment.
version_added: "2.5"
options:
    waas_policy_id:
        description: The OCID of the WAAS policy.
        type: str
    compartment_id:
        description: The OCID of the compartment.
        type: str
    work_request_id:
        description: The OCID of the work request. Required to retrieve a specific work request.
        type: str
    sort_by:
        description: The value by which work requests are sorted in a paginated 'List' call.
                     If unspecified, defaults to timeAccepted.
        type: str
        choices: ["id", "status", "timeAccepted", "timeStarted", "timeFinished", "operationType"]
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle, oracle_sort_order_option ]
"""

EXAMPLES = """
- name: Get all the work requests for a waas policy in a compartment
  oci_waas_work_request_facts:
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get all the work requests for a waas policy in a compartment sorted by timeFinished
  oci_waas_work_request_facts:
    waas_policy_id: ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    sort_by: timeFinished

- name: Get a specific waas work request using its OCID
  oci_waas_work_request_facts:
    work_request_id: ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx
"""

RETURN = """
waas_work_requests:
    description: List of work requests
    returned: on success
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment that contains the work request.
            returned: success
            type: str
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        errors:
            description: The list of errors that occurred while fulfilling the work request.
            returned: success
            type: list
            sample: []
        id:
            description: The OCID of the work request.
            returned: success
            type: str
            sample: ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx
        logs:
            description: The list of log entries from the work request workflow.
            returned: success
            type: list
            sample: [
                {
                    "message": "Work request complete",
                    "timestamp": "2019-04-10T19:31:57.364000+00:00"
                },
                {
                    "message": "PersistWaasOp: start (100% of request completed)",
                    "timestamp": "2019-04-10T19:31:57.360000+00:00"
                },
                {
                    "message": "Starting Work Request",
                    "timestamp": "2019-04-10T19:31:57.261000+00:00"
                }
            ]
        operation_type:
            description: A description of the operation requested by the work request.
            returned: success
            type: str
            sample: "CREATE_WAAS_POLICY"
        percent_complete:
            description: The percentage of work completed by the work request.
            returned: success
            type: int
            sample: 50
        resources:
            description: The resources being used to complete the work request operation.
            returned: success
            type: str
            sample: [
                {
                    "action_type": "CREATED",
                    "entity_type": "waas",
                    "entity_uri": "/20181116/waasPolicies/ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx",
                    "identifier": "ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx"
                }
            ]
        status:
            description: The current status of the work request.
            returned: success
            type: str
            sample: "IN_PROGRESS"
        time_accepted:
            description: The date and time the work request was created, in the format defined by RFC3339.
            returned: success
            type: str
            sample: 2019-03-22T13:02:55.563000+00:00
        time_finished:
            description: The date and time the work request was fulfilled or terminated, expressed in RFC 3339
                         timestamp format.
            returned: success
            type: str
            sample: 2019-03-22T13:02:59.563000+00:00
        time_started:
            description: The date and time the work request moved from the ACCEPTED state to the IN_PROGRESS state,
                         expressed in RFC 3339 timestamp format.
            returned: success
            type: str
            sample: 2019-03-22T13:02:56.563000+00:00
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
        "errors": [],
        "id": "ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx",
        "logs": [
            {
                "message": "addWhitelistOp: start",
                "timestamp": "2019-04-10T18:46:05.663000+00:00"
            },
            {
                "message": "addWhitelistOp: finished (45% of request completed)",
                "timestamp": "2019-04-10T18:46:05.663000+00:00"
            },
            {
                "message": "updateProtectionSettingsOp: start",
                "timestamp": "2019-04-10T18:46:05.403000+00:00"
            },
        ],
        "operation_type": "CREATE_WAAS_POLICY",
        "percent_complete": 45,
        "resources": [
            {
                "action_type": "CREATED",
                "entity_type": "waas",
                "entity_uri": "/20181116/waasPolicies/ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx",
                "identifier": "ocid1.waaspolicy.oc1..xxxxxEXAMPLExxxxx"
            }
        ],
        "status": "IN_PROGRESS",
        "time_accepted": "2019-04-10T18:45:45.044000+00:00",
        "time_finished": null,
        "time_started": "2019-04-10T18:45:49+00:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.waas.waas_client import WaasClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def list_work_requests(waas_client, module):
    if not (
        module.params.get("waas_policy_id") and module.params.get("compartment_id")
    ):
        module.fail_json(
            msg="waas_policy_id and compartment_id are required to list work requests."
        )
    optional_list_method_params = ["sort_by", "sort_order"]
    optional_kwargs = dict(
        (param, module.params[param])
        for param in optional_list_method_params
        if module.params.get(param) is not None
    )
    return to_dict(
        [
            oci_utils.call_with_backoff(
                waas_client.get_work_request, work_request_id=work_request.id
            ).data
            for work_request in oci_utils.list_all_resources(
                waas_client.list_work_requests,
                waas_policy_id=module.params["waas_policy_id"],
                compartment_id=module.params["compartment_id"],
                **optional_kwargs
            )
        ]
    )


def get_work_request(waas_client, module):
    return to_dict(
        [
            oci_utils.call_with_backoff(
                waas_client.get_work_request,
                work_request_id=module.params["work_request_id"],
            ).data
        ]
    )


def main():
    module_args = oci_utils.get_facts_module_arg_spec(
        filter_by_display_name=False,
        supports_sort=True,
        sort_by_choices=[
            "id",
            "status",
            "timeAccepted",
            "timeStarted",
            "timeFinished",
            "operationType",
        ],
    )
    module_args.update(
        dict(
            work_request_id=dict(type="str"),
            compartment_id=dict(type="str"),
            waas_policy_id=dict(type="str"),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[
            ["work_request_id", "compartment_id"],
            ["work_request_id", "waas_policy_id"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    waas_client = oci_utils.create_service_client(module, WaasClient)

    try:
        if module.params["work_request_id"]:
            result = get_work_request(waas_client, module)
        elif module.params["waas_policy_id"] and module.params["compartment_id"]:
            result = list_work_requests(waas_client, module)
        else:
            module.fail_json(
                msg="Specify waas_policy_id and compartment_id to get all the work requests for a waas policy in the"
                "compartment or work_request_id to retrieve a specific work request."
            )
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(waas_work_requests=result)


if __name__ == "__main__":
    main()

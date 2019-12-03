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
module: oci_waas_work_request
short_description: Manage WAAS policy work requests in OCI
description:
    - This module allows the user to cancel a WAAS policy work request in OCI.
version_added: "2.5"
options:
    work_request_id:
        description: The OCID of the work request. Required to retrieve a specific work request.
        type: str
        required: true
    state:
        description: Cancel a WAAS work request with I(state=cancelled).
        default: cancelled
        choices: ['cancelled']
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
- name: Cancel a waas work request
  oci_waas_work_request:
    work_request_id: "ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx"
    state: cancelled

- name: Cancel a waas work request without explicitly stating the state as it is default
  oci_waas_work_request:
    work_request_id: "ocid1.waasworkrequest.oc1..xxxxxEXAMPLExxxxx"
"""

RETURN = """
waas_work_request:
    description: Information about the WAAS work request.
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
            sample: []
        operation_type:
            description: A description of the operation requested by the work request.
            returned: success
            type: str
            sample: "UPDATE_WAAS_POLICY"
        percent_complete:
            description: The percentage of work completed by the work request.
            returned: success
            type: int
            sample: 0
        resources:
            description: The resources being used to complete the work request operation.
            returned: success
            type: str
            sample: []
        status:
            description: The current status of the work request.
            returned: success
            type: str
            sample: "CANCELLED"
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
            sample: null
        time_started:
            description: The date and time the work request moved from the ACCEPTED state to the IN_PROGRESS state,
                         expressed in RFC 3339 timestamp format.
            returned: success
            type: str
            sample: null
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
        "errors": [],
        "logs": [],
        "operation_type": "UPDATE_WAAS_POLICY",
        "percent_complete": 0,
        "resources": [],
        "status": "CANCELLED",
        "time_accepted": "2019-03-22T13:02:55.563000+00:00",
        "time_finished": null,
        "time_started": null,
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    import oci
    from oci.util import to_dict
    from oci.exceptions import ServiceError
    from oci.waas.waas_client import WaasClient

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def cancel_work_request(waas_client, module):
    result = dict(changed=False)
    oci_utils.call_with_backoff(
        waas_client.cancel_work_request,
        work_request_id=module.params["work_request_id"],
    )
    result["changed"] = True
    work_request_response = oci_utils.call_with_backoff(
        waas_client.get_work_request, work_request_id=module.params["work_request_id"]
    )
    if not module.params.get("wait"):
        result["waas_work_request"] = to_dict(work_request_response.data)
        return result
    work_request_response = oci.wait_until(
        waas_client,
        work_request_response,
        evaluate_response=lambda r: r.data.status in oci_utils.CANCELLED_STATES,
        max_wait_seconds=module.params.get(
            "wait_timeout", oci_utils.MAX_WAIT_TIMEOUT_IN_SECONDS
        ),
    )
    result["waas_work_request"] = to_dict(work_request_response.data)
    return result


def main():
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            work_request_id=dict(type="str", required=True),
            state=dict(type="str", default="cancelled", choices=["cancelled"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    waas_client = oci_utils.create_service_client(module, WaasClient)

    try:
        result = cancel_work_request(waas_client, module)
    except ServiceError as se:
        module.fail_json(
            msg="Cancelling work request failed with error: {0}".format(se.message)
        )
    module.exit_json(**result)


if __name__ == "__main__":
    main()

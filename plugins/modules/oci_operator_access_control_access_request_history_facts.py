#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_operator_access_control_access_request_history_facts
short_description: Fetches details about one or multiple AccessRequestHistory resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AccessRequestHistory resources in Oracle Cloud Infrastructure
    - Returns a history of all status associated with the accessRequestId.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    access_request_id:
        description:
            - unique AccessRequest identifier
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List access_request_histories
  oci_operator_access_control_access_request_history_facts:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
access_request_histories:
    description:
        - List of AccessRequestHistory resources
    returned: on success
    type: complex
    contains:
        lifecycle_state:
            description:
                - The current state of the AccessRequest.
            returned: on success
            type: str
            sample: CREATED
        user_id:
            description:
                - Approver who modified the access request.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Reason or description about the cause of change.
            returned: on success
            type: str
            sample: description_example
        duration:
            description:
                - Duration for approval of request or extension depending on the type of action.
            returned: on success
            type: int
            sample: 56
        is_auto_approved:
            description:
                - Whether the access request was automatically approved.
            returned: on success
            type: bool
            sample: true
        actions_list:
            description:
                - List of operator actions for which approvals were requested by the operator.
            returned: on success
            type: list
            sample: []
        time_of_action:
            description:
                - "Time when the respective action happened in L(RFC 3339,https://tools.ietf.org/html/rfc3339)timestamp format. Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "lifecycle_state": "CREATED",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "duration": 56,
        "is_auto_approved": true,
        "actions_list": [],
        "time_of_action": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.operator_access_control import AccessRequestsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessRequestHistoryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "access_request_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_access_request_histories,
            access_request_id=self.module.params.get("access_request_id"),
            **optional_kwargs
        )


AccessRequestHistoryFactsHelperCustom = get_custom_class(
    "AccessRequestHistoryFactsHelperCustom"
)


class ResourceFactsHelper(
    AccessRequestHistoryFactsHelperCustom, AccessRequestHistoryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(access_request_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="access_request_history",
        service_client_class=AccessRequestsClient,
        namespace="operator_access_control",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(access_request_histories=result)


if __name__ == "__main__":
    main()

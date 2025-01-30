#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_lockbox_access_request_actions
short_description: Perform actions on an AccessRequest resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AccessRequest resource in Oracle Cloud Infrastructure
    - For I(action=handle), handle the AccessRequest
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    access_request_id:
        description:
            - The unique identifier (OCID) of the access request.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action take by persona
        type: str
        choices:
            - "approve"
            - "deny"
            - "revoke"
            - "cancel"
        required: true
    msg:
        description:
            - Action justification or details.
        type: str
        aliases: ["message"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action approve on access_request
  oci_lockbox_access_request_actions:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"
    action: APPROVE

    # optional
    msg: msg_example

- name: Perform action deny on access_request
  oci_lockbox_access_request_actions:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"
    action: APPROVE

    # optional
    msg: msg_example

- name: Perform action revoke on access_request
  oci_lockbox_access_request_actions:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"
    action: APPROVE

    # optional
    msg: msg_example

- name: Perform action cancel on access_request
  oci_lockbox_access_request_actions:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"
    action: APPROVE

    # optional
    msg: msg_example

"""

RETURN = """
access_request:
    description:
        - Details of the AccessRequest resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier (OCID) of the access request, which can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lockbox_id:
            description:
                - The unique identifier (OCID) of the lockbox box that the access request is associated with, which can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the access request.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - "The rationale for requesting the access request and any other related details.."
            returned: on success
            type: str
            sample: description_example
        requestor_id:
            description:
                - The unique identifier of the requestor.
            returned: on success
            type: str
            sample: "ocid1.requestor.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Possible access request lifecycle states.
            returned: on success
            type: str
            sample: IN_PROGRESS
        lifecycle_state_details:
            description:
                - Details of access request lifecycle state.
            returned: on success
            type: str
            sample: PROCESSING
        access_duration:
            description:
                - The maximum amount of time operator has access to associated resources.
            returned: on success
            type: str
            sample: access_duration_example
        context:
            description:
                - The context object containing the access request specific details.
            returned: on success
            type: dict
            sample: {}
        activity_logs:
            description:
                - The actions taken by different persona on the access request, e.g. approve/deny/revoke
            returned: on success
            type: complex
            contains:
                user_id:
                    description:
                        - User OCID of the persona
                    returned: on success
                    type: str
                    sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
                user_level:
                    description:
                        - Level of the persona
                    returned: on success
                    type: str
                    sample: LEVEL1
                action:
                    description:
                        - The action take by persona
                    returned: on success
                    type: str
                    sample: APPROVE
                message:
                    description:
                        - The action justification or details.
                    returned: on success
                    type: str
                    sample: message_example
                time_updated:
                    description:
                        - "The time the action was taken. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                          Example: `2020-01-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - "The time the access request was created. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time the access request was last updated. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_expired:
            description:
                - "The time the access request expired. Format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lockbox_id": "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "requestor_id": "ocid1.requestor.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "IN_PROGRESS",
        "lifecycle_state_details": "PROCESSING",
        "access_duration": "access_duration_example",
        "context": {},
        "activity_logs": [{
            "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
            "user_level": "LEVEL1",
            "action": "APPROVE",
            "message": "message_example",
            "time_updated": "2013-10-20T19:20:30+01:00"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_expired": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.lockbox import LockboxClient
    from oci.lockbox.models import HandleAccessRequestDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessRequestActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        handle
    """

    @staticmethod
    def get_module_resource_id_param():
        return "access_request_id"

    def get_module_resource_id(self):
        return self.module.params.get("access_request_id")

    def get_get_fn(self):
        return self.client.get_access_request

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_request,
            access_request_id=self.module.params.get("access_request_id"),
        )

    def get_action_fn(self, action):
        action = action.lower()
        if action in [
            "approve",
            "deny",
            "revoke",
            "cancel",
        ]:
            self.module.params["action"] = action.upper()
            return getattr(self, "handle", None)
        return super(AccessRequestActionsHelperGen, self).get_action_fn(action)

    def handle(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, HandleAccessRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.handle_access_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                handle_access_request_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AccessRequestActionsHelperCustom = get_custom_class("AccessRequestActionsHelperCustom")


class ResourceHelper(AccessRequestActionsHelperCustom, AccessRequestActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            access_request_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["approve", "deny", "revoke", "cancel"],
            ),
            msg=dict(aliases=["message"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="access_request",
        service_client_class=LockboxClient,
        namespace="lockbox",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

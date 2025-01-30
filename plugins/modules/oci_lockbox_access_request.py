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
module: oci_lockbox_access_request
short_description: Manage an AccessRequest resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create an AccessRequest resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new access request.
    - "This resource has the following action operations in the M(oracle.oci.oci_lockbox_access_request_actions) module: approve, deny, revoke, cancel."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    lockbox_id:
        description:
            - The unique identifier (OCID) of the lockbox box that the access request is associated with which is immutable.
        type: str
        required: true
    display_name:
        description:
            - The name of the access request.
        type: str
        aliases: ["name"]
    description:
        description:
            - The rationale for requesting the access request.
        type: str
        required: true
    context:
        description:
            - The context object containing the access request specific details.
        type: dict
    access_duration:
        description:
            - The maximum amount of time operator has access to associated resources.
        type: str
        required: true
    state:
        description:
            - The state of the AccessRequest.
            - Use I(state=present) to create an AccessRequest.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create access_request
  oci_lockbox_access_request:
    # required
    lockbox_id: "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx"
    description: description_example
    access_duration: access_duration_example

    # optional
    display_name: display_name_example
    context: null

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.lockbox import LockboxClient
    from oci.lockbox.models import CreateAccessRequestDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessRequestHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get and list"""

    def get_possible_entity_types(self):
        return super(AccessRequestHelperGen, self).get_possible_entity_types() + [
            "lockboxaccessrequest",
            "lockboxaccessrequests",
            "lockboxlockboxaccessrequest",
            "lockboxlockboxaccessrequests",
            "lockboxaccessrequestresource",
            "lockboxaccessrequestsresource",
            "accessrequest",
            "accessrequests",
            "accessrequestresource",
            "accessrequestsresource",
            "lockbox",
        ]

    def get_get_fn(self):
        return self.client.get_access_request

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_request, access_request_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_request,
            access_request_id=self.module.params.get("access_request_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["lockbox_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_access_requests, **kwargs
        )

    def get_create_model_class(self):
        return CreateAccessRequestDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_access_request,
            call_fn_args=(),
            call_fn_kwargs=dict(create_access_request_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AccessRequestHelperCustom = get_custom_class("AccessRequestHelperCustom")


class ResourceHelper(AccessRequestHelperCustom, AccessRequestHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            lockbox_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str", required=True),
            context=dict(type="dict"),
            access_duration=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
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

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

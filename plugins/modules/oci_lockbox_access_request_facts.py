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
module: oci_lockbox_access_request_facts
short_description: Fetches details about one or multiple AccessRequest resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AccessRequest resources in Oracle Cloud Infrastructure
    - Retrieves a list of AccessRequestSummary objects in a compartment.
    - If I(access_request_id) is specified, the details of a single AccessRequest will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    access_request_id:
        description:
            - The unique identifier (OCID) of the access request.
            - Required to get a specific access_request.
        type: str
        aliases: ["id"]
    lockbox_id:
        description:
            - The unique identifier (OCID) of the associated lockbox.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "IN_PROGRESS"
            - "WAITING"
            - "SUCCEEDED"
            - "CANCELING"
            - "CANCELED"
            - "FAILED"
    lockbox_partner:
        description:
            - The name of the lockbox partner.
        type: str
        choices:
            - "FAAAS"
            - "CANARY"
    requestor_id:
        description:
            - The unique identifier (OCID) of the requestor in which to list resources.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
            - "id"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific access_request
  oci_lockbox_access_request_facts:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"

- name: List access_requests
  oci_lockbox_access_request_facts:

    # optional
    lockbox_id: "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: IN_PROGRESS
    lockbox_partner: FAAAS
    requestor_id: "ocid1.requestor.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
access_requests:
    description:
        - List of AccessRequest resources
    returned: on success
    type: complex
    contains:
        lifecycle_state_details:
            description:
                - Details of access request lifecycle state.
                - Returned for get operation
            returned: on success
            type: str
            sample: PROCESSING
        context:
            description:
                - The context object containing the access request specific details.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        activity_logs:
            description:
                - The actions taken by different persona on the access request, e.g. approve/deny/revoke
                - Returned for get operation
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
        access_duration:
            description:
                - The maximum amount of time operator has access to associated resources.
            returned: on success
            type: str
            sample: access_duration_example
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
    sample: [{
        "lifecycle_state_details": "PROCESSING",
        "context": {},
        "activity_logs": [{
            "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
            "user_level": "LEVEL1",
            "action": "APPROVE",
            "message": "message_example",
            "time_updated": "2013-10-20T19:20:30+01:00"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lockbox_id": "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "requestor_id": "ocid1.requestor.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "IN_PROGRESS",
        "access_duration": "access_duration_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_expired": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.lockbox import LockboxClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessRequestFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "access_request_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_request,
            access_request_id=self.module.params.get("access_request_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lockbox_id",
            "display_name",
            "lifecycle_state",
            "lockbox_partner",
            "requestor_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_access_requests, **optional_kwargs
        )


AccessRequestFactsHelperCustom = get_custom_class("AccessRequestFactsHelperCustom")


class ResourceFactsHelper(AccessRequestFactsHelperCustom, AccessRequestFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            access_request_id=dict(aliases=["id"], type="str"),
            lockbox_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "IN_PROGRESS",
                    "WAITING",
                    "SUCCEEDED",
                    "CANCELING",
                    "CANCELED",
                    "FAILED",
                ],
            ),
            lockbox_partner=dict(type="str", choices=["FAAAS", "CANARY"]),
            requestor_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName", "id"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="access_request",
        service_client_class=LockboxClient,
        namespace="lockbox",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(access_requests=result)


if __name__ == "__main__":
    main()

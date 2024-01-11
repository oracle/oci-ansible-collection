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
module: oci_ons_publish_result
short_description: Manage a PublishResult resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a PublishResult resource in Oracle Cloud Infrastructure
    - For I(state=present), publishes a message to the specified topic.
    - The topic endpoint is required for this operation.
      To get the topic endpoint, use L(GetTopic,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/notification/20181201/NotificationTopic/GetTopic)
      and review the `apiEndpoint` value in the response (L(NotificationTopic,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/notification/20181201/NotificationTopic)).
    - Limits information follows.
    - "Message size limit per request: 64KB."
    - "Message delivery rate limit per endpoint: 60 messages per minute for HTTP-based protocols, 10 messages per minute for the `EMAIL` protocol.
      HTTP-based protocols use URL endpoints that begin with \\"http:\\" or \\"https:\\"."
    - "Transactions Per Minute (TPM) per-tenancy limit for this operation: 60 per topic. (This TPM limit represents messages per minute.)"
    - For more information about publishing messages, see L(Publishing
      Messages,https://docs.cloud.oracle.com/iaas/Content/Notification/Tasks/publishingmessages.htm).
      For steps to request a limit increase, see L(Requesting a Service Limit
      Increase,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#three).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    topic_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic.
        type: str
        required: true
    title:
        description:
            - The title of the message to be published. Avoid entering confidential information.
        type: str
    body:
        description:
            - The body of the message to be published.
              Avoid entering confidential information.
        type: str
        required: true
    message_type:
        description:
            - "**Deprecated.**
              Support for JSON is deprecated.
              You can send a JSON payload even when transmitting the payload as a raw string.
              Configure your receiving system to read the raw payload as JSON format."
            - "Type of message body in the request.
              For `messageType` of JSON, a default key-value pair is required. Example: `{\\"default\\": \\"Alarm breached\\", \\"Email\\": \\"Alarm breached:
              <url>\\"}.`"
        type: str
        choices:
            - "JSON"
            - "RAW_TEXT"
    state:
        description:
            - The state of the PublishResult.
            - Use I(state=present) to create a PublishResult.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create publish_result
  oci_ons_publish_result:
    # required
    topic_id: "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx"
    body: body_example

    # optional
    title: title_example
    message_type: JSON

"""

RETURN = """
publish_result:
    description:
        - Details of the PublishResult resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        message_id:
            description:
                - The UUID of the message.
            returned: on success
            type: str
            sample: "ocid1.message.oc1..xxxxxxEXAMPLExxxxxx"
        time_stamp:
            description:
                - The time that the service received the message.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "message_id": "ocid1.message.oc1..xxxxxxEXAMPLExxxxxx",
        "time_stamp": "2013-10-20T19:20:30+01:00"
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
    from oci.ons import NotificationDataPlaneClient
    from oci.ons.models import MessageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublishResultHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_possible_entity_types(self):
        return super(PublishResultHelperGen, self).get_possible_entity_types() + [
            "publishresult",
            "publishresults",
            "onspublishresult",
            "onspublishresults",
            "publishresultresource",
            "publishresultsresource",
            "message",
            "messages",
            "onsmessage",
            "onsmessages",
            "messageresource",
            "messagesresource",
            "ons",
        ]

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return MessageDetails

    def create_resource(self):
        create_details = self.get_create_model()
        optional_enum_params = [
            "message_type",
        ]
        optional_enum_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_enum_params
            if self.module.params.get(param) is not None
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.publish_message,
            call_fn_args=(),
            call_fn_kwargs=dict(
                topic_id=self.module.params.get("topic_id"),
                message_details=create_details,
                **optional_enum_kwargs
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


PublishResultHelperCustom = get_custom_class("PublishResultHelperCustom")


class ResourceHelper(PublishResultHelperCustom, PublishResultHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            topic_id=dict(type="str", required=True),
            title=dict(type="str"),
            body=dict(type="str", required=True),
            message_type=dict(type="str", choices=["JSON", "RAW_TEXT"]),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="publish_result",
        service_client_class=NotificationDataPlaneClient,
        namespace="ons",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

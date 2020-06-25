#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_ons_notification_topic
short_description: Manage a NotificationTopic resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a NotificationTopic resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a topic in the specified compartment. For general information about topics, see
      L(Managing Topics and Subscriptions,https://docs.cloud.oracle.com/iaas/Content/Notification/Tasks/managingtopicsandsubscriptions.htm).
    - For the purposes of access control, you must provide the OCID of the compartment where you want the topic to reside.
      For information about access control and compartments, see L(Overview of the IAM
      Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
    - You must specify a display name for the topic.
    - All Oracle Cloud Infrastructure resources, including topics, get an Oracle-assigned, unique ID called an
      Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also
      retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the
      Console. For more information, see L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "Transactions Per Minute (TPM) per-tenancy limit for this operation: 60."
version_added: "2.9"
author: Oracle (@oracle)
options:
    name:
        description:
            - The name of the topic being created. The topic name must be unique across the tenancy. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to create the topic in.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - The description of the topic being created. Avoid entering confidential information.
            - Required for update using I(state=present) with topic_id present.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    topic_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic to update.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the NotificationTopic.
            - Use I(state=present) to create or update a NotificationTopic.
            - Use I(state=absent) to delete a NotificationTopic.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create notification_topic
  oci_ons_notification_topic:
    name: Admins
    compartment_id: compartment_OCID
    description: Channel for admin messages

- name: Update notification_topic using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ons_notification_topic:
    description: Channel for admin messages

- name: Update notification_topic
  oci_ons_notification_topic:
    description: Channel for admin messages
    topic_id: ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete notification_topic
  oci_ons_notification_topic:
    topic_id: ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete notification_topic using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ons_notification_topic:
    name: Admins
    compartment_id: compartment_OCID
    state: absent

"""

RETURN = """
notification_topic:
    description:
        - Details of the NotificationTopic resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the topic.
            returned: on success
            type: string
            sample: name_example
        topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic.
            returned: on success
            type: string
            sample: ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment for the topic.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The lifecycle state of the topic.
            returned: on success
            type: string
            sample: ACTIVE
        description:
            description:
                - The description of the topic.
            returned: on success
            type: string
            sample: description_example
        time_created:
            description:
                - The time the topic was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        etag:
            description:
                - For optimistic concurrency control. See `if-match`.
            returned: on success
            type: string
            sample: etag_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        api_endpoint:
            description:
                - The endpoint for managing subscriptions or publishing messages to the topic.
            returned: on success
            type: string
            sample: api_endpoint_example
    sample: {
        "name": "name_example",
        "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "etag": "etag_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "api_endpoint": "api_endpoint_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.ons import NotificationControlPlaneClient
    from oci.ons.models import CreateTopicDetails
    from oci.ons.models import TopicAttributesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NotificationTopicHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "topic_id"

    def get_module_resource_id(self):
        return self.module.params.get("topic_id")

    def get_get_fn(self):
        return self.client.get_topic

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_topic, topic_id=self.module.params.get("topic_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(self.client.list_topics, **kwargs)

    def get_create_model_class(self):
        return CreateTopicDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_topic,
            call_fn_args=(),
            call_fn_kwargs=dict(create_topic_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return TopicAttributesDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_topic,
            call_fn_args=(),
            call_fn_kwargs=dict(
                topic_id=self.module.params.get("topic_id"),
                topic_attributes_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_topic,
            call_fn_args=(),
            call_fn_kwargs=dict(topic_id=self.module.params.get("topic_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


NotificationTopicHelperCustom = get_custom_class("NotificationTopicHelperCustom")


class ResourceHelper(NotificationTopicHelperCustom, NotificationTopicHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            topic_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="notification_topic",
        service_client_class=NotificationControlPlaneClient,
        namespace="ons",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

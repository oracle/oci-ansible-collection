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
module: oci_queue
short_description: Manage a Queue resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Queue resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Queue.
    - "This resource has the following action operations in the M(oracle.oci.oci_queue_actions) module: change_compartment, purge."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
        type: str
    retention_in_seconds:
        description:
            - The retention period of the messages in the queue, in seconds.
        type: int
    display_name:
        description:
            - Queue Identifier
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    visibility_in_seconds:
        description:
            - The default visibility of the messages consumed from the queue.
            - This parameter is updatable.
        type: int
    timeout_in_seconds:
        description:
            - The default polling timeout of the messages in the queue, in seconds.
            - This parameter is updatable.
        type: int
    dead_letter_queue_delivery_count:
        description:
            - The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is
              not used.
            - This parameter is updatable.
        type: int
    custom_encryption_key_id:
        description:
            - Id of the custom master encryption key which will be used to encrypt messages content
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    queue_id:
        description:
            - unique Queue identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Queue.
            - Use I(state=present) to create or update a Queue.
            - Use I(state=absent) to delete a Queue.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create queue
  oci_queue:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    retention_in_seconds: 56
    visibility_in_seconds: 56
    timeout_in_seconds: 56
    dead_letter_queue_delivery_count: 56
    custom_encryption_key_id: "ocid1.customencryptionkey.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update queue
  oci_queue:
    # required
    queue_id: "ocid1.queue.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    visibility_in_seconds: 56
    timeout_in_seconds: 56
    dead_letter_queue_delivery_count: 56
    custom_encryption_key_id: "ocid1.customencryptionkey.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update queue using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_queue:
    # required
    display_name: display_name_example

    # optional
    visibility_in_seconds: 56
    timeout_in_seconds: 56
    dead_letter_queue_delivery_count: 56
    custom_encryption_key_id: "ocid1.customencryptionkey.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete queue
  oci_queue:
    # required
    queue_id: "ocid1.queue.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete queue using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_queue:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
queue:
    description:
        - Details of the Queue resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Queue Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the the Queue was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Queue was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Queue.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        messages_endpoint:
            description:
                - The endpoint to use to consume or publish messages in the queue.
            returned: on success
            type: str
            sample: messages_endpoint_example
        retention_in_seconds:
            description:
                - The retention period of the messages in the queue, in seconds.
            returned: on success
            type: int
            sample: 56
        visibility_in_seconds:
            description:
                - The default visibility of the messages consumed from the queue.
            returned: on success
            type: int
            sample: 56
        timeout_in_seconds:
            description:
                - The default polling timeout of the messages in the queue, in seconds.
            returned: on success
            type: int
            sample: 56
        dead_letter_queue_delivery_count:
            description:
                - The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ
                  is not used.
            returned: on success
            type: int
            sample: 56
        custom_encryption_key_id:
            description:
                - Id of the custom master encryption key which will be used to encrypt messages content
            returned: on success
            type: str
            sample: "ocid1.customencryptionkey.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "messages_endpoint": "messages_endpoint_example",
        "retention_in_seconds": 56,
        "visibility_in_seconds": 56,
        "timeout_in_seconds": 56,
        "dead_letter_queue_delivery_count": 56,
        "custom_encryption_key_id": "ocid1.customencryptionkey.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.queue import QueueAdminClient
    from oci.queue.models import CreateQueueDetails
    from oci.queue.models import UpdateQueueDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QueueHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(QueueHelperGen, self).get_possible_entity_types() + [
            "queue",
            "queues",
            "queuequeue",
            "queuequeues",
            "queueresource",
            "queuesresource",
        ]

    def get_module_resource_id_param(self):
        return "queue_id"

    def get_module_resource_id(self):
        return self.module.params.get("queue_id")

    def get_get_fn(self):
        return self.client.get_queue

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_queue, queue_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_queue, queue_id=self.module.params.get("queue_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_queues, **kwargs)

    def get_create_model_class(self):
        return CreateQueueDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_queue,
            call_fn_args=(),
            call_fn_kwargs=dict(create_queue_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateQueueDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_queue,
            call_fn_args=(),
            call_fn_kwargs=dict(
                queue_id=self.module.params.get("queue_id"),
                update_queue_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_queue,
            call_fn_args=(),
            call_fn_kwargs=dict(queue_id=self.module.params.get("queue_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


QueueHelperCustom = get_custom_class("QueueHelperCustom")


class ResourceHelper(QueueHelperCustom, QueueHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            retention_in_seconds=dict(type="int"),
            display_name=dict(aliases=["name"], type="str"),
            visibility_in_seconds=dict(type="int"),
            timeout_in_seconds=dict(type="int"),
            dead_letter_queue_delivery_count=dict(type="int"),
            custom_encryption_key_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            queue_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="queue",
        service_client_class=QueueAdminClient,
        namespace="queue",
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

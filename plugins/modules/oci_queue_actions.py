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
module: oci_queue_actions
short_description: Perform actions on a Queue resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Queue resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Queue resource from one compartment identifier to another. When provided, If-Match is checked against ETag
      values of the resource.
    - For I(action=purge), deletes all messages present in the queue at the time of invocation. Only one concurrent purge operation is supported for any given
      queue.
      However multiple concurrent purge operations are supported for different queues.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    queue_id:
        description:
            - unique Queue identifier
        type: str
        aliases: ["id"]
        required: true
    purge_type:
        description:
            - "Type of the purge to perform:
              - NORMAL - purge only normal queue
              - DLQ - purge only DLQ
              - BOTH - purge both normal queue and DLQ"
            - Required for I(action=purge).
        type: str
        choices:
            - "NORMAL"
            - "DLQ"
            - "BOTH"
    action:
        description:
            - The action to perform on the Queue.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "purge"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on queue
  oci_queue_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    queue_id: "ocid1.queue.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action purge on queue
  oci_queue_actions:
    # required
    queue_id: "ocid1.queue.oc1..xxxxxxEXAMPLExxxxxx"
    purge_type: NORMAL
    action: purge

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.queue import QueueAdminClient
    from oci.queue.models import ChangeQueueCompartmentDetails
    from oci.queue.models import PurgeQueueDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QueueActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        purge
    """

    @staticmethod
    def get_module_resource_id_param():
        return "queue_id"

    def get_module_resource_id(self):
        return self.module.params.get("queue_id")

    def get_get_fn(self):
        return self.client.get_queue

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_queue, queue_id=self.module.params.get("queue_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeQueueCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_queue_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                queue_id=self.module.params.get("queue_id"),
                change_queue_compartment_details=action_details,
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

    def purge(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, PurgeQueueDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.purge_queue,
            call_fn_args=(),
            call_fn_kwargs=dict(
                queue_id=self.module.params.get("queue_id"),
                purge_queue_details=action_details,
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


QueueActionsHelperCustom = get_custom_class("QueueActionsHelperCustom")


class ResourceHelper(QueueActionsHelperCustom, QueueActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            queue_id=dict(aliases=["id"], type="str", required=True),
            purge_type=dict(type="str", choices=["NORMAL", "DLQ", "BOTH"]),
            action=dict(
                type="str", required=True, choices=["change_compartment", "purge"]
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

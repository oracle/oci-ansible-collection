#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_streaming_stream_pool_actions
short_description: Perform actions on a StreamPool resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a StreamPool resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    stream_pool_id:
        description:
            - The OCID of the stream pool.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the StreamPool.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on stream_pool
  oci_streaming_stream_pool_actions:
    # required
    stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
stream_pool:
    description:
        - Details of the StreamPool resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the stream pool.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment OCID that the pool belongs to.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the stream pool.
            returned: on success
            type: str
            sample: name_example
        lifecycle_state:
            description:
                - The current state of the stream pool.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_state_details:
            description:
                - Any additional details about the current state of the stream.
            returned: on success
            type: str
            sample: lifecycle_state_details_example
        time_created:
            description:
                - The date and time the stream pool was created, expressed in in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2018-04-20T00:00:07.405Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        kafka_settings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                bootstrap_servers:
                    description:
                        - Bootstrap servers.
                    returned: on success
                    type: str
                    sample: bootstrap_servers_example
                auto_create_topics_enable:
                    description:
                        - Enable auto creation of topic on the server.
                    returned: on success
                    type: bool
                    sample: true
                log_retention_hours:
                    description:
                        - The number of hours to keep a log file before deleting it (in hours).
                    returned: on success
                    type: int
                    sample: 56
                num_partitions:
                    description:
                        - The default number of log partitions per topic.
                    returned: on success
                    type: int
                    sample: 56
        custom_encryption_key:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                kms_key_id:
                    description:
                        - Custom Encryption Key (Master Key) ocid.
                    returned: on success
                    type: str
                    sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                key_state:
                    description:
                        - Life cycle State of the custom key
                    returned: on success
                    type: str
                    sample: ACTIVE
        is_private:
            description:
                - True if the stream pool is private, false otherwise.
                  If the stream pool is private, the streams inside the stream pool can only be accessed from inside the associated subnetId.
            returned: on success
            type: bool
            sample: true
        endpoint_fqdn:
            description:
                - The FQDN used to access the streams inside the stream pool (same FQDN as the messagesEndpoint attribute of a
                  L(Stream,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/streaming/20180418/Stream) object).
                  If the stream pool is private, the FQDN is customized and can only be accessed from inside the associated subnetId, otherwise the FQDN is
                  publicly resolvable.
                  Depending on which protocol you attempt to use, you need to either prepend https or append the Kafka port.
            returned: on success
            type: str
            sample: endpoint_fqdn_example
        private_endpoint_settings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                subnet_id:
                    description:
                        - The subnet id from which the private stream pool can be accessed.
                          Trying to access the streams from another network location will result in an error.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                private_endpoint_ip:
                    description:
                        - "The private IP associated with the stream pool in the associated subnetId.
                          The stream pool's FQDN resolves to that IP and should be used - instead of the private IP - in order to not trigger any TLS issues."
                    returned: on success
                    type: str
                    sample: private_endpoint_ip_example
                nsg_ids:
                    description:
                        - The optional list of network security groups that are associated with the private endpoint of the stream pool.
                    returned: on success
                    type: list
                    sample: []
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-
                  compatibility only.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}'"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "lifecycle_state": "CREATING",
        "lifecycle_state_details": "lifecycle_state_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "kafka_settings": {
            "bootstrap_servers": "bootstrap_servers_example",
            "auto_create_topics_enable": true,
            "log_retention_hours": 56,
            "num_partitions": 56
        },
        "custom_encryption_key": {
            "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
            "key_state": "ACTIVE"
        },
        "is_private": true,
        "endpoint_fqdn": "endpoint_fqdn_example",
        "private_endpoint_settings": {
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "private_endpoint_ip": "private_endpoint_ip_example",
            "nsg_ids": []
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.streaming import StreamAdminClient
    from oci.streaming.models import ChangeStreamPoolCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StreamPoolActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "stream_pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("stream_pool_id")

    def get_get_fn(self):
        return self.client.get_stream_pool

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_pool,
            stream_pool_id=self.module.params.get("stream_pool_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeStreamPoolCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_stream_pool_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stream_pool_id=self.module.params.get("stream_pool_id"),
                change_stream_pool_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


StreamPoolActionsHelperCustom = get_custom_class("StreamPoolActionsHelperCustom")


class ResourceHelper(StreamPoolActionsHelperCustom, StreamPoolActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            stream_pool_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="stream_pool",
        service_client_class=StreamAdminClient,
        namespace="streaming",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

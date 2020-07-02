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
module: oci_streaming_stream_facts
short_description: Fetches details about one or multiple Stream resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Stream resources in Oracle Cloud Infrastructure
    - Lists the streams in the given compartment id.
      If the compartment id is specified, it will list streams in the compartment, regardless of their stream pool.
      If the stream pool id is specified, the action will be scoped to that stream pool.
      The compartment id and stream pool id cannot be specified at the same time.
    - If I(stream_id) is specified, the details of a single Stream will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    stream_id:
        description:
            - The OCID of the stream.
            - Required to get a specific stream.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment. Is exclusive with the `streamPoolId` parameter. One of them is required.
        type: str
    stream_pool_id:
        description:
            - The OCID of the stream pool. Is exclusive with the `compartmentId` parameter. One of them is required.
        type: str
    id:
        description:
            - A filter to return only resources that match the given ID exactly.
        type: str
    name:
        description:
            - A filter to return only resources that match the given name exactly.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide no more than one sort order. By default, `TIMECREATED` sorts results in descending order and `NAME` sorts
              results in ascending order.
        type: str
        choices:
            - "NAME"
            - "TIMECREATED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "UPDATING"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List streams
  oci_streaming_stream_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific stream
  oci_streaming_stream_facts:
    stream_id: ocid1.stream.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
streams:
    description:
        - List of Stream resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the stream. Avoid entering confidential information.
                - "Example: `TelemetryEvents`"
            returned: on success
            type: string
            sample: TelemetryEvents
        id:
            description:
                - The OCID of the stream.
            returned: on success
            type: string
            sample: ocid1.stream.realm.region.mnopqr789
        partitions:
            description:
                - The number of partitions in the stream.
            returned: on success
            type: int
            sample: 10
        retention_in_hours:
            description:
                - The retention period of the stream, in hours. This property is read-only.
            returned: on success
            type: int
            sample: 24
        compartment_id:
            description:
                - The OCID of the stream.
            returned: on success
            type: string
            sample: ocid1.compinstance.realm.region.zxcvbn432765
        stream_pool_id:
            description:
                - The OCID of the stream pool that contains the stream.
            returned: on success
            type: string
            sample: ocid1.streampool.realm.region.zxcvbn432765
        lifecycle_state:
            description:
                - The current state of the stream.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_state_details:
            description:
                - Any additional details about the current state of the stream.
            returned: on success
            type: string
            sample: lifecycle_state_details_example
        time_created:
            description:
                - The date and time the stream was created, expressed in in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2018-04-20T00:00:07.405Z`"
            returned: on success
            type: string
            sample: 2018-04-20T00:00:07.405Z
        messages_endpoint:
            description:
                - The endpoint to use when creating the StreamClient to consume or publish messages in the stream.
                  If the associated stream pool is private, the endpoint is also private and can only be accessed from inside the stream pool's associated
                  subnet.
            returned: on success
            type: string
            sample: messages_endpoint_example
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
    sample: [{
        "name": "TelemetryEvents",
        "id": "ocid1.stream.realm.region.mnopqr789",
        "partitions": 10,
        "retention_in_hours": 24,
        "compartment_id": "ocid1.compinstance.realm.region.zxcvbn432765",
        "stream_pool_id": "ocid1.streampool.realm.region.zxcvbn432765",
        "lifecycle_state": "CREATING",
        "lifecycle_state_details": "lifecycle_state_details_example",
        "time_created": "2018-04-20T00:00:07.405Z",
        "messages_endpoint": "messages_endpoint_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.streaming import StreamAdminClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StreamFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "stream_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream, stream_id=self.module.params.get("stream_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "stream_pool_id",
            "id",
            "name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_streams, **optional_kwargs
        )


StreamFactsHelperCustom = get_custom_class("StreamFactsHelperCustom")


class ResourceFactsHelper(StreamFactsHelperCustom, StreamFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            stream_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            stream_pool_id=dict(type="str"),
            id=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["NAME", "TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "UPDATING",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="stream",
        service_client_class=StreamAdminClient,
        namespace="streaming",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(streams=result)


if __name__ == "__main__":
    main()

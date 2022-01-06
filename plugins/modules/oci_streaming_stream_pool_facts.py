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
module: oci_streaming_stream_pool_facts
short_description: Fetches details about one or multiple StreamPool resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple StreamPool resources in Oracle Cloud Infrastructure
    - List the stream pools for a given compartment ID.
    - If I(stream_pool_id) is specified, the details of a single StreamPool will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    stream_pool_id:
        description:
            - The OCID of the stream pool.
            - Required to get a specific stream_pool.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple stream_pools.
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
- name: Get a specific stream_pool
  oci_streaming_stream_pool_facts:
    # required
    stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"

- name: List stream_pools
  oci_streaming_stream_pool_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_by: NAME
    sort_order: ASC
    lifecycle_state: CREATING

"""

RETURN = """
stream_pools:
    description:
        - List of StreamPool resources
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
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: str
            sample: endpoint_fqdn_example
        private_endpoint_settings:
            description:
                - ""
                - Returned for get operation
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
    sample: [{
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


class StreamPoolFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "stream_pool_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_pool,
            stream_pool_id=self.module.params.get("stream_pool_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_stream_pools,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


StreamPoolFactsHelperCustom = get_custom_class("StreamPoolFactsHelperCustom")


class ResourceFactsHelper(StreamPoolFactsHelperCustom, StreamPoolFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            stream_pool_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
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
        resource_type="stream_pool",
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

    module.exit_json(stream_pools=result)


if __name__ == "__main__":
    main()

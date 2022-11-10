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
module: oci_streaming_stream_pool
short_description: Manage a StreamPool resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a StreamPool resource in Oracle Cloud Infrastructure
    - For I(state=present), starts the provisioning of a new stream pool.
      To track the progress of the provisioning, you can periodically call GetStreamPool.
      In the response, the `lifecycleState` parameter of the object tells you its current state.
    - "This resource has the following action operations in the M(oracle.oci.oci_streaming_stream_pool_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that contains the stream.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    private_endpoint_details:
        description:
            - ""
        type: dict
        suboptions:
            subnet_id:
                description:
                    - If specified, the stream pool will be private and only accessible from inside that subnet.
                      Producing-to and consuming-from a stream inside a private stream pool can also only be done from inside the subnet.
                      That value cannot be changed.
                type: str
            private_endpoint_ip:
                description:
                    - The optional private IP you want to be associated with your private stream pool.
                      That parameter can only be specified when the subnetId parameter is set. It cannot be changed.
                      The private IP needs to be part of the CIDR range of the specified subnetId or the creation will fail.
                      If not specified a random IP inside the subnet will be chosen.
                      After the stream pool is created, a custom FQDN, pointing to this private IP, is created.
                      The FQDN is then used to access the service instead of the private IP.
                type: str
            nsg_ids:
                description:
                    - The optional list of network security groups to be used with the private endpoint of the stream pool.
                      That value cannot be changed.
                type: list
                elements: str
    name:
        description:
            - The name of the stream pool. Avoid entering confidential information.
            - "Example: `MyStreamPool`"
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    kafka_settings:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            bootstrap_servers:
                description:
                    - Bootstrap servers.
                type: str
            auto_create_topics_enable:
                description:
                    - Enable auto creation of topic on the server.
                type: bool
            log_retention_hours:
                description:
                    - The number of hours to keep a log file before deleting it (in hours).
                type: int
            num_partitions:
                description:
                    - The default number of log partitions per topic.
                type: int
    custom_encryption_key_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            kms_key_id:
                description:
                    - Custom Encryption Key (Master Key) ocid.
                type: str
                required: true
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for
              cross-compatibility only.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    stream_pool_id:
        description:
            - The OCID of the stream pool.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the StreamPool.
            - Use I(state=present) to create or update a StreamPool.
            - Use I(state=absent) to delete a StreamPool.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create stream_pool
  oci_streaming_stream_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    private_endpoint_details:
      # optional
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
      private_endpoint_ip: private_endpoint_ip_example
      nsg_ids: [ "nsg_ids_example" ]
    kafka_settings:
      # optional
      bootstrap_servers: bootstrap_servers_example
      auto_create_topics_enable: true
      log_retention_hours: 56
      num_partitions: 56
    custom_encryption_key_details:
      # required
      kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update stream_pool
  oci_streaming_stream_pool:
    # required
    stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    kafka_settings:
      # optional
      bootstrap_servers: bootstrap_servers_example
      auto_create_topics_enable: true
      log_retention_hours: 56
      num_partitions: 56
    custom_encryption_key_details:
      # required
      kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update stream_pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_streaming_stream_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    kafka_settings:
      # optional
      bootstrap_servers: bootstrap_servers_example
      auto_create_topics_enable: true
      log_retention_hours: 56
      num_partitions: 56
    custom_encryption_key_details:
      # required
      kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete stream_pool
  oci_streaming_stream_pool:
    # required
    stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete stream_pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_streaming_stream_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

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
    from oci.streaming import StreamAdminClient
    from oci.streaming.models import CreateStreamPoolDetails
    from oci.streaming.models import UpdateStreamPoolDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StreamPoolHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(StreamPoolHelperGen, self).get_possible_entity_types() + [
            "streampool",
            "streampools",
            "streamingstreampool",
            "streamingstreampools",
            "streampoolresource",
            "streampoolsresource",
            "streaming",
        ]

    def get_module_resource_id_param(self):
        return "stream_pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("stream_pool_id")

    def get_get_fn(self):
        return self.client.get_stream_pool

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_pool, stream_pool_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_pool,
            stream_pool_id=self.module.params.get("stream_pool_id"),
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
        return oci_common_utils.list_all_resources(
            self.client.list_stream_pools, **kwargs
        )

    def get_create_model_class(self):
        return CreateStreamPoolDetails

    def get_exclude_attributes(self):
        return ["private_endpoint_details", "custom_encryption_key_details"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_stream_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(create_stream_pool_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateStreamPoolDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_stream_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stream_pool_id=self.module.params.get("stream_pool_id"),
                update_stream_pool_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_stream_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stream_pool_id=self.module.params.get("stream_pool_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


StreamPoolHelperCustom = get_custom_class("StreamPoolHelperCustom")


class ResourceHelper(StreamPoolHelperCustom, StreamPoolHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            private_endpoint_details=dict(
                type="dict",
                options=dict(
                    subnet_id=dict(type="str"),
                    private_endpoint_ip=dict(type="str"),
                    nsg_ids=dict(type="list", elements="str"),
                ),
            ),
            name=dict(type="str"),
            kafka_settings=dict(
                type="dict",
                options=dict(
                    bootstrap_servers=dict(type="str"),
                    auto_create_topics_enable=dict(type="bool"),
                    log_retention_hours=dict(type="int"),
                    num_partitions=dict(type="int"),
                ),
            ),
            custom_encryption_key_details=dict(
                type="dict",
                no_log=False,
                options=dict(kms_key_id=dict(type="str", required=True)),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            stream_pool_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="stream_pool",
        service_client_class=StreamAdminClient,
        namespace="streaming",
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

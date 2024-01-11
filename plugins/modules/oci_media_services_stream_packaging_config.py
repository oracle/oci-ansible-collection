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
module: oci_media_services_stream_packaging_config
short_description: Manage a StreamPackagingConfig resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a StreamPackagingConfig resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Packaging Configuration.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    distribution_channel_id:
        description:
            - Unique identifier of the Distribution Channel that this stream packaging configuration belongs to.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    stream_packaging_format:
        description:
            - The output format for the package.
            - Required for create using I(state=present).
        type: str
        choices:
            - "HLS"
            - "DASH"
    segment_time_in_seconds:
        description:
            - The duration in seconds for each fragment.
            - Required for create using I(state=present).
        type: int
    encryption:
        description:
            - ""
        type: dict
        suboptions:
            kms_key_id:
                description:
                    - The identifier of the customer managed Vault KMS symmetric encryption key (null if Oracle managed).
                    - Applicable when algorithm is 'AES128'
                type: str
            algorithm:
                description:
                    - The encryption algorithm for the stream packaging configuration.
                type: str
                choices:
                    - "AES128"
                    - "NONE"
                required: true
    display_name:
        description:
            - The name of the stream Packaging Configuration. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
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
    stream_packaging_config_id:
        description:
            - Unique Stream Packaging Configuration path identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the StreamPackagingConfig.
            - Use I(state=present) to create or update a StreamPackagingConfig.
            - Use I(state=absent) to delete a StreamPackagingConfig.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create stream_packaging_config
  oci_media_services_stream_packaging_config:
    # required
    distribution_channel_id: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
    stream_packaging_format: HLS
    segment_time_in_seconds: 56
    display_name: display_name_example

    # optional
    encryption:
      # required
      algorithm: AES128

      # optional
      kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update stream_packaging_config
  oci_media_services_stream_packaging_config:
    # required
    stream_packaging_config_id: "ocid1.streampackagingconfig.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update stream_packaging_config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_stream_packaging_config:
    # required
    distribution_channel_id: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete stream_packaging_config
  oci_media_services_stream_packaging_config:
    # required
    stream_packaging_config_id: "ocid1.streampackagingconfig.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete stream_packaging_config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_stream_packaging_config:
    # required
    distribution_channel_id: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
stream_packaging_config:
    description:
        - Details of the StreamPackagingConfig resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        distribution_channel_id:
            description:
                - Unique identifier of the Distribution Channel that this stream packaging configuration belongs to.
            returned: on success
            type: str
            sample: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the stream packaging configuration. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        stream_packaging_format:
            description:
                - The output format for the package.
            returned: on success
            type: str
            sample: HLS
        segment_time_in_seconds:
            description:
                - The duration in seconds for each fragment.
            returned: on success
            type: int
            sample: 56
        encryption:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                kms_key_id:
                    description:
                        - The identifier of the customer managed Vault KMS symmetric encryption key (null if Oracle managed).
                    returned: on success
                    type: str
                    sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                algorithm:
                    description:
                        - The encryption algorithm for the stream packaging configuration.
                    returned: on success
                    type: str
                    sample: NONE
        time_created:
            description:
                - The time when the Packaging Configuration was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the Packaging Configuration was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Packaging Configuration.
            returned: on success
            type: str
            sample: ACTIVE
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "distribution_channel_id": "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "stream_packaging_format": "HLS",
        "segment_time_in_seconds": 56,
        "encryption": {
            "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
            "algorithm": "NONE"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
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
    from oci.media_services import MediaServicesClient
    from oci.media_services.models import CreateStreamPackagingConfigDetails
    from oci.media_services.models import UpdateStreamPackagingConfigDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StreamPackagingConfigHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            StreamPackagingConfigHelperGen, self
        ).get_possible_entity_types() + [
            "streampackagingconfig",
            "streampackagingconfigs",
            "mediaServicesstreampackagingconfig",
            "mediaServicesstreampackagingconfigs",
            "streampackagingconfigresource",
            "streampackagingconfigsresource",
            "mediaservices",
        ]

    def get_module_resource_id_param(self):
        return "stream_packaging_config_id"

    def get_module_resource_id(self):
        return self.module.params.get("stream_packaging_config_id")

    def get_get_fn(self):
        return self.client.get_stream_packaging_config

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_packaging_config,
            stream_packaging_config_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_packaging_config,
            stream_packaging_config_id=self.module.params.get(
                "stream_packaging_config_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "distribution_channel_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["stream_packaging_config_id", "display_name"]

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
            self.client.list_stream_packaging_configs, **kwargs
        )

    def get_create_model_class(self):
        return CreateStreamPackagingConfigDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_stream_packaging_config,
            call_fn_args=(),
            call_fn_kwargs=dict(create_stream_packaging_config_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateStreamPackagingConfigDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_stream_packaging_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stream_packaging_config_id=self.module.params.get(
                    "stream_packaging_config_id"
                ),
                update_stream_packaging_config_details=update_details,
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
            call_fn=self.client.delete_stream_packaging_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stream_packaging_config_id=self.module.params.get(
                    "stream_packaging_config_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


StreamPackagingConfigHelperCustom = get_custom_class(
    "StreamPackagingConfigHelperCustom"
)


class ResourceHelper(StreamPackagingConfigHelperCustom, StreamPackagingConfigHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            distribution_channel_id=dict(type="str"),
            stream_packaging_format=dict(type="str", choices=["HLS", "DASH"]),
            segment_time_in_seconds=dict(type="int"),
            encryption=dict(
                type="dict",
                options=dict(
                    kms_key_id=dict(type="str"),
                    algorithm=dict(
                        type="str", required=True, choices=["AES128", "NONE"]
                    ),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            stream_packaging_config_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="stream_packaging_config",
        service_client_class=MediaServicesClient,
        namespace="media_services",
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

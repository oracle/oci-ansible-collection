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
module: oci_media_services_stream_cdn_config
short_description: Manage a StreamCdnConfig resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a StreamCdnConfig resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new CDN Configuration.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    distribution_channel_id:
        description:
            - Distribution Channel Identifier.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - CDN Config display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    is_enabled:
        description:
            - Whether publishing to CDN is enabled.
            - This parameter is updatable.
        type: bool
    config:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            origin_auth_sign_type:
                description:
                    - The type of data used to compute the signature.
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: str
                choices:
                    - "ForwardURL"
            origin_auth_sign_encryption:
                description:
                    - The type of encryption used to compute the signature.
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: str
                choices:
                    - "SHA256-HMAC"
            origin_auth_secret_key_a:
                description:
                    - The shared secret key A, two for errorless key rotation.
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: str
            origin_auth_secret_key_nonce_a:
                description:
                    - Nonce identifier for originAuthSecretKeyA (used to determine key used to sign).
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: str
            origin_auth_secret_key_b:
                description:
                    - The shared secret key B, two for errorless key rotation.
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: str
            origin_auth_secret_key_nonce_b:
                description:
                    - Nonce identifier for originAuthSecretKeyB (used to determine key used to sign).
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: str
            edge_hostname:
                description:
                    - The hostname of the CDN edge server to use when building CDN URLs.
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: str
            edge_path_prefix:
                description:
                    - The path to prepend when building CDN URLs.
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: str
            is_edge_token_auth:
                description:
                    - Whether token authentication should be used at the CDN edge.
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: bool
            edge_token_key:
                description:
                    - The encryption key to use for edge token authentication.
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: str
            edge_token_salt:
                description:
                    - Salt to use when encrypting authentication token.
                    - Applicable when type is 'AKAMAI_MANUAL'
                type: str
            type:
                description:
                    - The name of the CDN configuration type.
                type: str
                choices:
                    - "AKAMAI_MANUAL"
                    - "EDGE"
                required: true
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
    stream_cdn_config_id:
        description:
            - Unique StreamCdnConfig identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the StreamCdnConfig.
            - Use I(state=present) to create or update a StreamCdnConfig.
            - Use I(state=absent) to delete a StreamCdnConfig.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create stream_cdn_config
  oci_media_services_stream_cdn_config:
    # required
    distribution_channel_id: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    config:
      # required
      type: AKAMAI_MANUAL

      # optional
      origin_auth_sign_type: ForwardURL
      origin_auth_sign_encryption: SHA256-HMAC
      origin_auth_secret_key_a: origin_auth_secret_key_a_example
      origin_auth_secret_key_nonce_a: origin_auth_secret_key_nonce_a_example
      origin_auth_secret_key_b: origin_auth_secret_key_b_example
      origin_auth_secret_key_nonce_b: origin_auth_secret_key_nonce_b_example
      edge_hostname: edge_hostname_example
      edge_path_prefix: edge_path_prefix_example
      is_edge_token_auth: true
      edge_token_key: edge_token_key_example
      edge_token_salt: edge_token_salt_example

    # optional
    is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update stream_cdn_config
  oci_media_services_stream_cdn_config:
    # required
    stream_cdn_config_id: "ocid1.streamcdnconfig.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    is_enabled: true
    config:
      # required
      type: AKAMAI_MANUAL

      # optional
      origin_auth_sign_type: ForwardURL
      origin_auth_sign_encryption: SHA256-HMAC
      origin_auth_secret_key_a: origin_auth_secret_key_a_example
      origin_auth_secret_key_nonce_a: origin_auth_secret_key_nonce_a_example
      origin_auth_secret_key_b: origin_auth_secret_key_b_example
      origin_auth_secret_key_nonce_b: origin_auth_secret_key_nonce_b_example
      edge_hostname: edge_hostname_example
      edge_path_prefix: edge_path_prefix_example
      is_edge_token_auth: true
      edge_token_key: edge_token_key_example
      edge_token_salt: edge_token_salt_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update stream_cdn_config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_stream_cdn_config:
    # required
    distribution_channel_id: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    is_enabled: true
    config:
      # required
      type: AKAMAI_MANUAL

      # optional
      origin_auth_sign_type: ForwardURL
      origin_auth_sign_encryption: SHA256-HMAC
      origin_auth_secret_key_a: origin_auth_secret_key_a_example
      origin_auth_secret_key_nonce_a: origin_auth_secret_key_nonce_a_example
      origin_auth_secret_key_b: origin_auth_secret_key_b_example
      origin_auth_secret_key_nonce_b: origin_auth_secret_key_nonce_b_example
      edge_hostname: edge_hostname_example
      edge_path_prefix: edge_path_prefix_example
      is_edge_token_auth: true
      edge_token_key: edge_token_key_example
      edge_token_salt: edge_token_salt_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete stream_cdn_config
  oci_media_services_stream_cdn_config:
    # required
    stream_cdn_config_id: "ocid1.streamcdnconfig.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete stream_cdn_config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_stream_cdn_config:
    # required
    distribution_channel_id: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
stream_cdn_config:
    description:
        - Details of the StreamCdnConfig resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The CDN Configuration identifier or display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        distribution_channel_id:
            description:
                - Distribution Channel Identifier.
            returned: on success
            type: str
            sample: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
        is_enabled:
            description:
                - Whether publishing to CDN is enabled.
            returned: on success
            type: bool
            sample: true
        config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                origin_auth_sign_type:
                    description:
                        - The type of data used to compute the signature.
                    returned: on success
                    type: str
                    sample: ForwardURL
                origin_auth_sign_encryption:
                    description:
                        - The type of encryption used to compute the signature.
                    returned: on success
                    type: str
                    sample: SHA256-HMAC
                origin_auth_secret_key_a:
                    description:
                        - The shared secret key A, two for errorless key rotation.
                    returned: on success
                    type: str
                    sample: origin_auth_secret_key_a_example
                origin_auth_secret_key_nonce_a:
                    description:
                        - Nonce identifier for originAuthSecretKeyA (used to determine key used to sign).
                    returned: on success
                    type: str
                    sample: origin_auth_secret_key_nonce_a_example
                origin_auth_secret_key_b:
                    description:
                        - The shared secret key B, two for errorless key rotation.
                    returned: on success
                    type: str
                    sample: origin_auth_secret_key_b_example
                origin_auth_secret_key_nonce_b:
                    description:
                        - Nonce identifier for originAuthSecretKeyB (used to determine key used to sign).
                    returned: on success
                    type: str
                    sample: origin_auth_secret_key_nonce_b_example
                edge_hostname:
                    description:
                        - The hostname of the CDN edge server to use when building CDN URLs.
                    returned: on success
                    type: str
                    sample: edge_hostname_example
                edge_path_prefix:
                    description:
                        - The path to prepend when building CDN URLs.
                    returned: on success
                    type: str
                    sample: edge_path_prefix_example
                is_edge_token_auth:
                    description:
                        - Whether token authentication should be used at the CDN edge.
                    returned: on success
                    type: bool
                    sample: true
                edge_token_key:
                    description:
                        - The encryption key to use for edge token authentication.
                    returned: on success
                    type: str
                    sample: edge_token_key_example
                edge_token_salt:
                    description:
                        - Salt to use when encrypting authentication token.
                    returned: on success
                    type: str
                    sample: edge_token_salt_example
                type:
                    description:
                        - The name of the CDN configuration type.
                    returned: on success
                    type: str
                    sample: EDGE
        time_created:
            description:
                - The time when the CDN Config was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the CDN Config was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the CDN Configuration.
            returned: on success
            type: str
            sample: ACTIVE
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecyle_details_example
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
        "distribution_channel_id": "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx",
        "is_enabled": true,
        "config": {
            "origin_auth_sign_type": "ForwardURL",
            "origin_auth_sign_encryption": "SHA256-HMAC",
            "origin_auth_secret_key_a": "origin_auth_secret_key_a_example",
            "origin_auth_secret_key_nonce_a": "origin_auth_secret_key_nonce_a_example",
            "origin_auth_secret_key_b": "origin_auth_secret_key_b_example",
            "origin_auth_secret_key_nonce_b": "origin_auth_secret_key_nonce_b_example",
            "edge_hostname": "edge_hostname_example",
            "edge_path_prefix": "edge_path_prefix_example",
            "is_edge_token_auth": true,
            "edge_token_key": "edge_token_key_example",
            "edge_token_salt": "edge_token_salt_example",
            "type": "EDGE"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecyle_details": "lifecyle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.media_services import MediaServicesClient
    from oci.media_services.models import CreateStreamCdnConfigDetails
    from oci.media_services.models import UpdateStreamCdnConfigDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StreamCdnConfigHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(StreamCdnConfigHelperGen, self).get_possible_entity_types() + [
            "streamcdnconfig",
            "streamcdnconfigs",
            "mediaServicesstreamcdnconfig",
            "mediaServicesstreamcdnconfigs",
            "streamcdnconfigresource",
            "streamcdnconfigsresource",
            "mediaservices",
        ]

    def get_module_resource_id_param(self):
        return "stream_cdn_config_id"

    def get_module_resource_id(self):
        return self.module.params.get("stream_cdn_config_id")

    def get_get_fn(self):
        return self.client.get_stream_cdn_config

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_cdn_config, stream_cdn_config_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_cdn_config,
            stream_cdn_config_id=self.module.params.get("stream_cdn_config_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "distribution_channel_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_stream_cdn_configs, **kwargs
        )

    def get_create_model_class(self):
        return CreateStreamCdnConfigDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_stream_cdn_config,
            call_fn_args=(),
            call_fn_kwargs=dict(create_stream_cdn_config_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateStreamCdnConfigDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_stream_cdn_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stream_cdn_config_id=self.module.params.get("stream_cdn_config_id"),
                update_stream_cdn_config_details=update_details,
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
            call_fn=self.client.delete_stream_cdn_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stream_cdn_config_id=self.module.params.get("stream_cdn_config_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


StreamCdnConfigHelperCustom = get_custom_class("StreamCdnConfigHelperCustom")


class ResourceHelper(StreamCdnConfigHelperCustom, StreamCdnConfigHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            distribution_channel_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_enabled=dict(type="bool"),
            config=dict(
                type="dict",
                options=dict(
                    origin_auth_sign_type=dict(type="str", choices=["ForwardURL"]),
                    origin_auth_sign_encryption=dict(
                        type="str", choices=["SHA256-HMAC"]
                    ),
                    origin_auth_secret_key_a=dict(type="str", no_log=True),
                    origin_auth_secret_key_nonce_a=dict(type="str", no_log=True),
                    origin_auth_secret_key_b=dict(type="str", no_log=True),
                    origin_auth_secret_key_nonce_b=dict(type="str", no_log=True),
                    edge_hostname=dict(type="str"),
                    edge_path_prefix=dict(type="str"),
                    is_edge_token_auth=dict(type="bool", no_log=True),
                    edge_token_key=dict(type="str", no_log=True),
                    edge_token_salt=dict(type="str", no_log=True),
                    type=dict(
                        type="str", required=True, choices=["AKAMAI_MANUAL", "EDGE"]
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            stream_cdn_config_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="stream_cdn_config",
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

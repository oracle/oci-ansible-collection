#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_media_services_stream_cdn_config_facts
short_description: Fetches details about one or multiple StreamCdnConfig resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple StreamCdnConfig resources in Oracle Cloud Infrastructure
    - Lists the StreamCdnConfig.
    - If I(stream_cdn_config_id) is specified, the details of a single StreamCdnConfig will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    stream_cdn_config_id:
        description:
            - Unique StreamCdnConfig identifier.
            - Required to get a specific stream_cdn_config.
        type: str
        aliases: ["id"]
    distribution_channel_id:
        description:
            - The Stream Distribution Channel identifier this CdnConfig belongs to.
            - Required to list multiple stream_cdn_configs.
        type: str
    lifecycle_state:
        description:
            - A filter to return only the resources with lifecycleState matching the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "NEEDS_ATTENTION"
            - "DELETED"
    display_name:
        description:
            - A filter to return only the resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default
              order for displayName is ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific stream_cdn_config
  oci_media_services_stream_cdn_config_facts:
    # required
    stream_cdn_config_id: "ocid1.streamcdnconfig.oc1..xxxxxxEXAMPLExxxxxx"

- name: List stream_cdn_configs
  oci_media_services_stream_cdn_config_facts:
    # required
    distribution_channel_id: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACTIVE
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
stream_cdn_configs:
    description:
        - List of StreamCdnConfig resources
    returned: on success
    type: complex
    contains:
        config:
            description:
                - ""
                - Returned for get operation
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
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecyle_details_example
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
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for list operation
            returned: on success
            type: str
            sample: lifecycle_details_example
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
    sample: [{
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
        "lifecyle_details": "lifecyle_details_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "distribution_channel_id": "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx",
        "is_enabled": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.media_services import MediaServicesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StreamCdnConfigFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "stream_cdn_config_id",
        ]

    def get_required_params_for_list(self):
        return [
            "distribution_channel_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_cdn_config,
            stream_cdn_config_id=self.module.params.get("stream_cdn_config_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_stream_cdn_configs,
            distribution_channel_id=self.module.params.get("distribution_channel_id"),
            **optional_kwargs
        )


StreamCdnConfigFactsHelperCustom = get_custom_class("StreamCdnConfigFactsHelperCustom")


class ResourceFactsHelper(
    StreamCdnConfigFactsHelperCustom, StreamCdnConfigFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            stream_cdn_config_id=dict(aliases=["id"], type="str"),
            distribution_channel_id=dict(type="str"),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "NEEDS_ATTENTION", "DELETED"]
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="stream_cdn_config",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(stream_cdn_configs=result)


if __name__ == "__main__":
    main()

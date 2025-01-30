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
module: oci_media_services_stream_distribution_channel_actions
short_description: Perform actions on a StreamDistributionChannel resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a StreamDistributionChannel resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Stream Distribution Channel resource from one compartment identifier to another.
    - For I(action=ingest), ingests an Asset into a Distribution Channel.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    stream_distribution_channel_id:
        description:
            - Unique Stream Distribution Channel path identifier.
        type: str
        aliases: ["id"]
        required: true
    ingest_payload_type:
        description:
            - Ingest Payload Type
            - Required for I(action=ingest).
        type: str
        choices:
            - "ASSET_METADATA_MEDIA_ASSET"
    media_asset_id:
        description:
            - The Media Asset ID to ingest into the Distribution Channel.
            - Required for I(action=ingest).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
            - Required for I(action=change_compartment).
            - Applicable when $p.relatedDiscriminatorFieldName is 'ASSET_METADATA_MEDIA_ASSET'
        type: str
    action:
        description:
            - The action to perform on the StreamDistributionChannel.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "ingest"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on stream_distribution_channel
  oci_media_services_stream_distribution_channel_actions:
    # required
    stream_distribution_channel_id: "ocid1.streamdistributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action ingest on stream_distribution_channel with ingest_payload_type = ASSET_METADATA_MEDIA_ASSET
  oci_media_services_stream_distribution_channel_actions:
    # required
    ingest_payload_type: ASSET_METADATA_MEDIA_ASSET
    media_asset_id: "ocid1.mediaasset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
stream_distribution_channel:
    description:
        - Details of the StreamDistributionChannel resource acted upon by the current operation
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
                - Stream Distribution Channel display name. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        domain_name:
            description:
                - Unique domain name of the Distribution Channel.
            returned: on success
            type: str
            sample: domain_name_example
        time_created:
            description:
                - The time when the Stream Distribution Channel was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the Stream Distribution Channel was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Stream Distribution Channel.
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
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "domain_name": "domain_name_example",
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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.media_services import MediaServicesClient
    from oci.media_services.models import (
        ChangeStreamDistributionChannelCompartmentDetails,
    )
    from oci.media_services.models import IngestStreamDistributionChannelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StreamDistributionChannelActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        ingest
    """

    @staticmethod
    def get_module_resource_id_param():
        return "stream_distribution_channel_id"

    def get_module_resource_id(self):
        return self.module.params.get("stream_distribution_channel_id")

    def get_get_fn(self):
        return self.client.get_stream_distribution_channel

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_distribution_channel,
            stream_distribution_channel_id=self.module.params.get(
                "stream_distribution_channel_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeStreamDistributionChannelCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_stream_distribution_channel_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stream_distribution_channel_id=self.module.params.get(
                    "stream_distribution_channel_id"
                ),
                change_stream_distribution_channel_compartment_details=action_details,
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

    def ingest(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestStreamDistributionChannelDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_stream_distribution_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                stream_distribution_channel_id=self.module.params.get(
                    "stream_distribution_channel_id"
                ),
                ingest_stream_distribution_channel_details=action_details,
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


StreamDistributionChannelActionsHelperCustom = get_custom_class(
    "StreamDistributionChannelActionsHelperCustom"
)


class ResourceHelper(
    StreamDistributionChannelActionsHelperCustom,
    StreamDistributionChannelActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            stream_distribution_channel_id=dict(
                aliases=["id"], type="str", required=True
            ),
            ingest_payload_type=dict(
                type="str", choices=["ASSET_METADATA_MEDIA_ASSET"]
            ),
            media_asset_id=dict(type="str"),
            compartment_id=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["change_compartment", "ingest"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="stream_distribution_channel",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

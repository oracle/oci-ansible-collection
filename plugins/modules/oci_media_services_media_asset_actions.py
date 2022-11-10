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
module: oci_media_services_media_asset_actions
short_description: Perform actions on a MediaAsset resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a MediaAsset resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a MediaAsset resource from one compartment identifier to another.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    media_asset_id:
        description:
            - Unique MediaAsset identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - Compartment Identifier.
        type: str
        required: true
    action:
        description:
            - The action to perform on the MediaAsset.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on media_asset
  oci_media_services_media_asset_actions:
    # required
    media_asset_id: "ocid1.mediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
media_asset:
    description:
        - Details of the MediaAsset resource acted upon by the current operation
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
                - The ID of the compartment containing the MediaAsset.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        source_media_workflow_id:
            description:
                - The ID of the MediaWorkflow used to produce this asset.
            returned: on success
            type: str
            sample: "ocid1.sourcemediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"
        media_workflow_job_id:
            description:
                - The ID of the MediaWorkflowJob used to produce this asset.
            returned: on success
            type: str
            sample: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
        source_media_workflow_version:
            description:
                - The version of the MediaWorkflow used to produce this asset.
            returned: on success
            type: int
            sample: 56
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The time when the MediaAsset was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the MediaAsset.
            returned: on success
            type: str
            sample: CREATING
        type:
            description:
                - The type of the media asset.
            returned: on success
            type: str
            sample: AUDIO
        parent_media_asset_id:
            description:
                - The ID of the parent asset from which this asset is derived.
            returned: on success
            type: str
            sample: "ocid1.parentmediaasset.oc1..xxxxxxEXAMPLExxxxxx"
        master_media_asset_id:
            description:
                - The ID of the senior most asset from which this asset is derived.
            returned: on success
            type: str
            sample: "ocid1.mastermediaasset.oc1..xxxxxxEXAMPLExxxxxx"
        bucket_name:
            description:
                - The name of the object storage bucket where this represented asset is located.
            returned: on success
            type: str
            sample: bucket_name_example
        namespace_name:
            description:
                - The object storage namespace where this asset is located.
            returned: on success
            type: str
            sample: namespace_name_example
        object_name:
            description:
                - The object storage object name that identifies this asset.
            returned: on success
            type: str
            sample: object_name_example
        object_etag:
            description:
                - eTag of the underlying object storage object.
            returned: on success
            type: str
            sample: object_etag_example
        time_updated:
            description:
                - The time when the MediaAsset was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        segment_range_start_index:
            description:
                - The start index for video segment files.
            returned: on success
            type: int
            sample: 56
        segment_range_end_index:
            description:
                - The end index of video segment files.
            returned: on success
            type: int
            sample: 56
        metadata:
            description:
                - List of Metadata.
            returned: on success
            type: complex
            contains:
                metadata:
                    description:
                        - JSON string containing the technial metadata for the media asset.
                    returned: on success
                    type: str
                    sample: metadata_example
        media_asset_tags:
            description:
                - List of tags for the MediaAsset.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of the tag.
                    returned: on success
                    type: str
                    sample: USER
                value:
                    description:
                        - Tag of the MediaAsset.
                    returned: on success
                    type: str
                    sample: value_example
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
        "source_media_workflow_id": "ocid1.sourcemediaworkflow.oc1..xxxxxxEXAMPLExxxxxx",
        "media_workflow_job_id": "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx",
        "source_media_workflow_version": 56,
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "type": "AUDIO",
        "parent_media_asset_id": "ocid1.parentmediaasset.oc1..xxxxxxEXAMPLExxxxxx",
        "master_media_asset_id": "ocid1.mastermediaasset.oc1..xxxxxxEXAMPLExxxxxx",
        "bucket_name": "bucket_name_example",
        "namespace_name": "namespace_name_example",
        "object_name": "object_name_example",
        "object_etag": "object_etag_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "segment_range_start_index": 56,
        "segment_range_end_index": 56,
        "metadata": [{
            "metadata": "metadata_example"
        }],
        "media_asset_tags": [{
            "type": "USER",
            "value": "value_example"
        }],
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
    from oci.media_services.models import ChangeMediaAssetCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaAssetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "media_asset_id"

    def get_module_resource_id(self):
        return self.module.params.get("media_asset_id")

    def get_get_fn(self):
        return self.client.get_media_asset

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_asset,
            media_asset_id=self.module.params.get("media_asset_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeMediaAssetCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_media_asset_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_asset_id=self.module.params.get("media_asset_id"),
                change_media_asset_compartment_details=action_details,
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


MediaAssetActionsHelperCustom = get_custom_class("MediaAssetActionsHelperCustom")


class ResourceHelper(MediaAssetActionsHelperCustom, MediaAssetActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            media_asset_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="media_asset",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

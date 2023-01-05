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
module: oci_media_services_media_asset_facts
short_description: Fetches details about one or multiple MediaAsset resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MediaAsset resources in Oracle Cloud Infrastructure
    - Returns a list of MediaAssetSummary.
    - If I(media_asset_id) is specified, the details of a single MediaAsset will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    media_asset_id:
        description:
            - Unique MediaAsset identifier
            - Required to get a specific media_asset.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    display_name:
        description:
            - A filter to return only the resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only the resources with lifecycleState matching the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "compartmentId"
            - "type"
            - "lifecycleState"
            - "parentMediaAssetId"
            - "masterMediaAssetId"
            - "displayName"
            - "timeCreated"
            - "timeUpdated"
    distribution_channel_id:
        description:
            - Unique DistributionChannel identifier.
        type: str
    parent_media_asset_id:
        description:
            - Unique MediaAsset identifier of the asset from which this asset is derived.
        type: str
    master_media_asset_id:
        description:
            - Unique MediaAsset identifier of the first asset upload.
        type: str
    type:
        description:
            - Filter MediaAsset by the asset type.
        type: str
        choices:
            - "AUDIO"
            - "VIDEO"
            - "PLAYLIST"
            - "IMAGE"
            - "CAPTION_FILE"
            - "UNKNOWN"
    bucket_name:
        description:
            - Filter MediaAsset by the bucket where the object is stored.
        type: str
    object_name:
        description:
            - Filter MediaAsset by the name of the object in object storage.
        type: str
    media_workflow_job_id:
        description:
            - The ID of the MediaWorkflowJob used to produce this asset, if this parameter is supplied then the workflow ID must also be supplied.
        type: str
    source_media_workflow_id:
        description:
            - The ID of the MediaWorkflow used to produce this asset.
        type: str
    source_media_workflow_version:
        description:
            - The version of the MediaWorkflow used to produce this asset.
        type: int
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific media_asset
  oci_media_services_media_asset_facts:
    # required
    media_asset_id: "ocid1.mediaasset.oc1..xxxxxxEXAMPLExxxxxx"

- name: List media_assets
  oci_media_services_media_asset_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: compartmentId
    distribution_channel_id: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
    parent_media_asset_id: "ocid1.parentmediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    master_media_asset_id: "ocid1.mastermediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    type: AUDIO
    bucket_name: bucket_name_example
    object_name: object_name_example
    media_workflow_job_id: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
    source_media_workflow_id: "ocid1.sourcemediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"
    source_media_workflow_version: 56

"""

RETURN = """
media_assets:
    description:
        - List of MediaAsset resources
    returned: on success
    type: complex
    contains:
        source_media_workflow_id:
            description:
                - The ID of the MediaWorkflow used to produce this asset.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.sourcemediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"
        media_workflow_job_id:
            description:
                - The ID of the MediaWorkflowJob used to produce this asset.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
        source_media_workflow_version:
            description:
                - The version of the MediaWorkflow used to produce this asset.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        bucket_name:
            description:
                - The name of the object storage bucket where this represented asset is located.
                - Returned for get operation
            returned: on success
            type: str
            sample: bucket_name_example
        namespace_name:
            description:
                - The object storage namespace where this asset is located.
                - Returned for get operation
            returned: on success
            type: str
            sample: namespace_name_example
        object_name:
            description:
                - The object storage object name that identifies this asset.
                - Returned for get operation
            returned: on success
            type: str
            sample: object_name_example
        object_etag:
            description:
                - eTag of the underlying object storage object.
                - Returned for get operation
            returned: on success
            type: str
            sample: object_etag_example
        segment_range_start_index:
            description:
                - The start index for video segment files.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        segment_range_end_index:
            description:
                - The end index of video segment files.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        metadata:
            description:
                - List of Metadata.
                - Returned for get operation
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
                - Returned for get operation
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
        time_updated:
            description:
                - The time when the MediaAsset was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        master_media_asset_id:
            description:
                - The ID of the senior most asset from which this asset is derived.
            returned: on success
            type: str
            sample: "ocid1.mastermediaasset.oc1..xxxxxxEXAMPLExxxxxx"
        parent_media_asset_id:
            description:
                - The ID of the parent asset from which this asset is derived.
            returned: on success
            type: str
            sample: "ocid1.parentmediaasset.oc1..xxxxxxEXAMPLExxxxxx"
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
        "source_media_workflow_id": "ocid1.sourcemediaworkflow.oc1..xxxxxxEXAMPLExxxxxx",
        "media_workflow_job_id": "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx",
        "source_media_workflow_version": 56,
        "bucket_name": "bucket_name_example",
        "namespace_name": "namespace_name_example",
        "object_name": "object_name_example",
        "object_etag": "object_etag_example",
        "segment_range_start_index": 56,
        "segment_range_end_index": 56,
        "metadata": [{
            "metadata": "metadata_example"
        }],
        "media_asset_tags": [{
            "type": "USER",
            "value": "value_example"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "type": "AUDIO",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "master_media_asset_id": "ocid1.mastermediaasset.oc1..xxxxxxEXAMPLExxxxxx",
        "parent_media_asset_id": "ocid1.parentmediaasset.oc1..xxxxxxEXAMPLExxxxxx",
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


class MediaAssetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "media_asset_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_asset,
            media_asset_id=self.module.params.get("media_asset_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "distribution_channel_id",
            "parent_media_asset_id",
            "master_media_asset_id",
            "type",
            "bucket_name",
            "object_name",
            "media_workflow_job_id",
            "source_media_workflow_id",
            "source_media_workflow_version",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_media_assets, **optional_kwargs
        )


MediaAssetFactsHelperCustom = get_custom_class("MediaAssetFactsHelperCustom")


class ResourceFactsHelper(MediaAssetFactsHelperCustom, MediaAssetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            media_asset_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "compartmentId",
                    "type",
                    "lifecycleState",
                    "parentMediaAssetId",
                    "masterMediaAssetId",
                    "displayName",
                    "timeCreated",
                    "timeUpdated",
                ],
            ),
            distribution_channel_id=dict(type="str"),
            parent_media_asset_id=dict(type="str"),
            master_media_asset_id=dict(type="str"),
            type=dict(
                type="str",
                choices=[
                    "AUDIO",
                    "VIDEO",
                    "PLAYLIST",
                    "IMAGE",
                    "CAPTION_FILE",
                    "UNKNOWN",
                ],
            ),
            bucket_name=dict(type="str"),
            object_name=dict(type="str"),
            media_workflow_job_id=dict(type="str"),
            source_media_workflow_id=dict(type="str"),
            source_media_workflow_version=dict(type="int"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="media_asset",
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

    module.exit_json(media_assets=result)


if __name__ == "__main__":
    main()
